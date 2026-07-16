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