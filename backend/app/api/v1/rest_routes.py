from datetime import datetime, timedelta, timezone
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, Query, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.db.session import get_db_session
# FIX: Added ChargingService to the explicit imports list
from app.services.telemetry import TelemetryService, BatteryService, LocationService, ChargingService
from app.models.domain import TelemetryRecord, LocationHistory, ChargingSession

router = APIRouter(prefix="/api/v1", tags=["Telemetry & Domain Data"])

# ---------------------------------------------------------
# PYDANTIC INGESTION SCHEMAS
# ---------------------------------------------------------
class TelemetryManualInput(BaseModel):
    vehicle_id: str
    speed_kph: float
    odometer_km: float
    motor_temperature_c: float
    torque_nm: float

class LocationManualInput(BaseModel):
    vehicle_id: str
    latitude: float
    longitude: float
    altitude_m: float
    heading_deg: float
    gps_fix_quality: str

class ChargingSessionCreate(BaseModel):
    vehicle_id: str
    charger_id: str
    starting_soc: float = 0.0

class ChargingSessionUpdate(BaseModel):
    end_time: datetime
    energy_consumed_kwh: float
    ending_soc: float
    status: str = "COMPLETED"

# ---------------------------------------------------------
# WEBSOCKET BROADCAST MANAGER
# ---------------------------------------------------------
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast_event(self, message: Dict[str, Any]):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                pass

ws_manager = ConnectionManager()

@router.websocket("/ws/telemetry")
async def ws_telemetry_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)

# ---------------------------------------------------------
# 1. TELEMETRY APIS
# ---------------------------------------------------------
@router.post("/telemetry", status_code=201)
async def manual_telemetry_ingestion(payload: TelemetryManualInput, session: AsyncSession = Depends(get_db_session)):
    """Manual telemetry debug ingestion endpoint."""
    service = TelemetryService(session)
    record = TelemetryRecord(
        vehicle_id=payload.vehicle_id,
        timestamp=datetime.now(timezone.utc),
        speed_kph=payload.speed_kph,
        odometer_km=payload.odometer_km,
        motor_temperature_c=payload.motor_temperature_c,
        torque_nm=payload.torque_nm
    )
    await service.store_telemetry(record)
    
    await ws_manager.broadcast_event({
        "topic": "ev.telemetry",
        "vehicle_id": payload.vehicle_id,
        "payload": payload.model_dump()
    })
    # FIX: Return a clear status block instead of relying on unpopulated auto-increment hypertable fields
    return {"status": "SUCCESS", "vehicle_id": payload.vehicle_id}

@router.get("/telemetry/latest")
async def get_latest_telemetry(vehicle_id: str, session: AsyncSession = Depends(get_db_session)):
    service = TelemetryService(session)
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=1)
    
    records = await service.get_history(vehicle_id, start_time=start, end_time=end, limit=1)
    if not records:
        raise HTTPException(status_code=404, detail="No recent telemetry found for this vehicle.")
    return records[0]

@router.get("/telemetry/history")
async def get_telemetry_history(
    vehicle_id: str, 
    start_time: datetime, 
    end_time: datetime, 
    limit: int = Query(100, le=1000), 
    session: AsyncSession = Depends(get_db_session)
):
    service = TelemetryService(session)
    return await service.get_history(vehicle_id, start_time, end_time, limit)

@router.get("/telemetry/timeseries")
async def get_telemetry_timeseries(
    vehicle_id: str,
    interval: str = Query("1 minute", description="TimescaleDB interval block"),
    limit: int = Query(24, le=1000),
    session: AsyncSession = Depends(get_db_session)
):
    service = TelemetryService(session)
    return await service.get_timeseries(vehicle_id, interval=interval, limit=limit)

# ---------------------------------------------------------
# 2. CHARGING APIS
# ---------------------------------------------------------
@router.post("/charging/session", status_code=201)
async def start_charging_session(payload: ChargingSessionCreate, session: AsyncSession = Depends(get_db_session)):
    service = ChargingService(session)
    new_session = ChargingSession(
        vehicle_id=payload.vehicle_id,
        charger_id=payload.charger_id,
        start_time=datetime.now(timezone.utc),
        starting_soc=payload.starting_soc,
        status="ACTIVE",
        energy_consumed_kwh=0.0
    )
    return await service.create_charging_session(new_session)

@router.patch("/charging/session/{session_id}")
async def patch_charging_session(session_id: int, payload: ChargingSessionUpdate, session: AsyncSession = Depends(get_db_session)):
    service = ChargingService(session)
    # FIX: Converts returning updated object cleanly to prevent dictionary unpacking visualization errors
    result = await service.update_charging_session(session_id, payload.model_dump(exclude_unset=True))
    return result

@router.get("/charging/history")
async def get_charging_history(vehicle_id: str, session: AsyncSession = Depends(get_db_session)):
    service = ChargingService(session)
    return await service.get_charging_history(vehicle_id)

# ---------------------------------------------------------
# 3. LOCATION & BATTERY APIS
# ---------------------------------------------------------
@router.post("/location", status_code=201)
async def manual_location_ingestion(payload: LocationManualInput, session: AsyncSession = Depends(get_db_session)):
    service = LocationService(session)
    record = LocationHistory(
        vehicle_id=payload.vehicle_id,
        timestamp=datetime.now(timezone.utc),
        latitude=payload.latitude,
        longitude=payload.longitude,
        altitude_m=payload.altitude_m,
        heading_deg=payload.heading_deg,
        gps_fix_quality=payload.gps_fix_quality
    )
    await service.store_location(record)
    # FIX: Clean static layout response dictionary target
    return {"status": "SUCCESS", "vehicle_id": payload.vehicle_id}

@router.get("/location/latest")
async def get_latest_location(vehicle_id: str, session: AsyncSession = Depends(get_db_session)):
    service = LocationService(session)
    # FIX: Gracefully evaluate fallback range checks to prevent driver crashes
    try:
        return await service.get_latest_location(vehicle_id)
    except Exception:
        # Fallback to standard range tracking if direct lookup encounters layout limitations
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=1)
        records = await service.get_route(vehicle_id, start, end)
        if not records:
            raise HTTPException(status_code=404, detail="No recent location found for this vehicle.")
        return records[0]

@router.get("/location/history")
async def get_location_history(vehicle_id: str, start_time: datetime, end_time: datetime, session: AsyncSession = Depends(get_db_session)):
    service = LocationService(session)
    return await service.get_route(vehicle_id, start_time, end_time)

@router.get("/battery/latest")
async def get_latest_battery(vehicle_id: str, session: AsyncSession = Depends(get_db_session)):
    service = BatteryService(session)
    return await service.get_latest(vehicle_id)