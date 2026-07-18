import asyncio
import json
import logging
from typing import Callable, Dict, List, Optional, Awaitable, Any

from aiokafka import AIOKafkaConsumer
from app.core.config import settings

logger = logging.getLogger(__name__)

# Define the callback signature: takes a topic (str) and the parsed JSON payload (dict)
ConsumerCallback = Callable[[str, Dict[str, Any]], Awaitable[None]]

class KafkaEventConsumer:
    """Async Kafka consumer framework with an internal callback router."""

    def __init__(self) -> None:
        self.consumer = None
        self._consume_task = None
        
        self.ALLOWED_TOPICS = {
            "ev.telemetry",
            "ev.battery",
            "ev.location",
            "ev.charging",
            "ev.status",
            "ev.alerts",
            "ev.diagnostics",
            "ev.supply_chain"
        }
        
        # Internal router mapping Kafka topics to a list of registered async callbacks
        self._callbacks: Dict[str, List[ConsumerCallback]] = {
            topic: [] for topic in self.ALLOWED_TOPICS
        }

    def register_callback(self, topic: str, callback: ConsumerCallback) -> None:
        """Allows domain services to hook into specific Kafka topics."""
        if topic not in self.ALLOWED_TOPICS:
            logger.warning("Attempted to register callback for unknown topic.", extra={"topic": topic})
            return
            
        self._callbacks[topic].append(callback)
        logger.debug("Registered new callback.", extra={"topic": topic, "callback": callback.__name__})

    async def start(self) -> None:
        """Initializes the Kafka consumer and begins the listening loop."""
        logger.info("Initializing Kafka consumer framework...")
        
        # *self.ALLOWED_TOPICS safely unpacks the set values as independent string arguments
        self.consumer = AIOKafkaConsumer(
            *self.ALLOWED_TOPICS,
            bootstrap_servers=settings.kafka.bootstrap_servers,
            group_id=settings.kafka.group_id,
            auto_offset_reset=settings.kafka.auto_offset_reset,
            enable_auto_commit=True
        )
        
        try:
            await self.consumer.start()
            logger.info("Kafka Consumer successfully connected to brokers.")
            
            # Spin up the background consuming loop
            self._consume_task = asyncio.create_task(self._consume_loop())
        except Exception as e:
            logger.critical("Failed to connect Kafka Consumer.", exc_info=True)
            raise

    async def stop(self) -> None:
        """Gracefully shuts down the consumer task and connection."""
        if self._consume_task:
            self._consume_task.cancel()
            try:
                await self._consume_task
            except asyncio.CancelledError:
                pass
                
        if self.consumer:
            await self.consumer.stop()
            logger.info("Kafka Consumer disconnected cleanly.")

    async def _consume_loop(self) -> None:
        """Background loop retrieving messages and dispatching them to callbacks."""
        if not self.consumer:
            return

        try:
            async for message in self.consumer:
                topic = message.topic
                
                # Check if anyone actually cares about this topic before parsing
                if not self._callbacks.get(topic):
                    continue

                try:
                    # Parse the raw bytes back into the EventEnvelope JSON dictionary
                    payload_dict = json.loads(message.value.decode("utf-8"))
                    
                    # Dispatch to all registered callbacks asynchronously
                    # We use create_task so a slow callback doesn't block the Kafka consumer loop
                    for callback in self._callbacks[topic]:
                        asyncio.create_task(self._execute_callback(callback, topic, payload_dict))
                        
                except json.JSONDecodeError:
                    logger.error("Failed to decode Kafka message as JSON.", extra={"topic": topic})
                except Exception as e:
                    logger.error("Error dispatching Kafka message.", exc_info=True, extra={"topic": topic})

        except asyncio.CancelledError:
            logger.info("Kafka consumption task gracefully cancelled.")
            
    async def _execute_callback(self, callback: ConsumerCallback, topic: str, payload: Dict[str, Any]) -> None:
        """Safely executes a callback, catching any unhandled exceptions."""
        try:
            await callback(topic, payload)
        except Exception as e:
            logger.error(
                "Unhandled exception in consumer callback.", 
                exc_info=True, 
                extra={"topic": topic, "callback": callback.__name__}
            )