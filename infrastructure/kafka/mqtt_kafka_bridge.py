import os
import sys
import json
import logging
import time

try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("Error: paho-mqtt not installed. Run 'pip install paho-mqtt'")
    sys.exit(1)

try:
    from kafka import KafkaProducer
except ImportError:
    print("Error: kafka-python not installed. Run 'pip install kafka-python'")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("mqtt_kafka_bridge")

# Configurations from environment variables
MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "ev/battery/#")

KAFKA_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "ev-telemetry")

producer = None

def on_connect(client, userdata, flags, reason_code, properties=None):
    """Callback when connected to MQTT Broker."""
    logger.info(f"Connected to Mosquitto Broker at {MQTT_HOST}:{MQTT_PORT}")
    client.subscribe(MQTT_TOPIC)
    logger.info(f"Subscribed to MQTT Topic: {MQTT_TOPIC}")

def on_message(client, userdata, msg):
    """Callback when a message is received from MQTT Broker."""
    global producer
    try:
        payload = msg.payload.decode("utf-8")
        logger.info(f"Received MQTT payload on topic {msg.topic}: {payload}")
        
        # Verify JSON validity
        data = json.loads(payload)
        
        # Enrich data with source MQTT topic
        data["mqtt_source_topic"] = msg.topic
        
        # Forward to Kafka
        if producer:
            future = producer.send(KAFKA_TOPIC, value=data)
            # block for a maximum of 10 seconds to confirm send
            record_metadata = future.get(timeout=10)
            logger.info(f"Forwarded message to Kafka topic '{record_metadata.topic}' partition [{record_metadata.partition}] offset {record_metadata.offset}")
        else:
            logger.warning("Kafka Producer is offline. Event dropped.")
            
    except Exception as e:
        logger.error(f"Failed to forward message from MQTT to Kafka: {e}")

def main():
    global producer
    
    # 1. Initialize Kafka Producer
    logger.info(f"Initializing Kafka Producer connecting to: {KAFKA_SERVERS}...")
    retries = 5
    while retries > 0:
        try:
            producer = KafkaProducer(
                bootstrap_servers=KAFKA_SERVERS,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                acks="all",
                retries=3
            )
            logger.info("Kafka Producer successfully initialized.")
            break
        except Exception as e:
            retries -= 1
            logger.warning(f"Failed to connect to Kafka. Retrying in 5 seconds... (Retries left: {retries}). Error: {e}")
            time.sleep(5)
            
    if not producer:
        logger.error("Could not establish connection to Kafka. Exiting bridge.")
        sys.exit(1)

    # 2. Initialize MQTT Client
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2 if hasattr(mqtt, 'CallbackAPIVersion') else None)
    client.on_connect = on_connect
    client.on_message = on_message

    logger.info(f"Connecting to Mosquitto Broker at {MQTT_HOST}:{MQTT_PORT}...")
    try:
        client.connect(MQTT_HOST, MQTT_PORT, 60)
    except Exception as e:
        logger.error(f"Failed to connect to MQTT Broker: {e}")
        sys.exit(1)

    # 3. Block and listen
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        logger.info("Bridge loop terminated by user.")
    finally:
        client.disconnect()
        if producer:
            producer.close()
            logger.info("Kafka Producer resources released.")

if __name__ == "__main__":
    main()
