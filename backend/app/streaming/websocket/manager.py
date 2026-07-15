import logging
import json
from typing import Dict, Set, Any
from fastapi import WebSocket

logger = logging.getLogger(__name__)

class WebSocketManager:
    """Manages active dashboard WebSocket connections and topic subscriptions."""
    
    def __init__(self) -> None:
        # Maps active WebSocket connections to a set of their subscribed topics
        self.active_connections: Dict[WebSocket, Set[str]] = {}

    async def connect(self, websocket: WebSocket) -> None:
        """Accepts a new connection and initializes an empty subscription set."""
        await websocket.accept()
        self.active_connections[websocket] = set()
        logger.info("New WebSocket dashboard connection established.")

    def disconnect(self, websocket: WebSocket) -> None:
        """Removes a connection from the active pool cleanly."""
        if websocket in self.active_connections:
            del self.active_connections[websocket]
            logger.info("WebSocket dashboard connection removed.")

    async def subscribe(self, websocket: WebSocket, topic: str) -> None:
        """Adds a Kafka topic to the client's subscription list."""
        if websocket in self.active_connections:
            self.active_connections[websocket].add(topic)
            logger.debug("WebSocket subscribed to topic.", extra={"topic": topic})

    async def unsubscribe(self, websocket: WebSocket, topic: str) -> None:
        """Removes a Kafka topic from the client's subscription list."""
        if websocket in self.active_connections and topic in self.active_connections[websocket]:
            self.active_connections[websocket].remove(topic)
            logger.debug("WebSocket unsubscribed from topic.", extra={"topic": topic})

    async def broadcast(self, topic: str, payload: Dict[str, Any]) -> None:
        """Pushes an event payload to all clients subscribed to the topic."""
        # Convert the dictionary payload to a JSON string for transmission
        message = json.dumps({"topic": topic, "data": payload})
        
        stale_connections = []
        
        for websocket, subscriptions in self.active_connections.items():
            if topic in subscriptions:
                try:
                    await websocket.send_text(message)
                except Exception as e:
                    logger.error("Failed to send WebSocket message.", exc_info=True)
                    stale_connections.append(websocket)
                    
        # Cleanup connections that dropped without closing properly
        for stale in stale_connections:
            self.disconnect(stale)

# Global manager instance
ws_manager = WebSocketManager()