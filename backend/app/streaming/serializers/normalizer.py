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