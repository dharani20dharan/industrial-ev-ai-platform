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

# Map incoming MQTT topics to target Kafka topics/event types
MQTT_TO_KAFKA_ROUTE = {
    "ev/telemetry": "telemetry.raw",
    "ev/battery": "telemetry.raw",
    "ev/location": "telemetry.raw",
    "ev/charging": "telemetry.raw",
    "ev/status": "telemetry.raw",
    "ev/alerts": "alerts",
    "ev/heartbeat": "telemetry.raw"
}

def normalize_to_envelope(mqtt_topic: str, payload: BaseModel) -> EventEnvelope:
    """Wraps the validated payload. Extracts asset contexts cleanly if present."""
    target_event_type = MQTT_TO_KAFKA_ROUTE.get(mqtt_topic, "unknown.raw")
    
    # Proactively grab the real vehicle identity from the simulator payload
    extracted_vehicle = getattr(payload, "vehicle_id", "VEH-SIM-UNKNOWN")
    
    envelope = EventEnvelope(
        event_type=target_event_type,
        source="streaming_ingestion_node",
        vehicle_id=extracted_vehicle,
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