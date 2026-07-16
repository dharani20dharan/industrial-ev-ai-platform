import json
import logging
from typing import Optional, Dict, Type
from pydantic import BaseModel, ValidationError

from app.schemas.payloads import (
    TelemetryPayload, BatteryPayload, LocationPayload,
    ChargingPayload, StatusPayload, AlertsPayload, HeartbeatPayload
)

# FIX: Changed level to WARNING to prevent logs bleeding into execution terminals
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

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
    schema_cls = TOPIC_SCHEMA_MAP.get(topic)
    if not schema_cls:
        return None

    try:
        parsed_json = json.loads(raw_data)
        validated_model = schema_cls.model_validate(parsed_json)
        return validated_model
    except (json.JSONDecodeError, ValidationError, Exception) as e:
        # Crucial processing errors fallback quietly to system logs without flooding stdout
        logger.error(f"Ingestion structural exception caught on topic {topic}: {e}")
        return None