# Project Dump

Project: backend

## Directory Tree

```text
backend
├── app
│   ├── api
│   │   ├── health.py
│   │   ├── v1
│   │   │   ├── api.py
│   │   │   └── endpoints
│   │   │       ├── health.py
│   │   │       ├── ml_inference.py
│   │   │       ├── supply_chain.py
│   │   │       ├── sustainability.py
│   │   │       └── telemetry.py
│   │   └── ws_routes.py
│   ├── contracts
│   │   └── envelope.py
│   ├── core
│   │   └── container.py
│   ├── main.py
│   ├── models
│   │   └── relational.py
│   ├── repositories
│   ├── schemas
│   │   ├── payloads.py
│   │   └── telemetry.py
│   ├── services
│   ├── streaming
│   │   ├── config
│   │   ├── consumers
│   │   │   └── client.py
│   │   ├── kafka
│   │   ├── mqtt
│   │   │   └── client.py
│   │   ├── producers
│   │   │   └── client.py
│   │   ├── serializers
│   │   │   ├── normalizer.py
│   │   │   └── validator.py
│   │   └── websocket
│   │       ├── adapter.py
│   │       └── manager.py
│   └── utils
├── project_dump.md
└── requirements.txt
```

# File Contents

---

## project_dump.md

**[Empty File]**

---

## requirements.txt

```text
fastapi>=0.100.0
uvicorn>=0.22.0
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
websockets>=11.0
neo4j>=5.10.0
python-dotenv>=1.0.0
```

---

## app\main.py

```python
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.logging import setup_logging
from app.core.container import container
from app.streaming.mqtt.client import MqttIngestionClient
from app.streaming.producers.client import KafkaEventProducer
from app.streaming.consumers.client import KafkaEventConsumer
from app.streaming.websocket.adapter import kafka_to_ws_broadcaster

from app.api.health import router as health_router
from app.api.ws_routes import router as ws_router

# Initialize early logging
setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manages the startup and graceful shutdown of all async infrastructure clients."""
    logger.info("Initializing platform infrastructure...")

    # 1. Instantiate Clients
    mqtt_client = MqttIngestionClient()
    kafka_producer = KafkaEventProducer()
    kafka_consumer = KafkaEventConsumer()

    # 2. Register to Dependency Injection Container
    container.register_mqtt_client(mqtt_client)
    container.register_kafka_producer(kafka_producer)
    container.register_kafka_consumer(kafka_consumer)

    # 3. Wire Callbacks (from Phase 6)
    kafka_consumer.register_callback("telemetry.raw", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("alerts", kafka_to_ws_broadcaster)

    # 4. Start Downstream First (Kafka)
    await kafka_producer.start()
    await kafka_consumer.start()
    
    # 5. Start Upstream Last (MQTT Ingestion)
    await mqtt_client.start()
    
    logger.info("Platform streaming layer fully operational.")
    
    yield  # Application runs here

    logger.info("Initiating graceful shutdown sequence...")
    
    # 6. Stop Upstream First (Halt new ingestion)
    await mqtt_client.stop()
    
    # 7. Stop Consumers (Halt internal processing)
    await kafka_consumer.stop()
    
    # 8. Stop Downstream Last (Flush pending producer batches)
    await kafka_producer.stop()
    
    logger.info("Shutdown complete. All connections closed safely.")

# Initialize the FastAPI application
app = FastAPI(title="Industrial EV AI Platform - Streaming Layer", lifespan=lifespan)

# Include core routers
app.include_router(health_router)
app.include_router(ws_router)
```

---

## app\api\health.py

```python
import logging
from fastapi import APIRouter, HTTPException, status
from app.core.container import container

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/health", tags=["Monitoring"])

@router.get("")
async def liveness_check():
    """Basic HTTP liveness probe to verify the API event loop is running."""
    return {"status": "alive", "service": "streaming_layer"}

@router.get("/mqtt")
async def mqtt_readiness_check():
    """Verifies the Mosquitto MQTT broker connection is active."""
    try:
        mqtt = container.mqtt_client
        # Verify the client exists and the background consumption task is actively running
        if mqtt and mqtt._consume_task and not mqtt._consume_task.done():
            return {"status": "connected", "protocol": "mqtt"}
    except RuntimeError:
        # Caught if the DI container hasn't initialized the client yet
        pass
        
    logger.warning("MQTT health check failed.")
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
        detail="MQTT broker connection is not active."
    )

@router.get("/kafka")
async def kafka_readiness_check():
    """Verifies both Kafka Producer and Consumer are active."""
    try:
        producer = container.kafka_producer
        consumer = container.kafka_consumer
        
        is_producer_ok = producer and producer.producer
        is_consumer_ok = consumer and consumer._consume_task and not consumer._consume_task.done()
        
        if is_producer_ok and is_consumer_ok:
            return {"status": "connected", "protocol": "kafka", "components": ["producer", "consumer"]}
            
    except RuntimeError:
        pass
        
    logger.warning("Kafka health check failed.")
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
        detail="Kafka event bus connections are not fully active."
    )
```

---

## app\api\ws_routes.py

```python
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.streaming.websocket.manager import ws_manager

logger = logging.getLogger(__name__)
router = APIRouter()

@router.websocket("/ws/dashboard")
async def dashboard_websocket_endpoint(websocket: WebSocket) -> None:
    """
    WebSocket endpoint for the React frontend.
    Expects incoming JSON commands: {"action": "subscribe", "topic": "telemetry.raw"}
    """
    await ws_manager.connect(websocket)
    
    try:
        while True:
            # Wait for control commands from the client
            data = await websocket.receive_json()
            action = data.get("action")
            topic = data.get("topic")
            
            if action == "subscribe" and topic:
                await ws_manager.subscribe(websocket, topic)
            elif action == "unsubscribe" and topic:
                await ws_manager.unsubscribe(websocket, topic)
                
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
    except Exception as e:
        logger.error("WebSocket connection error.", exc_info=True)
        ws_manager.disconnect(websocket)
```

---

## app\contracts\envelope.py

```python
from datetime import datetime, timezone
from typing import Generic, TypeVar, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# Generic Type for payload validation flexibility
T = TypeVar('T', bound=BaseModel)

class EventEnvelope(BaseModel, Generic[T]):
    """Standardized event envelope wrapping all platform domain payloads."""
    
    event_id: UUID = Field(default_factory=uuid4, description="Unique identifier for this specific event instance")
    event_type: str = Field(..., description="The type of event (e.g., 'telemetry.raw', 'battery.alert')")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="UTC timestamp of event generation")
    source: str = Field(..., description="Originating service or simulator node name")
    vehicle_id: str = Field(..., description="Unique immutable ID of the industrial vehicle")
    fleet_id: str = Field(..., description="Identifier for the tracking fleet operational partition")
    correlation_id: UUID = Field(default_factory=uuid4, description="Tracing ID sustained across asynchronous boundaries")
    
    payload: T = Field(..., description="The concrete domain data model matching the event type")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            UUID: lambda v: str(v)
        }
```

---

## app\core\container.py

```python
import logging
from typing import Any, Optional
from app.core.config import settings

logger = logging.getLogger(__name__)

class ApplicationContainer:
    """Manages system-wide client allocations and lifecycle liftoffs."""
    
    def __init__(self) -> None:
        self.settings = settings
        
        # Placeholders for explicit network clients initialized during app startup
        self._mqtt_client: Optional[Any] = None
        self._kafka_producer: Optional[Any] = None
        self._kafka_consumer: Optional[Any] = None

    def register_mqtt_client(self, client: Any) -> None:
        self._mqtt_client = client
        logger.debug("Async MQTT Client registered to DI container.")

    def register_kafka_producer(self, producer: Any) -> None:
        self._kafka_producer = producer
        logger.debug("Async Kafka Producer registered to DI container.")

    def register_kafka_consumer(self, consumer: Any) -> None:
        self._kafka_consumer = consumer
        logger.debug("Async Kafka Consumer Framework registered to DI container.")

    @property
    def mqtt_client(self) -> Any:
        if not self._mqtt_client:
            raise RuntimeError("MQTT Client requested before initialization.")
        return self._mqtt_client

    @property
    def kafka_producer(self) -> Any:
        if not self._kafka_producer:
            raise RuntimeError("Kafka Producer requested before initialization.")
        return self._kafka_producer
        
    @property
    def kafka_consumer(self) -> Any:
        if not self._kafka_consumer:
            raise RuntimeError("Kafka Consumer requested before initialization.")
        return self._kafka_consumer

    def get_kafka_consumer(self) -> Any:
        """Explicit getter used during startup to wire WebSocket callbacks."""
        if not self._kafka_consumer:
            raise RuntimeError("Kafka Consumer requested before initialization.")
        return self._kafka_consumer


# Global container instance
container = ApplicationContainer()
```

---

## app\models\relational.py

```python
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, index=True)
    voltage = Column(Float, nullable=False)
    current = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    soc = Column(Float, nullable=False)  # State of Charge (0-100)

class ChargingSession(Base):
    __tablename__ = "charging_sessions"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)
    energy_delivered_kwh = Column(Float, nullable=False)
    starting_soc = Column(Float, nullable=False)
    ending_soc = Column(Float, nullable=True)

class BatteryHealth(Base):
    __tablename__ = "battery_health"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), unique=True, nullable=False, index=True)
    capacity_fade = Column(Float, nullable=False)  # Ah drop
    cycle_count = Column(Integer, nullable=False)
    state_of_health = Column(Float, nullable=False)  # percentage (0-100)
    remaining_useful_life = Column(Integer, nullable=False)  # estimated cycles remaining

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    severity = Column(String(20), nullable=False)  # Critical, Warning, Info
    type = Column(String(50), nullable=False)  # Thermal, Over-voltage, Anomaly
    description = Column(String(255), nullable=False)
    resolved = Column(Boolean, default=False)

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    risk_score = Column(Float, default=0.0)
    material_supplied = Column(String(50), nullable=False)  # Lithium, Cobalt, Nickel, etc.

class MaintenanceLog(Base):
    __tablename__ = "maintenance_logs"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String(255), nullable=False)
    action_taken = Column(String(255), nullable=True)
    status = Column(String(50), default="Pending")  # Pending, In Progress, Completed
```

---

## app\schemas\payloads.py

```python
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class TelemetryPayload(BaseModel):
    """Core kinematic data from the vehicle's engine and operational control units."""
    speed_kph: float = Field(..., ge=0, le=200)
    odometer_km: float = Field(..., ge=0)
    motor_temperature_c: float = Field(..., ge=-40, le=150)
    torque_nm: float = Field(...)
    inverter_efficiency: float = Field(..., ge=0, le=1)


class BatteryPayload(BaseModel):
    """Real-time electro-chemical battery state statistics."""
    state_of_charge_pct: float = Field(..., ge=0, le=100)
    state_of_health_pct: float = Field(..., ge=0, le=100)
    voltage: float = Field(..., ge=0, le=1000)
    current_amps: float = Field(...)
    cell_temperature_max_c: float = Field(..., ge=-40, le=100)
    internal_resistance_ohm: float = Field(..., ge=0)


class LocationPayload(BaseModel):
    """High-precision positional telemetry coordinate data."""
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    altitude_m: float = Field(..., ge=-500, le=9000)
    heading_deg: float = Field(..., ge=0, le=360)
    gps_fix_quality: int = Field(..., description="0=Invalid, 1=GPS, 2=DGPS")


class ChargingPayload(BaseModel):
    """State management metrics during an active battery charging session."""
    charger_id: str = Field(...)
    charging_rate_kw: float = Field(..., ge=0)
    time_to_full_mins: float = Field(..., ge=0)
    connector_type: str = Field(..., description="CCS2, Megawatt, etc.")


class StatusPayload(BaseModel):
    """High-level operating mode state flags."""
    operational_status: str = Field(..., description="READY, OPERATIONAL, FAULT, OFFLINE")
    active_error_codes: list[str] = Field(default_factory=list)
    driver_id: Optional[str] = Field(default=None)


class AlertsPayload(BaseModel):
    """Immediate hardware or safety critical notifications."""
    alert_code: str = Field(...)
    severity: str = Field(..., description="INFO, WARNING, CRITICAL")
    component: str = Field(..., description="BATTERY, MOTOR, BRAKES, POWERTRAIN")
    description: str = Field(...)


class HeartbeatPayload(BaseModel):
    """Lightweight diagnostics asserting infrastructure network health."""
    uptime_seconds: int = Field(..., ge=0)
    firmware_version: str = Field(...)
    signal_strength_dbm: int = Field(..., le=0)
```

---

## app\schemas\telemetry.py

```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class TelemetryBase(BaseModel):
    vehicle_id: str
    voltage: float
    current: float
    temperature: float
    soc: float

class TelemetryCreate(TelemetryBase):
    pass

class TelemetryResponse(TelemetryBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class BatteryHealthResponse(BaseModel):
    vehicle_id: str
    capacity_fade: float
    cycle_count: int
    state_of_health: float
    remaining_useful_life: int

    class Config:
        from_attributes = True

class AlertResponse(BaseModel):
    id: int
    vehicle_id: str
    timestamp: datetime
    severity: str
    type: str
    description: str
    resolved: bool

    class Config:
        from_attributes = True

class SupplierRiskResponse(BaseModel):
    id: int
    name: str
    location: str
    risk_score: float
    material_supplied: str

    class Config:
        from_attributes = True

class DependencyNode(BaseModel):
    id: str
    label: str
    properties: dict

class DependencyEdge(BaseModel):
    source: str
    target: str
    type: str

class GraphDependencyResponse(BaseModel):
    nodes: List[DependencyNode]
    edges: List[DependencyEdge]
```

---

## app\api\v1\api.py

```python
from fastapi import APIRouter
from .endpoints import health, telemetry, ml_inference, supply_chain, sustainability

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(telemetry.router, tags=["telemetry"])
api_router.include_router(ml_inference.router, tags=["ml_inference"])
api_router.include_router(supply_chain.router, tags=["supply_chain"])
api_router.include_router(sustainability.router, tags=["sustainability"])
```

---

## app\api\v1\endpoints\health.py

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": "2026-07-10T09:05:00Z",
        "version": "1.0.0"
    }
```

---

## app\api\v1\endpoints\ml_inference.py

```python
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException
from ....schemas.telemetry import BatteryHealthResponse
import asyncio
import random
import json

router = APIRouter()

MOCK_BATTERY_HEALTH = {
    "EV-HD-001": {"vehicle_id": "EV-HD-001", "capacity_fade": 5.8, "cycle_count": 260, "state_of_health": 96.0, "remaining_useful_life": 1240},
    "EV-HD-002": {"vehicle_id": "EV-HD-002", "capacity_fade": 9.2, "cycle_count": 410, "state_of_health": 91.0, "remaining_useful_life": 890},
    "EV-HD-003": {"vehicle_id": "EV-HD-003", "capacity_fade": 2.1, "cycle_count": 95, "state_of_health": 98.0, "remaining_useful_life": 1450},
    "EV-HD-004": {"vehicle_id": "EV-HD-004", "capacity_fade": 17.5, "cycle_count": 780, "state_of_health": 83.0, "remaining_useful_life": 430},
}

@router.get("/battery/status", response_model=BatteryHealthResponse)
def get_battery_status(vehicle_id: str = Query(..., description="ID of the EV vehicle asset")):
    if vehicle_id not in MOCK_BATTERY_HEALTH:
        raise HTTPException(status_code=404, detail="Battery status not found for vehicle")
    return MOCK_BATTERY_HEALTH[vehicle_id]

@router.post("/predict/rul")
def predict_rul(payload: dict):
    # Mock ML inference request utilizing temperature, voltage, cycle profiles
    voltage = payload.get("voltage", 380)
    temperature = payload.get("temperature", 35)
    cycle_count = payload.get("cycle_count", 100)
    
    # Simple linear degradation simulation
    base_life = 1500
    degradation = (cycle_count * 1.1) + (temperature * 2.5) + (400 - voltage)
    estimated_rul = max(0, int(base_life - degradation))
    
    return {
        "predicted_rul_cycles": estimated_rul,
        "confidence_interval": [estimated_rul - 50, estimated_rul + 50],
        "model_version": "xgboost-battery-rul-v1.0"
    }

@router.post("/predict/soh")
def predict_soh(payload: dict):
    capacity = payload.get("capacity", 120.0)
    nominal_capacity = payload.get("nominal_capacity", 120.0)
    
    soh = (capacity / nominal_capacity) * 100.0
    return {
        "state_of_health": round(soh, 2),
        "capacity_fade_ah": round(nominal_capacity - capacity, 2),
        "model_version": "regression-degradation-soh-v1.0"
    }

@router.post("/predict/anomaly")
def predict_anomaly(payload: dict):
    temperature = payload.get("temperature", 25.0)
    voltage = payload.get("voltage", 390.0)
    
    # Anomaly indicator: if temp exceeds threshold or voltage is abnormally low
    is_anomaly = False
    anomaly_score = 0.05
    
    if temperature > 45.0 or voltage < 320.0:
        is_anomaly = True
        anomaly_score = 0.89 + (temperature * 0.002)
        
    return {
        "is_anomaly": is_anomaly,
        "anomaly_score": round(anomaly_score, 3),
        "anomalous_features": ["temperature" if temperature > 45.0 else None, "voltage" if voltage < 320.0 else None],
        "model_version": "isolation-forest-anomaly-v1.0"
    }

@router.websocket("/telemetry/ws/{vehicle_id}")
async def websocket_endpoint(websocket: WebSocket, vehicle_id: str):
    await websocket.accept()
    try:
        while True:
            # Generate simulated live streaming data for WebSockets
            data = {
                "vehicle_id": vehicle_id,
                "timestamp": str(asyncio.get_event_loop().time()),
                "voltage": round(random.uniform(370, 410), 2),
                "current": round(random.uniform(-50, 50), 2),
                "temperature": round(random.uniform(30, 48), 2),
                "soc": round(random.uniform(20, 99), 1)
              }
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        pass
```

---

## app\api\v1\endpoints\supply_chain.py

```python
from fastapi import APIRouter
from ....schemas.telemetry import SupplierRiskResponse, GraphDependencyResponse
from typing import List

router = APIRouter()

MOCK_SUPPLIERS = [
    {"id": 1, "name": "Salar de Atacama Minerals", "location": "Chile", "risk_score": 24.5, "material_supplied": "Lithium"},
    {"id": 2, "name": "Tianqi Lithium Refining", "location": "Sichuan, China", "risk_score": 86.2, "material_supplied": "Refined Lithium Hydroxide"},
    {"id": 3, "name": "Democratic Republic of Congo Mining", "location": "Katanga", "risk_score": 68.0, "material_supplied": "Cobalt Ore"},
    {"id": 4, "name": "Sumitomo Metal Mining", "location": "Japan", "risk_score": 15.4, "material_supplied": "Cathode Precursors"},
]

@router.get("/suppliers", response_model=List[SupplierRiskResponse])
def get_suppliers():
    return MOCK_SUPPLIERS

@router.get("/risk")
def get_supply_chain_risk():
    return {
        "global_risk_index": 54.8,
        "critical_vulnerability": "High concentration of refining capacity in Sichuan region.",
        "mitigation_plan": "Diversify sourcing contracts with North American refiners.",
        "last_updated": "2026-07-10T09:05:00Z"
    }

@router.get("/materials")
def get_materials_flow():
    return {
        "materials": [
            {"name": "Lithium", "active_flow_tons": 450, "safety_buffer_days": 45},
            {"name": "Cobalt", "active_flow_tons": 120, "safety_buffer_days": 30},
            {"name": "Nickel", "active_flow_tons": 800, "safety_buffer_days": 60},
        ]
    }

@router.get("/dependencies", response_model=GraphDependencyResponse)
def get_dependencies_graph():
    # Return structured nodes & edges simulating a Neo4j Cypher query response
    return {
        "nodes": [
            {"id": "node_mine_1", "label": "Mine", "properties": {"name": "Salar de Atacama Mine", "country": "Chile"}},
            {"id": "node_refiner_1", "label": "Refiner", "properties": {"name": "Tianqi Refining", "country": "China"}},
            {"id": "node_plant_1", "label": "Battery Plant", "properties": {"name": "CATL Yibin", "capacity_gwh": 20}},
            {"id": "node_fleet_1", "label": "Fleet Vehicle", "properties": {"vehicle_id": "EV-HD-004", "hub": "Denver"}}
        ],
        "edges": [
            {"source": "node_mine_1", "target": "node_refiner_1", "type": "SUPPLIES_RAW_MATERIAL"},
            {"source": "node_refiner_1", "target": "node_plant_1", "type": "DELIVERS_REFINED_LITHIUM"},
            {"source": "node_plant_1", "target": "node_fleet_1", "type": "EQUIP_BATTERY_TO"}
        ]
    }
```

---

## app\api\v1\endpoints\sustainability.py

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/carbon")
def get_carbon_metrics():
    return {
        "co2_savings_ytd_tons": 142.6,
        "diesel_displacement_gallons": 14500,
        "grid_emission_intensity_kwh": 0.32,  # kg CO2/kWh
        "scope_1_direct_displaced_tons": 160.4,
        "scope_3_grid_indirect_tons": 17.8
    }

@router.get("/electrification")
def get_electrification_readiness():
    return {
        "readiness_score": 84,
        "total_active_routes": 195,
        "electrified_routes": 82,
        "recommendations": [
            {
                "route_id": "DEN-BOU-01",
                "name": "Denver - Boulder Corridor",
                "readiness_percentage": 94,
                "reason": "Short length, highly dense public fast chargers, low grade variance."
            },
            {
                "route_id": "HOU-LOC-04",
                "name": "Houston Local Hub Delivery",
                "readiness_percentage": 88,
                "reason": "Repeated stop patterns allow dwell-time depot charging."
            }
        ]
    }
```

---

## app\api\v1\endpoints\telemetry.py

```python
from fastapi import APIRouter, Query, HTTPException
from typing import List
from ....schemas.telemetry import TelemetryResponse
import datetime

router = APIRouter()

MOCK_VEHICLES = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]

MOCK_TELEMETRY = {
    "EV-HD-001": {"vehicle_id": "EV-HD-001", "voltage": 395.2, "current": 12.4, "temperature": 34.5, "soc": 88.0, "id": 1, "timestamp": datetime.datetime.utcnow()},
    "EV-HD-002": {"vehicle_id": "EV-HD-002", "voltage": 380.1, "current": -45.0, "temperature": 38.2, "soc": 42.0, "id": 2, "timestamp": datetime.datetime.utcnow()},
    "EV-HD-003": {"vehicle_id": "EV-HD-003", "voltage": 401.5, "current": 10.1, "temperature": 33.1, "soc": 91.0, "id": 3, "timestamp": datetime.datetime.utcnow()},
    "EV-HD-004": {"vehicle_id": "EV-HD-004", "voltage": 372.4, "current": 115.0, "temperature": 44.8, "soc": 76.0, "id": 4, "timestamp": datetime.datetime.utcnow()},
}

@router.get("/vehicles", response_model=List[str])
def get_vehicles():
    return MOCK_VEHICLES

@router.get("/telemetry/live", response_model=TelemetryResponse)
def get_live_telemetry(vehicle_id: str = Query(..., description="ID of the EV vehicle asset")):
    if vehicle_id not in MOCK_TELEMETRY:
        raise HTTPException(status_code=404, detail="Vehicle telemetry not found")
    # Update timestamp to match current query time
    telemetry = MOCK_TELEMETRY[vehicle_id]
    telemetry["timestamp"] = datetime.datetime.utcnow()
    return telemetry
```

---

## app\streaming\consumers\client.py

```python
import asyncio
import json
import logging
from typing import Callable, Dict, List, Optional, Awaitable, Any

from aiokafka import AIOKafkaConsumer
from app.core.config import settings

logger = logging.getLogger(__name__)

# Define the callback signature: takes a topic (str) and the parsed JSON payload (dict)
ConsumerCallback = Callable[[str, Dict[str, Any]], Awaitable[None]]

class KafkaEventConsumer:
    """Async Kafka consumer framework with an internal callback router."""
    
    # The fixed list of topics our backend is allowed to consume
    ALLOWED_TOPICS = [
        "telemetry.raw", 
        "telemetry.processed", 
        "predictions", 
        "alerts", 
        "maintenance", 
        "supplychain", 
        "sustainability"
    ]

    def __init__(self) -> None:
        self.consumer: Optional[AIOKafkaConsumer] = None
        self._consume_task: Optional[asyncio.Task] = None
        
        # Internal router mapping Kafka topics to a list of registered async callbacks
        self._callbacks: Dict[str, List[ConsumerCallback]] = {
            topic: [] for topic in self.ALLOWED_TOPICS
        }

    def register_callback(self, topic: str, callback: ConsumerCallback) -> None:
        """Allows domain services to hook into specific Kafka topics."""
        if topic not in self.ALLOWED_TOPICS:
            logger.warning("Attempted to register callback for unknown topic.", extra={"topic": topic})
            return
            
        self._callbacks[topic].append(callback)
        logger.debug("Registered new callback.", extra={"topic": topic, "callback": callback.__name__})

    async def start(self) -> None:
        """Initializes the Kafka consumer and begins the listening loop."""
        logger.info("Initializing Kafka consumer framework...")
        
        self.consumer = AIOKafkaConsumer(
            *self.ALLOWED_TOPICS,
            bootstrap_servers=settings.kafka.bootstrap_servers,
            group_id=settings.kafka.group_id,
            auto_offset_reset=settings.kafka.auto_offset_reset,
            enable_auto_commit=True
        )
        
        try:
            await self.consumer.start()
            logger.info("Kafka Consumer successfully connected to brokers.")
            
            # Spin up the background consuming loop
            self._consume_task = asyncio.create_task(self._consume_loop())
        except Exception as e:
            logger.critical("Failed to connect Kafka Consumer.", exc_info=True)
            raise

    async def stop(self) -> None:
        """Gracefully shuts down the consumer task and connection."""
        if self._consume_task:
            self._consume_task.cancel()
            try:
                await self._consume_task
            except asyncio.CancelledError:
                pass
                
        if self.consumer:
            await self.consumer.stop()
            logger.info("Kafka Consumer disconnected cleanly.")

    async def _consume_loop(self) -> None:
        """Background loop retrieving messages and dispatching them to callbacks."""
        if not self.consumer:
            return

        try:
            async for message in self.consumer:
                topic = message.topic
                
                # Check if anyone actually cares about this topic before parsing
                if not self._callbacks.get(topic):
                    continue

                try:
                    # Parse the raw bytes back into the EventEnvelope JSON dictionary
                    payload_dict = json.loads(message.value.decode("utf-8"))
                    
                    # Dispatch to all registered callbacks asynchronously
                    # We use create_task so a slow callback doesn't block the Kafka consumer loop
                    for callback in self._callbacks[topic]:
                        asyncio.create_task(self._execute_callback(callback, topic, payload_dict))
                        
                except json.JSONDecodeError:
                    logger.error("Failed to decode Kafka message as JSON.", extra={"topic": topic})
                except Exception as e:
                    logger.error("Error dispatching Kafka message.", exc_info=True, extra={"topic": topic})

        except asyncio.CancelledError:
            logger.info("Kafka consumption task gracefully cancelled.")
            
    async def _execute_callback(self, callback: ConsumerCallback, topic: str, payload: Dict[str, Any]) -> None:
        """Safely executes a callback, catching any unhandled exceptions."""
        try:
            await callback(topic, payload)
        except Exception as e:
            logger.error(
                "Unhandled exception in consumer callback.", 
                exc_info=True, 
                extra={"topic": topic, "callback": callback.__name__}
            )
```

---

## app\streaming\mqtt\client.py

```python
import asyncio
import logging
from typing import Optional
import aiomqtt
from aiomqtt.exceptions import MqttError

from app.core.config import settings
from app.schemas.payloads import TOPIC_SCHEMA_MAP
from app.streaming.serializers.validator import validate_raw_payload
from app.streaming.serializers.normalizer import normalize_to_envelope, MQTT_TO_KAFKA_ROUTE
from app.core.container import container

logger = logging.getLogger(__name__)

class MqttIngestionClient:
    """Async MQTT client handling simulator data ingestion."""
    
    def __init__(self) -> None:
        self.client: Optional[aiomqtt.Client] = None
        self._consume_task: Optional[asyncio.Task] = None
        # Derive immutable topics directly from our Phase 2 schema map
        self.topics = list(TOPIC_SCHEMA_MAP.keys())

    async def start(self) -> None:
        """Establishes broker connection and initiates the listener task."""
        logger.info("Initializing MQTT ingestion client...")
        
        self.client = aiomqtt.Client(
            hostname=settings.mqtt.host,
            port=settings.mqtt.port,
            username=settings.mqtt.username,
            password=settings.mqtt.password,
            client_id=settings.mqtt.client_id,
            keepalive=settings.mqtt.keepalive
        )
        
        try:
            await self.client.connect()
            logger.info("Connected to Mosquitto broker.", extra={"broker": settings.mqtt.host})
            
            # Spin up the background listening loop
            self._consume_task = asyncio.create_task(self._consume_loop())
        except MqttError as e:
            logger.critical("Failed to connect to MQTT broker.", exc_info=True)
            raise

    async def stop(self) -> None:
        """Gracefully tears down the consumption task and broker connection."""
        if self._consume_task:
            self._consume_task.cancel()
            try:
                await self._consume_task
            except asyncio.CancelledError:
                pass
                
        if self.client:
            await self.client.disconnect()
            logger.info("Disconnected from Mosquitto broker.")

    async def _consume_loop(self) -> None:
        """Background loop that subscribes to topics and awaits messages."""
        if not self.client:
            return

        try:
            async with self.client.messages() as messages:
                # 1. Subscribe to the strictly required, immutable topics
                for topic in self.topics:
                    await self.client.subscribe(topic)
                    logger.info("Subscribed to MQTT topic", extra={"mqtt_topic": topic})
                    
                # 2. Continuous asynchronous event consumption
                async for message in messages:
                    self._process_message(message)
                    
        except asyncio.CancelledError:
            logger.info("MQTT consumption task gracefully cancelled.")
        except MqttError as e:
            logger.error("MQTT connection lost during consumption.", exc_info=True)
            # In a production environment, this is where we would trigger an exponential backoff reconnect

    def _process_message(self, message: aiomqtt.Message) -> None:
        """Routes incoming messages through validation, normalization, and publishing."""
        topic = str(message.topic)
        payload_bytes = message.payload
        
        if not isinstance(payload_bytes, bytes):
            return

        # 1. Validate
        validated_model = validate_raw_payload(topic, payload_bytes)
        
        if validated_model:
            # 2. Normalize
            envelope = normalize_to_envelope(topic, validated_model)
            target_kafka_topic = MQTT_TO_KAFKA_ROUTE.get(topic, "telemetry.raw")
            
            # 3. Publish asynchronously without blocking the MQTT consumption loop
            kafka_producer = container.kafka_producer
            asyncio.create_task(kafka_producer.publish(target_kafka_topic, envelope)) 
```

---

## app\streaming\producers\client.py

```python
import logging
from typing import Optional
from aiokafka import AIOKafkaProducer

from app.core.config import settings
from app.contracts.envelope import EventEnvelope

logger = logging.getLogger(__name__)

class KafkaEventProducer:
    """Async Kafka producer for routing normalized events to the message bus."""
    
    def __init__(self) -> None:
        self.producer: Optional[AIOKafkaProducer] = None

    async def start(self) -> None:
        """Initializes the Kafka producer connection pool."""
        logger.info("Initializing Kafka producer...", extra={"brokers": settings.kafka.bootstrap_servers})
        
        self.producer = AIOKafkaProducer(
            bootstrap_servers=settings.kafka.bootstrap_servers,
            client_id="ev_streaming_producer",
            # Acknowledge leader write for high throughput, safe enough for telemetry
            acks=1 
        )
        
        try:
            await self.producer.start()
            logger.info("Kafka Producer successfully connected.")
        except Exception as e:
            logger.critical("Failed to connect Kafka Producer.", exc_info=True)
            raise

    async def stop(self) -> None:
        """Flushes pending batches and cleanly disconnects."""
        if self.producer:
            await self.producer.stop()
            logger.info("Kafka Producer disconnected.")

    async def publish(self, target_topic: str, event: EventEnvelope) -> None:
        """Serializes the event envelope and publishes it to the specified topic."""
        if not self.producer:
            logger.error("Attempted to publish without an active Kafka connection.")
            return

        try:
            # Pydantic v2 serialization to JSON bytes
            payload_bytes = event.model_dump_json().encode("utf-8")
            
            # Fire-and-forget for telemetry throughput, though send_and_wait can be used for guarantees
            await self.producer.send(target_topic, value=payload_bytes)
            
        except Exception as e:
            logger.error(
                "Failed to publish event to Kafka.",
                exc_info=True,
                extra={"target_topic": target_topic, "event_id": str(event.event_id)}
            )
```

---

## app\streaming\serializers\normalizer.py

```python
import logging
from typing import Dict
from pydantic import BaseModel
from app.contracts.envelope import EventEnvelope

logger = logging.getLogger(__name__)

# Map incoming MQTT topics to target Kafka topics/event types
MQTT_TO_KAFKA_ROUTE: Dict[str, str] = {
    "ev/telemetry": "telemetry.raw",
    "ev/battery": "telemetry.raw",  # Routing battery data to the same raw firehose for now
    "ev/location": "telemetry.raw",
    "ev/charging": "telemetry.raw",
    "ev/status": "telemetry.raw",
    "ev/alerts": "alerts",
    "ev/heartbeat": "telemetry.raw"
}

def normalize_to_envelope(mqtt_topic: str, payload: BaseModel) -> EventEnvelope:
    """
    Wraps a validated domain payload into the standard Event Envelope.
    Generates event_id and correlation_id automatically via the schema defaults.
    """
    target_event_type = MQTT_TO_KAFKA_ROUTE.get(mqtt_topic, "unknown.raw")
    
    # In a fully integrated environment, vehicle_id and fleet_id might be extracted
    # from the MQTT topic structure (e.g., ev/telemetry/{fleet_id}/{vehicle_id}) 
    # or the payload itself. Since our topics are fixed, we inject placeholders 
    # for the infrastructure integration phase.
    
    envelope = EventEnvelope(
        event_type=target_event_type,
        source="streaming_ingestion_node",
        vehicle_id="VEH-SIM-001",
        fleet_id="FLT-ALPHA-01",
        payload=payload
    )
    
    logger.debug(
        "Normalized event payload.",
        extra={
            "event_id": str(envelope.event_id),
            "correlation_id": str(envelope.correlation_id),
            "event_type": target_event_type
        }
    )
    return envelope
```

---

## app\streaming\serializers\validator.py

```python
import json
import logging
from typing import Optional, Dict, Type
from pydantic import BaseModel, ValidationError

from app.schemas.payloads import (
    TelemetryPayload, BatteryPayload, LocationPayload,
    ChargingPayload, StatusPayload, AlertsPayload, HeartbeatPayload
)

logger = logging.getLogger(__name__)

# Map fixed, immutable MQTT topics to their structural validators
TOPIC_SCHEMA_MAP: Dict[str, Type[BaseModel]] = {
    "ev/telemetry": TelemetryPayload,
    "ev/battery": BatteryPayload,
    "ev/location": LocationPayload,
    "ev/charging": ChargingPayload,
    "ev/status": StatusPayload,
    "ev/alerts": AlertsPayload,
    "ev/heartbeat": HeartbeatPayload
}

def validate_raw_payload(topic: str, raw_data: bytes) -> Optional[BaseModel]:
    """
    Parses and structural-checks incoming binary JSON string payloads against domain schemas.
    
    Returns a Pydantic Model instance if valid; returns None if malformed or unknown.
    """
    schema_cls = TOPIC_SCHEMA_MAP.get(topic)
    
    if not schema_cls:
        logger.warning(
            "Received event on unregistered topic. Processing discarded.",
            extra={"mqtt_topic": topic}
        )
        return None

    try:
        # Step 1: Deserialize JSON payload safely
        parsed_json = json.loads(raw_data)
        
        # Step 2: Perform schema enforcement via Pydantic
        validated_model = schema_cls.model_validate(parsed_json)
        return validated_model
        
    except json.JSONDecodeError as jde:
        logger.error(
            "Failed to deserialize payload. Raw input is not clean JSON.",
            exc_info=True,
            extra={"mqtt_topic": topic}
        )
    except ValidationError as ve:
        logger.warning(
            "Payload failed schema compliance assertions. Event dropped.",
            extra={
                "mqtt_topic": topic,
                "validation_errors": ve.errors(include_url=False)
            }
        )
    except Exception as e:
        logger.critical(
            "Unexpected processing failure during validation pipeline.",
            exc_info=True,
            extra={"mqtt_topic": topic}
        )
        
    return None
```

---

## app\streaming\websocket\adapter.py

```python
import logging
from typing import Dict, Any
from app.streaming.websocket.manager import ws_manager

logger = logging.getLogger(__name__)

async def kafka_to_ws_broadcaster(topic: str, payload: Dict[str, Any]) -> None:
    """
    Standard callback registered with the Kafka Event Consumer.
    Bridges the Kafka bus directly to the WebSocket manager.
    """
    logger.debug("Relaying Kafka event to WebSockets.", extra={"topic": topic})
    await ws_manager.broadcast(topic, payload)
```

---

## app\streaming\websocket\manager.py

```python
import logging
import json
from typing import Dict, Set, Any
from fastapi import WebSocket

logger = logging.getLogger(__name__)

class WebSocketManager:
    """Manages active dashboard WebSocket connections and topic subscriptions."""
    
    def __init__(self) -> None:
        # Maps active WebSocket connections to a set of their subscribed topics
        self.active_connections: Dict[WebSocket, Set[str]] = {}

    async def connect(self, websocket: WebSocket) -> None:
        """Accepts a new connection and initializes an empty subscription set."""
        await websocket.accept()
        self.active_connections[websocket] = set()
        logger.info("New WebSocket dashboard connection established.")

    def disconnect(self, websocket: WebSocket) -> None:
        """Removes a connection from the active pool cleanly."""
        if websocket in self.active_connections:
            del self.active_connections[websocket]
            logger.info("WebSocket dashboard connection removed.")

    async def subscribe(self, websocket: WebSocket, topic: str) -> None:
        """Adds a Kafka topic to the client's subscription list."""
        if websocket in self.active_connections:
            self.active_connections[websocket].add(topic)
            logger.debug("WebSocket subscribed to topic.", extra={"topic": topic})

    async def unsubscribe(self, websocket: WebSocket, topic: str) -> None:
        """Removes a Kafka topic from the client's subscription list."""
        if websocket in self.active_connections and topic in self.active_connections[websocket]:
            self.active_connections[websocket].remove(topic)
            logger.debug("WebSocket unsubscribed from topic.", extra={"topic": topic})

    async def broadcast(self, topic: str, payload: Dict[str, Any]) -> None:
        """Pushes an event payload to all clients subscribed to the topic."""
        # Convert the dictionary payload to a JSON string for transmission
        message = json.dumps({"topic": topic, "data": payload})
        
        stale_connections = []
        
        for websocket, subscriptions in self.active_connections.items():
            if topic in subscriptions:
                try:
                    await websocket.send_text(message)
                except Exception as e:
                    logger.error("Failed to send WebSocket message.", exc_info=True)
                    stale_connections.append(websocket)
                    
        # Cleanup connections that dropped without closing properly
        for stale in stale_connections:
            self.disconnect(stale)

# Global manager instance
ws_manager = WebSocketManager()
```
