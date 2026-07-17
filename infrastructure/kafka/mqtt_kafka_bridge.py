import os
import sys
import json
import logging
import time

try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("Error: 'paho-mqtt' is not installed. Please run: pip install paho-mqtt")
    sys.exit(1)

try:
    from kafka import KafkaProducer
except ImportError:
    print("Error: 'kafka-python' is not installed. Please run: pip install kafka-python")
    sys.exit(1)

# Keep log level tight to avoid console flood
logging.basicConfig(level=logging.WARNING, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("mqtt_kafka_bridge")

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "ev/#")  
KAFKA_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

MQTT_TO_KAFKA_ROUTE = {
    "ev/telemetry": "ev.telemetry",
    "ev/battery": "ev.battery",
    "ev/location": "ev.location",
    "ev/charging": "ev.charging",
    "ev/status": "ev.status",
    "ev/alerts": "ev.alerts",
    "ev/heartbeat": "ev.diagnostics"
}

producer = None

def on_connect(client, userdata, flags, reason_code, properties=None):
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    global producer
    try:
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)
        data["mqtt_source_topic"] = msg.topic

        target_kafka_topic = MQTT_TO_KAFKA_ROUTE.get(msg.topic, "ev.unknown")
        if target_kafka_topic == "ev.unknown":
            return

        if producer:
            future = producer.send(target_kafka_topic, value=data)
            future.get(timeout=10)
    except Exception as e:
        logger.error(f"Bridge routing exception: {e}")

def main():
    global producer
    retries = 5
    while retries > 0:
        try:
            producer = KafkaProducer(
                bootstrap_servers=KAFKA_SERVERS,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                acks="all",
                retries=3
            )
            break
        except Exception:
            retries -= 1
            time.sleep(5)

    if not producer:
        logger.error("Could not establish connection to Kafka broker.")
        sys.exit(1)

    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2 if hasattr(mqtt, 'CallbackAPIVersion') else None)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(MQTT_HOST, MQTT_PORT, 60)
        print(">>> MQTT-Kafka Ingestion Bridge Running [Errors Only Mode] <<<")
        client.loop_forever()
    except Exception as e:
        logger.error(f"Bridge runtime fatal crash: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()