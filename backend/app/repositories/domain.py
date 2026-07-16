from typing import List, Optional, Dict, Any
from datetime import datetime
from sqlalchemy import select, desc, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

class TelemetryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: TelemetryRecord) -> TelemetryRecord:
        """Stores a single telemetry record."""
        self.session.add(record)
        await self.session.commit()
        return record

    async def bulk_insert(self, records: List[TelemetryRecord]) -> None:
        """Handles high-throughput batch writes efficiently (Requirement 8)."""
        self.session.add_all(records)
        await self.session.commit()

    async def timeseries_aggregation(self, vehicle_id: str, interval: str = "1 minute", limit: int = 24) -> List[Dict[str, Any]]:
        """Uses TimescaleDB's native time_bucket function to aggregate data efficiently."""
        query = text("""
            SELECT 
                time_bucket(CAST(CAST(:bucket_interval AS TEXT) AS INTERVAL), timestamp) AS time_bucket,
                AVG(voltage) AS avg_speed,
                MAX(temperature) AS max_motor_temp,
                AVG(soc) AS avg_torque
            FROM telemetry
            WHERE vehicle_id = :vehicle_id
            GROUP BY time_bucket
            ORDER BY time_bucket DESC
            LIMIT :limit;
        """)
        
        result = await self.session.execute(
            query, 
            {
                "bucket_interval": str(interval),
                "vehicle_id": str(vehicle_id), 
                "limit": int(limit)
            }
        )
        
        return [
            {
                "time": row[0].isoformat() if hasattr(row[0], "isoformat") else str(row[0]), 
                "avg_speed": round(row[1], 2) if row[1] is not None else 0.0, 
                "max_temp": round(row[2], 2) if row[2] is not None else 0.0
            } 
            for row in result.fetchall()
        ]
    
    async def history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Retrieves raw telemetry history lines within an explicit time window."""
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
        return list(result.scalars().all())


class BatteryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: BatteryRecord) -> None:
        self.session.add(record)
        await self.session.commit()

    async def latest(self, vehicle_id: str) -> Optional[BatteryRecord]:
        stmt = (
            select(BatteryRecord)
            .where(BatteryRecord.vehicle_id == vehicle_id)
            .order_by(desc(BatteryRecord.timestamp))
            .limit(1)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()


class LocationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: LocationHistory) -> LocationHistory:
        """High-speed async insert for vehicle coordinates."""
        self.session.add(record)
        await self.session.commit()
        return record

    async def get_latest(self, vehicle_id: str) -> Optional[LocationHistory]:
        """Fetches absolute latest geographic trace coordinate node (Requirement 8)."""
        stmt = (
            select(LocationHistory)
            .where(LocationHistory.vehicle_id == vehicle_id)
            .order_by(desc(LocationHistory.timestamp))
            .limit(1)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def route_playback(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """Retrieves an ordered array of coordinates for spatial path tracking."""
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
        return list(result.scalars().all())
    

class ChargingRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_session(self, session_record: ChargingSession) -> ChargingSession:
        self.session.add(session_record)
        await self.session.commit()
        await self.session.refresh(session_record)
        return session_record

    async def update_session(self, session_id: int, updates: Dict[str, Any]) -> Optional[ChargingSession]:
        """Applies dynamic PATCH field changes to an active charging entity (Requirement 8)."""
        stmt = (
            update(ChargingSession)
            .where(ChargingSession.id == session_id)
            .values(**updates)
        )
        await self.session.execute(stmt)
        await self.session.commit()
        
        # Retrieve the updated model record cleanly
        fetch_stmt = select(ChargingSession).where(ChargingSession.id == session_id)
        result = await self.session.execute(fetch_stmt)
        return result.scalar_one_or_none()

    async def get_history(self, vehicle_id: str) -> List[ChargingSession]:
        """Returns historical tracking elements collection sorted chronologically (Requirement 8)."""
        stmt = (
            select(ChargingSession)
            .where(ChargingSession.vehicle_id == vehicle_id)
            .order_by(desc(ChargingSession.start_time))
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())