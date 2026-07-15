import json
import os
import time

try:
    from kafka import KafkaConsumer
except ImportError:
    KafkaConsumer = None

def run_consumer():
    if KafkaConsumer is None:
        print("[KAFKA DRY-RUN] Python kafka-python package not installed. Skip network connection.")
        return

    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    topic = os.getenv("KAFKA_TOPIC", "telemetry.raw")

    print(f"Connecting to Kafka topic '{topic}' at {bootstrap_servers}...")

    consumer = None
    retries = 5
    while retries > 0:
        try:
            consumer = KafkaConsumer(
                topic,
                bootstrap_servers=bootstrap_servers,
                auto_offset_reset='latest',
                value_deserializer=lambda m: json.loads(m.decode('utf-8'))
            )
            print("Successfully connected to Kafka!")
            break
        except Exception as e:
            retries -= 1
            print(f"Kafka not ready, retrying in 5 seconds... ({retries} attempts left). Error: {e}")
            time.sleep(5)

    if not consumer:
        print("Failed to connect to Kafka. Exiting.")
        return

    print("Waiting for messages...")
    for message in consumer:
        data = message.value
        print(f"Received telemetry event: {data}")

if __name__ == "__main__":
    run_consumer()
