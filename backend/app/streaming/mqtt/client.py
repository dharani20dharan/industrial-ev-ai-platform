# import asyncio
# import logging
# from typing import Optional
# import aiomqtt
# from aiomqtt.exceptions import MqttError


# from app.core.config import settings
# from app.streaming.serializers.validator import TOPIC_SCHEMA_MAP, validate_raw_payload
# from app.streaming.serializers.normalizer import normalize_to_envelope, MQTT_TO_KAFKA_ROUTE
# from app.core.container import container

# logger = logging.getLogger(__name__)

# class MqttIngestionClient:
#     """Async MQTT client handling simulator data ingestion."""
    
#     def __init__(self) -> None:
#         self.client: Optional[aiomqtt.Client] = None
#         self._consume_task: Optional[asyncio.Task] = None
#         # Derive immutable topics directly from our Phase 2 schema map
#         self.topics = list(TOPIC_SCHEMA_MAP.keys())

#     async def start(self) -> None:
#         """Establishes broker connection and initiates the listener task."""
#         logger.info("Initializing MQTT ingestion client...")
        
#         self.client = aiomqtt.Client(
#             hostname=settings.mqtt.host,
#             port=settings.mqtt.port,
#             username=settings.mqtt.username,
#             password=settings.mqtt.password,
#             identifier=settings.mqtt.client_id,
#             keepalive=settings.mqtt.keepalive
#         )
        
#         try:
#             await self.client.connect()
#             logger.info("Connected to Mosquitto broker.", extra={"broker": settings.mqtt.host})
            
#             # Spin up the background listening loop
#             self._consume_task = asyncio.create_task(self._consume_loop())
#         except MqttError as e:
#             logger.critical("Failed to connect to MQTT broker.", exc_info=True)
#             raise

#     async def stop(self) -> None:
#         """Gracefully tears down the consumption task and broker connection."""
#         if self._consume_task:
#             self._consume_task.cancel()
#             try:
#                 await self._consume_task
#             except asyncio.CancelledError:
#                 pass
                
#         if self.client:
#             await self.client.disconnect()
#             logger.info("Disconnected from Mosquitto broker.")

#     async def _consume_loop(self) -> None:
#         """Background loop that subscribes to topics and awaits messages."""
#         if not self.client:
#             return

#         try:
#             async with self.client.messages() as messages:
#                 # 1. Subscribe to the strictly required, immutable topics
#                 for topic in self.topics:
#                     await self.client.subscribe(topic)
#                     logger.info("Subscribed to MQTT topic", extra={"mqtt_topic": topic})
                    
#                 # 2. Continuous asynchronous event consumption
#                 async for message in messages:
#                     self._process_message(message)
                    
#         except asyncio.CancelledError:
#             logger.info("MQTT consumption task gracefully cancelled.")
#         except MqttError as e:
#             logger.error("MQTT connection lost during consumption.", exc_info=True)
#             # In a production environment, this is where we would trigger an exponential backoff reconnect

#     def _process_message(self, message: aiomqtt.Message) -> None:
#         """Routes incoming messages through validation, normalization, and publishing."""
#         topic = str(message.topic)
#         payload_bytes = message.payload
        
#         if not isinstance(payload_bytes, bytes):
#             return

#         # 1. Validate
#         validated_model = validate_raw_payload(topic, payload_bytes)
        
#         if validated_model:
#             # 2. Normalize
#             envelope = normalize_to_envelope(topic, validated_model)
#             target_kafka_topic = MQTT_TO_KAFKA_ROUTE.get(topic, "telemetry.raw")
            
#             # 3. Publish asynchronously without blocking the MQTT consumption loop
#             kafka_producer = container.kafka_producer
#             asyncio.create_task(kafka_producer.publish(target_kafka_topic, envelope)) 

import asyncio
import logging
from typing import Optional
import aiomqtt
from aiomqtt.exceptions import MqttError

from app.core.config import settings
from app.streaming.serializers.validator import TOPIC_SCHEMA_MAP, validate_raw_payload
from app.streaming.serializers.normalizer import normalize_to_envelope, MQTT_TO_KAFKA_ROUTE
from app.core.container import container

logger = logging.getLogger(__name__)

class MqttIngestionClient:
    """Async MQTT client handling simulator data ingestion using modern context managers."""
    
    def __init__(self) -> None:
        self._consume_task: Optional[asyncio.Task] = None
        self.topics = list(TOPIC_SCHEMA_MAP.keys())

    async def start(self) -> None:
        """Kicks off the background telemetry consumption loop task."""
        logger.info("Initializing MQTT ingestion client background engine...")
        # Spin up the connection loop in a non-blocking background task
        self._consume_task = asyncio.create_task(self._consume_loop())

    async def stop(self) -> None:
        """Gracefully tears down the consumption task."""
        if self._consume_task:
            self._consume_task.cancel()
            try:
                await self._consume_task
            except asyncio.CancelledError:
                pass
            logger.info("MQTT consumption engine cleanly stopped.")

    async def _consume_loop(self) -> None:
        """Handles context-managed network connections and continuous ingestion loops."""
        logger.info("Connecting to Mosquitto Broker...", extra={"broker": settings.mqtt.host})
        
        try:
            # Modern aiomqtt 2.0+ requires context-managed lifecycles
            async with aiomqtt.Client(
                hostname=settings.mqtt.host,
                port=settings.mqtt.port,
                username=settings.mqtt.username,
                password=settings.mqtt.password,
                identifier=settings.mqtt.client_id,
                keepalive=settings.mqtt.keepalive
            ) as client:
                logger.info("Connected to Mosquitto broker successfully.")
                
                # 1. Subscribe to all fixed data topics with wildcards
                for topic in self.topics:
                    await client.subscribe(topic + "/#")
                    logger.info("Subscribed to MQTT topic with wildcard", extra={"mqtt_topic": topic + "/#"})
                
                # 2. Consume incoming message frames asynchronously
                async for message in client.messages:
                    self._process_message(client, message)
                        
        except asyncio.CancelledError:
            logger.info("MQTT consumption loop task gracefully cancelled.")
        except MqttError as e:
            logger.error("MQTT broker connection dropped or encountered a network error.", exc_info=True)

    def _process_message(self, client: aiomqtt.Client, message: aiomqtt.Message) -> None:
        """Routes incoming raw binary messages through validation, normalization, and domain streams."""
        topic = str(message.topic)
        payload_bytes = message.payload
        
        if not isinstance(payload_bytes, bytes):
            return

        # 1. Extract base topic (e.g., "ev/battery" from "ev/battery/EV-001")
        parts = topic.split("/")
        base_topic = "/".join(parts[:2]) if len(parts) >= 2 else topic

        # 2. Structural Schema Validation Check
        validated_model = validate_raw_payload(base_topic, payload_bytes)
        
        if validated_model:
            # 3. Normalize and extract the target domain channel type
            envelope = normalize_to_envelope(base_topic, validated_model)
            
            # DYNAMIC ROUTING FIX: Grab the exact destination from the normalizer mapping
            target_kafka_topic = envelope.event_type
            
            # 4. Stream asynchronously straight onto the specific Kafka Topic Bus line
            kafka_producer = container.kafka_producer
            asyncio.create_task(kafka_producer.publish(target_kafka_topic, envelope))