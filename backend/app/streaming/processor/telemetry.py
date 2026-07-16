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

        # Instantiates using the explicit kinematic parameter names
        record = TelemetryRecord(
            vehicle_id=vehicle_id,
            timestamp=ts,
            speed_kph=float(payload.get("speed_kph", 0.0)),
            odometer_km=float(payload.get("odometer_km", 0.0)),
            motor_temperature_c=float(payload.get("motor_temperature_c", 0.0)),
            torque_nm=float(payload.get("torque_nm", 0.0))
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