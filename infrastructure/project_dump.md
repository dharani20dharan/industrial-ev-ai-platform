# Project Dump

Project: infrastructure

## Directory Tree

```text
infrastructure
├── kafka
│   ├── consumers
│   │   ├── db_writer.py
│   │   └── telemetry_consumer.py
│   └── mqtt_kafka_bridge.py
├── mosquitto
│   └── mosquitto.conf
├── neo4j
│   ├── init_db.py
│   └── init_graph.cypher
├── project_dump.md
└── timescaledb
    └── init.sql
```

# File Contents

---

## project_dump.md

**[Empty File]**

---

## kafka\mqtt_kafka_bridge.py

```python
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
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "ev/#")  # Changed from ev/battery/# to catch all contract topics

KAFKA_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "telemetry.raw")  # Changed from ev-telemetry to telemetry.raw

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
```

---

## mosquitto\mosquitto.conf

```
listener 1883
allow_anonymous true

listener 9001
protocol websockets
allow_anonymous true
```

---

## neo4j\init_db.py

```python
import os
import sys
from neo4j import GraphDatabase

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4jpassword")

def load_cypher_file(file_path):
    """Loads and splits Cypher queries from the file, stripping comments."""
    if not os.path.exists(file_path):
        print(f"Error: Cypher file not found at {file_path}")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    queries = []
    current_query = []
    
    for line in content.split("\n"):
        stripped = line.strip()
        if not stripped:
            if current_query:
                queries.append("\n".join(current_query))
                current_query = []
            continue
        if stripped.startswith("//"):
            continue
        current_query.append(line)
        
    if current_query:
        queries.append("\n".join(current_query))
        
    return [q.strip() for q in queries if q.strip()]

def seed_database():
    print("Starting Neo4j database seeding...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cypher_path = os.path.join(script_dir, "init_graph.cypher")
    
    queries = load_cypher_file(cypher_path)
    if not queries:
        print("No Cypher queries found to execute.")
        return

    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            # Clean existing nodes and relationships first to avoid duplicates
            print("Cleaning existing graph data...")
            session.run("MATCH (n) DETACH DELETE n")
            
            # Execute initialization queries
            print(f"Executing {len(queries)} seeding queries...")
            for i, query in enumerate(queries, 1):
                print(f"Executing query {i}/{len(queries)}...")
                session.run(query)
                
            print("Successfully seeded Neo4j graph database!")
            
        driver.close()
    except Exception as e:
        print(f"Error connecting to or seeding Neo4j database: {e}")
        sys.exit(1)

if __name__ == "__main__":
    seed_database()
```

---

## neo4j\init_graph.cypher

```
// Create Mine Nodes
CREATE (m1:Mine {name: "Salar de Atacama", location: "Chile", material: "Lithium Brine", capacity_tons_year: 50000})
CREATE (m2:Mine {name: "Katanga Copper-Cobalt Mine", location: "DR Congo", material: "Cobalt Ore", capacity_tons_year: 25000})

// Create Refiner Nodes
CREATE (r1:Refiner {name: "Tianqi Lithium", location: "Sichuan, China", material: "Battery-grade Lithium Hydroxide"})
CREATE (r2:Refiner {name: "Sumitomo Metal Mining", location: "Niihama, Japan", material: "Cathode Precursor Material"})

// Create Battery Plant Nodes
CREATE (p1:BatteryPlant {name: "CATL Yibin", location: "Sichuan, China", cell_type: "LFP", annual_gwh: 40})
CREATE (p2:BatteryPlant {name: "Panasonic Gigafactory", location: "Nevada, USA", cell_type: "NCA", annual_gwh: 35})

// Create Vehicle Nodes
CREATE (v1:Vehicle {id: "EV-HD-001", model: "Industrial Heavy Hauler", location: "Denver Hub"})
CREATE (v2:Vehicle {id: "EV-HD-002", model: "Yard Tractor", location: "Denver Hub"})
CREATE (v3:Vehicle {id: "EV-HD-003", model: "Heavy Duty Hauler", location: "Houston Hub"})
CREATE (v4:Vehicle {id: "EV-HD-004", model: "Last Mile Delivery", location: "Chicago Hub"})

// Create Relationships (Supply Chain Dependency Chains)
CREATE (m1)-[:SUPPLIES_RAW_TO {transit_time_days: 12}]->(r1)
CREATE (m2)-[:SUPPLIES_RAW_TO {transit_time_days: 28}]->(r2)
CREATE (r1)-[:DELIVERS_REFINED_TO {transit_time_days: 4}]->(p1)
CREATE (r2)-[:DELIVERS_REFINED_TO {transit_time_days: 8}]->(p2)
CREATE (p1)-[:SHIPS_CELLS_TO {transit_time_days: 18}]->(v1)
CREATE (p1)-[:SHIPS_CELLS_TO {transit_time_days: 18}]->(v2)
CREATE (p2)-[:SHIPS_CELLS_TO {transit_time_days: 2}]->(v3)
CREATE (p2)-[:SHIPS_CELLS_TO {transit_time_days: 4}]->(v4)
```

---

## timescaledb\init.sql

```sql
-- Initial TimescaleDB Schema Setup
-- Relational & Time-Series tables for EV Telemetry Ingestion

-- 1. Enable TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

-- 2. Create raw telemetry table (Time-Series Hypertable candidate)
CREATE TABLE IF NOT EXISTS telemetry (
    id SERIAL,
    vehicle_id VARCHAR(50) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    voltage DOUBLE PRECISION NOT NULL,
    current DOUBLE PRECISION NOT NULL,
    temperature DOUBLE PRECISION NOT NULL,
    soc DOUBLE PRECISION NOT NULL
);

-- 3. Convert telemetry to hypertable (partitioned by timestamp)
SELECT create_hypertable('telemetry', 'timestamp', if_not_exists => TRUE);

-- 4. Create indexes for performance tuning
CREATE INDEX IF NOT EXISTS idx_telemetry_vehicle_timestamp ON telemetry (vehicle_id, timestamp DESC);

-- 5. Relational Table: Charging Sessions
CREATE TABLE IF NOT EXISTS charging_sessions (
    id SERIAL PRIMARY KEY,
    vehicle_id VARCHAR(50) NOT NULL,
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ,
    energy_delivered_kwh DOUBLE PRECISION NOT NULL,
    starting_soc DOUBLE PRECISION NOT NULL,
    ending_soc DOUBLE PRECISION
);

-- 6. Relational Table: Battery Health Indicators
CREATE TABLE IF NOT EXISTS battery_health (
    id SERIAL PRIMARY KEY,
    vehicle_id VARCHAR(50) UNIQUE NOT NULL,
    capacity_fade DOUBLE PRECISION NOT NULL,
    cycle_count INTEGER NOT NULL,
    state_of_health DOUBLE PRECISION NOT NULL,
    remaining_useful_life INTEGER NOT NULL
);

-- 7. Relational Table: System Alerts Log
CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    vehicle_id VARCHAR(50) NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    severity VARCHAR(20) NOT NULL,
    type VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL,
    resolved BOOLEAN DEFAULT FALSE
);

-- 8. Relational Table: Graph Supplier Metadata
CREATE TABLE IF NOT EXISTS suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    risk_score DOUBLE PRECISION DEFAULT 0.0,
    material_supplied VARCHAR(50) NOT NULL
);

-- 9. Relational Table: Maintenance Logs
CREATE TABLE IF NOT EXISTS maintenance_logs (
    id SERIAL PRIMARY KEY,
    vehicle_id VARCHAR(50) NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255) NOT NULL,
    action_taken VARCHAR(255),
    status VARCHAR(50) DEFAULT 'Pending'
);
```

---

## kafka\consumers\db_writer.py

```python
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
```

---

## kafka\consumers\telemetry_consumer.py

```python
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
```
