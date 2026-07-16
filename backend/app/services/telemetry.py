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

    async def store_telemetry(self, record: TelemetryRecord) -> TelemetryRecord:
        """Stores a raw manual telemetry record (Requirement 9)."""
        return await self.repo.insert(record)

    async def get_history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Validates the time window before fetching raw kinematic history."""
        validate_time_window(start_time, end_time, max_days=30)
        return await self.repo.history(vehicle_id, start_time, end_time, limit)

    async def get_timeseries(self, vehicle_id: str, interval: str = "1 hour", limit: int = 24) -> List[Dict[str, Any]]:
        """Pass-through for aggregated time-series data."""
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
        """Battery degradation analytics window over a longer timeframe."""
        validate_time_window(start_time, end_time, max_days=90)
        return await self.repo.degradation_history(vehicle_id, start_time, end_time)


class LocationService:
    def __init__(self, session: AsyncSession):
        self.repo = LocationRepository(session)

    async def store_location(self, record: LocationHistory) -> LocationHistory:
        """Stores a manual GPS coordinate update (Requirement 9)."""
        return await self.repo.insert(record)

    async def get_latest_location(self, vehicle_id: str) -> Optional[LocationHistory]:
        """Retrieves the latest known vehicle position (Requirement 9)."""
        record = await self.repo.get_latest(vehicle_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"No location metrics found for vehicle {vehicle_id}")
        return record

    async def get_route(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """GPS route playback engine tracking sequence loops."""
        validate_time_window(start_time, end_time, max_days=7)
        return await self.repo.route_playback(vehicle_id, start_time, end_time)

class ChargingService:
    def __init__(self, session: AsyncSession):
        self.repo = ChargingRepository(session)

    async def create_charging_session(self, session_record: ChargingSession) -> ChargingSession:
        return await self.repo.create_session(session_record)

    async def update_charging_session(self, session_id: int, updates: Dict[str, Any]) -> ChargingSession:
        """Applies updates to an active session, raising a clean 404 if the target ID is missing."""
        updated = await self.repo.update_session(session_id, updates)
        if not updated:
            raise HTTPException(
                status_code=404, 
                detail=f"Active tracking session ID {session_id} does not exist in the database system."
            )
        return updated

    async def get_charging_history(self, vehicle_id: str) -> List[ChargingSession]:
        """Pulls comprehensive charging history arrays, safely returning empty arrays if none exist."""
        records = await self.repo.get_history(vehicle_id)
        return records if records is not None else []