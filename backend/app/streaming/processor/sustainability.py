import logging
from typing import Dict, Any
from datetime import datetime
from dateutil.parser import isoparse

from app.db.session import AsyncSessionLocal
from app.services.sustainability import CarbonService
from app.schemas.sustainability import CarbonCalculationRequest
from app.streaming.websocket.adapter import kafka_to_ws_broadcaster

logger = logging.getLogger(__name__)

class CarbonProcessor:
    """Processes incoming telemetry streams to generate real-time carbon intelligence reports."""

    @staticmethod
    def _parse_timestamp(ts_str: str) -> datetime:
        """Safely parses ISO-8601 UTC timestamp strings into Python datetime objects."""
        try:
            return isoparse(ts_str)
        except Exception:
            return datetime.utcnow()

    async def process_telemetry(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """
        Processes 'ev.telemetry' events, calculates carbon metrics, 
        persists the report, and broadcasts updates via WebSocket.
        """
        try:
            payload = event_envelope.get("payload", {})
            vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id"))
            
            if not vehicle_id:
                logger.warning("CarbonProcessor: Missing vehicle_id in telemetry event. Skipping.")
                return
                
            ts_str = payload.get("timestamp")
            if not ts_str:
                logger.warning(f"CarbonProcessor: Missing timestamp for vehicle {vehicle_id}. Skipping.")
                return

            event_date = self._parse_timestamp(ts_str).date()

            request = CarbonCalculationRequest(
                vehicle_id=vehicle_id,
                start_date=event_date,
                end_date=event_date,
                grid_region="india" # Defaulting to India as per implementation plan
            )

            async with AsyncSessionLocal() as session:
                carbon_service = CarbonService(session)
                
                # This orchestrates calculation and DB persistence automatically
                report_response = await carbon_service.calculate_carbon(request)
                
                # Broadcast the new report to the frontend
                ws_envelope = {
                    "event_type": "carbon_report_generated",
                    "timestamp": datetime.utcnow().isoformat(),
                    "payload": report_response.model_dump(mode="json")
                }
                
                await kafka_to_ws_broadcaster(topic="ws.carbon.update", event_envelope=ws_envelope)
                
                logger.info(f"CarbonProcessor: Successfully generated and broadcasted carbon report for {vehicle_id}")

        except Exception as e:
            logger.error(f"CarbonProcessor: Failed to process telemetry event: {e}", exc_info=True)
            # We swallow the exception here so the Kafka consumer loop is never terminated
