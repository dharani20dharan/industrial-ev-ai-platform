import sys
import os
import asyncio
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

if sys.platform.lower() == "win32" or os.name.lower() == "nt":
    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

from app.core.logging import setup_logging
from app.core.container import container
from app.streaming.mqtt.client import MqttIngestionClient
from app.streaming.producers.client import KafkaEventProducer
from app.streaming.consumers.client import KafkaEventConsumer
from app.streaming.websocket.adapter import kafka_to_ws_broadcaster
from app.streaming.processor.telemetry import TelemetryProcessor
from app.api.v1.rest_routes import router as rest_router
from app.api.v1.api import api_router as v1_api_router

from app.api.health import router as health_router
from app.api.ws_routes import router as ws_router

setup_logging()
# Force clean warning filters over platform launch sequence
logging.getLogger("paho").setLevel(logging.WARNING)
logging.getLogger("kafka").setLevel(logging.WARNING)

@asynccontextmanager
async def lifespan(app: FastAPI):
    mqtt_client = MqttIngestionClient()
    kafka_producer = KafkaEventProducer()
    kafka_consumer = KafkaEventConsumer()

    container.register_mqtt_client(mqtt_client)
    container.register_kafka_producer(kafka_producer)
    container.register_kafka_consumer(kafka_consumer)

    telemetry_processor = TelemetryProcessor()

    # Domain routing bindings
    kafka_consumer.register_callback("ev.telemetry", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.telemetry", telemetry_processor.process_kinematics)

    kafka_consumer.register_callback("ev.battery", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.battery", telemetry_processor.process_battery)

    kafka_consumer.register_callback("ev.location", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.location", telemetry_processor.process_location)

    kafka_consumer.register_callback("ev.charging", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.charging", telemetry_processor.process_charging)

    # Map the incoming stream topic straight into the processing instance method
    kafka_consumer.register_callback(
        topic="ev.alerts",
        callback=telemetry_processor.process_alerts
    )

    try:
        await kafka_producer.start()
    except Exception as e:
        print(f"[WARN] Failed to start Kafka Producer (broker offline): {e}")
        
    try:
        await kafka_consumer.start()
    except Exception as e:
        print(f"[WARN] Failed to start Kafka Consumer (broker offline): {e}")
        
    try:
        await mqtt_client.start()
    except Exception as e:
        print(f"[WARN] Failed to start MQTT Client (broker offline): {e}")

    print(">>> FastAPI Enterprise Platform Streaming Engine Running (Offline Fallbacks Active) <<<")
    yield

    try:
        await mqtt_client.stop()
    except Exception:
        pass
    try:
        await kafka_consumer.stop()
    except Exception:
        pass
    try:
        await kafka_producer.stop()
    except Exception:
        pass

app = FastAPI(title="Industrial EV AI Platform", lifespan=lifespan)

app.include_router(health_router)
app.include_router(ws_router)
app.include_router(rest_router)
app.include_router(v1_api_router, prefix="/api/v1")
