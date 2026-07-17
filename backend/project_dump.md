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
│   │   │   ├── endpoints
│   │   │   │   ├── health.py
│   │   │   │   ├── ml_inference.py
│   │   │   │   ├── supply_chain.py
│   │   │   │   ├── sustainability.py
│   │   │   │   └── telemetry.py
│   │   │   └── rest_routes.py
│   │   └── ws_routes.py
│   ├── contracts
│   │   └── envelope.py
│   ├── core
│   │   ├── config.py
│   │   ├── container.py
│   │   └── logging.py
│   ├── db
│   │   ├── init_timescale.py
│   │   └── session.py
│   ├── main.py
│   ├── models
│   │   ├── domain.py
│   │   └── relational.py
│   ├── repositories
│   │   └── domain.py
│   ├── schemas
│   │   ├── payloads.py
│   │   └── telemetry.py
│   ├── services
│   │   └── telemetry.py
│   ├── streaming
│   │   ├── config
│   │   ├── consumers
│   │   │   └── client.py
│   │   ├── kafka
│   │   ├── mqtt
│   │   │   └── client.py
│   │   ├── processor
│   │   │   └── telemetry.py
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
aiomqtt>=2.0.0
aiokafka>=0.8.1
asyncpg>=0.28.0
```

---

## app\main.py

```python
import sys
import os
import asyncio
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

# Windows proactor event loop fix for aiomqtt socket polling
if sys.platform.lower() == "win32" or os.name.lower() == "nt":
    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

from app.core.logging import setup_logging
from app.core.container import container
from app.streaming.mqtt.client import MqttIngestionClient
from app.streaming.producers.client import KafkaEventProducer
from app.streaming.consumers.client import KafkaEventConsumer
from app.streaming.websocket.adapter import kafka_to_ws_broadcaster
from app.streaming.processor.telemetry import TelemetryProcessor
from app.api.v1.rest_routes import router as rest_router

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

    # FIXED: Added missing comma and cleaned out duplicate string literals
    target_domain_topics = [
        "ev.telemetry",
        "ev.battery",
        "ev.location",
        "ev.charging",
        "ev.status",
        "ev.alerts",
        "ev.diagnostics"
    ]
    
    # Register the live debug output print callback across all domain streams
    for domain_topic in target_domain_topics:
        kafka_consumer.register_callback(domain_topic, kafka_to_ws_broadcaster)
        logger.debug(f"Registered WebSocket broadcaster hook for topic: {domain_topic}")

    # Instantiate the new database persistence bridge worker
    telemetry_processor = TelemetryProcessor()

    # Domain specific callback routing matrix mapping
    # Every channel triggers BOTH the real-time WebSocket pipe AND the TimescaleDB storage engine
    kafka_consumer.register_callback("ev.telemetry", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.telemetry", telemetry_processor.process_kinematics)

    kafka_consumer.register_callback("ev.battery", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.battery", telemetry_processor.process_battery)

    kafka_consumer.register_callback("ev.location", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.location", telemetry_processor.process_location)

    kafka_consumer.register_callback("ev.charging", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.charging", telemetry_processor.process_charging)

    # For channels that do not have repositories yet, keep the legacy console broadcast active
    kafka_consumer.register_callback("ev.status", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.alerts", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.diagnostics", kafka_to_ws_broadcaster)

    # 3. Start Downstream First (Kafka)
    await kafka_producer.start()
    await kafka_consumer.start()
    
    # 4. Start Upstream Last (MQTT Ingestion)
    await mqtt_client.start()
    
    logger.info("Platform streaming layer fully operational.")
    
    yield  # Application runs here

    logger.info("Initiating graceful shutdown sequence...")
    
    # 5. Stop Upstream First (Halt new ingestion)
    await mqtt_client.stop()
    
    # 6. Stop Consumers (Halt internal processing)
    await kafka_consumer.stop()
    
    # 7. Stop Downstream Last (Flush pending producer batches)
    await kafka_producer.stop()
    
    logger.info("Shutdown complete. All connections closed safely.")

# Initialize the FastAPI application
app = FastAPI(title="Industrial EV AI Platform - Streaming Layer", lifespan=lifespan)

# Include core routers
app.include_router(health_router)
app.include_router(ws_router)

app.include_router(rest_router)
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
# import logging
# from fastapi import APIRouter, WebSocket, WebSocketDisconnect
# from app.streaming.websocket.manager import ws_manager

# logger = logging.getLogger(__name__)
# router = APIRouter()

# @router.websocket("/ws/dashboard")
# async def dashboard_websocket_endpoint(websocket: WebSocket) -> None:
#     """
#     WebSocket endpoint for the React frontend.
#     Expects incoming JSON commands: {"action": "subscribe", "topic": "telemetry.raw"}
#     """
#     await ws_manager.connect(websocket)
    
#     try:
#         while True:
#             # Wait for control commands from the client
#             data = await websocket.receive_json()
#             action = data.get("action")
#             topic = data.get("topic")
            
#             if action == "subscribe" and topic:
#                 await ws_manager.subscribe(websocket, topic)
#             elif action == "unsubscribe" and topic:
#                 await ws_manager.unsubscribe(websocket, topic)
                
#     except WebSocketDisconnect:
#         ws_manager.disconnect(websocket)
#     except Exception as e:
#         logger.error("WebSocket connection error.", exc_info=True)
#         ws_manager.disconnect(websocket)

import logging
import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.streaming.websocket.manager import ws_manager

logger = logging.getLogger(__name__)
router = APIRouter()

@router.websocket("/ws/dashboard")
async def dashboard_websocket_endpoint(websocket: WebSocket) -> None:
    """
    WebSocket endpoint for the React frontend.
    Logs traffic to the terminal for debugging without a UI.
    """
    await ws_manager.connect(websocket)
    logger.info("=== [TESTING] Terminal Client Connected to Dashboard Stream ===")
    
    try:
        while True:
            data = await websocket.receive_json()
            action = data.get("action")
            topic = data.get("topic")
            
            if action == "subscribe" and topic:
                await ws_manager.subscribe(websocket, topic)
                print(f"\n[SUBSCRIPTION] Client listening to Kafka topic: {topic}")
            elif action == "unsubscribe" and topic:
                await ws_manager.unsubscribe(websocket, topic)
                print(f"\n[UNSUBSCRIPTION] Client stopped listening to Kafka topic: {topic}")
                
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
        logger.info("=== [TESTING] Terminal Client Disconnected ===")
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

## app\core\config.py

```python
from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MqttSettings(BaseSettings):
    host: str = Field(default="localhost")
    port: int = Field(default=1883)
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    keepalive: int = Field(default=60)
    client_id: str = Field(default="industrial_ev_streaming_layer")


class KafkaSettings(BaseSettings):
    bootstrap_servers: List[str] = Field(default=["localhost:9092"])
    group_id: str = Field(default="ev_streaming_group")
    auto_offset_reset: str = Field(default="earliest")


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__", extra="ignore")
    database_url: str = "postgresql+asyncpg://ev_admin:ev_password@localhost:5432/ev_platform"
    environment: str = Field(default="development")
    debug: bool = Field(default=False)
    mqtt: MqttSettings = MqttSettings()
    kafka: KafkaSettings = KafkaSettings()


settings = AppSettings()
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

## app\core\logging.py

```python
import sys
import logging
import json
from datetime import datetime, timezone
from app.core.config import settings


class JsonFormatter(logging.Formatter):
    """Formats log records as single-line JSON strings for production parsing."""
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        if hasattr(record, "correlation_id"):
            log_data["correlation_id"] = record.correlation_id
        if hasattr(record, "vehicle_id"):
            log_data["vehicle_id"] = record.vehicle_id
            
        return json.dumps(log_data)


import os

def setup_logging() -> None:
    """Initializes global logging configurations."""
    root_logger = logging.getLogger()
    
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        
    handler = logging.StreamHandler(sys.stdout)
    
    # Check for custom LOG_LEVEL env var first
    env_log_level = os.getenv("LOG_LEVEL")
    if env_log_level:
        level = getattr(logging, env_log_level.upper(), logging.INFO)
    else:
        level = logging.DEBUG if getattr(settings, "debug", False) else logging.INFO
    
    if hasattr(settings, "environment") and settings.environment.lower() == "production":
        handler.setFormatter(JsonFormatter())
        root_logger.setLevel(level)
    else:
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        root_logger.setLevel(level)
        
    root_logger.addHandler(handler)
    
    logging.getLogger("aiokafka").setLevel(logging.WARNING)
    logging.getLogger("aiomqtt").setLevel(logging.WARNING)
```

---

## app\db\init_timescale.py

```python
import asyncio
import logging
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings
from app.models.domain import Base

logger = logging.getLogger(__name__)

# Ensure your settings point to asyncpg: "postgresql+asyncpg://user:pass@localhost:5432/ev_platform"
DATABASE_URL = settings.database_url 

async def init_db():
    logger.info("Initializing database and TimescaleDB hypertables...")
    engine = create_async_engine(DATABASE_URL, echo=True)

    async with engine.begin() as conn:
        # 1. Create standard PostgreSQL tables
        await conn.run_sync(Base.metadata.create_all)
        
        logger.info("Standard tables created. Converting time-series tables to TimescaleDB hypertables...")

        # 2. Execute TimescaleDB Hypertable conversion commands
        # The 'IF NOT EXISTS' equivalent in Timescale is handled by checking if it's already a hypertable,
        # but create_hypertable has a 'if_not_exists' flag we can use.
        hypertable_queries = [
            "SELECT create_hypertable('telemetry_records', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('battery_records', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('location_history', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('status_history', 'timestamp', if_not_exists => TRUE);"
        ]

        for query in hypertable_queries:
            try:
                # We use text() wrapper for raw SQL in SQLAlchemy 2.0
                from sqlalchemy import text
                await conn.execute(text(query))
            except Exception as e:
                # If TimescaleDB extension is missing, this will catch and warn you
                logger.warning(f"Failed to create hypertable (ensure TimescaleDB extension is enabled): {e}")

    await engine.dispose()
    logger.info("Database initialization complete.")

if __name__ == "__main__":
    asyncio.run(init_db())
```

---

## app\db\session.py

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

# 1. Create the Async Engine
engine = create_async_engine(
    settings.database_url,
    echo=False,  # Set to True for debugging SQL queries
    pool_size=20, # Connection pool optimized for high-throughput streaming
    max_overflow=10
)

# 2. Create the Async Session Maker
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False # Prevents SQLAlchemy from issuing extra SELECTs after commit
)

# 3. Dependency function for FastAPI routes and Kafka processors
async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session
```

---

## app\models\domain.py

```python
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# ---------------------------------------------------------
# TIME-SERIES HYPERTABLE MODELS (High-Frequency Data)
# ---------------------------------------------------------

class TelemetryRecord(Base):
    __tablename__ = "telemetry_records"

    # TimescaleDB requires the time column in the primary key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    speed_kph = Column(Float, nullable=False)
    odometer_km = Column(Float, nullable=False)
    motor_temperature_c = Column(Float, nullable=False)
    torque_nm = Column(Float, nullable=False)
    inverter_efficiency = Column(Float, nullable=False)

class BatteryRecord(Base):
    __tablename__ = "battery_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    state_of_charge_pct = Column(Float, nullable=False)
    state_of_health_pct = Column(Float, nullable=False)
    voltage = Column(Float, nullable=False)
    current_amps = Column(Float, nullable=False)
    cell_temperature_max_c = Column(Float, nullable=False)
    internal_resistance_ohm = Column(Float, nullable=False)

class LocationHistory(Base):
    __tablename__ = "location_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    altitude_m = Column(Float, nullable=True)
    heading_deg = Column(Integer, nullable=True)
    gps_fix_quality = Column(String(20), nullable=True)

class StatusHistory(Base):
    __tablename__ = "status_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    operational_status = Column(String(50), nullable=False)
    active_error_codes = Column(JSON, default=list)
    driver_id = Column(String(50), nullable=True)

# ---------------------------------------------------------
# RELATIONAL MODELS (Low-Frequency / State Data)
# ---------------------------------------------------------

class ChargingSession(Base):
    __tablename__ = "charging_sessions"

    # Standard relational table: only ID is the primary key
    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, name="id")
    vehicle_id = Column(String(50), nullable=False, index=True)
    charger_id = Column(String(50), nullable=True)
    
    start_time = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    end_time = Column(DateTime(timezone=True), nullable=True)
    
    status = Column(String(20), nullable=False, default="ACTIVE") # ACTIVE, COMPLETED, FAILED
    energy_consumed_kwh = Column(Float, nullable=True, default=0.0)
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

## app\repositories\domain.py

```python
from typing import List, Optional, Dict, Any
from datetime import datetime
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

class TelemetryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: TelemetryRecord) -> None:
        """High-speed async insert for kinematic telemetry."""
        self.session.add(record)
        await self.session.commit()

    async def history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Retrieves raw kinematics history within a time window."""
        stmt = (
            select(TelemetryRecord)
            .where(
                TelemetryRecord.vehicle_id == vehicle_id,
                TelemetryRecord.timestamp >= start_time,
                TelemetryRecord.timestamp <= end_time
            )
            .order_by(desc(TelemetryRecord.timestamp))
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def timeseries_aggregation(self, vehicle_id: str, interval: str = "1 hour", limit: int = 24) -> List[Dict[str, Any]]:
        """
        Uses TimescaleDB's native time_bucket function to aggregate data efficiently.
        Returns the average speed and max motor temperature per time bucket.
        """
        # FIX: Changed FROM ev_telemetry to FROM telemetry_records to match domain.py
        query = text("""
            SELECT 
                time_bucket(CAST(:interval AS INTERVAL), timestamp) AS time_bucket,
                AVG(speed_kph) AS avg_speed,
                MAX(motor_temperature_c) AS max_motor_temp,
                AVG(torque_nm) AS avg_torque
            FROM telemetry_records
            WHERE vehicle_id = :vehicle_id
            GROUP BY time_bucket
            ORDER BY time_bucket DESC
            LIMIT :limit;
        """)
        
        result = await self.session.execute(query, {"interval": interval, "vehicle_id": vehicle_id, "limit": limit})
        
        return [
            {"time": row[0], "avg_speed": round(row[1], 2) if row[1] is not None else 0.0, "max_temp": round(row[2], 2) if row[2] is not None else 0.0} 
            for row in result.fetchall()
        ]


class BatteryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: BatteryRecord) -> None:
        """High-speed async insert for electro-chemical metrics."""
        self.session.add(record)
        await self.session.commit()

    async def latest(self, vehicle_id: str) -> Optional[BatteryRecord]:
        """Fetches the absolute latest battery state."""
        stmt = (
            select(BatteryRecord)
            .where(BatteryRecord.vehicle_id == vehicle_id)
            .order_by(desc(BatteryRecord.timestamp))
            .limit(1)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def degradation_history(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[Dict[str, Any]]:
        """
        Calculates daily State of Health (SoH) degradation and Internal Resistance growth.
        """
        query = text("""
            SELECT
                time_bucket('1 day', timestamp) AS day,
                MIN(state_of_health_pct) as min_soh,
                MAX(internal_resistance_ohm) as max_resistance
            FROM battery_records
            WHERE vehicle_id = :vehicle_id AND timestamp >= :start AND timestamp <= :end
            GROUP BY day
            ORDER BY day ASC;
        """)
        
        result = await self.session.execute(
            query, {"vehicle_id": vehicle_id, "start": start_time, "end": end_time}
        )
        return [{"date": row[0], "soh_pct": float(row[1]), "resistance_ohm": float(row[2])} for row in result.fetchall()]


class LocationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: LocationHistory) -> None:
        self.session.add(record)
        await self.session.commit()

    async def route_playback(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """Retrieves an ordered path of coordinates for map playback."""
        stmt = (
            select(LocationHistory)
            .where(
                LocationHistory.vehicle_id == vehicle_id,
                LocationHistory.timestamp >= start_time,
                LocationHistory.timestamp <= end_time
            )
            .order_by(LocationHistory.timestamp)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()


class ChargingRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_session(self, session_record: ChargingSession) -> ChargingSession:
        """Initializes a new charging session."""
        self.session.add(session_record)
        await self.session.commit()
        await self.session.refresh(session_record)
        return session_record

    async def complete_session(self, session_id: str, end_time: datetime, total_kwh: float) -> Optional[ChargingSession]:
        """Updates an active charging session to COMPLETED."""
        stmt = select(ChargingSession).where(ChargingSession.session_id == session_id)
        result = await self.session.execute(stmt)
        charging_session = result.scalar_one_or_none()
        
        if charging_session:
            charging_session.end_time = end_time
            charging_session.energy_consumed_kwh = total_kwh
            charging_session.status = "COMPLETED"
            await self.session.commit()
            
        return charging_session
```

---

## app\schemas\payloads.py

```python
# from typing import Dict, Any, Optional
# from pydantic import BaseModel, Field

# class TelemetryPayload(BaseModel):
#     """Core kinematic data from the vehicle's engine and operational control units."""
#     speed_kph: float = Field(..., ge=0, le=200)
#     odometer_km: float = Field(..., ge=0)
#     motor_temperature_c: float = Field(..., ge=-40, le=150)
#     torque_nm: float = Field(...)
#     inverter_efficiency: float = Field(..., ge=0, le=1)


# class BatteryPayload(BaseModel):
#     """Real-time electro-chemical battery state statistics."""
#     state_of_charge_pct: float = Field(..., ge=0, le=100)
#     state_of_health_pct: float = Field(..., ge=0, le=100)
#     voltage: float = Field(..., ge=0, le=1000)
#     current_amps: float = Field(...)
#     cell_temperature_max_c: float = Field(..., ge=-40, le=100)
#     internal_resistance_ohm: float = Field(..., ge=0)


# class LocationPayload(BaseModel):
#     """High-precision positional telemetry coordinate data."""
#     latitude: float = Field(..., ge=-90, le=90)
#     longitude: float = Field(..., ge=-180, le=180)
#     altitude_m: float = Field(..., ge=-500, le=9000)
#     heading_deg: float = Field(..., ge=0, le=360)
#     gps_fix_quality: int = Field(..., description="0=Invalid, 1=GPS, 2=DGPS")


# class ChargingPayload(BaseModel):
#     """State management metrics during an active battery charging session."""
#     charger_id: str = Field(...)
#     charging_rate_kw: float = Field(..., ge=0)
#     time_to_full_mins: float = Field(..., ge=0)
#     connector_type: str = Field(..., description="CCS2, Megawatt, etc.")


# class StatusPayload(BaseModel):
#     """High-level operating mode state flags."""
#     operational_status: str = Field(..., description="READY, OPERATIONAL, FAULT, OFFLINE")
#     active_error_codes: list[str] = Field(default_factory=list)
#     driver_id: Optional[str] = Field(default=None)


# class AlertsPayload(BaseModel):
#     """Immediate hardware or safety critical notifications."""
#     alert_code: str = Field(...)
#     severity: str = Field(..., description="INFO, WARNING, CRITICAL")
#     component: str = Field(..., description="BATTERY, MOTOR, BRAKES, POWERTRAIN")
#     description: str = Field(...)


# class HeartbeatPayload(BaseModel):
#     """Lightweight diagnostics asserting infrastructure network health."""
#     uptime_seconds: int = Field(..., ge=0)
#     firmware_version: str = Field(...)
#     signal_strength_dbm: int = Field(..., le=0)



from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field, ConfigDict

# 1. CREATE THE BASE CLASS
class BasePayload(BaseModel):
    """Base configuration allowing both old aliases and new enterprise keys, while keeping extra data."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")

# 2. INHERIT FROM BasePayload (not BaseModel) FOR ALL YOUR SCHEMAS

class TelemetryPayload(BasePayload):
    """Kinematic data mapping simulator inputs to system targets with safe defaults."""
    speed_kph: float = Field(default=0.0, validation_alias="speed", ge=0, le=200)
    odometer_km: float = Field(default=0.0, validation_alias="odometer", ge=0)
    motor_temperature_c: float = Field(default=65.0, validation_alias="ambient_temperature", ge=-40, le=150)
    # Simulator doesn't provide torque or efficiency yet; generate clean platform mock defaults
    torque_nm: float = Field(default=210.5, description="Fallback tracking default")
    inverter_efficiency: float = Field(default=0.94, ge=0, le=1)

class BatteryPayload(BasePayload):
    """Electro-chemical stats providing field transformations for native simulator outputs."""
    state_of_charge_pct: float = Field(..., validation_alias="soc", ge=0, le=100)
    state_of_health_pct: float = Field(..., validation_alias="soh", ge=0, le=100)
    voltage: float = Field(..., ge=0, le=1000)
    current_amps: float = Field(..., validation_alias="current")
    cell_temperature_max_c: float = Field(..., validation_alias="cell_temperature", ge=-40, le=100)
    internal_resistance_ohm: float = Field(..., validation_alias="internal_resistance", ge=0)

class LocationPayload(BasePayload):
    """Positional mapping supporting clean initialization blocks for empty topics."""
    latitude: float = Field(default=39.7392, ge=-90, le=90)
    longitude: float = Field(default=-104.9903, ge=-180, le=180)
    altitude_m: float = Field(default=1609.0, ge=-500, le=9000)
    heading_deg: float = Field(default=0.0, ge=0, le=360)
    gps_fix_quality: int = Field(default=1)

class ChargingPayload(BasePayload):
    """Fallback charging structures for silent initialization loops."""
    charger_id: str = Field(default="CHG-STATION-MOCK")
    charging_rate_kw: float = Field(default=0.0, ge=0)
    time_to_full_mins: float = Field(default=0.0, ge=0)
    connector_type: str = Field(default="CCS2")

class StatusPayload(BasePayload):
    operational_status: str = Field(default="OPERATIONAL")
    active_error_codes: List[str] = Field(default_factory=list)
    driver_id: Optional[str] = Field(default="SYSTEM_AUTO")

class AlertsPayload(BasePayload):
    alert_code: str = Field(default="CLR_00")
    severity: str = Field(default="INFO")
    component: str = Field(default="SYSTEM")
    description: str = Field(default="Healthy baseline initialization status.")

class HeartbeatPayload(BasePayload):
    uptime_seconds: int = Field(default=0, ge=0)
    firmware_version: str = Field(default="v1.0.0-mock")
    signal_strength_dbm: int = Field(default=-50, le=0)
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

## app\services\telemetry.py

```python
from datetime import datetime
from typing import List, Dict, Any, Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.domain import (
    TelemetryRepository,
    BatteryRepository,
    LocationRepository,
    ChargingRepository
)
from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

# ---------------------------------------------------------
# BUSINESS LOGIC & VALIDATION RULES
# ---------------------------------------------------------

def validate_time_window(start_time: datetime, end_time: datetime, max_days: int = 30) -> None:
    """Enforces strict boundaries on historical queries to prevent database memory exhaustion."""
    if start_time > end_time:
        raise HTTPException(
            status_code=400, 
            detail="Invalid request: start_time cannot be later than end_time."
        )
    
    delta = end_time - start_time
    if delta.days > max_days:
        raise HTTPException(
            status_code=400, 
            detail=f"Query rejected: Requested time range of {delta.days} days exceeds the maximum allowed window of {max_days} days."
        )

# ---------------------------------------------------------
# DOMAIN SERVICES
# ---------------------------------------------------------

class TelemetryService:
    def __init__(self, session: AsyncSession):
        self.repo = TelemetryRepository(session)

    async def get_history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Validates the time window before fetching raw kinematic history."""
        validate_time_window(start_time, end_time, max_days=30)
        return await self.repo.history(vehicle_id, start_time, end_time, limit)

    async def get_timeseries(self, vehicle_id: str, interval: str = "1 hour", limit: int = 24) -> List[Dict[str, Any]]:
        """Pass-through for aggregated time-series data."""
        # TimescaleDB handles intervals safely, but we cap the limit to prevent runaway aggregations
        safe_limit = min(limit, 1000) 
        return await self.repo.timeseries_aggregation(vehicle_id, interval, safe_limit)


class BatteryService:
    def __init__(self, session: AsyncSession):
        self.repo = BatteryRepository(session)

    async def get_latest(self, vehicle_id: str) -> Optional[BatteryRecord]:
        """Fetches the current real-time state of the battery."""
        record = await self.repo.latest(vehicle_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"No battery telemetry found for vehicle {vehicle_id}")
        return record

    async def get_degradation(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[Dict[str, Any]]:
        """
        Battery degradation occurs slowly, so we allow a longer 90-day analytics window 
        specifically for this aggregated query.
        """
        validate_time_window(start_time, end_time, max_days=90)
        return await self.repo.degradation_history(vehicle_id, start_time, end_time)


class LocationService:
    def __init__(self, session: AsyncSession):
        self.repo = LocationRepository(session)

    async def get_route(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """
        GPS route playback queries pull dense datasets. 
        We enforce a strict 7-day maximum window to protect bandwidth and memory.
        """
        validate_time_window(start_time, end_time, max_days=7)
        return await self.repo.route_playback(vehicle_id, start_time, end_time)
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

## app\api\v1\rest_routes.py

```python
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.db.session import get_db_session
from app.services.telemetry import TelemetryService, BatteryService, LocationService
from app.repositories.domain import ChargingRepository
from app.models.domain import ChargingSession

router = APIRouter(prefix="/api/v1", tags=["Telemetry & Domain Data"])

# ---------------------------------------------------------
# REQUEST SCHEMAS
# ---------------------------------------------------------
class ChargingSessionCreate(BaseModel):
    vehicle_id: str
    charger_id: str

# ---------------------------------------------------------
# TELEMETRY ENDPOINTS
# ---------------------------------------------------------

@router.get("/telemetry/latest")
async def get_latest_telemetry(
    vehicle_id: str,
    session: AsyncSession = Depends(get_db_session)
):
    """Returns the most recent kinematics reading for a specific vehicle."""
    service = TelemetryService(session)
    # We query history with a limit of 1 over the last 24 hours to find the absolute latest
    end = datetime.utcnow()
    start = end - timedelta(days=1)
    
    records = await service.get_history(vehicle_id, start_time=start, end_time=end, limit=1)
    if not records:
        raise HTTPException(status_code=404, detail="No recent telemetry found for this vehicle.")
    return records[0]


@router.get("/telemetry/timeseries")
async def get_telemetry_timeseries(
    vehicle_id: str,
    interval: str = Query("1 hour", description="TimescaleDB interval (e.g., '15 minutes', '1 hour')"),
    limit: int = Query(24, le=1000),
    session: AsyncSession = Depends(get_db_session)
):
    """Returns aggregated kinematic metrics grouped by time buckets for charting."""
    service = TelemetryService(session)
    return await service.get_timeseries(vehicle_id, interval=interval, limit=limit)

# ---------------------------------------------------------
# BATTERY ENDPOINTS
# ---------------------------------------------------------

@router.get("/battery/latest")
async def get_latest_battery(
    vehicle_id: str,
    session: AsyncSession = Depends(get_db_session)
):
    """Returns the absolute real-time State of Charge and Health for the battery."""
    service = BatteryService(session)
    return await service.get_latest(vehicle_id)

# ---------------------------------------------------------
# LOCATION ENDPOINTS
# ---------------------------------------------------------

@router.get("/location/history")
async def get_location_history(
    vehicle_id: str,
    start_time: datetime,
    end_time: datetime,
    session: AsyncSession = Depends(get_db_session)
):
    """Retrieves an ordered array of GPS coordinates for map route playback."""
    service = LocationService(session)
    return await service.get_route(vehicle_id, start_time, end_time)

# ---------------------------------------------------------
# CHARGING ENDPOINTS
# ---------------------------------------------------------

@router.post("/charging/session")
async def start_charging_session(
    payload: ChargingSessionCreate,
    session: AsyncSession = Depends(get_db_session)
):
    """Initializes a new charging session in the database with explicit timestamping."""
    repo = ChargingRepository(session)
    new_session = ChargingSession(
        vehicle_id=payload.vehicle_id,
        charger_id=payload.charger_id,
        start_time=datetime.utcnow(),  # Add this explicit timestamp
        status="ACTIVE",
        energy_consumed_kwh=0.0
    )
    return await repo.create_session(new_session)
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

    def __init__(self) -> None:
        self.consumer = None
        self._consume_task = None
        
        # UNIFIED NAME: Changed from self.valid_topics to self.ALLOWED_TOPICS
        self.ALLOWED_TOPICS = {
            "ev.telemetry",
            "ev.battery",
            "ev.location",
            "ev.charging",
            "ev.status",
            "ev.alerts",
            "ev.diagnostics"
        }
        
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
        
        # *self.ALLOWED_TOPICS safely unpacks the set values as independent string arguments
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
# import asyncio
# import logging
# from typing import Optional
# import aiomqtt
# from aiomqtt.exceptions import MqttError


# from app.core.config import settings
# from app.streaming.serializers.validator import TOPIC_SCHEMA_MAP, validate_raw_payload
# from app.streaming.serializers.normalizer import normalize_to_envelope, MQTT_TO_KAFKA_ROUTE
# from app.core.container import container

# logger = logging.getLogger(__name__)

# class MqttIngestionClient:
#     """Async MQTT client handling simulator data ingestion."""
    
#     def __init__(self) -> None:
#         self.client: Optional[aiomqtt.Client] = None
#         self._consume_task: Optional[asyncio.Task] = None
#         # Derive immutable topics directly from our Phase 2 schema map
#         self.topics = list(TOPIC_SCHEMA_MAP.keys())

#     async def start(self) -> None:
#         """Establishes broker connection and initiates the listener task."""
#         logger.info("Initializing MQTT ingestion client...")
        
#         self.client = aiomqtt.Client(
#             hostname=settings.mqtt.host,
#             port=settings.mqtt.port,
#             username=settings.mqtt.username,
#             password=settings.mqtt.password,
#             identifier=settings.mqtt.client_id,
#             keepalive=settings.mqtt.keepalive
#         )
        
#         try:
#             await self.client.connect()
#             logger.info("Connected to Mosquitto broker.", extra={"broker": settings.mqtt.host})
            
#             # Spin up the background listening loop
#             self._consume_task = asyncio.create_task(self._consume_loop())
#         except MqttError as e:
#             logger.critical("Failed to connect to MQTT broker.", exc_info=True)
#             raise

#     async def stop(self) -> None:
#         """Gracefully tears down the consumption task and broker connection."""
#         if self._consume_task:
#             self._consume_task.cancel()
#             try:
#                 await self._consume_task
#             except asyncio.CancelledError:
#                 pass
                
#         if self.client:
#             await self.client.disconnect()
#             logger.info("Disconnected from Mosquitto broker.")

#     async def _consume_loop(self) -> None:
#         """Background loop that subscribes to topics and awaits messages."""
#         if not self.client:
#             return

#         try:
#             async with self.client.messages() as messages:
#                 # 1. Subscribe to the strictly required, immutable topics
#                 for topic in self.topics:
#                     await self.client.subscribe(topic)
#                     logger.info("Subscribed to MQTT topic", extra={"mqtt_topic": topic})
                    
#                 # 2. Continuous asynchronous event consumption
#                 async for message in messages:
#                     self._process_message(message)
                    
#         except asyncio.CancelledError:
#             logger.info("MQTT consumption task gracefully cancelled.")
#         except MqttError as e:
#             logger.error("MQTT connection lost during consumption.", exc_info=True)
#             # In a production environment, this is where we would trigger an exponential backoff reconnect

#     def _process_message(self, message: aiomqtt.Message) -> None:
#         """Routes incoming messages through validation, normalization, and publishing."""
#         topic = str(message.topic)
#         payload_bytes = message.payload
        
#         if not isinstance(payload_bytes, bytes):
#             return

#         # 1. Validate
#         validated_model = validate_raw_payload(topic, payload_bytes)
        
#         if validated_model:
#             # 2. Normalize
#             envelope = normalize_to_envelope(topic, validated_model)
#             target_kafka_topic = MQTT_TO_KAFKA_ROUTE.get(topic, "telemetry.raw")
            
#             # 3. Publish asynchronously without blocking the MQTT consumption loop
#             kafka_producer = container.kafka_producer
#             asyncio.create_task(kafka_producer.publish(target_kafka_topic, envelope)) 

import asyncio
import logging
from typing import Optional
import aiomqtt
from aiomqtt.exceptions import MqttError

from app.core.config import settings
from app.streaming.serializers.validator import TOPIC_SCHEMA_MAP, validate_raw_payload
from app.streaming.serializers.normalizer import normalize_to_envelope, MQTT_TO_KAFKA_ROUTE
from app.core.container import container

logger = logging.getLogger(__name__)

class MqttIngestionClient:
    """Async MQTT client handling simulator data ingestion using modern context managers."""
    
    def __init__(self) -> None:
        self._consume_task: Optional[asyncio.Task] = None
        self.topics = list(TOPIC_SCHEMA_MAP.keys())

    async def start(self) -> None:
        """Kicks off the background telemetry consumption loop task."""
        logger.info("Initializing MQTT ingestion client background engine...")
        # Spin up the connection loop in a non-blocking background task
        self._consume_task = asyncio.create_task(self._consume_loop())

    async def stop(self) -> None:
        """Gracefully tears down the consumption task."""
        if self._consume_task:
            self._consume_task.cancel()
            try:
                await self._consume_task
            except asyncio.CancelledError:
                pass
            logger.info("MQTT consumption engine cleanly stopped.")

    async def _consume_loop(self) -> None:
        """Handles context-managed network connections and continuous ingestion loops."""
        logger.info("Connecting to Mosquitto Broker...", extra={"broker": settings.mqtt.host})
        
        try:
            # Modern aiomqtt 2.0+ requires context-managed lifecycles
            async with aiomqtt.Client(
                hostname=settings.mqtt.host,
                port=settings.mqtt.port,
                username=settings.mqtt.username,
                password=settings.mqtt.password,
                identifier=settings.mqtt.client_id,
                keepalive=settings.mqtt.keepalive
            ) as client:
                logger.info("Connected to Mosquitto broker successfully.")
                
                # 1. Subscribe to all fixed data topics
                for topic in self.topics:
                    await client.subscribe(topic)
                    logger.info("Subscribed to MQTT topic", extra={"mqtt_topic": topic})
                
                # 2. Consume incoming message frames asynchronously
                async for message in client.messages:
                    self._process_message(client, message)
                        
        except asyncio.CancelledError:
            logger.info("MQTT consumption loop task gracefully cancelled.")
        except MqttError as e:
            logger.error("MQTT broker connection dropped or encountered a network error.", exc_info=True)

    def _process_message(self, client: aiomqtt.Client, message: aiomqtt.Message) -> None:
        """Routes incoming raw binary messages through validation, normalization, and domain streams."""
        topic = str(message.topic)
        payload_bytes = message.payload
        
        if not isinstance(payload_bytes, bytes):
            return

        # 1. Structural Schema Validation Check
        validated_model = validate_raw_payload(topic, payload_bytes)
        
        if validated_model:
            # 2. Normalize and extract the target domain channel type
            envelope = normalize_to_envelope(topic, validated_model)
            
            # DYNAMIC ROUTING FIX: Grab the exact destination from the normalizer mapping
            target_kafka_topic = envelope.event_type
            
            # 3. Stream asynchronously straight onto the specific Kafka Topic Bus line
            kafka_producer = container.kafka_producer
            asyncio.create_task(kafka_producer.publish(target_kafka_topic, envelope))
```

---

## app\streaming\processor\telemetry.py

```python
import logging
from typing import Dict, Any
from datetime import datetime
from dateutil.parser import isoparse

from app.db.session import AsyncSessionLocal
from app.repositories.domain import (
    TelemetryRepository, 
    BatteryRepository, 
    LocationRepository, 
    ChargingRepository
)
from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

class TelemetryProcessor:
    """Bridges incoming Kafka EventEnvelope payloads to target domain database repositories."""

    @staticmethod
    def _parse_timestamp(ts_str: str) -> datetime:
        """Safely parses ISO-8601 UTC timestamp strings into Python datetime objects."""
        try:
            return isoparse(ts_str)
        except Exception:
            return datetime.utcnow()

    async def process_kinematics(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.telemetry' streams and persists kinematic vectors."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))

        logger.info(f"[PROCESSOR] Intercepted kinematics for vehicle {vehicle_id}")

        record = TelemetryRecord(
            vehicle_id=vehicle_id,
            timestamp=ts,
            speed_kph=float(payload.get("speed_kph", 0.0)),
            odometer_km=float(payload.get("odometer_km", 0.0)),
            motor_temperature_c=float(payload.get("motor_temperature_c", 0.0)),
            torque_nm=float(payload.get("torque_nm", 0.0)),
            inverter_efficiency=float(payload.get("inverter_efficiency", 1.0))
        )

        async with AsyncSessionLocal() as session:
            repo = TelemetryRepository(session)
            await repo.insert(record)

    async def process_battery(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.battery' streams and persists electro-chemical metrics."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))

        logger.info(f"[PROCESSOR] Intercepted battery diagnostics for vehicle {vehicle_id}")

        record = BatteryRecord(
            vehicle_id=vehicle_id,
            timestamp=ts,
            state_of_charge_pct=float(payload.get("state_of_charge_pct", 0.0)),
            state_of_health_pct=float(payload.get("state_of_health_pct", 100.0)),
            voltage=float(payload.get("voltage", 0.0)),
            current_amps=float(payload.get("current_amps", 0.0)),
            cell_temperature_max_c=float(payload.get("cell_temperature_max_c", 0.0)),
            internal_resistance_ohm=float(payload.get("internal_resistance_ohm", 0.0))
        )

        async with AsyncSessionLocal() as session:
            repo = BatteryRepository(session)
            await repo.insert(record)

    async def process_location(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.location' streams and persists geospatial telemetry chunks."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))

        logger.info(f"[PROCESSOR] Intercepted geospatial logs for vehicle {vehicle_id}")

        record = LocationHistory(
            vehicle_id=vehicle_id,
            timestamp=ts,
            latitude=float(payload.get("latitude", 0.0)),
            longitude=float(payload.get("longitude", 0.0)),
            altitude_m=float(payload.get("altitude_m", 0.0)) if payload.get("altitude_m") else None,
            heading_deg=int(payload.get("heading_deg", 0)) if payload.get("heading_deg") else None,
            gps_fix_quality=payload.get("gps_fix_quality", "UNKNOWN")
        )

        async with AsyncSessionLocal() as session:
            repo = LocationRepository(session)
            await repo.insert(record)

    async def process_charging(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.charging' infrastructure streams to manage session lifecycle state."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))
        
        charger_id = payload.get("charger_id")
        connector_type = payload.get("connector_type", "NONE")

        # In a real environment, you would check for an active session to see whether to create or update.
        # For this stage of the bridge ingestion path, we register the event log explicitly.
        if charger_id and connector_type != "NONE":
            logger.info(f"[PROCESSOR] Processing active charging payload for vehicle {vehicle_id}")
            record = ChargingSession(
                vehicle_id=vehicle_id,
                charger_id=charger_id,
                start_time=ts,
                status="ACTIVE",
                energy_consumed_kwh=float(payload.get("charging_rate_kw", 0.0)) / 60.0 # Instantaneous integration approximation
            )
            async with AsyncSessionLocal() as session:
                repo = ChargingRepository(session)
                await repo.create_session(record)
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
# import logging
# from typing import Dict
# from pydantic import BaseModel
# from app.contracts.envelope import EventEnvelope

# logger = logging.getLogger(__name__)

# # Map incoming MQTT topics to target Kafka topics/event types
# MQTT_TO_KAFKA_ROUTE: Dict[str, str] = {
#     "ev/telemetry": "telemetry.raw",
#     "ev/battery": "telemetry.raw",  # Routing battery data to the same raw firehose for now
#     "ev/location": "telemetry.raw",
#     "ev/charging": "telemetry.raw",
#     "ev/status": "telemetry.raw",
#     "ev/alerts": "alerts",
#     "ev/heartbeat": "telemetry.raw"
# }

# def normalize_to_envelope(mqtt_topic: str, payload: BaseModel) -> EventEnvelope:
#     """
#     Wraps a validated domain payload into the standard Event Envelope.
#     Generates event_id and correlation_id automatically via the schema defaults.
#     """
#     target_event_type = MQTT_TO_KAFKA_ROUTE.get(mqtt_topic, "unknown.raw")
    
#     # In a fully integrated environment, vehicle_id and fleet_id might be extracted
#     # from the MQTT topic structure (e.g., ev/telemetry/{fleet_id}/{vehicle_id}) 
#     # or the payload itself. Since our topics are fixed, we inject placeholders 
#     # for the infrastructure integration phase.
    
#     envelope = EventEnvelope(
#         event_type=target_event_type,
#         source="streaming_ingestion_node",
#         vehicle_id="VEH-SIM-001",
#         fleet_id="FLT-ALPHA-01",
#         payload=payload
#     )
    
#     logger.debug(
#         "Normalized event payload.",
#         extra={
#             "event_id": str(envelope.event_id),
#             "correlation_id": str(envelope.correlation_id),
#             "event_type": target_event_type
#         }
#     )
#     return envelope



import logging
from pydantic import BaseModel
from app.contracts.envelope import EventEnvelope

logger = logging.getLogger(__name__)

# Segmenting the single firehose into clean domain streams
MQTT_TO_KAFKA_ROUTE = {
    "ev/telemetry": "ev.telemetry",
    "ev/battery": "ev.battery",
    "ev/location": "ev.location",
    "ev/charging": "ev.charging",
    "ev/status": "ev.status",
    "ev/alerts": "ev.alerts",
    "ev/heartbeat": "ev.diagnostics"
}

def normalize_to_envelope(mqtt_topic: str, payload: BaseModel) -> EventEnvelope:
    """Wraps the validated payload and dynamically assigns its destination event_type."""
    target_event_type = MQTT_TO_KAFKA_ROUTE.get(mqtt_topic, "ev.unknown")
    
    extracted_vehicle = getattr(payload, "vehicle_id", "VEH-SIM-UNKNOWN")
    
    envelope = EventEnvelope(
        event_type=target_event_type,  # The envelope type now matches the domain stream name
        source="streaming_ingestion_node",
        vehicle_id=extracted_vehicle,
        fleet_id="FLT-ALPHA-01",
        payload=payload
    )
    
    logger.debug(
        "Normalized event payload targeted for domain topic.",
        extra={
            "event_id": str(envelope.event_id),
            "target_topic": target_event_type
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
logger.setLevel(logging.WARNING)

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
        
        # print(f"\n--- [LIVE BUS EVENT] Topic: {topic} ---")
        # print(json.dumps(payload, indent=2))
        # print("-" * 40)
        
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
