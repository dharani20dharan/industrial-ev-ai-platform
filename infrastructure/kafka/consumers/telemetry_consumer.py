import json
import os
import sys
import time

try:
    from kafka import KafkaConsumer
except ImportError:
    KafkaConsumer = None

def run_consumer():
    if KafkaConsumer is None:
        print("Error: kafka-python package not installed.")
        return

    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    topic_pattern = r"ev\..*"

    consumer = None
    retries = 5
    while retries > 0:
        try:
            consumer = KafkaConsumer(
                bootstrap_servers=bootstrap_servers,
                auto_offset_reset='latest',
                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                group_id="infrastructure_telemetry_debug_group"
            )
            consumer.subscribe(pattern=topic_pattern)
            break
        except Exception as e:
            retries -= 1
            time.sleep(5)

    if not consumer:
        sys.exit(1)

    print("=== LIVE TELEMETRY LOG BUS RUNNING ===")
    for message in consumer:
        print(f"[{message.topic}] Vehicle: {message.value.get('vehicle_id')} | Time: {message.value.get('timestamp')}")

if __name__ == "__main__":
    run_consumer()