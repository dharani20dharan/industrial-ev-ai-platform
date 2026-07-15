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