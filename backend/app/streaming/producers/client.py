import logging
from typing import Optional
from aiokafka import AIOKafkaProducer

from app.core.config import settings
from app.contracts.envelope import EventEnvelope

logger = logging.getLogger(__name__)

class KafkaEventProducer:
    """Async Kafka producer for routing normalized events to the message bus."""
    
    def __init__(self) -> None:
        self.producer: Optional[AIOKafkaProducer] = None

    async def start(self) -> None:
        """Initializes the Kafka producer connection pool."""
        logger.info("Initializing Kafka producer...", extra={"brokers": settings.kafka.bootstrap_servers})
        
        self.producer = AIOKafkaProducer(
            bootstrap_servers=settings.kafka.bootstrap_servers,
            client_id="ev_streaming_producer",
            # Acknowledge leader write for high throughput, safe enough for telemetry
            acks=1 
        )
        
        try:
            await self.producer.start()
            logger.info("Kafka Producer successfully connected.")
        except Exception as e:
            logger.critical("Failed to connect Kafka Producer.", exc_info=True)
            raise

    async def stop(self) -> None:
        """Flushes pending batches and cleanly disconnects."""
        if self.producer:
            await self.producer.stop()
            logger.info("Kafka Producer disconnected.")

    async def publish(self, target_topic: str, event: EventEnvelope) -> None:
        """Serializes the event envelope and publishes it to the specified topic."""
        if not self.producer:
            logger.error("Attempted to publish without an active Kafka connection.")
            return

        try:
            # Pydantic v2 serialization to JSON bytes
            payload_bytes = event.model_dump_json().encode("utf-8")
            
            # Fire-and-forget for telemetry throughput, though send_and_wait can be used for guarantees
            await self.producer.send(target_topic, value=payload_bytes)
            
        except Exception as e:
            logger.error(
                "Failed to publish event to Kafka.",
                exc_info=True,
                extra={"target_topic": target_topic, "event_id": str(event.event_id)}
            )