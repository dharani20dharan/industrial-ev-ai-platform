import logging
from typing import Any, Optional
from app.core.config import settings

logger = logging.getLogger(__name__)

class ApplicationContainer:
    """Manages system-wide client allocations and lifecycle liftoffs."""
    
    def __init__(self) -> None:
        self.settings = settings
        
        # Placeholders for explicit network clients initialized during app startup
        self._mqtt_client: Optional[Any] = None
        self._kafka_producer: Optional[Any] = None
        self._kafka_consumer: Optional[Any] = None

    def register_mqtt_client(self, client: Any) -> None:
        self._mqtt_client = client
        logger.debug("Async MQTT Client registered to DI container.")

    def register_kafka_producer(self, producer: Any) -> None:
        self._kafka_producer = producer
        logger.debug("Async Kafka Producer registered to DI container.")

    def register_kafka_consumer(self, consumer: Any) -> None:
        self._kafka_consumer = consumer
        logger.debug("Async Kafka Consumer Framework registered to DI container.")

    @property
    def mqtt_client(self) -> Any:
        if not self._mqtt_client:
            raise RuntimeError("MQTT Client requested before initialization.")
        return self._mqtt_client

    @property
    def kafka_producer(self) -> Any:
        if not self._kafka_producer:
            raise RuntimeError("Kafka Producer requested before initialization.")
        return self._kafka_producer
        
    @property
    def kafka_consumer(self) -> Any:
        if not self._kafka_consumer:
            raise RuntimeError("Kafka Consumer requested before initialization.")
        return self._kafka_consumer

    def get_kafka_consumer(self) -> Any:
        """Explicit getter used during startup to wire WebSocket callbacks."""
        if not self._kafka_consumer:
            raise RuntimeError("Kafka Consumer requested before initialization.")
        return self._kafka_consumer


# Global container instance
container = ApplicationContainer()