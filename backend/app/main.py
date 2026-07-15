import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.logging import setup_logging
from app.core.container import container
from app.streaming.mqtt.client import MqttIngestionClient
from app.streaming.producers.client import KafkaEventProducer
from app.streaming.consumers.client import KafkaEventConsumer
from app.streaming.websocket.adapter import kafka_to_ws_broadcaster

from app.api.health import router as health_router
from app.api.ws_routes import router as ws_router

# Initialize early logging
setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manages the startup and graceful shutdown of all async infrastructure clients."""
    logger.info("Initializing platform infrastructure...")

    # 1. Instantiate Clients
    mqtt_client = MqttIngestionClient()
    kafka_producer = KafkaEventProducer()
    kafka_consumer = KafkaEventConsumer()

    # 2. Register to Dependency Injection Container
    container.register_mqtt_client(mqtt_client)
    container.register_kafka_producer(kafka_producer)
    container.register_kafka_consumer(kafka_consumer)

    # 3. Wire Callbacks (from Phase 6)
    kafka_consumer.register_callback("telemetry.raw", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("alerts", kafka_to_ws_broadcaster)

    # 4. Start Downstream First (Kafka)
    await kafka_producer.start()
    await kafka_consumer.start()
    
    # 5. Start Upstream Last (MQTT Ingestion)
    await mqtt_client.start()
    
    logger.info("Platform streaming layer fully operational.")
    
    yield  # Application runs here

    logger.info("Initiating graceful shutdown sequence...")
    
    # 6. Stop Upstream First (Halt new ingestion)
    await mqtt_client.stop()
    
    # 7. Stop Consumers (Halt internal processing)
    await kafka_consumer.stop()
    
    # 8. Stop Downstream Last (Flush pending producer batches)
    await kafka_producer.stop()
    
    logger.info("Shutdown complete. All connections closed safely.")

# Initialize the FastAPI application
app = FastAPI(title="Industrial EV AI Platform - Streaming Layer", lifespan=lifespan)

# Include core routers
app.include_router(health_router)
app.include_router(ws_router)