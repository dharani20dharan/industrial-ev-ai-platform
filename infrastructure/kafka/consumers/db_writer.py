import os
import sys
import json
import logging
import time
from datetime import datetime

try:
    from kafka import KafkaConsumer
except ImportError:
    print("Error: 'kafka-python' is not installed. Please run: pip install kafka-python")
    sys.exit(1)

try:
    import psycopg2
    from psycopg2 import pool
except ImportError:
    print("Error: 'psycopg2' is not installed. Please run: pip install psycopg2-binary")
    sys.exit(1)

logging.basicConfig(level=logging.WARNING, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("db_writer")

KAFKA_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
# Aligned to intercept the exact stream target coming out of the bridge
KAFKA_TOPIC = "ev.telemetry"

# Change these lines near the top of db_writer.py:
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "ev_platform")     
DB_USER = os.getenv("DB_USER", "ev_admin")         
DB_PASSWORD = os.getenv("DB_PASSWORD", "ev_password")
db_pool = None

def init_db_pool():
    global db_pool
    try:
        db_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10, host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
    except Exception as e:
        logger.error(f"TimescaleDB pool allocation failure: {e}")
        sys.exit(1)

def write_telemetry_to_db(data):
    global db_pool
    if not db_pool:
        return False
    conn = None
    try:
        vehicle_id = data.get("vehicle_id")
        timestamp_str = data.get("timestamp")
        
        # Ininit.sql provides: voltage, current, temperature, soc
        # Maps raw kinetic parameters into physical database equivalents
        voltage = float(data.get("speed", 0.0))
        current = float(data.get("odometer", 0.0))
        temperature = float(data.get("motor_rpm", 0.0))
        soc = float(data.get("power_output", 0.0))

        timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
        conn = db_pool.getconn()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO telemetry (vehicle_id, timestamp, voltage, current, temperature, soc)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (vehicle_id, timestamp, voltage, current, temperature, soc)
            )
            conn.commit()
        db_pool.putconn(conn)
        return True
    except Exception as e:
        logger.error(f"TimescaleDB Write Exception: {e}")
        if conn:
            conn.rollback()
            db_pool.putconn(conn)
        return False

def main():
    init_db_pool()
    consumer = None
    retries = 5
    while retries > 0:
        try:
            consumer = KafkaConsumer(
                KAFKA_TOPIC,
                bootstrap_servers=KAFKA_SERVERS,
                auto_offset_reset='latest',
                enable_auto_commit=True,
                group_id='timescaledb-writer-group',
                value_deserializer=lambda m: json.loads(m.decode('utf-8'))
            )
            break
        except Exception:
            retries -= 1
            time.sleep(5)

    if not consumer:
        logger.error("Could not establish connection to Kafka broker.")
        sys.exit(1)

    print(">>> Database Ingestion Pipeline Running [Errors Only Mode] <<<")
    try:
        for message in consumer:
            write_telemetry_to_db(message.value)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()