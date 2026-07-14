import os
import sys
import json
import logging
import time
from datetime import datetime

try:
    from kafka import KafkaConsumer
except ImportError:
    print("Error: kafka-python package not installed. Run 'pip install kafka-python'")
    sys.exit(1)

try:
    import psycopg2
    from psycopg2 import pool
except ImportError:
    print("Error: psycopg2 package not installed. Run 'pip install psycopg2-binary'")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("db_writer")

# Configuration from environment variables
KAFKA_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "ev-telemetry")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "ev_platform")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgrespassword")

db_pool = None

def init_db_pool():
    """Initializes a connection pool for TimescaleDB."""
    global db_pool
    try:
        db_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        logger.info(f"Connected to TimescaleDB pool at {DB_HOST}:{DB_PORT}/{DB_NAME}")
    except Exception as e:
        logger.error(f"Failed to initialize TimescaleDB pool: {e}")
        sys.exit(1)

def write_telemetry_to_db(data):
    """Inserts a single telemetry record into TimescaleDB."""
    global db_pool
    if not db_pool:
        return False
        
    conn = None
    try:
        # Extract columns
        vehicle_id = data.get("vehicle_id")
        timestamp_str = data.get("timestamp")
        voltage = data.get("voltage")
        current = data.get("current")
        temperature = data.get("temperature")
        soc = data.get("soc")
        
        if not all([vehicle_id, timestamp_str, voltage is not None, current is not None, temperature is not None, soc is not None]):
            logger.warning(f"Malformed telemetry record ignored: {data}")
            return False

        # Convert ISO timestamp string to Python datetime object
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
            logger.info(f"Logged database event: vehicle={vehicle_id} timestamp={timestamp_str} SoC={soc}%")
            
        db_pool.putconn(conn)
        return True
    except Exception as e:
        logger.error(f"Failed to write record to TimescaleDB: {e}")
        if conn:
            conn.rollback()
            db_pool.putconn(conn)
        return False

def main():
    init_db_pool()
    
    # Initialize Kafka Consumer
    logger.info(f"Initializing Kafka Consumer for topic '{KAFKA_TOPIC}' on {KAFKA_SERVERS}...")
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
            logger.info("Kafka Consumer successfully initialized.")
            break
        except Exception as e:
            retries -= 1
            logger.warning(f"Failed to connect to Kafka. Retrying in 5 seconds... (Retries left: {retries}). Error: {e}")
            time.sleep(5)

    if not consumer:
        logger.error("Could not establish connection to Kafka. Exiting consumer.")
        sys.exit(1)

    # Listen to events
    logger.info("Database ingestion pipeline is active. Consuming messages...")
    try:
        for message in consumer:
            logger.info(f"Fetched message from topic: {message.topic}")
            data = message.value
            write_telemetry_to_db(data)
    except KeyboardInterrupt:
        logger.info("Ingestion pipeline terminated by user.")
    finally:
        if consumer:
            consumer.close()
        if db_pool:
            db_pool.closeall()
            logger.info("TimescaleDB database pool closed.")

if __name__ == "__main__":
    main()
