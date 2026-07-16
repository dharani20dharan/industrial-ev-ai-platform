# Project Dump

Project: industrial-ev-ai-platform

## Directory Tree

```text
industrial-ev-ai-platform
├── .gitignore
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── health.py
│   │   │   ├── v1
│   │   │   │   ├── api.py
│   │   │   │   ├── endpoints
│   │   │   │   │   ├── health.py
│   │   │   │   │   ├── ml_inference.py
│   │   │   │   │   ├── supply_chain.py
│   │   │   │   │   ├── sustainability.py
│   │   │   │   │   └── telemetry.py
│   │   │   │   └── rest_routes.py
│   │   │   └── ws_routes.py
│   │   ├── contracts
│   │   │   └── envelope.py
│   │   ├── core
│   │   │   ├── config.py
│   │   │   ├── container.py
│   │   │   └── logging.py
│   │   ├── db
│   │   │   ├── init_timescale.py
│   │   │   └── session.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── domain.py
│   │   │   └── relational.py
│   │   ├── repositories
│   │   │   └── domain.py
│   │   ├── schemas
│   │   │   ├── payloads.py
│   │   │   └── telemetry.py
│   │   ├── services
│   │   │   └── telemetry.py
│   │   ├── streaming
│   │   │   ├── config
│   │   │   ├── consumers
│   │   │   │   └── client.py
│   │   │   ├── kafka
│   │   │   ├── mqtt
│   │   │   │   └── client.py
│   │   │   ├── processor
│   │   │   │   └── telemetry.py
│   │   │   ├── producers
│   │   │   │   └── client.py
│   │   │   ├── serializers
│   │   │   │   ├── normalizer.py
│   │   │   │   └── validator.py
│   │   │   └── websocket
│   │   │       ├── adapter.py
│   │   │       └── manager.py
│   │   └── utils
│   ├── project_dump.md
│   └── requirements.txt
├── common_schemas
│   ├── ai_Prediction_service
│   ├── alert_notification_service
│   ├── analytics_dashoard_service
│   ├── backend_summary
│   ├── battery_Intelligence
│   ├── core_platform.txt
│   ├── fleet_management
│   ├── predictive_maintenance_service
│   ├── real_time_streaming_service
│   ├── supply_chain_intelligence
│   ├── sustainablity_carbon_intelligence
│   └── teleentry_timeseries
├── docker-compose.yml
├── frontend
│   ├── components.json
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── src
│   │   ├── App.tsx
│   │   ├── index.css
│   │   ├── layouts
│   │   │   └── DashboardLayout.tsx
│   │   ├── main.tsx
│   │   ├── pages
│   │   │   ├── Alerts.tsx
│   │   │   ├── BatteryAnalytics.tsx
│   │   │   ├── CarbonAnalytics.tsx
│   │   │   ├── FleetOverview.tsx
│   │   │   └── SupplyChain.tsx
│   │   └── router
│   │       └── index.tsx
│   ├── tailwind.config.js
│   ├── tsconfig.json
│   └── vite.config.ts
├── infrastructure
│   ├── kafka
│   │   ├── consumers
│   │   │   ├── db_writer.py
│   │   │   └── telemetry_consumer.py
│   │   └── mqtt_kafka_bridge.py
│   ├── mosquitto
│   │   └── mosquitto.conf
│   ├── neo4j
│   │   ├── init_db.py
│   │   └── init_graph.cypher
│   ├── project_dump.md
│   └── timescaledb
│       └── init.sql
├── ml
│   ├── notebooks
│   │   └── README.md
│   ├── project_dump.md
│   ├── requirements.txt
│   ├── simulator
│   │   └── simulator.py
│   └── src
│       └── preprocessing.py
├── project_dump.md
└── README.md
```

# File Contents

---

## .gitignore

```
# Prerequisites
*.d

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#1255, pipenv should generally check in Pipfile.lock.
#   For libraries, check in Pipfile.lock.
# Pipfile.lock

# poetry
#   Similar to Pipenv, poetry.lock should be checked in for applications.
# poetry.lock

# pdm
#   Similar to Pipenv, pdm.lock should be checked in for applications.
# pdm.lock

# virtualenv
.venv
venv/
ENV/
env/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype
.pytype/

# Cython debug symbols
cython_debug/

# Node modules & frontend artifacts
node_modules/
/frontend/dist
/frontend/build
.eslintcache
.stylelintcache
*.local
.env
!.env.example

# IDEs
.vscode/
.idea/
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# Database/Infrastructure Data
infrastructure/data/
neo4j/data/
timescaledb/data/
kafka/data/
mosquitto/data/
data/

# OS metadata
.DS_Store
Thumbs.db
```

---

## docker-compose.yml

```yaml
services:
  mosquitto:
    image: eclipse-mosquitto:2
    container_name: mosquitto_broker
    ports:
      - "1883:1883"
      - "9001:9001"
    volumes:
      - ./infrastructure/mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf
    networks:
      - ev-network

  kafka:
      image: bitnamilegacy/kafka:latest
      container_name: kafka_broker
      ports:
        - "9092:9092"
      environment:
        - KAFKA_CFG_NODE_ID=1
        - KAFKA_CFG_PROCESS_ROLES=broker,controller
        - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka:9093
        - KAFKA_CFG_LISTENERS=INTERNAL://:9095,EXTERNAL://:9092,CONTROLLER://:9093
        - KAFKA_CFG_ADVERTISED_LISTENERS=INTERNAL://kafka:9095,EXTERNAL://localhost:9092
        - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT,CONTROLLER:PLAINTEXT
        - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
        - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=INTERNAL
        - KAFKA_CFG_LOG4J_ROOT_LOGLEVEL=WARN
      networks:
        - ev-network

  kafka-setup:
      image: bitnamilegacy/kafka:latest
      container_name: kafka_setup
      depends_on:
        - kafka
      networks:
        - ev-network
      command: >
        bash -c "
          echo 'Waiting for Kafka to be ready...'
          until kafka-topics.sh --bootstrap-server kafka:9095 --list 2>/dev/null; do
            echo 'Kafka is not ready yet, waiting 5 seconds...'
            sleep 5
          done
          echo 'Kafka is online! Provisioning Enterprise Domain Topics...'
          kafka-topics.sh --create --if-not-exists --bootstrap-server kafka:9095 --topic ev.telemetry --partitions 3
          kafka-topics.sh --create --if-not-exists --bootstrap-server kafka:9095 --topic ev.battery --partitions 3
          kafka-topics.sh --create --if-not-exists --bootstrap-server kafka:9095 --topic ev.location --partitions 3
          kafka-topics.sh --create --if-not-exists --bootstrap-server kafka:9095 --topic ev.charging --partitions 2
          kafka-topics.sh --create --if-not-exists --bootstrap-server kafka:9095 --topic ev.status --partitions 2
          kafka-topics.sh --create --if-not-exists --bootstrap-server kafka:9095 --topic ev.alerts --partitions 2
          kafka-topics.sh --create --if-not-exists --bootstrap-server kafka:9095 --topic ev.diagnostics --partitions 2
          echo 'Domain Topics created successfully.'
        "

  timescaledb:
    image: timescale/timescaledb:latest-pg14
    container_name: timescaledb
    environment:
      - POSTGRES_USER=ev_admin
      - POSTGRES_PASSWORD=ev_password
      - POSTGRES_DB=ev_platform
    ports:
      - "5432:5432"
    volumes:
      - ./infrastructure/timescaledb/init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - ev-network

  neo4j:
    image: neo4j:5
    container_name: neo4j_db
    environment:
      - NEO4J_AUTH=neo4j/ev_password
    ports:
      - "7474:7474"
      - "7687:7687"
    networks:
      - ev-network

networks:
  ev-network:
    driver: bridge
```

---

## project_dump.md

**[Empty File]**

---

## README.md

```markdown
# Industrial EV AI Platform

An enterprise-grade, end-to-end Industrial IoT (IIoT) analytics and intelligence platform designed for electric vehicle (EV) fleet asset monitoring, predictive maintenance, supply chain graph analysis, and carbon accounting.

---

## 🏗️ System Architecture

The platform is designed around a decoupled, highly scalable event-driven architecture to support sub-second telemetry ingestion, graph traversal, and ML inference.

```mermaid
graph TD
    %% Telemetry Stream Ingestion
    subgraph Data Generation & Ingestion
        Sim[EV Telemetry Simulator] -->|MQTT Publish| Mosquitto[Eclipse Mosquitto Broker]
        Mosquitto -->|ev/battery/*| KP[Kafka Producer Bridge]
        KP -->|Event Ingestion| Kafka[Apache Kafka Broker]
    end

    %% Storage & Streaming Analytics
    subgraph Data Storage & Real-Time Processing
        Kafka -->|Kafka Consumer| TSDB[(TimescaleDB hypertable)]
        Kafka -->|Live WebSockets| FastAPI[FastAPI Web Server]
    end

    %% Databases & Models
    subgraph Data Models & Intelligence
        FastAPI -->|REST API & Cypher Queries| Neo4j[(Neo4j Graph Database)]
        FastAPI -->|ML Feature Vector| ML[Predictive AI Engine]
        ML -->|Isolation Forest| Anom[Anomaly Detection]
        ML -->|XGBoost| RUL[Remaining Useful Life]
    end

    %% Presentation Layer
    subgraph Presentation
        FastAPI -->|WebSocket & JSON APIs| React[React + TS Dashboard]
    end

    classDef db fill:#2f3b52,stroke:#4f5d75,stroke-width:2px;
    classDef broker fill:#1f3322,stroke:#2a5c37,stroke-width:2px;
    classDef engine fill:#3d1a3d,stroke:#732973,stroke-width:2px;
    class TSDB,Neo4j db;
    class Mosquitto,Kafka broker;
    class ML,Anom,RUL engine;
```

---

## 🌟 Key Platform Capabilities

### 1. High-Throughput Telemetry Streaming
*   Continuous state transmission (Voltage, Current, State of Charge, Core temperature) via **MQTT**.
*   Buffered event ingestion using **Apache Kafka** partitioned topic distributions.
*   Timeseries persistence leveraging **TimescaleDB** hypertables with dynamic temporal indexing and range-partition optimizations.

### 2. Battery & Predictive Maintenance Intelligence
*   **State of Health (SoH) Analytics:** Tracks capacity fade using cumulative discharge integration (Ah depletion curves).
*   **Remaining Useful Life (RUL) Forecasting:** Predicts cycles remaining until battery capacity falls below the 80% degradation threshold using **XGBoost regression**.
*   **Anomaly Diagnostics:** Identifies thermal runaways and cell-level voltage imbalances using unsupervised **Isolation Forest models**.

### 3. Supply Chain Graph Analytics
*   Maps multi-tier mineral dependencies (Mine ➔ Refiner ➔ Battery Plant ➔ Assembly Pack ➔ Fleet Vehicle) using **Neo4j Graph Database**.
*   Propagates cascading risks (geopolitical instability, shipping bottlenecks, and material shortage) along supply chains utilizing optimized Cypher graph traversal algorithms.

### 4. Carbon & Electrification Analytics
*   Displaces direct Scope-1 combustion emissions vs Scope-3 charging grid emissions (based on local carbon intensity coefficients).
*   Calculates EV conversion suitability scores for internal combustion engine (ICE) routes based on payload, travel distances, charging station density, and depot dwell times.

---

## 🛠️ Tech Stack Alignment

| Layer | Technologies | Key Functionality |
| :--- | :--- | :--- |
| **Frontend UI** | React, TypeScript, TailwindCSS, ShadCN UI, Recharts | Control dashboard views, responsive metrics widgets, live WebSocket visualization |
| **API Backend** | FastAPI, SQLAlchemy, Pydantic, Uvicorn | REST endpoints, Swagger/OpenAPI documentation, WebSocket gateways |
| **Databases** | TimescaleDB (PostgreSQL), Neo4j Graph Database | Scalable telemetry timeseries, multi-tier dependency mapping |
| **Event Pipeline** | Eclipse Mosquitto (MQTT), Apache Kafka, Zookeeper | Sub-second telemetry publisher/subscriber and streaming queues |
| **AI/ML Stack** | NumPy, Pandas, Scikit-Learn, XGBoost | Data preprocessing, anomaly isolation, RUL regression forecasts |

---

## 📂 Repository Folder Layout

```
├── .gitignore                      # Python, Node, environment configurations ignore
├── docker-compose.yml              # Local infrastructure stack (TimescaleDB, Neo4j, MQTT, Kafka)
├── README.md                       # This document
├── frontend/                       # React + TS + TailwindCSS Dashboard UI
│   ├── package.json                # Frontend package dependencies
│   ├── tsconfig.json               # TypeScript compiler config
│   ├── tailwind.config.js          # Tailwind theme configurations
│   ├── components.json            # ShadCN UI components config
│   ├── src/
│   │   ├── components/             # Reusable UI widgets (gauges, alerts panels)
│   │   ├── layouts/                # Dashboard sidebar and navbar shell
│   │   ├── pages/                  # Route views (Fleet, Battery, Supply Chain, Carbon, Alerts)
│   │   └── router/                 # React Router definition mappings
├── backend/                        # FastAPI Web API Backend
│   ├── requirements.txt            # Python web server dependencies
│   ├── app/
│   │   ├── main.py                 # FastAPI core initializations & configurations
│   │   ├── models/                 # SQLAlchemy schemas (telemetry, charging logs)
│   │   ├── schemas/                # Pydantic serialization models
│   │   └── api/                    # Routers (health, live telemetry, ML, Neo4j supply chain)
├── ml/                             # ML Analytics & Synthetic Data Ingestion
│   ├── requirements.txt            # Data science packages
│   ├── notebooks/                  # EDA, NASA battery dataset profiling, model files
│   ├── src/                        # Preprocessing pipelines (thermal variance, discharge slope)
│   └── simulator/                  # Paho-MQTT based synthetic telemetry stream simulator
└── infrastructure/                 # Databases, brokers, and streaming configurations
    ├── timescaledb/                # Hypertable init scripts & partitioning queries
    ├── neo4j/                      # Cypher query imports & relationship setup
    ├── kafka/                      # Kafka producers & consumers
    └── mosquitto/                  # MQTT broker configurations
```

---

### 2. Infrastructure Setup
Spin up the local containerized databases, brokers, and event pipelines (including auto-provisioning Kafka topics):
```bash
docker-compose up -d

```

*(Optional: Verify Kafka topics are created by checking the setup logs: `docker logs -f kafka_setup`)*

### 3. Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

```

*Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).*

### 4. Frontend Setup

```bash
cd frontend
npm install
npm run dev

```

*Access the control dashboard interface at [http://localhost:3000](http://localhost:3000).*

### 5. End-to-End Infrastructure Pipeline Test

To test the flow of data from generation to Kafka consumption, configure a Python virtual environment at the project root:

```bash
# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install messaging dependencies
pip install paho-mqtt kafka-python numpy

```

Open **three separate terminal windows**, activate the virtual environment (`source venv/bin/activate`) in each, and run the following services in order:

**Terminal 1: Start the Kafka Consumer (Destination)**

```bash
python infrastructure/kafka/consumers/telemetry_consumer.py

```

**Terminal 2: Start the MQTT-to-Kafka Bridge (Router)**

```bash
python infrastructure/kafka/mqtt_kafka_bridge.py

```

**Terminal 3: Start the Data Simulator (Source)**

```bash
python ml/simulator/simulator.py

```
```

---

## backend\project_dump.md

```markdown
# Project Dump

Project: backend

## Directory Tree

```text
backend
├── app
│   ├── api
│   │   ├── health.py
│   │   ├── v1
│   │   │   ├── api.py
│   │   │   ├── endpoints
│   │   │   │   ├── health.py
│   │   │   │   ├── ml_inference.py
│   │   │   │   ├── supply_chain.py
│   │   │   │   ├── sustainability.py
│   │   │   │   └── telemetry.py
│   │   │   └── rest_routes.py
│   │   └── ws_routes.py
│   ├── contracts
│   │   └── envelope.py
│   ├── core
│   │   ├── config.py
│   │   ├── container.py
│   │   └── logging.py
│   ├── db
│   │   ├── init_timescale.py
│   │   └── session.py
│   ├── main.py
│   ├── models
│   │   ├── domain.py
│   │   └── relational.py
│   ├── repositories
│   │   └── domain.py
│   ├── schemas
│   │   ├── payloads.py
│   │   └── telemetry.py
│   ├── services
│   │   └── telemetry.py
│   ├── streaming
│   │   ├── config
│   │   ├── consumers
│   │   │   └── client.py
│   │   ├── kafka
│   │   ├── mqtt
│   │   │   └── client.py
│   │   ├── processor
│   │   │   └── telemetry.py
│   │   ├── producers
│   │   │   └── client.py
│   │   ├── serializers
│   │   │   ├── normalizer.py
│   │   │   └── validator.py
│   │   └── websocket
│   │       ├── adapter.py
│   │       └── manager.py
│   └── utils
├── project_dump.md
└── requirements.txt
```

# File Contents

---

## project_dump.md

**[Empty File]**

---

## requirements.txt

```text
fastapi>=0.100.0
uvicorn>=0.22.0
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
websockets>=11.0
neo4j>=5.10.0
python-dotenv>=1.0.0
aiomqtt>=2.0.0
aiokafka>=0.8.1
asyncpg>=0.28.0
```

---

## app\main.py

```python
import sys
import os
import asyncio
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

# Windows proactor event loop fix for aiomqtt socket polling
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

    # FIXED: Added missing comma and cleaned out duplicate string literals
    target_domain_topics = [
        "ev.telemetry",
        "ev.battery",
        "ev.location",
        "ev.charging",
        "ev.status",
        "ev.alerts",
        "ev.diagnostics"
    ]
    
    # Register the live debug output print callback across all domain streams
    for domain_topic in target_domain_topics:
        kafka_consumer.register_callback(domain_topic, kafka_to_ws_broadcaster)
        logger.debug(f"Registered WebSocket broadcaster hook for topic: {domain_topic}")

    # Instantiate the new database persistence bridge worker
    telemetry_processor = TelemetryProcessor()

    # Domain specific callback routing matrix mapping
    # Every channel triggers BOTH the real-time WebSocket pipe AND the TimescaleDB storage engine
    kafka_consumer.register_callback("ev.telemetry", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.telemetry", telemetry_processor.process_kinematics)

    kafka_consumer.register_callback("ev.battery", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.battery", telemetry_processor.process_battery)

    kafka_consumer.register_callback("ev.location", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.location", telemetry_processor.process_location)

    kafka_consumer.register_callback("ev.charging", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.charging", telemetry_processor.process_charging)

    # For channels that do not have repositories yet, keep the legacy console broadcast active
    kafka_consumer.register_callback("ev.status", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.alerts", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.diagnostics", kafka_to_ws_broadcaster)

    # 3. Start Downstream First (Kafka)
    await kafka_producer.start()
    await kafka_consumer.start()
    
    # 4. Start Upstream Last (MQTT Ingestion)
    await mqtt_client.start()
    
    logger.info("Platform streaming layer fully operational.")
    
    yield  # Application runs here

    logger.info("Initiating graceful shutdown sequence...")
    
    # 5. Stop Upstream First (Halt new ingestion)
    await mqtt_client.stop()
    
    # 6. Stop Consumers (Halt internal processing)
    await kafka_consumer.stop()
    
    # 7. Stop Downstream Last (Flush pending producer batches)
    await kafka_producer.stop()
    
    logger.info("Shutdown complete. All connections closed safely.")

# Initialize the FastAPI application
app = FastAPI(title="Industrial EV AI Platform - Streaming Layer", lifespan=lifespan)

# Include core routers
app.include_router(health_router)
app.include_router(ws_router)

app.include_router(rest_router)
```

---

## app\api\health.py

```python
import logging
from fastapi import APIRouter, HTTPException, status
from app.core.container import container

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/health", tags=["Monitoring"])

@router.get("")
async def liveness_check():
    """Basic HTTP liveness probe to verify the API event loop is running."""
    return {"status": "alive", "service": "streaming_layer"}

@router.get("/mqtt")
async def mqtt_readiness_check():
    """Verifies the Mosquitto MQTT broker connection is active."""
    try:
        mqtt = container.mqtt_client
        # Verify the client exists and the background consumption task is actively running
        if mqtt and mqtt._consume_task and not mqtt._consume_task.done():
            return {"status": "connected", "protocol": "mqtt"}
    except RuntimeError:
        # Caught if the DI container hasn't initialized the client yet
        pass
        
    logger.warning("MQTT health check failed.")
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
        detail="MQTT broker connection is not active."
    )

@router.get("/kafka")
async def kafka_readiness_check():
    """Verifies both Kafka Producer and Consumer are active."""
    try:
        producer = container.kafka_producer
        consumer = container.kafka_consumer
        
        is_producer_ok = producer and producer.producer
        is_consumer_ok = consumer and consumer._consume_task and not consumer._consume_task.done()
        
        if is_producer_ok and is_consumer_ok:
            return {"status": "connected", "protocol": "kafka", "components": ["producer", "consumer"]}
            
    except RuntimeError:
        pass
        
    logger.warning("Kafka health check failed.")
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
        detail="Kafka event bus connections are not fully active."
    )
```

---

## app\api\ws_routes.py

```python
# import logging
# from fastapi import APIRouter, WebSocket, WebSocketDisconnect
# from app.streaming.websocket.manager import ws_manager

# logger = logging.getLogger(__name__)
# router = APIRouter()

# @router.websocket("/ws/dashboard")
# async def dashboard_websocket_endpoint(websocket: WebSocket) -> None:
#     """
#     WebSocket endpoint for the React frontend.
#     Expects incoming JSON commands: {"action": "subscribe", "topic": "telemetry.raw"}
#     """
#     await ws_manager.connect(websocket)
    
#     try:
#         while True:
#             # Wait for control commands from the client
#             data = await websocket.receive_json()
#             action = data.get("action")
#             topic = data.get("topic")
            
#             if action == "subscribe" and topic:
#                 await ws_manager.subscribe(websocket, topic)
#             elif action == "unsubscribe" and topic:
#                 await ws_manager.unsubscribe(websocket, topic)
                
#     except WebSocketDisconnect:
#         ws_manager.disconnect(websocket)
#     except Exception as e:
#         logger.error("WebSocket connection error.", exc_info=True)
#         ws_manager.disconnect(websocket)

import logging
import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.streaming.websocket.manager import ws_manager

logger = logging.getLogger(__name__)
router = APIRouter()

@router.websocket("/ws/dashboard")
async def dashboard_websocket_endpoint(websocket: WebSocket) -> None:
    """
    WebSocket endpoint for the React frontend.
    Logs traffic to the terminal for debugging without a UI.
    """
    await ws_manager.connect(websocket)
    logger.info("=== [TESTING] Terminal Client Connected to Dashboard Stream ===")
    
    try:
        while True:
            data = await websocket.receive_json()
            action = data.get("action")
            topic = data.get("topic")
            
            if action == "subscribe" and topic:
                await ws_manager.subscribe(websocket, topic)
                print(f"\n[SUBSCRIPTION] Client listening to Kafka topic: {topic}")
            elif action == "unsubscribe" and topic:
                await ws_manager.unsubscribe(websocket, topic)
                print(f"\n[UNSUBSCRIPTION] Client stopped listening to Kafka topic: {topic}")
                
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
        logger.info("=== [TESTING] Terminal Client Disconnected ===")
    except Exception as e:
        logger.error("WebSocket connection error.", exc_info=True)
        ws_manager.disconnect(websocket)
```

---

## app\contracts\envelope.py

```python
from datetime import datetime, timezone
from typing import Generic, TypeVar, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# Generic Type for payload validation flexibility
T = TypeVar('T', bound=BaseModel)

class EventEnvelope(BaseModel, Generic[T]):
    """Standardized event envelope wrapping all platform domain payloads."""
    
    event_id: UUID = Field(default_factory=uuid4, description="Unique identifier for this specific event instance")
    event_type: str = Field(..., description="The type of event (e.g., 'telemetry.raw', 'battery.alert')")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="UTC timestamp of event generation")
    source: str = Field(..., description="Originating service or simulator node name")
    vehicle_id: str = Field(..., description="Unique immutable ID of the industrial vehicle")
    fleet_id: str = Field(..., description="Identifier for the tracking fleet operational partition")
    correlation_id: UUID = Field(default_factory=uuid4, description="Tracing ID sustained across asynchronous boundaries")
    
    payload: T = Field(..., description="The concrete domain data model matching the event type")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            UUID: lambda v: str(v)
        }
```

---

## app\core\config.py

```python
from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MqttSettings(BaseSettings):
    host: str = Field(default="localhost")
    port: int = Field(default=1883)
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    keepalive: int = Field(default=60)
    client_id: str = Field(default="industrial_ev_streaming_layer")


class KafkaSettings(BaseSettings):
    bootstrap_servers: List[str] = Field(default=["localhost:9092"])
    group_id: str = Field(default="ev_streaming_group")
    auto_offset_reset: str = Field(default="earliest")


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__", extra="ignore")
    database_url: str = "postgresql+asyncpg://ev_admin:ev_password@localhost:5432/ev_platform"
    environment: str = Field(default="development")
    debug: bool = Field(default=False)
    mqtt: MqttSettings = MqttSettings()
    kafka: KafkaSettings = KafkaSettings()


settings = AppSettings()
```

---

## app\core\container.py

```python
import logging
from typing import Any, Optional
from app.core.config import settings

logger = logging.getLogger(__name__)

class ApplicationContainer:
    """Manages system-wide client allocations and lifecycle liftoffs."""
    
    def __init__(self) -> None:
        self.settings = settings
        
        # Placeholders for explicit network clients initialized during app startup
        self._mqtt_client: Optional[Any] = None
        self._kafka_producer: Optional[Any] = None
        self._kafka_consumer: Optional[Any] = None

    def register_mqtt_client(self, client: Any) -> None:
        self._mqtt_client = client
        logger.debug("Async MQTT Client registered to DI container.")

    def register_kafka_producer(self, producer: Any) -> None:
        self._kafka_producer = producer
        logger.debug("Async Kafka Producer registered to DI container.")

    def register_kafka_consumer(self, consumer: Any) -> None:
        self._kafka_consumer = consumer
        logger.debug("Async Kafka Consumer Framework registered to DI container.")

    @property
    def mqtt_client(self) -> Any:
        if not self._mqtt_client:
            raise RuntimeError("MQTT Client requested before initialization.")
        return self._mqtt_client

    @property
    def kafka_producer(self) -> Any:
        if not self._kafka_producer:
            raise RuntimeError("Kafka Producer requested before initialization.")
        return self._kafka_producer
        
    @property
    def kafka_consumer(self) -> Any:
        if not self._kafka_consumer:
            raise RuntimeError("Kafka Consumer requested before initialization.")
        return self._kafka_consumer

    def get_kafka_consumer(self) -> Any:
        """Explicit getter used during startup to wire WebSocket callbacks."""
        if not self._kafka_consumer:
            raise RuntimeError("Kafka Consumer requested before initialization.")
        return self._kafka_consumer


# Global container instance
container = ApplicationContainer()
```

---

## app\core\logging.py

```python
import sys
import logging
import json
from datetime import datetime, timezone
from app.core.config import settings


class JsonFormatter(logging.Formatter):
    """Formats log records as single-line JSON strings for production parsing."""
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        if hasattr(record, "correlation_id"):
            log_data["correlation_id"] = record.correlation_id
        if hasattr(record, "vehicle_id"):
            log_data["vehicle_id"] = record.vehicle_id
            
        return json.dumps(log_data)


import os

def setup_logging() -> None:
    """Initializes global logging configurations."""
    root_logger = logging.getLogger()
    
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        
    handler = logging.StreamHandler(sys.stdout)
    
    # Check for custom LOG_LEVEL env var first
    env_log_level = os.getenv("LOG_LEVEL")
    if env_log_level:
        level = getattr(logging, env_log_level.upper(), logging.INFO)
    else:
        level = logging.DEBUG if getattr(settings, "debug", False) else logging.INFO
    
    if hasattr(settings, "environment") and settings.environment.lower() == "production":
        handler.setFormatter(JsonFormatter())
        root_logger.setLevel(level)
    else:
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        root_logger.setLevel(level)
        
    root_logger.addHandler(handler)
    
    logging.getLogger("aiokafka").setLevel(logging.WARNING)
    logging.getLogger("aiomqtt").setLevel(logging.WARNING)
```

---

## app\db\init_timescale.py

```python
import asyncio
import logging
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings
from app.models.domain import Base

logger = logging.getLogger(__name__)

# Ensure your settings point to asyncpg: "postgresql+asyncpg://user:pass@localhost:5432/ev_platform"
DATABASE_URL = settings.database_url 

async def init_db():
    logger.info("Initializing database and TimescaleDB hypertables...")
    engine = create_async_engine(DATABASE_URL, echo=True)

    async with engine.begin() as conn:
        # 1. Create standard PostgreSQL tables
        await conn.run_sync(Base.metadata.create_all)
        
        logger.info("Standard tables created. Converting time-series tables to TimescaleDB hypertables...")

        # 2. Execute TimescaleDB Hypertable conversion commands
        # The 'IF NOT EXISTS' equivalent in Timescale is handled by checking if it's already a hypertable,
        # but create_hypertable has a 'if_not_exists' flag we can use.
        hypertable_queries = [
            "SELECT create_hypertable('telemetry_records', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('battery_records', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('location_history', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('status_history', 'timestamp', if_not_exists => TRUE);"
        ]

        for query in hypertable_queries:
            try:
                # We use text() wrapper for raw SQL in SQLAlchemy 2.0
                from sqlalchemy import text
                await conn.execute(text(query))
            except Exception as e:
                # If TimescaleDB extension is missing, this will catch and warn you
                logger.warning(f"Failed to create hypertable (ensure TimescaleDB extension is enabled): {e}")

    await engine.dispose()
    logger.info("Database initialization complete.")

if __name__ == "__main__":
    asyncio.run(init_db())
```

---

## app\db\session.py

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

# 1. Create the Async Engine
engine = create_async_engine(
    settings.database_url,
    echo=False,  # Set to True for debugging SQL queries
    pool_size=20, # Connection pool optimized for high-throughput streaming
    max_overflow=10
)

# 2. Create the Async Session Maker
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False # Prevents SQLAlchemy from issuing extra SELECTs after commit
)

# 3. Dependency function for FastAPI routes and Kafka processors
async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session
```

---

## app\models\domain.py

```python
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# ---------------------------------------------------------
# TIME-SERIES HYPERTABLE MODELS (High-Frequency Data)
# ---------------------------------------------------------

class TelemetryRecord(Base):
    __tablename__ = "telemetry_records"

    # TimescaleDB requires the time column in the primary key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    speed_kph = Column(Float, nullable=False)
    odometer_km = Column(Float, nullable=False)
    motor_temperature_c = Column(Float, nullable=False)
    torque_nm = Column(Float, nullable=False)
    inverter_efficiency = Column(Float, nullable=False)

class BatteryRecord(Base):
    __tablename__ = "battery_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    state_of_charge_pct = Column(Float, nullable=False)
    state_of_health_pct = Column(Float, nullable=False)
    voltage = Column(Float, nullable=False)
    current_amps = Column(Float, nullable=False)
    cell_temperature_max_c = Column(Float, nullable=False)
    internal_resistance_ohm = Column(Float, nullable=False)

class LocationHistory(Base):
    __tablename__ = "location_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    altitude_m = Column(Float, nullable=True)
    heading_deg = Column(Integer, nullable=True)
    gps_fix_quality = Column(String(20), nullable=True)

class StatusHistory(Base):
    __tablename__ = "status_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    operational_status = Column(String(50), nullable=False)
    active_error_codes = Column(JSON, default=list)
    driver_id = Column(String(50), nullable=True)

# ---------------------------------------------------------
# RELATIONAL MODELS (Low-Frequency / State Data)
# ---------------------------------------------------------

class ChargingSession(Base):
    __tablename__ = "charging_sessions"

    # Standard relational table: only ID is the primary key
    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, name="id")
    vehicle_id = Column(String(50), nullable=False, index=True)
    charger_id = Column(String(50), nullable=True)
    
    start_time = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    end_time = Column(DateTime(timezone=True), nullable=True)
    
    status = Column(String(20), nullable=False, default="ACTIVE") # ACTIVE, COMPLETED, FAILED
    energy_consumed_kwh = Column(Float, nullable=True, default=0.0)
```

---

## app\models\relational.py

```python
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, index=True)
    voltage = Column(Float, nullable=False)
    current = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    soc = Column(Float, nullable=False)  # State of Charge (0-100)

class ChargingSession(Base):
    __tablename__ = "charging_sessions"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)
    energy_delivered_kwh = Column(Float, nullable=False)
    starting_soc = Column(Float, nullable=False)
    ending_soc = Column(Float, nullable=True)

class BatteryHealth(Base):
    __tablename__ = "battery_health"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), unique=True, nullable=False, index=True)
    capacity_fade = Column(Float, nullable=False)  # Ah drop
    cycle_count = Column(Integer, nullable=False)
    state_of_health = Column(Float, nullable=False)  # percentage (0-100)
    remaining_useful_life = Column(Integer, nullable=False)  # estimated cycles remaining

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    severity = Column(String(20), nullable=False)  # Critical, Warning, Info
    type = Column(String(50), nullable=False)  # Thermal, Over-voltage, Anomaly
    description = Column(String(255), nullable=False)
    resolved = Column(Boolean, default=False)

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    risk_score = Column(Float, default=0.0)
    material_supplied = Column(String(50), nullable=False)  # Lithium, Cobalt, Nickel, etc.

class MaintenanceLog(Base):
    __tablename__ = "maintenance_logs"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String(255), nullable=False)
    action_taken = Column(String(255), nullable=True)
    status = Column(String(50), default="Pending")  # Pending, In Progress, Completed
```

---

## app\repositories\domain.py

```python
from typing import List, Optional, Dict, Any
from datetime import datetime
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

class TelemetryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: TelemetryRecord) -> None:
        """High-speed async insert for kinematic telemetry."""
        self.session.add(record)
        await self.session.commit()

    async def history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Retrieves raw kinematics history within a time window."""
        stmt = (
            select(TelemetryRecord)
            .where(
                TelemetryRecord.vehicle_id == vehicle_id,
                TelemetryRecord.timestamp >= start_time,
                TelemetryRecord.timestamp <= end_time
            )
            .order_by(desc(TelemetryRecord.timestamp))
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def timeseries_aggregation(self, vehicle_id: str, interval: str = "1 hour", limit: int = 24) -> List[Dict[str, Any]]:
        """
        Uses TimescaleDB's native time_bucket function to aggregate data efficiently.
        Returns the average speed and max motor temperature per time bucket.
        """
        # FIX: Changed FROM ev_telemetry to FROM telemetry_records to match domain.py
        query = text("""
            SELECT 
                time_bucket(CAST(:interval AS INTERVAL), timestamp) AS time_bucket,
                AVG(speed_kph) AS avg_speed,
                MAX(motor_temperature_c) AS max_motor_temp,
                AVG(torque_nm) AS avg_torque
            FROM telemetry_records
            WHERE vehicle_id = :vehicle_id
            GROUP BY time_bucket
            ORDER BY time_bucket DESC
            LIMIT :limit;
        """)
        
        result = await self.session.execute(query, {"interval": interval, "vehicle_id": vehicle_id, "limit": limit})
        
        return [
            {"time": row[0], "avg_speed": round(row[1], 2) if row[1] is not None else 0.0, "max_temp": round(row[2], 2) if row[2] is not None else 0.0} 
            for row in result.fetchall()
        ]


class BatteryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: BatteryRecord) -> None:
        """High-speed async insert for electro-chemical metrics."""
        self.session.add(record)
        await self.session.commit()

    async def latest(self, vehicle_id: str) -> Optional[BatteryRecord]:
        """Fetches the absolute latest battery state."""
        stmt = (
            select(BatteryRecord)
            .where(BatteryRecord.vehicle_id == vehicle_id)
            .order_by(desc(BatteryRecord.timestamp))
            .limit(1)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def degradation_history(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[Dict[str, Any]]:
        """
        Calculates daily State of Health (SoH) degradation and Internal Resistance growth.
        """
        query = text("""
            SELECT
                time_bucket('1 day', timestamp) AS day,
                MIN(state_of_health_pct) as min_soh,
                MAX(internal_resistance_ohm) as max_resistance
            FROM battery_records
            WHERE vehicle_id = :vehicle_id AND timestamp >= :start AND timestamp <= :end
            GROUP BY day
            ORDER BY day ASC;
        """)
        
        result = await self.session.execute(
            query, {"vehicle_id": vehicle_id, "start": start_time, "end": end_time}
        )
        return [{"date": row[0], "soh_pct": float(row[1]), "resistance_ohm": float(row[2])} for row in result.fetchall()]


class LocationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: LocationHistory) -> None:
        self.session.add(record)
        await self.session.commit()

    async def route_playback(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """Retrieves an ordered path of coordinates for map playback."""
        stmt = (
            select(LocationHistory)
            .where(
                LocationHistory.vehicle_id == vehicle_id,
                LocationHistory.timestamp >= start_time,
                LocationHistory.timestamp <= end_time
            )
            .order_by(LocationHistory.timestamp)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()


class ChargingRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_session(self, session_record: ChargingSession) -> ChargingSession:
        """Initializes a new charging session."""
        self.session.add(session_record)
        await self.session.commit()
        await self.session.refresh(session_record)
        return session_record

    async def complete_session(self, session_id: str, end_time: datetime, total_kwh: float) -> Optional[ChargingSession]:
        """Updates an active charging session to COMPLETED."""
        stmt = select(ChargingSession).where(ChargingSession.session_id == session_id)
        result = await self.session.execute(stmt)
        charging_session = result.scalar_one_or_none()
        
        if charging_session:
            charging_session.end_time = end_time
            charging_session.energy_consumed_kwh = total_kwh
            charging_session.status = "COMPLETED"
            await self.session.commit()
            
        return charging_session
```

---

## app\schemas\payloads.py

```python
# from typing import Dict, Any, Optional
# from pydantic import BaseModel, Field

# class TelemetryPayload(BaseModel):
#     """Core kinematic data from the vehicle's engine and operational control units."""
#     speed_kph: float = Field(..., ge=0, le=200)
#     odometer_km: float = Field(..., ge=0)
#     motor_temperature_c: float = Field(..., ge=-40, le=150)
#     torque_nm: float = Field(...)
#     inverter_efficiency: float = Field(..., ge=0, le=1)


# class BatteryPayload(BaseModel):
#     """Real-time electro-chemical battery state statistics."""
#     state_of_charge_pct: float = Field(..., ge=0, le=100)
#     state_of_health_pct: float = Field(..., ge=0, le=100)
#     voltage: float = Field(..., ge=0, le=1000)
#     current_amps: float = Field(...)
#     cell_temperature_max_c: float = Field(..., ge=-40, le=100)
#     internal_resistance_ohm: float = Field(..., ge=0)


# class LocationPayload(BaseModel):
#     """High-precision positional telemetry coordinate data."""
#     latitude: float = Field(..., ge=-90, le=90)
#     longitude: float = Field(..., ge=-180, le=180)
#     altitude_m: float = Field(..., ge=-500, le=9000)
#     heading_deg: float = Field(..., ge=0, le=360)
#     gps_fix_quality: int = Field(..., description="0=Invalid, 1=GPS, 2=DGPS")


# class ChargingPayload(BaseModel):
#     """State management metrics during an active battery charging session."""
#     charger_id: str = Field(...)
#     charging_rate_kw: float = Field(..., ge=0)
#     time_to_full_mins: float = Field(..., ge=0)
#     connector_type: str = Field(..., description="CCS2, Megawatt, etc.")


# class StatusPayload(BaseModel):
#     """High-level operating mode state flags."""
#     operational_status: str = Field(..., description="READY, OPERATIONAL, FAULT, OFFLINE")
#     active_error_codes: list[str] = Field(default_factory=list)
#     driver_id: Optional[str] = Field(default=None)


# class AlertsPayload(BaseModel):
#     """Immediate hardware or safety critical notifications."""
#     alert_code: str = Field(...)
#     severity: str = Field(..., description="INFO, WARNING, CRITICAL")
#     component: str = Field(..., description="BATTERY, MOTOR, BRAKES, POWERTRAIN")
#     description: str = Field(...)


# class HeartbeatPayload(BaseModel):
#     """Lightweight diagnostics asserting infrastructure network health."""
#     uptime_seconds: int = Field(..., ge=0)
#     firmware_version: str = Field(...)
#     signal_strength_dbm: int = Field(..., le=0)



from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field, ConfigDict

# 1. CREATE THE BASE CLASS
class BasePayload(BaseModel):
    """Base configuration allowing both old aliases and new enterprise keys, while keeping extra data."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")

# 2. INHERIT FROM BasePayload (not BaseModel) FOR ALL YOUR SCHEMAS

class TelemetryPayload(BasePayload):
    """Kinematic data mapping simulator inputs to system targets with safe defaults."""
    speed_kph: float = Field(default=0.0, validation_alias="speed", ge=0, le=200)
    odometer_km: float = Field(default=0.0, validation_alias="odometer", ge=0)
    motor_temperature_c: float = Field(default=65.0, validation_alias="ambient_temperature", ge=-40, le=150)
    # Simulator doesn't provide torque or efficiency yet; generate clean platform mock defaults
    torque_nm: float = Field(default=210.5, description="Fallback tracking default")
    inverter_efficiency: float = Field(default=0.94, ge=0, le=1)

class BatteryPayload(BasePayload):
    """Electro-chemical stats providing field transformations for native simulator outputs."""
    state_of_charge_pct: float = Field(..., validation_alias="soc", ge=0, le=100)
    state_of_health_pct: float = Field(..., validation_alias="soh", ge=0, le=100)
    voltage: float = Field(..., ge=0, le=1000)
    current_amps: float = Field(..., validation_alias="current")
    cell_temperature_max_c: float = Field(..., validation_alias="cell_temperature", ge=-40, le=100)
    internal_resistance_ohm: float = Field(..., validation_alias="internal_resistance", ge=0)

class LocationPayload(BasePayload):
    """Positional mapping supporting clean initialization blocks for empty topics."""
    latitude: float = Field(default=39.7392, ge=-90, le=90)
    longitude: float = Field(default=-104.9903, ge=-180, le=180)
    altitude_m: float = Field(default=1609.0, ge=-500, le=9000)
    heading_deg: float = Field(default=0.0, ge=0, le=360)
    gps_fix_quality: int = Field(default=1)

class ChargingPayload(BasePayload):
    """Fallback charging structures for silent initialization loops."""
    charger_id: str = Field(default="CHG-STATION-MOCK")
    charging_rate_kw: float = Field(default=0.0, ge=0)
    time_to_full_mins: float = Field(default=0.0, ge=0)
    connector_type: str = Field(default="CCS2")

class StatusPayload(BasePayload):
    operational_status: str = Field(default="OPERATIONAL")
    active_error_codes: List[str] = Field(default_factory=list)
    driver_id: Optional[str] = Field(default="SYSTEM_AUTO")

class AlertsPayload(BasePayload):
    alert_code: str = Field(default="CLR_00")
    severity: str = Field(default="INFO")
    component: str = Field(default="SYSTEM")
    description: str = Field(default="Healthy baseline initialization status.")

class HeartbeatPayload(BasePayload):
    uptime_seconds: int = Field(default=0, ge=0)
    firmware_version: str = Field(default="v1.0.0-mock")
    signal_strength_dbm: int = Field(default=-50, le=0)
```

---

## app\schemas\telemetry.py

```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class TelemetryBase(BaseModel):
    vehicle_id: str
    voltage: float
    current: float
    temperature: float
    soc: float

class TelemetryCreate(TelemetryBase):
    pass

class TelemetryResponse(TelemetryBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class BatteryHealthResponse(BaseModel):
    vehicle_id: str
    capacity_fade: float
    cycle_count: int
    state_of_health: float
    remaining_useful_life: int

    class Config:
        from_attributes = True

class AlertResponse(BaseModel):
    id: int
    vehicle_id: str
    timestamp: datetime
    severity: str
    type: str
    description: str
    resolved: bool

    class Config:
        from_attributes = True

class SupplierRiskResponse(BaseModel):
    id: int
    name: str
    location: str
    risk_score: float
    material_supplied: str

    class Config:
        from_attributes = True

class DependencyNode(BaseModel):
    id: str
    label: str
    properties: dict

class DependencyEdge(BaseModel):
    source: str
    target: str
    type: str

class GraphDependencyResponse(BaseModel):
    nodes: List[DependencyNode]
    edges: List[DependencyEdge]
```

---

## app\services\telemetry.py

```python
from datetime import datetime
from typing import List, Dict, Any, Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.domain import (
    TelemetryRepository,
    BatteryRepository,
    LocationRepository,
    ChargingRepository
)
from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

# ---------------------------------------------------------
# BUSINESS LOGIC & VALIDATION RULES
# ---------------------------------------------------------

def validate_time_window(start_time: datetime, end_time: datetime, max_days: int = 30) -> None:
    """Enforces strict boundaries on historical queries to prevent database memory exhaustion."""
    if start_time > end_time:
        raise HTTPException(
            status_code=400, 
            detail="Invalid request: start_time cannot be later than end_time."
        )
    
    delta = end_time - start_time
    if delta.days > max_days:
        raise HTTPException(
            status_code=400, 
            detail=f"Query rejected: Requested time range of {delta.days} days exceeds the maximum allowed window of {max_days} days."
        )

# ---------------------------------------------------------
# DOMAIN SERVICES
# ---------------------------------------------------------

class TelemetryService:
    def __init__(self, session: AsyncSession):
        self.repo = TelemetryRepository(session)

    async def get_history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Validates the time window before fetching raw kinematic history."""
        validate_time_window(start_time, end_time, max_days=30)
        return await self.repo.history(vehicle_id, start_time, end_time, limit)

    async def get_timeseries(self, vehicle_id: str, interval: str = "1 hour", limit: int = 24) -> List[Dict[str, Any]]:
        """Pass-through for aggregated time-series data."""
        # TimescaleDB handles intervals safely, but we cap the limit to prevent runaway aggregations
        safe_limit = min(limit, 1000) 
        return await self.repo.timeseries_aggregation(vehicle_id, interval, safe_limit)


class BatteryService:
    def __init__(self, session: AsyncSession):
        self.repo = BatteryRepository(session)

    async def get_latest(self, vehicle_id: str) -> Optional[BatteryRecord]:
        """Fetches the current real-time state of the battery."""
        record = await self.repo.latest(vehicle_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"No battery telemetry found for vehicle {vehicle_id}")
        return record

    async def get_degradation(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[Dict[str, Any]]:
        """
        Battery degradation occurs slowly, so we allow a longer 90-day analytics window 
        specifically for this aggregated query.
        """
        validate_time_window(start_time, end_time, max_days=90)
        return await self.repo.degradation_history(vehicle_id, start_time, end_time)


class LocationService:
    def __init__(self, session: AsyncSession):
        self.repo = LocationRepository(session)

    async def get_route(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """
        GPS route playback queries pull dense datasets. 
        We enforce a strict 7-day maximum window to protect bandwidth and memory.
        """
        validate_time_window(start_time, end_time, max_days=7)
        return await self.repo.route_playback(vehicle_id, start_time, end_time)
```

---

## app\api\v1\api.py

```python
from fastapi import APIRouter
from .endpoints import health, telemetry, ml_inference, supply_chain, sustainability

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(telemetry.router, tags=["telemetry"])
api_router.include_router(ml_inference.router, tags=["ml_inference"])
api_router.include_router(supply_chain.router, tags=["supply_chain"])
api_router.include_router(sustainability.router, tags=["sustainability"])
```

---

## app\api\v1\rest_routes.py

```python
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.db.session import get_db_session
from app.services.telemetry import TelemetryService, BatteryService, LocationService
from app.repositories.domain import ChargingRepository
from app.models.domain import ChargingSession

router = APIRouter(prefix="/api/v1", tags=["Telemetry & Domain Data"])

# ---------------------------------------------------------
# REQUEST SCHEMAS
# ---------------------------------------------------------
class ChargingSessionCreate(BaseModel):
    vehicle_id: str
    charger_id: str

# ---------------------------------------------------------
# TELEMETRY ENDPOINTS
# ---------------------------------------------------------

@router.get("/telemetry/latest")
async def get_latest_telemetry(
    vehicle_id: str,
    session: AsyncSession = Depends(get_db_session)
):
    """Returns the most recent kinematics reading for a specific vehicle."""
    service = TelemetryService(session)
    # We query history with a limit of 1 over the last 24 hours to find the absolute latest
    end = datetime.utcnow()
    start = end - timedelta(days=1)
    
    records = await service.get_history(vehicle_id, start_time=start, end_time=end, limit=1)
    if not records:
        raise HTTPException(status_code=404, detail="No recent telemetry found for this vehicle.")
    return records[0]


@router.get("/telemetry/timeseries")
async def get_telemetry_timeseries(
    vehicle_id: str,
    interval: str = Query("1 hour", description="TimescaleDB interval (e.g., '15 minutes', '1 hour')"),
    limit: int = Query(24, le=1000),
    session: AsyncSession = Depends(get_db_session)
):
    """Returns aggregated kinematic metrics grouped by time buckets for charting."""
    service = TelemetryService(session)
    return await service.get_timeseries(vehicle_id, interval=interval, limit=limit)

# ---------------------------------------------------------
# BATTERY ENDPOINTS
# ---------------------------------------------------------

@router.get("/battery/latest")
async def get_latest_battery(
    vehicle_id: str,
    session: AsyncSession = Depends(get_db_session)
):
    """Returns the absolute real-time State of Charge and Health for the battery."""
    service = BatteryService(session)
    return await service.get_latest(vehicle_id)

# ---------------------------------------------------------
# LOCATION ENDPOINTS
# ---------------------------------------------------------

@router.get("/location/history")
async def get_location_history(
    vehicle_id: str,
    start_time: datetime,
    end_time: datetime,
    session: AsyncSession = Depends(get_db_session)
):
    """Retrieves an ordered array of GPS coordinates for map route playback."""
    service = LocationService(session)
    return await service.get_route(vehicle_id, start_time, end_time)

# ---------------------------------------------------------
# CHARGING ENDPOINTS
# ---------------------------------------------------------

@router.post("/charging/session")
async def start_charging_session(
    payload: ChargingSessionCreate,
    session: AsyncSession = Depends(get_db_session)
):
    """Initializes a new charging session in the database with explicit timestamping."""
    repo = ChargingRepository(session)
    new_session = ChargingSession(
        vehicle_id=payload.vehicle_id,
        charger_id=payload.charger_id,
        start_time=datetime.utcnow(),  # Add this explicit timestamp
        status="ACTIVE",
        energy_consumed_kwh=0.0
    )
    return await repo.create_session(new_session)
```

---

## app\api\v1\endpoints\health.py

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": "2026-07-10T09:05:00Z",
        "version": "1.0.0"
    }
```

---

## app\api\v1\endpoints\ml_inference.py

```python
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException
from ....schemas.telemetry import BatteryHealthResponse
import asyncio
import random
import json

router = APIRouter()

MOCK_BATTERY_HEALTH = {
    "EV-HD-001": {"vehicle_id": "EV-HD-001", "capacity_fade": 5.8, "cycle_count": 260, "state_of_health": 96.0, "remaining_useful_life": 1240},
    "EV-HD-002": {"vehicle_id": "EV-HD-002", "capacity_fade": 9.2, "cycle_count": 410, "state_of_health": 91.0, "remaining_useful_life": 890},
    "EV-HD-003": {"vehicle_id": "EV-HD-003", "capacity_fade": 2.1, "cycle_count": 95, "state_of_health": 98.0, "remaining_useful_life": 1450},
    "EV-HD-004": {"vehicle_id": "EV-HD-004", "capacity_fade": 17.5, "cycle_count": 780, "state_of_health": 83.0, "remaining_useful_life": 430},
}

@router.get("/battery/status", response_model=BatteryHealthResponse)
def get_battery_status(vehicle_id: str = Query(..., description="ID of the EV vehicle asset")):
    if vehicle_id not in MOCK_BATTERY_HEALTH:
        raise HTTPException(status_code=404, detail="Battery status not found for vehicle")
    return MOCK_BATTERY_HEALTH[vehicle_id]

@router.post("/predict/rul")
def predict_rul(payload: dict):
    # Mock ML inference request utilizing temperature, voltage, cycle profiles
    voltage = payload.get("voltage", 380)
    temperature = payload.get("temperature", 35)
    cycle_count = payload.get("cycle_count", 100)
    
    # Simple linear degradation simulation
    base_life = 1500
    degradation = (cycle_count * 1.1) + (temperature * 2.5) + (400 - voltage)
    estimated_rul = max(0, int(base_life - degradation))
    
    return {
        "predicted_rul_cycles": estimated_rul,
        "confidence_interval": [estimated_rul - 50, estimated_rul + 50],
        "model_version": "xgboost-battery-rul-v1.0"
    }

@router.post("/predict/soh")
def predict_soh(payload: dict):
    capacity = payload.get("capacity", 120.0)
    nominal_capacity = payload.get("nominal_capacity", 120.0)
    
    soh = (capacity / nominal_capacity) * 100.0
    return {
        "state_of_health": round(soh, 2),
        "capacity_fade_ah": round(nominal_capacity - capacity, 2),
        "model_version": "regression-degradation-soh-v1.0"
    }

@router.post("/predict/anomaly")
def predict_anomaly(payload: dict):
    temperature = payload.get("temperature", 25.0)
    voltage = payload.get("voltage", 390.0)
    
    # Anomaly indicator: if temp exceeds threshold or voltage is abnormally low
    is_anomaly = False
    anomaly_score = 0.05
    
    if temperature > 45.0 or voltage < 320.0:
        is_anomaly = True
        anomaly_score = 0.89 + (temperature * 0.002)
        
    return {
        "is_anomaly": is_anomaly,
        "anomaly_score": round(anomaly_score, 3),
        "anomalous_features": ["temperature" if temperature > 45.0 else None, "voltage" if voltage < 320.0 else None],
        "model_version": "isolation-forest-anomaly-v1.0"
    }

@router.websocket("/telemetry/ws/{vehicle_id}")
async def websocket_endpoint(websocket: WebSocket, vehicle_id: str):
    await websocket.accept()
    try:
        while True:
            # Generate simulated live streaming data for WebSockets
            data = {
                "vehicle_id": vehicle_id,
                "timestamp": str(asyncio.get_event_loop().time()),
                "voltage": round(random.uniform(370, 410), 2),
                "current": round(random.uniform(-50, 50), 2),
                "temperature": round(random.uniform(30, 48), 2),
                "soc": round(random.uniform(20, 99), 1)
              }
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        pass
```

---

## app\api\v1\endpoints\supply_chain.py

```python
from fastapi import APIRouter
from ....schemas.telemetry import SupplierRiskResponse, GraphDependencyResponse
from typing import List

router = APIRouter()

MOCK_SUPPLIERS = [
    {"id": 1, "name": "Salar de Atacama Minerals", "location": "Chile", "risk_score": 24.5, "material_supplied": "Lithium"},
    {"id": 2, "name": "Tianqi Lithium Refining", "location": "Sichuan, China", "risk_score": 86.2, "material_supplied": "Refined Lithium Hydroxide"},
    {"id": 3, "name": "Democratic Republic of Congo Mining", "location": "Katanga", "risk_score": 68.0, "material_supplied": "Cobalt Ore"},
    {"id": 4, "name": "Sumitomo Metal Mining", "location": "Japan", "risk_score": 15.4, "material_supplied": "Cathode Precursors"},
]

@router.get("/suppliers", response_model=List[SupplierRiskResponse])
def get_suppliers():
    return MOCK_SUPPLIERS

@router.get("/risk")
def get_supply_chain_risk():
    return {
        "global_risk_index": 54.8,
        "critical_vulnerability": "High concentration of refining capacity in Sichuan region.",
        "mitigation_plan": "Diversify sourcing contracts with North American refiners.",
        "last_updated": "2026-07-10T09:05:00Z"
    }

@router.get("/materials")
def get_materials_flow():
    return {
        "materials": [
            {"name": "Lithium", "active_flow_tons": 450, "safety_buffer_days": 45},
            {"name": "Cobalt", "active_flow_tons": 120, "safety_buffer_days": 30},
            {"name": "Nickel", "active_flow_tons": 800, "safety_buffer_days": 60},
        ]
    }

@router.get("/dependencies", response_model=GraphDependencyResponse)
def get_dependencies_graph():
    # Return structured nodes & edges simulating a Neo4j Cypher query response
    return {
        "nodes": [
            {"id": "node_mine_1", "label": "Mine", "properties": {"name": "Salar de Atacama Mine", "country": "Chile"}},
            {"id": "node_refiner_1", "label": "Refiner", "properties": {"name": "Tianqi Refining", "country": "China"}},
            {"id": "node_plant_1", "label": "Battery Plant", "properties": {"name": "CATL Yibin", "capacity_gwh": 20}},
            {"id": "node_fleet_1", "label": "Fleet Vehicle", "properties": {"vehicle_id": "EV-HD-004", "hub": "Denver"}}
        ],
        "edges": [
            {"source": "node_mine_1", "target": "node_refiner_1", "type": "SUPPLIES_RAW_MATERIAL"},
            {"source": "node_refiner_1", "target": "node_plant_1", "type": "DELIVERS_REFINED_LITHIUM"},
            {"source": "node_plant_1", "target": "node_fleet_1", "type": "EQUIP_BATTERY_TO"}
        ]
    }
```

---

## app\api\v1\endpoints\sustainability.py

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/carbon")
def get_carbon_metrics():
    return {
        "co2_savings_ytd_tons": 142.6,
        "diesel_displacement_gallons": 14500,
        "grid_emission_intensity_kwh": 0.32,  # kg CO2/kWh
        "scope_1_direct_displaced_tons": 160.4,
        "scope_3_grid_indirect_tons": 17.8
    }

@router.get("/electrification")
def get_electrification_readiness():
    return {
        "readiness_score": 84,
        "total_active_routes": 195,
        "electrified_routes": 82,
        "recommendations": [
            {
                "route_id": "DEN-BOU-01",
                "name": "Denver - Boulder Corridor",
                "readiness_percentage": 94,
                "reason": "Short length, highly dense public fast chargers, low grade variance."
            },
            {
                "route_id": "HOU-LOC-04",
                "name": "Houston Local Hub Delivery",
                "readiness_percentage": 88,
                "reason": "Repeated stop patterns allow dwell-time depot charging."
            }
        ]
    }
```

---

## app\api\v1\endpoints\telemetry.py

```python
from fastapi import APIRouter, Query, HTTPException
from typing import List
from ....schemas.telemetry import TelemetryResponse
import datetime

router = APIRouter()

MOCK_VEHICLES = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]

MOCK_TELEMETRY = {
    "EV-HD-001": {"vehicle_id": "EV-HD-001", "voltage": 395.2, "current": 12.4, "temperature": 34.5, "soc": 88.0, "id": 1, "timestamp": datetime.datetime.utcnow()},
    "EV-HD-002": {"vehicle_id": "EV-HD-002", "voltage": 380.1, "current": -45.0, "temperature": 38.2, "soc": 42.0, "id": 2, "timestamp": datetime.datetime.utcnow()},
    "EV-HD-003": {"vehicle_id": "EV-HD-003", "voltage": 401.5, "current": 10.1, "temperature": 33.1, "soc": 91.0, "id": 3, "timestamp": datetime.datetime.utcnow()},
    "EV-HD-004": {"vehicle_id": "EV-HD-004", "voltage": 372.4, "current": 115.0, "temperature": 44.8, "soc": 76.0, "id": 4, "timestamp": datetime.datetime.utcnow()},
}

@router.get("/vehicles", response_model=List[str])
def get_vehicles():
    return MOCK_VEHICLES

@router.get("/telemetry/live", response_model=TelemetryResponse)
def get_live_telemetry(vehicle_id: str = Query(..., description="ID of the EV vehicle asset")):
    if vehicle_id not in MOCK_TELEMETRY:
        raise HTTPException(status_code=404, detail="Vehicle telemetry not found")
    # Update timestamp to match current query time
    telemetry = MOCK_TELEMETRY[vehicle_id]
    telemetry["timestamp"] = datetime.datetime.utcnow()
    return telemetry
```

---

## app\streaming\consumers\client.py

```python
import asyncio
import json
import logging
from typing import Callable, Dict, List, Optional, Awaitable, Any

from aiokafka import AIOKafkaConsumer
from app.core.config import settings

logger = logging.getLogger(__name__)

# Define the callback signature: takes a topic (str) and the parsed JSON payload (dict)
ConsumerCallback = Callable[[str, Dict[str, Any]], Awaitable[None]]

class KafkaEventConsumer:
    """Async Kafka consumer framework with an internal callback router."""

    def __init__(self) -> None:
        self.consumer = None
        self._consume_task = None
        
        # UNIFIED NAME: Changed from self.valid_topics to self.ALLOWED_TOPICS
        self.ALLOWED_TOPICS = {
            "ev.telemetry",
            "ev.battery",
            "ev.location",
            "ev.charging",
            "ev.status",
            "ev.alerts",
            "ev.diagnostics"
        }
        
        # Internal router mapping Kafka topics to a list of registered async callbacks
        self._callbacks: Dict[str, List[ConsumerCallback]] = {
            topic: [] for topic in self.ALLOWED_TOPICS
        }

    def register_callback(self, topic: str, callback: ConsumerCallback) -> None:
        """Allows domain services to hook into specific Kafka topics."""
        if topic not in self.ALLOWED_TOPICS:
            logger.warning("Attempted to register callback for unknown topic.", extra={"topic": topic})
            return
            
        self._callbacks[topic].append(callback)
        logger.debug("Registered new callback.", extra={"topic": topic, "callback": callback.__name__})

    async def start(self) -> None:
        """Initializes the Kafka consumer and begins the listening loop."""
        logger.info("Initializing Kafka consumer framework...")
        
        # *self.ALLOWED_TOPICS safely unpacks the set values as independent string arguments
        self.consumer = AIOKafkaConsumer(
            *self.ALLOWED_TOPICS,
            bootstrap_servers=settings.kafka.bootstrap_servers,
            group_id=settings.kafka.group_id,
            auto_offset_reset=settings.kafka.auto_offset_reset,
            enable_auto_commit=True
        )
        
        try:
            await self.consumer.start()
            logger.info("Kafka Consumer successfully connected to brokers.")
            
            # Spin up the background consuming loop
            self._consume_task = asyncio.create_task(self._consume_loop())
        except Exception as e:
            logger.critical("Failed to connect Kafka Consumer.", exc_info=True)
            raise

    async def stop(self) -> None:
        """Gracefully shuts down the consumer task and connection."""
        if self._consume_task:
            self._consume_task.cancel()
            try:
                await self._consume_task
            except asyncio.CancelledError:
                pass
                
        if self.consumer:
            await self.consumer.stop()
            logger.info("Kafka Consumer disconnected cleanly.")

    async def _consume_loop(self) -> None:
        """Background loop retrieving messages and dispatching them to callbacks."""
        if not self.consumer:
            return

        try:
            async for message in self.consumer:
                topic = message.topic
                
                # Check if anyone actually cares about this topic before parsing
                if not self._callbacks.get(topic):
                    continue

                try:
                    # Parse the raw bytes back into the EventEnvelope JSON dictionary
                    payload_dict = json.loads(message.value.decode("utf-8"))
                    
                    # Dispatch to all registered callbacks asynchronously
                    # We use create_task so a slow callback doesn't block the Kafka consumer loop
                    for callback in self._callbacks[topic]:
                        asyncio.create_task(self._execute_callback(callback, topic, payload_dict))
                        
                except json.JSONDecodeError:
                    logger.error("Failed to decode Kafka message as JSON.", extra={"topic": topic})
                except Exception as e:
                    logger.error("Error dispatching Kafka message.", exc_info=True, extra={"topic": topic})

        except asyncio.CancelledError:
            logger.info("Kafka consumption task gracefully cancelled.")
            
    async def _execute_callback(self, callback: ConsumerCallback, topic: str, payload: Dict[str, Any]) -> None:
        """Safely executes a callback, catching any unhandled exceptions."""
        try:
            await callback(topic, payload)
        except Exception as e:
            logger.error(
                "Unhandled exception in consumer callback.", 
                exc_info=True, 
                extra={"topic": topic, "callback": callback.__name__}
            )
```

---

## app\streaming\mqtt\client.py

```python
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
                
                # 1. Subscribe to all fixed data topics
                for topic in self.topics:
                    await client.subscribe(topic)
                    logger.info("Subscribed to MQTT topic", extra={"mqtt_topic": topic})
                
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

        # 1. Structural Schema Validation Check
        validated_model = validate_raw_payload(topic, payload_bytes)
        
        if validated_model:
            # 2. Normalize and extract the target domain channel type
            envelope = normalize_to_envelope(topic, validated_model)
            
            # DYNAMIC ROUTING FIX: Grab the exact destination from the normalizer mapping
            target_kafka_topic = envelope.event_type
            
            # 3. Stream asynchronously straight onto the specific Kafka Topic Bus line
            kafka_producer = container.kafka_producer
            asyncio.create_task(kafka_producer.publish(target_kafka_topic, envelope))
```

---

## app\streaming\processor\telemetry.py

```python
import logging
from typing import Dict, Any
from datetime import datetime
from dateutil.parser import isoparse

from app.db.session import AsyncSessionLocal
from app.repositories.domain import (
    TelemetryRepository, 
    BatteryRepository, 
    LocationRepository, 
    ChargingRepository
)
from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

class TelemetryProcessor:
    """Bridges incoming Kafka EventEnvelope payloads to target domain database repositories."""

    @staticmethod
    def _parse_timestamp(ts_str: str) -> datetime:
        """Safely parses ISO-8601 UTC timestamp strings into Python datetime objects."""
        try:
            return isoparse(ts_str)
        except Exception:
            return datetime.utcnow()

    async def process_kinematics(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.telemetry' streams and persists kinematic vectors."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))

        logger.info(f"[PROCESSOR] Intercepted kinematics for vehicle {vehicle_id}")

        record = TelemetryRecord(
            vehicle_id=vehicle_id,
            timestamp=ts,
            speed_kph=float(payload.get("speed_kph", 0.0)),
            odometer_km=float(payload.get("odometer_km", 0.0)),
            motor_temperature_c=float(payload.get("motor_temperature_c", 0.0)),
            torque_nm=float(payload.get("torque_nm", 0.0)),
            inverter_efficiency=float(payload.get("inverter_efficiency", 1.0))
        )

        async with AsyncSessionLocal() as session:
            repo = TelemetryRepository(session)
            await repo.insert(record)

    async def process_battery(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.battery' streams and persists electro-chemical metrics."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))

        logger.info(f"[PROCESSOR] Intercepted battery diagnostics for vehicle {vehicle_id}")

        record = BatteryRecord(
            vehicle_id=vehicle_id,
            timestamp=ts,
            state_of_charge_pct=float(payload.get("state_of_charge_pct", 0.0)),
            state_of_health_pct=float(payload.get("state_of_health_pct", 100.0)),
            voltage=float(payload.get("voltage", 0.0)),
            current_amps=float(payload.get("current_amps", 0.0)),
            cell_temperature_max_c=float(payload.get("cell_temperature_max_c", 0.0)),
            internal_resistance_ohm=float(payload.get("internal_resistance_ohm", 0.0))
        )

        async with AsyncSessionLocal() as session:
            repo = BatteryRepository(session)
            await repo.insert(record)

    async def process_location(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.location' streams and persists geospatial telemetry chunks."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))

        logger.info(f"[PROCESSOR] Intercepted geospatial logs for vehicle {vehicle_id}")

        record = LocationHistory(
            vehicle_id=vehicle_id,
            timestamp=ts,
            latitude=float(payload.get("latitude", 0.0)),
            longitude=float(payload.get("longitude", 0.0)),
            altitude_m=float(payload.get("altitude_m", 0.0)) if payload.get("altitude_m") else None,
            heading_deg=int(payload.get("heading_deg", 0)) if payload.get("heading_deg") else None,
            gps_fix_quality=payload.get("gps_fix_quality", "UNKNOWN")
        )

        async with AsyncSessionLocal() as session:
            repo = LocationRepository(session)
            await repo.insert(record)

    async def process_charging(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.charging' infrastructure streams to manage session lifecycle state."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))
        
        charger_id = payload.get("charger_id")
        connector_type = payload.get("connector_type", "NONE")

        # In a real environment, you would check for an active session to see whether to create or update.
        # For this stage of the bridge ingestion path, we register the event log explicitly.
        if charger_id and connector_type != "NONE":
            logger.info(f"[PROCESSOR] Processing active charging payload for vehicle {vehicle_id}")
            record = ChargingSession(
                vehicle_id=vehicle_id,
                charger_id=charger_id,
                start_time=ts,
                status="ACTIVE",
                energy_consumed_kwh=float(payload.get("charging_rate_kw", 0.0)) / 60.0 # Instantaneous integration approximation
            )
            async with AsyncSessionLocal() as session:
                repo = ChargingRepository(session)
                await repo.create_session(record)
```

---

## app\streaming\producers\client.py

```python
import logging
from typing import Optional
from aiokafka import AIOKafkaProducer

from app.core.config import settings
from app.contracts.envelope import EventEnvelope

logger = logging.getLogger(__name__)

class KafkaEventProducer:
    """Async Kafka producer for routing normalized events to the message bus."""
    
    def __init__(self) -> None:
        self.producer: Optional[AIOKafkaProducer] = None

    async def start(self) -> None:
        """Initializes the Kafka producer connection pool."""
        logger.info("Initializing Kafka producer...", extra={"brokers": settings.kafka.bootstrap_servers})
        
        self.producer = AIOKafkaProducer(
            bootstrap_servers=settings.kafka.bootstrap_servers,
            client_id="ev_streaming_producer",
            # Acknowledge leader write for high throughput, safe enough for telemetry
            acks=1 
        )
        
        try:
            await self.producer.start()
            logger.info("Kafka Producer successfully connected.")
        except Exception as e:
            logger.critical("Failed to connect Kafka Producer.", exc_info=True)
            raise

    async def stop(self) -> None:
        """Flushes pending batches and cleanly disconnects."""
        if self.producer:
            await self.producer.stop()
            logger.info("Kafka Producer disconnected.")

    async def publish(self, target_topic: str, event: EventEnvelope) -> None:
        """Serializes the event envelope and publishes it to the specified topic."""
        if not self.producer:
            logger.error("Attempted to publish without an active Kafka connection.")
            return

        try:
            # Pydantic v2 serialization to JSON bytes
            payload_bytes = event.model_dump_json().encode("utf-8")
            
            # Fire-and-forget for telemetry throughput, though send_and_wait can be used for guarantees
            await self.producer.send(target_topic, value=payload_bytes)
            
        except Exception as e:
            logger.error(
                "Failed to publish event to Kafka.",
                exc_info=True,
                extra={"target_topic": target_topic, "event_id": str(event.event_id)}
            )
```

---

## app\streaming\serializers\normalizer.py

```python
# import logging
# from typing import Dict
# from pydantic import BaseModel
# from app.contracts.envelope import EventEnvelope

# logger = logging.getLogger(__name__)

# # Map incoming MQTT topics to target Kafka topics/event types
# MQTT_TO_KAFKA_ROUTE: Dict[str, str] = {
#     "ev/telemetry": "telemetry.raw",
#     "ev/battery": "telemetry.raw",  # Routing battery data to the same raw firehose for now
#     "ev/location": "telemetry.raw",
#     "ev/charging": "telemetry.raw",
#     "ev/status": "telemetry.raw",
#     "ev/alerts": "alerts",
#     "ev/heartbeat": "telemetry.raw"
# }

# def normalize_to_envelope(mqtt_topic: str, payload: BaseModel) -> EventEnvelope:
#     """
#     Wraps a validated domain payload into the standard Event Envelope.
#     Generates event_id and correlation_id automatically via the schema defaults.
#     """
#     target_event_type = MQTT_TO_KAFKA_ROUTE.get(mqtt_topic, "unknown.raw")
    
#     # In a fully integrated environment, vehicle_id and fleet_id might be extracted
#     # from the MQTT topic structure (e.g., ev/telemetry/{fleet_id}/{vehicle_id}) 
#     # or the payload itself. Since our topics are fixed, we inject placeholders 
#     # for the infrastructure integration phase.
    
#     envelope = EventEnvelope(
#         event_type=target_event_type,
#         source="streaming_ingestion_node",
#         vehicle_id="VEH-SIM-001",
#         fleet_id="FLT-ALPHA-01",
#         payload=payload
#     )
    
#     logger.debug(
#         "Normalized event payload.",
#         extra={
#             "event_id": str(envelope.event_id),
#             "correlation_id": str(envelope.correlation_id),
#             "event_type": target_event_type
#         }
#     )
#     return envelope



import logging
from pydantic import BaseModel
from app.contracts.envelope import EventEnvelope

logger = logging.getLogger(__name__)

# Segmenting the single firehose into clean domain streams
MQTT_TO_KAFKA_ROUTE = {
    "ev/telemetry": "ev.telemetry",
    "ev/battery": "ev.battery",
    "ev/location": "ev.location",
    "ev/charging": "ev.charging",
    "ev/status": "ev.status",
    "ev/alerts": "ev.alerts",
    "ev/heartbeat": "ev.diagnostics"
}

def normalize_to_envelope(mqtt_topic: str, payload: BaseModel) -> EventEnvelope:
    """Wraps the validated payload and dynamically assigns its destination event_type."""
    target_event_type = MQTT_TO_KAFKA_ROUTE.get(mqtt_topic, "ev.unknown")
    
    extracted_vehicle = getattr(payload, "vehicle_id", "VEH-SIM-UNKNOWN")
    
    envelope = EventEnvelope(
        event_type=target_event_type,  # The envelope type now matches the domain stream name
        source="streaming_ingestion_node",
        vehicle_id=extracted_vehicle,
        fleet_id="FLT-ALPHA-01",
        payload=payload
    )
    
    logger.debug(
        "Normalized event payload targeted for domain topic.",
        extra={
            "event_id": str(envelope.event_id),
            "target_topic": target_event_type
        }
    )
    return envelope
```

---

## app\streaming\serializers\validator.py

```python
import json
import logging
from typing import Optional, Dict, Type
from pydantic import BaseModel, ValidationError

from app.schemas.payloads import (
    TelemetryPayload, BatteryPayload, LocationPayload,
    ChargingPayload, StatusPayload, AlertsPayload, HeartbeatPayload
)

logger = logging.getLogger(__name__)

# Map fixed, immutable MQTT topics to their structural validators
TOPIC_SCHEMA_MAP: Dict[str, Type[BaseModel]] = {
    "ev/telemetry": TelemetryPayload,
    "ev/battery": BatteryPayload,
    "ev/location": LocationPayload,
    "ev/charging": ChargingPayload,
    "ev/status": StatusPayload,
    "ev/alerts": AlertsPayload,
    "ev/heartbeat": HeartbeatPayload
}

def validate_raw_payload(topic: str, raw_data: bytes) -> Optional[BaseModel]:
    """
    Parses and structural-checks incoming binary JSON string payloads against domain schemas.
    
    Returns a Pydantic Model instance if valid; returns None if malformed or unknown.
    """
    schema_cls = TOPIC_SCHEMA_MAP.get(topic)
    
    if not schema_cls:
        logger.warning(
            "Received event on unregistered topic. Processing discarded.",
            extra={"mqtt_topic": topic}
        )
        return None

    try:
        # Step 1: Deserialize JSON payload safely
        parsed_json = json.loads(raw_data)
        
        # Step 2: Perform schema enforcement via Pydantic
        validated_model = schema_cls.model_validate(parsed_json)
        return validated_model
        
    except json.JSONDecodeError as jde:
        logger.error(
            "Failed to deserialize payload. Raw input is not clean JSON.",
            exc_info=True,
            extra={"mqtt_topic": topic}
        )
    except ValidationError as ve:
        logger.warning(
            "Payload failed schema compliance assertions. Event dropped.",
            extra={
                "mqtt_topic": topic,
                "validation_errors": ve.errors(include_url=False)
            }
        )
    except Exception as e:
        logger.critical(
            "Unexpected processing failure during validation pipeline.",
            exc_info=True,
            extra={"mqtt_topic": topic}
        )
        
    return None
```

---

## app\streaming\websocket\adapter.py

```python
import logging
from typing import Dict, Any
from app.streaming.websocket.manager import ws_manager

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

async def kafka_to_ws_broadcaster(topic: str, payload: Dict[str, Any]) -> None:
    """
    Standard callback registered with the Kafka Event Consumer.
    Bridges the Kafka bus directly to the WebSocket manager.
    """
    logger.debug("Relaying Kafka event to WebSockets.", extra={"topic": topic})
    await ws_manager.broadcast(topic, payload)
```

---

## app\streaming\websocket\manager.py

```python
import logging
import json
from typing import Dict, Set, Any
from fastapi import WebSocket

logger = logging.getLogger(__name__)

class WebSocketManager:
    """Manages active dashboard WebSocket connections and topic subscriptions."""
    
    def __init__(self) -> None:
        # Maps active WebSocket connections to a set of their subscribed topics
        self.active_connections: Dict[WebSocket, Set[str]] = {}

    async def connect(self, websocket: WebSocket) -> None:
        """Accepts a new connection and initializes an empty subscription set."""
        await websocket.accept()
        self.active_connections[websocket] = set()
        logger.info("New WebSocket dashboard connection established.")

    def disconnect(self, websocket: WebSocket) -> None:
        """Removes a connection from the active pool cleanly."""
        if websocket in self.active_connections:
            del self.active_connections[websocket]
            logger.info("WebSocket dashboard connection removed.")

    async def subscribe(self, websocket: WebSocket, topic: str) -> None:
        """Adds a Kafka topic to the client's subscription list."""
        if websocket in self.active_connections:
            self.active_connections[websocket].add(topic)
            logger.debug("WebSocket subscribed to topic.", extra={"topic": topic})

    async def unsubscribe(self, websocket: WebSocket, topic: str) -> None:
        """Removes a Kafka topic from the client's subscription list."""
        if websocket in self.active_connections and topic in self.active_connections[websocket]:
            self.active_connections[websocket].remove(topic)
            logger.debug("WebSocket unsubscribed from topic.", extra={"topic": topic})

    async def broadcast(self, topic: str, payload: Dict[str, Any]) -> None:
        """Pushes an event payload to all clients subscribed to the topic."""
        
        # print(f"\n--- [LIVE BUS EVENT] Topic: {topic} ---")
        # print(json.dumps(payload, indent=2))
        # print("-" * 40)
        
        # Convert the dictionary payload to a JSON string for transmission
        message = json.dumps({"topic": topic, "data": payload})
        
        stale_connections = []
        
        for websocket, subscriptions in self.active_connections.items():
            if topic in subscriptions:
                try:
                    await websocket.send_text(message)
                except Exception as e:
                    logger.error("Failed to send WebSocket message.", exc_info=True)
                    stale_connections.append(websocket)
                    
        # Cleanup connections that dropped without closing properly
        for stale in stale_connections:
            self.disconnect(stale)

# Global manager instance
ws_manager = WebSocketManager()
```
```

---

## backend\requirements.txt

```text
fastapi>=0.100.0
uvicorn>=0.22.0
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
websockets>=11.0
neo4j>=5.10.0
python-dotenv>=1.0.0
aiomqtt>=2.0.0
aiokafka>=0.8.1
asyncpg>=0.28.0
```

---

## common_schemas\ai_Prediction_service

```
Domain 5 — AI Prediction Service
Responsibility

Provides inference APIs for battery intelligence models. This module exposes machine learning predictions for battery health, remaining useful life, anomaly detection, and battery risk assessment. No model training or data preprocessing is performed within this service.

Directory Structure
backend/app/

schemas/
├── prediction.py

api/v1/endpoints/
├── prediction.py

services/
├── prediction_service.py
├── model_router.py

clients/
├── ml_client.py
Integrations
ML Inference Service
Model Registry (Future)
Supported Models
Remaining Useful Life (RUL)

State of Health Prediction (SoH)

Anomaly Detection

Failure Probability

Thermal Risk

Voltage Risk
Prediction Flow
Frontend

↓

FastAPI

↓

Prediction Service

↓

ML Service

↓

Prediction Response

↓

Frontend
API Definitions
POST /api/v1/predict/rul
Purpose

Predicts Remaining Useful Life (RUL) of a battery.

Request
{
  "vehicle_id":"EV-001",
  "timestamp":"2026-07-14T18:30:00Z",
  "state_of_charge":82,
  "state_of_health":94.2,
  "voltage":387.5,
  "current":42.3,
  "temperature":34.5,
  "capacity_kwh":34.1,
  "internal_resistance":0.012,
  "cycle_count":412
}
Response
{
  "success":true,
  "message":"Prediction Completed",
  "data":{
      "vehicle_id":"EV-001",
      "remaining_cycles":318,
      "remaining_days":214,
      "confidence":0.95
  }
}
POST /api/v1/predict/soh
Purpose

Predicts battery State of Health.

Request
{
  "vehicle_id":"EV-001",
  "timestamp":"2026-07-14T18:30:00Z",
  "voltage":387.5,
  "current":42.3,
  "temperature":34.5,
  "capacity_kwh":34.1,
  "internal_resistance":0.012,
  "cycle_count":412
}
Response
{
  "success":true,
  "message":"Prediction Completed",
  "data":{
      "vehicle_id":"EV-001",
      "predicted_soh":93.8,
      "confidence":0.96
  }
}
POST /api/v1/predict/anomaly
Purpose

Detects abnormal battery behaviour.

Request
{
  "vehicle_id":"EV-001",
  "voltage":387.5,
  "current":42.3,
  "temperature":58.2,
  "state_of_charge":82,
  "cycle_count":412
}
Response
{
  "success":true,
  "message":"Prediction Completed",
  "data":{
      "vehicle_id":"EV-001",
      "anomaly":true,
      "severity":"HIGH",
      "confidence":0.98
  }
}
POST /api/v1/predict/failure
Purpose

Predicts battery failure probability.

Request
{
  "vehicle_id":"EV-001",
  "state_of_health":78,
  "temperature":48,
  "internal_resistance":0.021,
  "cycle_count":812
}
Response
{
  "success":true,
  "message":"Prediction Completed",
  "data":{
      "failure_probability":0.82,
      "risk_level":"HIGH",
      "confidence":0.93
  }
}
POST /api/v1/predict/thermal-risk
Purpose

Evaluates thermal runaway risk.

Request
{
  "vehicle_id":"EV-001",
  "temperature":58,
  "current":62,
  "voltage":384
}
Response
{
  "success":true,
  "message":"Prediction Completed",
  "data":{
      "thermal_risk":"HIGH",
      "risk_score":91,
      "confidence":0.94
  }
}
POST /api/v1/predict/voltage-risk
Purpose

Evaluates voltage imbalance risk.

Request
{
  "vehicle_id":"EV-001",
  "cell_voltage_min":3.82,
  "cell_voltage_max":4.12
}
Response
{
  "success":true,
  "message":"Prediction Completed",
  "data":{
      "voltage_risk":"MEDIUM",
      "imbalance":0.30,
      "confidence":0.91
  }
}
Model Metadata API
GET /api/v1/predict/models
Purpose

Returns available prediction models.

Response
{
    "success":true,
    "message":"Available Models",
    "data":[
        {
            "model":"RUL",
            "version":"1.0"
        },
        {
            "model":"SOH",
            "version":"1.0"
        },
        {
            "model":"ANOMALY",
            "version":"1.0"
        }
    ]
}
Prediction History
GET /api/v1/predict/history
Purpose

Returns historical prediction results.

Query Parameters
vehicle_id

prediction_type

start_time

end_time
Pydantic Schemas
PredictionRequest
vehicle_id:str
timestamp:datetime
state_of_charge:float
state_of_health:float
voltage:float
current:float
temperature:float
capacity_kwh:float
internal_resistance:float
cycle_count:int
PredictionResponse
vehicle_id:str
prediction_type:str
prediction:float
confidence:float
generated_at:datetime
AnomalyResponse
vehicle_id:str
anomaly:bool
severity:str
confidence:float
RiskResponse
vehicle_id:str
risk_level:str
risk_score:float
confidence:float
Enumerations
PredictionType
RUL

SOH

ANOMALY

FAILURE

THERMAL

VOLTAGE
RiskLevel
LOW

MEDIUM

HIGH

CRITICAL
ModelStatus
AVAILABLE

LOADING

OFFLINE
Frontend Team Dependencies

The frontend can immediately integrate the following endpoints:

POST /api/v1/predict/rul

POST /api/v1/predict/soh

POST /api/v1/predict/anomaly

POST /api/v1/predict/failure

POST /api/v1/predict/thermal-risk

POST /api/v1/predict/voltage-risk

GET /api/v1/predict/history

GET /api/v1/predict/models

Primary UI screens:

AI Prediction Dashboard
RUL Card
Battery Health Card
Anomaly Panel
Risk Analysis
Prediction History
Infrastructure Team Dependencies

Required deployment:

ML Inference Service

REST Endpoint

or

ONNX Runtime

or

TorchServe

or

Local Model Loader

Environment variables

ML_SERVICE_URL

MODEL_TIMEOUT

MODEL_VERSION
ML Team Dependencies

This is the primary integration point between Backend and ML.

ML Service Contract

Required endpoint

POST /predict

Input

{
    "prediction_type":"RUL",
    "features":{}
}

Output

{
    "prediction":318,
    "confidence":0.94
}

Backend handles:

Validation
Authentication
Routing
Error handling
Response formatting

ML handles:

Feature preprocessing (if required)
Model inference
Confidence calculation
Error Codes
MODEL_NOT_FOUND

MODEL_TIMEOUT

INVALID_FEATURE_VECTOR

INFERENCE_FAILED

PREDICTION_NOT_SUPPORTED
Deliverables
APIs
POST /api/v1/predict/rul

POST /api/v1/predict/soh

POST /api/v1/predict/anomaly

POST /api/v1/predict/failure

POST /api/v1/predict/thermal-risk

POST /api/v1/predict/voltage-risk

GET /api/v1/predict/models

GET /api/v1/predict/history
Schemas
PredictionRequest

PredictionResponse

AnomalyResponse

RiskResponse
Enums
PredictionType

RiskLevel

ModelStatus
Environment Variables
ML_SERVICE_URL

MODEL_TIMEOUT

MODEL_VERSION
```

---

## common_schemas\alert_notification_service

```
Domain 6 — Alert & Notification Service
Responsibility

Centralized event and alert management service responsible for collecting events from all platform domains, generating alerts, managing alert lifecycle, and delivering real-time notifications to connected clients.

Directory Structure
backend/app/

models/
├── alert.py
├── notification.py

schemas/
├── alert.py
├── notification.py

api/v1/endpoints/
├── alerts.py
├── notifications.py

services/
├── alert_service.py
├── notification_service.py
├── websocket_manager.py
Main Entities
Alert

Represents an active or historical alert generated by the platform.

Attributes
alert_id
vehicle_id
source
category
severity
title
description
status
acknowledged_by
acknowledged_at
created_at
updated_at
Notification

Represents a notification delivered to dashboard clients.

Attributes
notification_id
alert_id
recipient
channel
status
delivered_at
read_at
Database Relationships
Vehicle

1

↓

Many

Alert

1

↓

Many

Notification
Alert Sources
TELEMETRY

AI

SUPPLY_CHAIN

SUSTAINABILITY

MAINTENANCE

SYSTEM
Alert Categories
BATTERY

THERMAL

VOLTAGE

CHARGING

LOCATION

SUPPLIER

CARBON

MAINTENANCE

SYSTEM
API Definitions
GET /api/v1/alerts
Purpose

Returns all alerts with filtering support.

Query Parameters
vehicle_id
severity
category
status
source
start_time
end_time
page
limit
Response
{
  "success": true,
  "message": "Alert List",
  "data": [
    {
      "alert_id": "ALT-1001",
      "vehicle_id": "EV-001",
      "severity": "HIGH",
      "category": "THERMAL",
      "title": "High Battery Temperature",
      "status": "ACTIVE",
      "created_at": "2026-07-14T18:30:00Z"
    }
  ]
}
GET /api/v1/alerts/{alert_id}
Purpose

Returns complete alert details.

Response
{
  "success": true,
  "message": "Alert Details",
  "data": {
    "alert_id": "ALT-1001",
    "vehicle_id": "EV-001",
    "source": "AI",
    "category": "THERMAL",
    "severity": "HIGH",
    "title": "High Battery Temperature",
    "description": "Battery temperature exceeded threshold.",
    "status": "ACTIVE",
    "created_at": "2026-07-14T18:30:00Z"
  }
}
POST /api/v1/alerts
Purpose

Creates a new alert (used internally by platform services).

Request
{
  "vehicle_id": "EV-001",
  "source": "AI",
  "category": "THERMAL",
  "severity": "HIGH",
  "title": "Thermal Risk Detected",
  "description": "Thermal runaway probability exceeded threshold."
}
Response
{
  "success": true,
  "message": "Alert Created",
  "data": {
    "alert_id": "ALT-1001"
  }
}
PATCH /api/v1/alerts/{alert_id}/acknowledge
Purpose

Acknowledges an active alert.

Request
{
  "acknowledged_by": "admin"
}
Response
{
  "success": true,
  "message": "Alert Acknowledged"
}
PATCH /api/v1/alerts/{alert_id}/resolve
Purpose

Marks an alert as resolved.

Response
{
  "success": true,
  "message": "Alert Resolved"
}
DELETE /api/v1/alerts/{alert_id}
Purpose

Deletes an alert (administrative operation).

Response
{
  "success": true,
  "message": "Alert Deleted"
}
GET /api/v1/alerts/history
Purpose

Returns historical alerts.

Query Parameters
vehicle_id
category
severity
start_time
end_time
GET /api/v1/alerts/summary
Purpose

Returns alert statistics for dashboard widgets.

Response
{
  "success": true,
  "message": "Alert Summary",
  "data": {
    "total": 152,
    "active": 12,
    "critical": 2,
    "high": 5,
    "medium": 3,
    "low": 2
  }
}
Notification APIs
GET /api/v1/notifications
Purpose

Returns notification history.

Query Parameters
recipient
status
page
limit
PATCH /api/v1/notifications/{notification_id}/read
Purpose

Marks a notification as read.

Response
{
  "success": true,
  "message": "Notification Marked as Read"
}
GET /api/v1/notifications/unread-count
Purpose

Returns unread notification count.

Response
{
  "success": true,
  "message": "Unread Notifications",
  "data": {
    "count": 8
  }
}

WebSocket APIs
WS /api/v1/ws/alerts
Purpose

Streams real-time alerts to connected dashboard clients.

Event Payload
{
  "alert_id": "ALT-1001",
  "vehicle_id": "EV-001",
  "severity": "HIGH",
  "category": "THERMAL",
  "title": "High Battery Temperature",
  "status": "ACTIVE",
  "created_at": "2026-07-14T18:30:00Z"
}
WS /api/v1/ws/notifications
Purpose

Streams notification events in real time.

Event Payload
{
  "notification_id": "NOT-1001",
  "alert_id": "ALT-1001",
  "title": "Thermal Risk Detected",
  "status": "UNREAD",
  "created_at": "2026-07-14T18:30:00Z"
}
Pydantic Schemas
AlertCreate
vehicle_id: str
source: str
category: str
severity: str
title: str
description: str
AlertResponse
alert_id: str
vehicle_id: str
source: str
category: str
severity: str
title: str
description: str
status: str
created_at: datetime
NotificationResponse
notification_id: str
alert_id: str
recipient: str
channel: str
status: str
delivered_at: datetime
Enumerations
AlertSeverity
LOW

MEDIUM

HIGH

CRITICAL
AlertStatus
ACTIVE

ACKNOWLEDGED

RESOLVED

CLOSED
AlertSource
TELEMETRY

AI

SUPPLY_CHAIN

SUSTAINABILITY

MAINTENANCE

SYSTEM
NotificationStatus
UNREAD

READ

DELIVERED

FAILED
NotificationChannel
DASHBOARD

EMAIL

SMS

WEBHOOK
Frontend Team Dependencies

The frontend can immediately integrate the following endpoints:

GET    /api/v1/alerts
GET    /api/v1/alerts/{alert_id}
GET    /api/v1/alerts/history
GET    /api/v1/alerts/summary

PATCH  /api/v1/alerts/{alert_id}/acknowledge
PATCH  /api/v1/alerts/{alert_id}/resolve

GET    /api/v1/notifications
GET    /api/v1/notifications/unread-count
PATCH  /api/v1/notifications/{notification_id}/read

WS     /api/v1/ws/alerts
WS     /api/v1/ws/notifications

Primary UI screens:

Alert Center
Alert Details
Notification Panel
Dashboard Alert Cards
Real-Time Notification Toasts
Infrastructure Team Dependencies

Required services:

PostgreSQL

Redis (optional for pub/sub)

WebSocket Server

Database tables:

alert

notification

Optional event bus integration:

Kafka

MQTT

Incoming topics/events:

telemetry.events

ai.events

maintenance.events

supply_chain.events

sustainability.events
ML Team Dependencies

The ML team publishes inference events that may generate alerts.

Expected event contract:

{
  "vehicle_id": "EV-001",
  "source": "AI",
  "prediction_type": "THERMAL",
  "severity": "HIGH",
  "title": "Thermal Risk Detected",
  "description": "Thermal runaway probability exceeded threshold."
}

The Alert Service consumes these events and creates platform alerts. The ML service should not directly create alerts in the database.

Deliverables
APIs
GET    /api/v1/alerts
POST   /api/v1/alerts
GET    /api/v1/alerts/{alert_id}
PATCH  /api/v1/alerts/{alert_id}/acknowledge
PATCH  /api/v1/alerts/{alert_id}/resolve
DELETE /api/v1/alerts/{alert_id}
GET    /api/v1/alerts/history
GET    /api/v1/alerts/summary

GET    /api/v1/notifications
PATCH  /api/v1/notifications/{notification_id}/read
GET    /api/v1/notifications/unread-count

WS     /api/v1/ws/alerts
WS     /api/v1/ws/notifications



Schemas
AlertCreate
AlertResponse
NotificationResponse
Database Tables
alert
notification
Enums
AlertSeverity
AlertStatus
AlertSource
NotificationStatus
NotificationChannel
```

---

## common_schemas\analytics_dashoard_service

```
Domain 11 — Analytics & Dashboard
Responsibility

Provides aggregated dashboard APIs that combine data from multiple backend domains into optimized responses for frontend dashboards. This service does not own business data; it aggregates, summarizes, and formats data for visualization.

Directory Structure
backend/app/

schemas/
├── dashboard.py

api/v1/endpoints/
├── dashboard.py

services/
├── dashboard_service.py
├── analytics_service.py
├── trend_service.py
Data Sources
Fleet Management

Telemetry & Time-Series

Battery Intelligence

AI Prediction

Alert Service

Maintenance

Supply Chain

Sustainability
API Definitions
GET /api/v1/dashboard/overview
Purpose

Returns the complete dashboard overview with all major KPIs.

Query Parameters
fleet_id (optional)

vehicle_id (optional)
Response
{
  "success": true,
  "message": "Dashboard Overview",
  "data": {
    "fleet": {
      "total_vehicles": 128,
      "active_vehicles": 119,
      "offline_vehicles": 9
    },
    "battery": {
      "average_soc": 81,
      "average_soh": 94,
      "critical_batteries": 3
    },
    "alerts": {
      "active": 12,
      "critical": 2
    },
    "maintenance": {
      "scheduled": 8,
      "pending": 4
    },
    "sustainability": {
      "carbon_saved": 48215,
      "average_readiness": 84
    },
    "supply_chain": {
      "critical_suppliers": 5,
      "high_risk_suppliers": 2
    }
  }
}
GET /api/v1/dashboard/fleet-trends
Purpose

Returns historical fleet statistics.

Query Parameters
period

start_date

end_date
Response
{
  "success": true,
  "message": "Fleet Trends",
  "data": [
    {
      "date": "2026-07-01",
      "active": 112,
      "offline": 5
    }
  ]
}
GET /api/v1/dashboard/battery-trends
Purpose

Returns historical battery KPIs.

Query Parameters
vehicle_id

period
Response
{
  "success": true,
  "message": "Battery Trends",
  "data": [
    {
      "timestamp": "2026-07-14T18:00:00Z",
      "soc": 82,
      "soh": 94,
      "temperature": 35.8
    }
  ]
}
GET /api/v1/dashboard/charging-analytics
Purpose

Returns charging behavior analytics.

Query Parameters
vehicle_id

start_date

end_date
Response
{
  "success": true,
  "message": "Charging Analytics",
  "data": {
    "total_sessions": 248,
    "average_duration": 68,
    "average_energy": 42,
    "charging_efficiency": 93
  }
}
GET /api/v1/dashboard/alert-analytics
Purpose

Returns aggregated alert analytics.

Query Parameters
period
Response
{
  "success": true,
  "message": "Alert Analytics",
  "data": {
    "total_alerts": 248,
    "critical": 12,
    "high": 26,
    "resolved": 198
  }
}
GET /api/v1/dashboard/maintenance-analytics
Purpose

Returns maintenance KPIs.

Response
{
  "success": true,
  "message": "Maintenance Analytics",
  "data": {
    "scheduled": 18,
    "completed": 132,
    "pending": 11,
    "average_completion_time": 4.6
  }
}
GET /api/v1/dashboard/sustainability-analytics
Purpose

Returns sustainability KPIs.

Response
{
  "success": true,
  "message": "Sustainability Analytics",
  "data": {
    "carbon_saved": 48215,
    "scope1": 0,
    "scope3": 1584,
    "average_readiness": 84
  }
}
GET /api/v1/dashboard/supply-chain-analytics
Purpose

Returns supply chain KPIs.

Response
{
  "success": true,
  "message": "Supply Chain Analytics",
  "data": {
    "suppliers": 128,
    "critical_suppliers": 5,
    "high_risk": 2,
    "materials": 18
  }
}
GET /api/v1/dashboard/live
Purpose

Returns frequently refreshed live dashboard metrics.

Response
{
  "success": true,
  "message": "Live Dashboard",
  "data": {
    "online_vehicles": 118,
    "active_alerts": 9,
    "average_soc": 81,
    "active_charging": 14
  }
}
Pydantic Schemas
DashboardOverviewResponse
fleet: dict
battery: dict
alerts: dict
maintenance: dict
sustainability: dict
supply_chain: dict
FleetTrendResponse
date: date
active: int
offline: int
BatteryTrendResponse
timestamp: datetime
soc: float
soh: float
temperature: float
ChargingAnalyticsResponse
total_sessions: int
average_duration: float
average_energy: float
charging_efficiency: float
AlertAnalyticsResponse
total_alerts: int
critical: int
high: int
resolved: int
SustainabilityAnalyticsResponse
carbon_saved: float
scope1: float
scope3: float
average_readiness: float
SupplyChainAnalyticsResponse
suppliers: int
critical_suppliers: int
high_risk: int
materials: int
Frontend Team Dependencies

The frontend can integrate the following endpoints:

GET /api/v1/dashboard/overview

GET /api/v1/dashboard/live

GET /api/v1/dashboard/fleet-trends

GET /api/v1/dashboard/battery-trends

GET /api/v1/dashboard/charging-analytics

GET /api/v1/dashboard/alert-analytics

GET /api/v1/dashboard/maintenance-analytics

GET /api/v1/dashboard/sustainability-analytics

GET /api/v1/dashboard/supply-chain-analytics

Primary UI screens:

Executive Dashboard
Fleet Dashboard
Battery Dashboard
Charging Dashboard
Alert Dashboard
Maintenance Dashboard
Sustainability Dashboard
Supply Chain Dashboard
Infrastructure Team Dependencies

No dedicated infrastructure is required.

Recommended optimization:

Redis Cache (optional)

Dashboard Response Cache

Materialized Views (optional)

TimescaleDB Continuous Aggregates (optional)
ML Team Dependencies

The Analytics service consumes outputs from the ML Prediction Service but performs no inference itself.

Consumed data includes:

Remaining Useful Life

State of Health Prediction

Anomaly Detection

Failure Probability

Thermal Risk

Voltage Risk

These values are aggregated into dashboard KPIs and trend visualizations.

Backend Domain Dependencies

This service aggregates data from the following domains:

Fleet Management

Telemetry & Time-Series

Battery Intelligence

AI Prediction Service

Alert & Notification Service

Predictive Maintenance

Supply Chain Intelligence

Sustainability & Carbon Intelligence
Deliverables
APIs
GET /api/v1/dashboard/overview

GET /api/v1/dashboard/live

GET /api/v1/dashboard/fleet-trends

GET /api/v1/dashboard/battery-trends

GET /api/v1/dashboard/charging-analytics

GET /api/v1/dashboard/alert-analytics

GET /api/v1/dashboard/maintenance-analytics

GET /api/v1/dashboard/sustainability-analytics

GET /api/v1/dashboard/supply-chain-analytics
Schemas
DashboardOverviewResponse

FleetTrendResponse

BatteryTrendResponse

ChargingAnalyticsResponse

AlertAnalyticsResponse

SustainabilityAnalyticsResponse

SupplyChainAnalyticsResponse
```

---

## common_schemas\backend_summary

```
Overall Backend Service Summary
Domain	Responsibility	Primary Role
1. Core Platform	Platform foundation	Common infrastructure, configuration, health checks, authentication, logging, dependency injection, standardized responses
2. Fleet Management	Fleet inventory	Vehicle registration, fleet metadata, assignments, vehicle lifecycle management
3. Telemetry & Time-Series	IoT telemetry	Stores and retrieves all incoming telemetry, charging sessions, GPS, historical time-series data using TimescaleDB
4. Battery Intelligence	Battery monitoring	Real-time battery metrics (SoC, SoH, voltage, current, temperature, cycle count) without AI predictions
5. AI Prediction Service	ML inference	Remaining Useful Life (RUL), SoH prediction, anomaly detection, thermal risk, voltage risk, failure probability
6. Alert & Notification Service	Event management	Centralized alert generation, acknowledgement, history, notification routing from all platform services
7. Predictive Maintenance	Maintenance intelligence	Maintenance recommendations, work orders, service history, maintenance scheduling
8. Supply Chain Intelligence	Graph analytics	Neo4j-based supplier graph, dependency analysis, risk propagation, material traceability
9. Sustainability & Carbon Intelligence	ESG analytics	Carbon calculations, diesel vs EV comparison, electrification readiness, procurement recommendations
10. Real-Time Streaming	Event pipeline	MQTT ingestion, Kafka messaging, WebSocket broadcasting, event routing between services
11. Analytics & Dashboard	Dashboard aggregation	Aggregates KPIs from all services into optimized dashboard APIs for the frontend
High-Level System Architecture
                       INDUSTRIAL EV AI PLATFORM

                       ┌──────────────────────────────┐
                       │      React Dashboard         │
                       │                              │
                       │ Fleet Dashboard              │
                       │ Battery Dashboard            │
                       │ AI Dashboard                 │
                       │ Alerts Dashboard             │
                       │ Supply Chain Dashboard       │
                       │ Sustainability Dashboard     │
                       └──────────────┬───────────────┘
                                      │
                     REST APIs + WebSockets
                                      │
──────────────────────────────────────┼──────────────────────────────────────

                    FastAPI Backend (API Gateway Layer)

                                      │
      ┌───────────────────────────────┼───────────────────────────────┐
      │                               │                               │
 Core Platform                 Dashboard APIs                 WebSocket APIs
 Authentication                Aggregated KPIs                Live Updates
 Health                        Analytics                      Event Streaming
 Logging                       Reports                        Notifications

──────────────────────────────────────────────────────────────────────────────

                     BUSINESS SERVICE LAYER

┌───────────────┐
│Fleet Service  │
└──────┬────────┘
       │
       ▼

┌────────────────────┐
│Telemetry Service   │◄──────────── MQTT Consumer
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│Battery Service     │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│AI Prediction       │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│Alert Service       │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│Maintenance Service │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│Supply Chain Service│
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│Sustainability      │
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│Analytics Service   │
└────────────────────┘

Detailed End-to-End Architecture Flow
                                  IoT Devices
                         (Vehicle / Simulator / Sensors)
                                        │
                         MQTT (ev/telemetry, battery, GPS)
                                        │
                                        ▼
                             ┌───────────────────┐
                             │ Mosquitto Broker  │
                             └─────────┬─────────┘
                                       │
                                       ▼
                             MQTT Consumer Service
                                       │
                                       ▼
                            Kafka Producer publishes
                                       │
                                       ▼
══════════════════════════════════════════════════════════════
                    Kafka Event Bus
══════════════════════════════════════════════════════════════

Topics

telemetry.raw
telemetry.processed
predictions
alerts
maintenance
supplychain

══════════════════════════════════════════════════════════════

               Kafka Consumers subscribe to events

               telemetry.raw
                      │
                      ▼
              Telemetry Processing
                      │
                      ▼
             telemetry.processed topic
                      │
      ┌───────────────┼────────────────────┐
      │               │                    │
      ▼               ▼                    ▼

Telemetry DB     Battery Service      AI Prediction
(TimescaleDB)    (Monitoring)         (ML Inference)

      │               │                    │
      │               │                    ▼
      │               │            predictions topic
      │               │                    │
      │               │                    ▼
      │               │              Alert Service
      │               │                    │
      │               │                    ▼
      │               │            alerts topic
      │               │                    │
      │               │                    ▼
      │               │          Maintenance Service
      │               │                    │
      │               │                    ▼
      │               │         maintenance topic
      │               │
      │               ▼
      │      Battery Health APIs
      │
      ▼

Historical Queries
Time-Series Analytics
Charging Analytics

──────────────────────────────────────────────────────────────

Fleet Service
      │
      ▼

Vehicle Metadata

Fleet Assignment

Vehicle Status

──────────────────────────────────────────────────────────────

Supply Chain Service
      │
      
Neo4j Database

Supplier Graph

Material Flow

Risk Propagation

Critical Dependency Analysis

──────────────────────────────────────────────────────────────

Sustainability Service
      │
      ▼

Carbon Calculation

Scope 1 / Scope 3

Diesel vs EV

Readiness Score

Procurement Recommendation

──────────────────────────────────────────────────────────────

Analytics Service

Collects information from

Fleet
Telemetry
Battery
AI
Alerts
Maintenance
Supply Chain
Sustainability

↓

Produces

/dashboard/overview

/dashboard/fleet-trends

/dashboard/battery-trends

/dashboard/charging-analytics

/dashboard/alert-analytics

/dashboard/supply-chain-analytics

/dashboard/sustainability-analytics

──────────────────────────────────────────────────────────────

                 FastAPI REST API Layer

/api/v1/fleet

/api/v1/telemetry

/api/v1/battery

/api/v1/predict

/api/v1/alerts

/api/v1/maintenance

/api/v1/supply-chain

/api/v1/sustainability

/api/v1/dashboard

──────────────────────────────────────────────────────────────

              WebSocket Manager

/ws/telemetry

/ws/battery

/ws/predictions

/ws/alerts

/ws/maintenance

/ws/supply-chain

──────────────────────────────────────────────────────────────

                 React Dashboard

Executive Dashboard

Fleet Dashboard

Battery Dashboard

Telemetry Dashboard

Charging Dashboard

Maintenance Dashboard

Supply Chain Dashboard

Carbon Dashboard

AI Prediction Dashboard

Live Notifications

──────────────────────────────────────────────

Supporting Infrastructure

PostgreSQL
│
├── Fleet
├── Alerts
├── Maintenance
├── Carbon Reports
└── User Data

TimescaleDB
│
├── Telemetry
├── Charging Sessions
└── GPS History

Neo4j
│
├── Suppliers
├── Plants
├── Materials
└── Dependencies

Kafka
│
├── Event Streaming
├── Event Routing
└── Service Communication

MQTT
│
└── IoT Device Communication

ML Service
│
├── RUL Prediction
├── SoH Prediction
├── Thermal Risk
├── Voltage Risk
└── Anomaly Detection
Overall Data Flow
IoT Devices
      │
      ▼
MQTT
      │
      ▼
Kafka
      │
      ▼
Telemetry Processing
      │
      ├────────► TimescaleDB
      │
      ├────────► Battery Monitoring
      │
      ├────────► AI Prediction
      │
      ├────────► Alert Generation
      │
      ├────────► Maintenance Recommendation
      │
      ├────────► Dashboard Aggregation
      │
      └────────► WebSocket Broadcast

Fleet Data ─────────────┐
Supply Chain ───────────┤
Carbon Intelligence ────┤
Maintenance ────────────┤
Alerts ─────────────────┤
AI Predictions ─────────┤
Telemetry ──────────────┘
            │
            ▼
 Analytics & Dashboard Service
            │
            ▼
     React Frontend
Overall Layered Architecture

The complete platform can be viewed as seven logical layers, each with a single responsibility:

Device Layer – EVs, sensors, simulators publishing telemetry over MQTT.
Streaming Layer – MQTT, Kafka, and WebSockets providing real-time event transport.
Core Platform Layer – Common infrastructure (health, configuration, authentication, logging, dependency injection).
Business Services Layer – Fleet, Telemetry, Battery, AI, Alerts, Maintenance, Supply Chain, Sustainability.
Data Layer – PostgreSQL (relational), TimescaleDB (time-series), Neo4j (graph).
Analytics Layer – Dashboard aggregation and KPI computation across all domains.
Presentation Layer – React dashboard consuming REST APIs for historical/aggregated data and WebSockets for live updates.
```

---

## common_schemas\battery_Intelligence

```
Domain 4 — Battery Intelligence
Responsibility

Provides monitoring and management APIs for battery health and battery status. This module exposes current battery metrics and historical battery information without performing any predictive analysis or AI inference.

Directory Structure
backend/app/

models/
├── battery_health.py
├── battery_status.py

schemas/
├── battery.py

api/v1/endpoints/
├── battery.py

services/
├── battery_service.py
Main Entities
BatteryHealth

Stores long-term battery health indicators.

Attributes
battery_health_id
vehicle_id
timestamp
state_of_health
capacity_kwh
capacity_percentage
internal_resistance
cycle_count
remaining_capacity
battery_age_days
BatteryStatus

Stores real-time battery operating parameters.

Attributes
battery_status_id
vehicle_id
timestamp
state_of_charge
voltage
current
power
temperature_avg
temperature_max
temperature_min
cell_voltage_min
cell_voltage_max
charging_status
battery_status
Database Relationships
Vehicle

1
│
├──────────────┐
│              │
▼              ▼
BatteryHealth  BatteryStatus
API Definitions
GET /api/v1/battery/status
Purpose

Returns the latest battery operating status for a vehicle.

Query Parameters
vehicle_id
Response
{
  "success": true,
  "message": "Battery Status",
  "data": {
    "vehicle_id": "EV-001",
    "timestamp": "2026-07-14T18:30:00Z",
    "state_of_charge": 82,
    "voltage": 387.5,
    "current": 42.3,
    "power": 16.4,
    "temperature_avg": 34.6,
    "temperature_max": 36.1,
    "temperature_min": 33.8,
    "cell_voltage_min": 3.88,
    "cell_voltage_max": 3.96,
    "charging_status": "DISCHARGING",
    "battery_status": "NORMAL"
  }
}
GET /api/v1/battery/health
Purpose

Returns the latest battery health metrics.

Query Parameters
vehicle_id
Response
{
  "success": true,
  "message": "Battery Health",
  "data": {
    "vehicle_id": "EV-001",
    "state_of_health": 94.8,
    "capacity_kwh": 34.2,
    "capacity_percentage": 97.7,
    "internal_resistance": 0.012,
    "cycle_count": 412,
    "remaining_capacity": 33.5,
    "battery_age_days": 521
  }
}
GET /api/v1/battery/summary
Purpose

Returns battery summary information for dashboard cards.

Query Parameters
vehicle_id
Response
{
  "success": true,
  "message": "Battery Summary",
  "data": {
    "state_of_charge": 82,
    "state_of_health": 94.8,
    "battery_status": "NORMAL",
    "charging_status": "DISCHARGING"
  }
}
GET /api/v1/battery/history
Purpose

Returns historical battery metrics.

Query Parameters
vehicle_id
metric
start_time
end_time
interval

Supported Metrics

state_of_charge
state_of_health
voltage
current
temperature
capacity
internal_resistance
cycle_count
Response
{
  "success": true,
  "message": "Battery History",
  "data": [
    {
      "timestamp": "2026-07-14T18:00:00Z",
      "value": 84
    },
    {
      "timestamp": "2026-07-14T18:05:00Z",
      "value": 83
    }
  ]
}
GET /api/v1/battery/cells
Purpose

Returns battery cell-level voltage and temperature information.

Query Parameters
vehicle_id
Response
{
  "success": true,
  "message": "Battery Cell Status",
  "data": {
    "cells": [
      {
        "cell_id": 1,
        "voltage": 3.91,
        "temperature": 33.4
      },
      {
        "cell_id": 2,
        "voltage": 3.92,
        "temperature": 33.8
      }
    ]
  }
}


GET /api/v1/battery/metrics
Purpose

Returns all available battery monitoring metrics.

Query Parameters
vehicle_id
Response
{
  "success": true,
  "message": "Battery Metrics",
  "data": {
    "state_of_charge": 82,
    "state_of_health": 94.8,
    "capacity_kwh": 34.2,
    "voltage": 387.5,
    "current": 42.3,
    "power": 16.4,
    "temperature_avg": 34.6,
    "temperature_max": 36.1,
    "temperature_min": 33.8,
    "internal_resistance": 0.012,
    "cycle_count": 412
  }
}
Pydantic Schemas
BatteryStatusResponse
vehicle_id: str
timestamp: datetime
state_of_charge: float
voltage: float
current: float
power: float
temperature_avg: float
temperature_max: float
temperature_min: float
cell_voltage_min: float
cell_voltage_max: float
charging_status: str
battery_status: str
BatteryHealthResponse
vehicle_id: str
timestamp: datetime
state_of_health: float
capacity_kwh: float
capacity_percentage: float
internal_resistance: float
cycle_count: int
remaining_capacity: float
battery_age_days: int
BatteryHistoryResponse
timestamp: datetime
value: float
BatteryCellResponse
cell_id: int
voltage: float
temperature: float
Enumerations
BatteryStatus
NORMAL
WARNING
CRITICAL
OFFLINE
ChargingStatus
CHARGING
DISCHARGING
IDLE
FULLY_CHARGED
BatteryMetric
state_of_charge
state_of_health
voltage
current
power
temperature
capacity
internal_resistance
cycle_count
Frontend Team Dependencies

The frontend can immediately integrate the following endpoints:

GET /api/v1/battery/status
GET /api/v1/battery/health
GET /api/v1/battery/summary
GET /api/v1/battery/history
GET /api/v1/battery/cells
GET /api/v1/battery/metrics

Primary UI screens:

Battery Overview
Battery Health Card
Battery Status Gauge
Cell Monitoring
Historical Battery Charts
Infrastructure Team Dependencies

Required database tables:

battery_health
battery_status

These tables may be populated directly from processed telemetry data or derived periodically from TimescaleDB, depending on the implementation strategy.

ML Team Dependencies

This domain provides the monitored battery features required as inputs to prediction models. No prediction APIs are exposed here.

Required fields:

vehicle_id
timestamp
state_of_charge
state_of_health
capacity_kwh
capacity_percentage
voltage
current
power
temperature_avg
temperature_max
temperature_min
internal_resistance
cycle_count
cell_voltage_min
cell_voltage_max
charging_status

These values are consumed by the ML team for:

Remaining Useful Life (RUL) prediction
State of Health (SoH) estimation
Battery degradation analysis
Anomaly detection
Deliverables
APIs
GET /api/v1/battery/status
GET /api/v1/battery/health
GET /api/v1/battery/summary
GET /api/v1/battery/history
GET /api/v1/battery/cells
GET /api/v1/battery/metrics


Schemas
BatteryStatusResponse
BatteryHealthResponse
BatteryHistoryResponse
BatteryCellResponse
Database Tables
battery_health
battery_status
Enums
BatteryStatus
ChargingStatus
BatteryMetric
```

---

## common_schemas\core_platform.txt

```text
backend/app/

core/
├── config.py
├── database.py
├── dependencies.py
├── exceptions.py
├── logging.py
├── response.py
├── security.py

schemas/
├── common.py
├── health.py
├── config.py

api/v1/endpoints/
├── health.py
├── system.py
├── version.py

services/
├── health_service.py
├── system_service.py


API versioning standard
/api/v1/


Standard Response Contract:

Success Response:
{
  "success": true,
  "message": "Operation completed successfully",
  "data": {},
  "metadata": {
    "timestamp": "2026-07-14T18:30:00Z"
  }
}

Error Response:
{
  "success": false,
  "message": "Validation Error",
  "error": {
    "code": "VALIDATION_ERROR",
    "details": []
  },
  "metadata": {
    "timestamp": "2026-07-14T18:30:00Z"
  }
}

Common Schemas:

class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any]
    metadata: dict

class ErrorResponse(BaseModel):
    success: bool
    message: str
    error: dict
    metadata: dict

class Metadata(BaseModel):
    timestamp: datetime

==============================================================================================
API Definitions:

Health APIs:


GET /api/v1/health  #Basic application health check.

Request
No payload.

Response
{
  "success": true,
  "message": "Service Healthy",
  "data": {
    "status": "UP"
  }
}

GET /api/v1/health/db
Purpose: Verify PostgreSQL/TimescaleDB connectivity.

Request
No payload.

Response
{
  "success": true,
  "message": "Database Healthy",
  "data": {
    "status": "UP",
    "database": "postgresql"
  }
}


GET /api/v1/health/kafka
Purpose : Verify Kafka broker availability.

Request
No payload.

Response
{
  "success": true,
  "message": "Kafka Healthy",
  "data": {
    "status": "UP",
    "broker": "kafka:9092"
  }
}


GET /api/v1/health/mqtt
Purpose: Verify MQTT broker connectivity.

Request
No payload.

Response
{
  "success": true,
  "message": "MQTT Healthy",
  "data": {
    "status": "UP",
    "broker": "mosquitto:1883"
  }
}


GET /api/v1/health/neo4j
Purpose : Verify Neo4j availability.

Request
No payload.

Response
{
  "success": true,
  "message": "Neo4j Healthy",
  "data": {
    "status": "UP",
    "database": "neo4j"
  }
}


GET /api/v1/health/ml
Purpose: Verify ML inference service availability.

Request
No payload.

Response
{
  "success": true,
  "message": "ML Service Healthy",
  "data": {
    "status": "UP",
    "service": "prediction-engine"
  }
}


System Status APIs
GET /api/v1/system/status
Purpose : Aggregated status of all connected services.

Request
No payload.

Response
{
  "success": true,
  "message": "System Status",
  "data": {
    "backend": "UP",
    "database": "UP",
    "kafka": "UP",
    "mqtt": "UP",
    "neo4j": "UP",
    "ml_service": "UP"
  }
}


GET /api/v1/system/info
Purpose : Expose platform information.

Request
No payload.

Response
{
  "success": true,
  "message": "System Information",
  "data": {
    "project": "Industrial EV AI Platform",
    "environment": "development",
    "uptime": 86400,
    "timezone": "UTC"
  }
}


Version APIs
GET /api/v1/version
Purpose : Expose API version.

Request
No payload.

Response
{
  "success": true,
  "message": "Version Information",
  "data": {
    "api_version": "v1",
    "build_version": "1.0.0",
    "release_date": "2026-07-14"
  }
}


Configuration APIs
GET /api/v1/config/public
Purpose: Expose non-sensitive frontend configuration.

Request
No payload.

Response
{
  "success": true,
  "message": "Public Configuration",
  "data": {
    "websocket_enabled": true,
    "telemetry_refresh_interval": 1,
    "dashboard_refresh_interval": 30
  }
}


Authentication Placeholder APIs
POST /api/v1/auth/login
Purpose : Placeholder endpoint for future authentication.
Request
{
  "username": "admin",
  "password": "password"
}
Response
{
  "success": true,
  "message": "Login Successful",
  "data": {
    "access_token": "jwt-token",
    "token_type": "bearer"
  }
}



GET /api/v1/auth/me
Purpose : Returns current user information.

Request
Authorization Header
Bearer <token>

Response
{
  "success": true,
  "message": "Current User",
  "data": {
    "id": 1,
    "username": "admin",
    "role": "administrator"
  }
}


GET /health/all
{
    "overall_status":"HEALTHY",
    "services":[
        ...
    ]
}


GET  /api/v1/health
GET  /api/v1/health/db
GET  /api/v1/health/kafka
GET  /api/v1/health/mqtt
GET  /api/v1/health/neo4j
GET  /api/v1/health/ml

GET  /api/v1/system/status
GET  /api/v1/system/info

GET  /api/v1/version

GET  /api/v1/config/public

POST /api/v1/auth/login
GET  /api/v1/auth/me

==============================================================================================
Error Codes::

ServiceStatus
  UP
  DOWN
  DEGRADED
  UNKNOWN

Generic:
  INTERNAL_SERVER_ERROR
  BAD_REQUEST
  NOT_FOUND
  UNAUTHORIZED
  FORBIDDEN
  VALIDATION_ERROR
  SERVICE_UNAVAILABLE

Infrastructure:
  DATABASE_UNAVAILABLE
  KAFKA_UNAVAILABLE
  MQTT_UNAVAILABLE
  NEO4J_UNAVAILABLE
  ML_SERVICE_UNAVAILABLE


====================================================================================

HTTP Status Mapping
HTTP Code	Usage
200	Success
201	Created
400	Validation Failure
401	Unauthorized
403	Forbidden
404	Resource Not Found
409	Conflict
422	Schema Validation
500	Internal Error
503	Dependency Unavailable


=============================================================================================

Environment Configuration Schema
.env Variables

APP_NAME=Industrial EV AI Platform
HOST=
PORT=
SECRET_KEY=
ACCESS_TOKEN_EXPIRE_MINUTES=
LOG_LEVEL=
ALLOWED_ORIGINS=
FRONTEND_URL=
ENVIRONMENT=development
API_VERSION=v1
DEBUG=true
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
KAFKA_BOOTSTRAP_SERVERS=
MQTT_BROKER=
MQTT_PORT=
NEO4J_URI=
NEO4J_USER=
NEO4J_PASSWORD=
ML_SERVICE_URL=



===========================================================================================

Logging Standard
Log Format
{
  "timestamp": "",
  "level": "INFO",
  "service": "backend",
  "module": "telemetry",
  "message": ""
}

Dependency Injection Contracts
Database Dependency
  get_db()
  Provides
  Session

Kafka Dependency
  get_kafka_producer()
    Provides
    KafkaProducer

Neo4j Dependency
  get_neo4j_driver()
    Provides
    Neo4j Driver

MQTT Dependency
  get_mqtt_client()
    Provides
    MQTT Client

```

---

## common_schemas\fleet_management

```
backend/app/

models/
├── vehicle.py
├── fleet.py
├── vehicle_profile.py

schemas/
├── vehicle.py
├── fleet.py
├── assignment.py

api/v1/endpoints/
├── fleet.py
├── vehicles.py

services/
├── fleet_service.py
├── vehicle_service.py



==========================================================================

Main Entities

Vehicle: Stores core information for each EV.
Attributes:
vehicle_id
fleet_id
vehicle_number
vehicle_name
manufacturer
model
battery_capacity_kwh
vehicle_type
manufacturing_year
status
assignment_status
created_at
updated_at


Fleet: Logical grouping of vehicles.
Attributes:
fleet_id
fleet_name
organization
description
location
total_vehicles
created_at
updated_at


VehicleProfile: Extended metadata for a vehicle.
Attributes:
vehicle_id
vin
firmware_version
battery_serial_number
odometer
last_service_date
purchase_date
warranty_expiry


DB relationship : 
Fleet: 1 to many
vechicle: 1 to 1


==========================================================================

API Definitions
GET /api/v1/fleet
Purpose: Returns all registered fleets.
Request: No payload.
Response
{
  "success": true,
  "message": "Fleet List",
  "data": [
    {
      "fleet_id": 1,
      "fleet_name": "South Region Fleet",
      "organization": "ABC Logistics",
      "total_vehicles": 42,
      "location": "Chennai"
    }
  ]
}


POST /api/v1/fleet
Purpose: Creates a new fleet.
Request
{
  "fleet_name": "South Region Fleet",
  "organization": "ABC Logistics",
  "description": "Primary delivery fleet",
  "location": "Chennai"
}
Response
{
  "success": true,
  "message": "Fleet Created",
  "data": {
    "fleet_id": 1
  }
}


GET /api/v1/fleet/{fleet_id}
Purpose: Returns fleet details.
Response
{
  "success": true,
  "message": "Fleet Details",
  "data": {
    "fleet_id": 1,
    "fleet_name": "South Region Fleet",
    "organization": "ABC Logistics",
    "total_vehicles": 42
  }
}


PATCH /api/v1/fleet/{fleet_id}
Purpose: Updates fleet information.
Request
{
  "fleet_name": "Updated Fleet",
  "location": "Bangalore"
}
Response
{
  "success": true,
  "message": "Fleet Updated"
}


DELETE /api/v1/fleet/{fleet_id}
Purpose: Deletes a fleet.
Response
{
  "success": true,
  "message": "Fleet Deleted"
}


Vehicle APIs
GET /api/v1/vehicles
Purpose: Returns all registered vehicles.

Query Parameters:
fleet_id
status
vehicle_type
page
limit

Response
{
  "success": true,
  "message": "Vehicle List",
  "data": [
    {
      "vehicle_id": "EV-001",
      "fleet_id": 1,
      "vehicle_number": "TN01AB1234",
      "manufacturer": "Tata",
      "model": "Ace EV",
      "status": "ACTIVE"
    }
  ]
}


POST /api/v1/vehicles
Purpose: Registers a new vehicle.
Request
{
  "fleet_id": 1,
  "vehicle_number": "TN01AB1234",
  "vehicle_name": "Delivery Van 1",
  "manufacturer": "Tata",
  "model": "Ace EV",
  "battery_capacity_kwh": 35,
  "vehicle_type": "Cargo"
}
Response
{
  "success": true,
  "message": "Vehicle Registered",
  "data": {
    "vehicle_id": "EV-001"
  }
}


GET /api/v1/vehicles/{vehicle_id}
Purpose: Returns complete vehicle information.
Response
{
  "success": true,
  "message": "Vehicle Details",
  "data": {
    "vehicle_id": "EV-001",
    "fleet_id": 1,
    "manufacturer": "Tata",
    "model": "Ace EV",
    "battery_capacity_kwh": 35,
    "status": "ACTIVE"
  }
}


PATCH /api/v1/vehicles/{vehicle_id}
Purpose: Updates vehicle metadata.
Request
{
  "status": "MAINTENANCE"
}
Response
{
  "success": true,
  "message": "Vehicle Updated"
}


DELETE /api/v1/vehicles/{vehicle_id}
Purpose: Removes vehicle from fleet.
Response
{
  "success": true,
  "message": "Vehicle Deleted"
}


Vehicle Profile APIs
GET /api/v1/vehicles/{vehicle_id}/profile
Purpose: Returns complete vehicle profile.
Response
{
  "success": true,
  "message": "Vehicle Profile",
  "data": {
    "vin": "MA3EV123456",
    "firmware_version": "v2.1.0",
    "battery_serial_number": "BAT-00982",
    "purchase_date": "2024-01-01",
    "warranty_expiry": "2032-01-01"
  }
}


PATCH /api/v1/vehicles/{vehicle_id}/profile
Purpose: Updates profile information.

Request
{
  "firmware_version": "v2.2.0"
}
Response
{
  "success": true,
  "message": "Profile Updated"
}


Assignment APIs
POST /api/v1/vehicles/{vehicle_id}/assign
Purpose: Assigns vehicle to a fleet or operational unit.

Request
{
  "fleet_id": 2
}
Response
{
  "success": true,
  "message": "Vehicle Assigned"
}


POST /api/v1/vehicles/{vehicle_id}/unassign
Purpose: Removes vehicle assignment.
Response
{
  "success": true,
  "message": "Vehicle Unassigned"
}


Fleet Summary API
GET /api/v1/fleet/summary
Purpose : Returns fleet-level KPIs for dashboard overview.
Response
{
  "success": true,
  "message": "Fleet Summary",
  "data": {
    "total_fleets": 5,
    "total_vehicles": 120,
    "active": 110,
    "maintenance": 6,
    "inactive": 4
  }
}



GET    /api/v1/fleet
POST   /api/v1/fleet
GET    /api/v1/fleet/{fleet_id}
PATCH  /api/v1/fleet/{fleet_id}
DELETE /api/v1/fleet/{fleet_id}

GET    /api/v1/fleet/summary

GET    /api/v1/vehicles
POST   /api/v1/vehicles
GET    /api/v1/vehicles/{vehicle_id}
PATCH  /api/v1/vehicles/{vehicle_id}
DELETE /api/v1/vehicles/{vehicle_id}

GET    /api/v1/vehicles/{vehicle_id}/profile
PATCH  /api/v1/vehicles/{vehicle_id}/profile

POST   /api/v1/vehicles/{vehicle_id}/assign
POST   /api/v1/vehicles/{vehicle_id}/unassign


==========================================================================

Pydantic Schemas:

VehicleCreate
fleet_id: int
vehicle_number: str
vehicle_name: str
manufacturer: str
model: str
battery_capacity_kwh: float
vehicle_type: str


VehicleUpdate
vehicle_name: Optional[str]
status: Optional[str]
battery_capacity_kwh: Optional[float]


FleetCreate
fleet_name: str
organization: str
description: str
location: str


VehicleProfileResponse:
vehicle_id: str
vin: str
firmware_version: str
battery_serial_number: str
purchase_date: date
warranty_expiry: date

===================================================================================
Enumerations:

VehicleStatus
  ACTIVE
  IDLE
  CHARGING
  MAINTENANCE
  OFFLINE
  RETIRED

VehicleType
  Cargo
  Passenger
  Bus
  Truck
  Forklift
  Other

AssignmentStatus
  ASSIGNED
  UNASSIGNED


==============================================================================================

Frontend Team Dependencies:
The frontend can immediately build the Fleet Management pages using these endpoints:

GET  /api/v1/fleet
GET  /api/v1/fleet/summary
GET  /api/v1/fleet/{fleet_id}

GET  /api/v1/vehicles
GET  /api/v1/vehicles/{vehicle_id}
GET  /api/v1/vehicles/{vehicle_id}/profile

Primary UI screens:

Fleet Overview
Vehicle List
Vehicle Details
Vehicle Profile
Fleet Summary Cards

================================================================================================
Infrastructure Team Dependencies

Required services:
PostgreSQL

Tables:
fleet
vehicle
vehicle_profile

Foreign Keys:
vehicle.fleet_id -> fleet.fleet_id
vehicle_profile.vehicle_id -> vehicle.vehicle_id

================================================================================================
ML Team Dependencies
No direct dependencies.
ML services should only consume the immutable identifier:
vehicle_id
All telemetry, prediction, and maintenance modules should reference the same vehicle_id to maintain consistency across the platform.
```

---

## common_schemas\predictive_maintenance_service

```
Domain 7 — Predictive Maintenance
Responsibility

Provides APIs for maintenance recommendations, work order management, maintenance scheduling, and service history. This module consumes outputs from AI Prediction and Alert services to support preventive and predictive maintenance workflows.

Directory Structure
backend/app/

models/
├── maintenance_record.py
├── recommendation.py
├── work_order.py

schemas/
├── maintenance.py

api/v1/endpoints/
├── maintenance.py

services/
├── maintenance_service.py
├── recommendation_service.py
├── workorder_service.py
Main Entities
MaintenanceRecord

Stores completed maintenance activities.

Attributes
maintenance_id
vehicle_id
work_order_id
maintenance_type
description
performed_by
performed_at
status
cost
odometer
remarks
created_at
updated_at
Recommendation

Stores AI-generated maintenance recommendations.

Attributes
recommendation_id
vehicle_id
source
recommendation_type
priority
title
description
recommended_date
status
created_at
WorkOrder

Represents an approved maintenance task.

Attributes
work_order_id
vehicle_id
recommendation_id
maintenance_type
assigned_to
scheduled_date
completed_date
status
priority
estimated_duration
created_at
updated_at
Database Relationships
Vehicle

1
│
├───────────────┐
│               │
▼               ▼
Recommendation  WorkOrder
                    │
                    ▼
            MaintenanceRecord
API Definitions
GET /api/v1/maintenance/recommendations
Purpose

Returns maintenance recommendations for one or more vehicles.

Query Parameters
vehicle_id
priority
status
page
limit
Response
{
  "success": true,
  "message": "Maintenance Recommendations",
  "data": [
    {
      "recommendation_id": "REC-1001",
      "vehicle_id": "EV-001",
      "recommendation_type": "BATTERY_INSPECTION",
      "priority": "HIGH",
      "title": "Inspect Battery Pack",
      "recommended_date": "2026-07-20",
      "status": "PENDING"
    }
  ]
}
GET /api/v1/maintenance/recommendations/{recommendation_id}
Purpose

Returns detailed recommendation information.

Response
{
  "success": true,
  "message": "Recommendation Details",
  "data": {
    "recommendation_id": "REC-1001",
    "vehicle_id": "EV-001",
    "source": "AI",
    "recommendation_type": "BATTERY_INSPECTION",
    "priority": "HIGH",
    "title": "Inspect Battery Pack",
    "description": "Battery degradation exceeds maintenance threshold.",
    "recommended_date": "2026-07-20",
    "status": "PENDING"
  }
}
PATCH /api/v1/maintenance/recommendations/{recommendation_id}
Purpose

Updates recommendation status (e.g., accepted, rejected).

Request
{
  "status": "ACCEPTED"
}
Response
{
  "success": true,
  "message": "Recommendation Updated"
}
POST /api/v1/maintenance/work-orders
Purpose

Creates a work order from a recommendation.

Request
{
  "vehicle_id": "EV-001",
  "recommendation_id": "REC-1001",
  "maintenance_type": "BATTERY_INSPECTION",
  "assigned_to": "Technician A",
  "scheduled_date": "2026-07-21",
  "priority": "HIGH"
}
Response
{
  "success": true,
  "message": "Work Order Created",
  "data": {
    "work_order_id": "WO-1001"
  }
}
GET /api/v1/maintenance/work-orders
Purpose

Returns work orders with filtering support.

Query Parameters
vehicle_id
status
priority
assigned_to
page
limit
Response
{
  "success": true,
  "message": "Work Orders",
  "data": [
    {
      "work_order_id": "WO-1001",
      "vehicle_id": "EV-001",
      "maintenance_type": "BATTERY_INSPECTION",
      "scheduled_date": "2026-07-21",
      "status": "SCHEDULED"
    }
  ]
}
GET /api/v1/maintenance/work-orders/{work_order_id}
Purpose

Returns detailed work order information.

PATCH /api/v1/maintenance/work-orders/{work_order_id}
Purpose

Updates work order status or scheduling.

Request
{
  "status": "IN_PROGRESS"
}
Response
{
  "success": true,
  "message": "Work Order Updated"
}
GET /api/v1/maintenance/history
Purpose

Returns completed maintenance records.

Query Parameters
vehicle_id
maintenance_type
start_date
end_date
page
limit
Response
{
  "success": true,
  "message": "Maintenance History",
  "data": [
    {
      "maintenance_id": "MNT-1001",
      "vehicle_id": "EV-001",
      "maintenance_type": "BATTERY_INSPECTION",
      "performed_at": "2026-06-15",
      "status": "COMPLETED"
    }
  ]
}
POST /api/v1/maintenance/history
Purpose

Creates a completed maintenance record.

Request
{
  "vehicle_id": "EV-001",
  "work_order_id": "WO-1001",
  "maintenance_type": "BATTERY_INSPECTION",
  "performed_by": "Technician A",
  "performed_at": "2026-07-21T14:30:00Z",
  "cost": 2500,
  "remarks": "Battery connections cleaned and tested."
}
Response
{
  "success": true,
  "message": "Maintenance Record Created",
  "data": {
    "maintenance_id": "MNT-1001"
  }
}
GET /api/v1/maintenance/upcoming
Purpose

Returns upcoming scheduled maintenance activities.

Query Parameters
vehicle_id
days
Response
{
  "success": true,
  "message": "Upcoming Maintenance",
  "data": [
    {
      "work_order_id": "WO-1001",
      "scheduled_date": "2026-07-21",
      "maintenance_type": "BATTERY_INSPECTION"
    }
  ]
}
GET /api/v1/maintenance/summary
Purpose

Returns maintenance statistics for dashboard overview.

Response
{
  "success": true,
  "message": "Maintenance Summary",
  "data": {
    "pending_recommendations": 12,
    "scheduled_work_orders": 8,
    "in_progress": 3,
    "completed_this_month": 25
  }
}
Pydantic Schemas
RecommendationResponse
recommendation_id: str
vehicle_id: str
recommendation_type: str
priority: str
title: str
description: str
recommended_date: date
status: str
WorkOrderCreate
vehicle_id: str
recommendation_id: str
maintenance_type: str
assigned_to: str
scheduled_date: date
priority: str
WorkOrderResponse
work_order_id: str
vehicle_id: str
maintenance_type: str
assigned_to: str
scheduled_date: date
status: str
priority: str
MaintenanceRecordResponse
maintenance_id: str
vehicle_id: str
work_order_id: str
maintenance_type: str
performed_by: str
performed_at: datetime
status: str
cost: float
remarks: str
Enumerations
RecommendationType
BATTERY_INSPECTION
CELL_BALANCING
COOLING_SYSTEM
CHARGING_SYSTEM
GENERAL_SERVICE
SOFTWARE_UPDATE
RecommendationStatus
PENDING
ACCEPTED
REJECTED
EXPIRED
WorkOrderStatus
SCHEDULED
IN_PROGRESS
COMPLETED
CANCELLED
PriorityLevel
LOW
MEDIUM
HIGH
CRITICAL
Frontend Team Dependencies

The frontend can immediately integrate the following endpoints:

GET    /api/v1/maintenance/recommendations
GET    /api/v1/maintenance/recommendations/{recommendation_id}
PATCH  /api/v1/maintenance/recommendations/{recommendation_id}

POST   /api/v1/maintenance/work-orders
GET    /api/v1/maintenance/work-orders
GET    /api/v1/maintenance/work-orders/{work_order_id}
PATCH  /api/v1/maintenance/work-orders/{work_order_id}

GET    /api/v1/maintenance/history
POST   /api/v1/maintenance/history

GET    /api/v1/maintenance/upcoming
GET    /api/v1/maintenance/summary

Primary UI screens:

Maintenance Dashboard
Recommendations List
Work Order Management
Maintenance History
Upcoming Maintenance Calendar
Maintenance Summary Cards
Infrastructure Team Dependencies

Required database tables:

recommendation
work_order
maintenance_record

Optional integrations:

Kafka
MQTT

Incoming event sources:

AI Prediction Service
Alert Service
Telemetry Service
ML Team Dependencies

The ML team produces maintenance recommendations but does not manage scheduling.

Expected recommendation payload:

{
  "vehicle_id": "EV-001",
  "recommendation_type": "BATTERY_INSPECTION",
  "priority": "HIGH",
  "title": "Inspect Battery Pack",
  "description": "Battery degradation exceeds threshold.",
  "recommended_date": "2026-07-20"
}

The backend:

Stores recommendations
Creates work orders
Tracks maintenance lifecycle
Maintains service history

The ML service:

Generates recommendation content only
Deliverables
APIs
GET    /api/v1/maintenance/recommendations
GET    /api/v1/maintenance/recommendations/{recommendation_id}
PATCH  /api/v1/maintenance/recommendations/{recommendation_id}

POST   /api/v1/maintenance/work-orders
GET    /api/v1/maintenance/work-orders
GET    /api/v1/maintenance/work-orders/{work_order_id}
PATCH  /api/v1/maintenance/work-orders/{work_order_id}

GET    /api/v1/maintenance/history
POST   /api/v1/maintenance/history

GET    /api/v1/maintenance/upcoming
GET    /api/v1/maintenance/summary
Schemas
RecommendationResponse
WorkOrderCreate
WorkOrderResponse
MaintenanceRecordResponse
Database Tables
recommendation
work_order
maintenance_record
Enums
RecommendationType
RecommendationStatus
WorkOrderStatus
PriorityLevel
```

---

## common_schemas\real_time_streaming_service

```
Domain 10 — Real-Time Streaming
Responsibility

Provides the event-driven messaging infrastructure for the platform. It ingests telemetry through MQTT, processes and routes events via Kafka, dispatches events to backend services, and streams live updates to frontend clients through WebSockets.

Directory Structure
backend/app/

streaming/
├── mqtt_consumer.py
├── kafka_consumer.py
├── kafka_producer.py
├── event_dispatcher.py
├── websocket_manager.py
├── serializers.py
├── topics.py

schemas/
├── events.py

api/v1/endpoints/
├── websocket.py
├── streaming.py

services/
├── stream_service.py
Components
MQTT Consumer

Receives raw telemetry from IoT devices.

Consumes:

ev/telemetry
ev/battery
ev/location
ev/charging
ev/alerts

Produces:

telemetry.raw
Kafka Producer

Publishes processed platform events.

Produces Topics

telemetry.raw

telemetry.processed

predictions

alerts

maintenance

supplychain
Kafka Consumer

Consumes platform events and dispatches them to domain services.

Consumes

telemetry.raw

telemetry.processed

predictions

alerts

maintenance

supplychain
Event Dispatcher

Routes incoming Kafka events to the appropriate backend service.

Routing

telemetry.processed

↓

Telemetry Service


predictions

↓

AI Prediction


alerts

↓

Alert Service


maintenance

↓

Maintenance Service


supplychain

↓

Supply Chain Service
WebSocket Manager

Maintains active frontend connections and broadcasts live platform events.

Event Topics
telemetry.raw

telemetry.processed

predictions

alerts

maintenance

supplychain
WebSocket APIs
WS /api/v1/ws/telemetry
Purpose

Streams live telemetry updates.

Event Payload
{
  "vehicle_id": "EV-001",
  "timestamp": "2026-07-14T18:30:00Z",
  "soc": 82,
  "voltage": 402,
  "current": 32,
  "temperature": 36.4,
  "speed": 58
}
WS /api/v1/ws/battery
Purpose

Streams live battery status updates.

Event Payload
{
  "vehicle_id": "EV-001",
  "soc": 82,
  "soh": 94,
  "cycle_count": 521,
  "temperature": 35.8
}
WS /api/v1/ws/predictions
Purpose

Streams AI prediction results.

Event Payload
{
  "vehicle_id": "EV-001",
  "prediction_type": "RUL",
  "value": 486,
  "unit": "cycles"
}
WS /api/v1/ws/alerts
Purpose

Streams alert events.

Event Payload
{
  "alert_id": "ALT-1001",
  "vehicle_id": "EV-001",
  "severity": "HIGH",
  "title": "High Battery Temperature"
}
WS /api/v1/ws/maintenance
Purpose

Streams maintenance updates.

Event Payload
{
  "vehicle_id": "EV-001",
  "work_order_id": "WO-1001",
  "status": "SCHEDULED"
}
WS /api/v1/ws/supply-chain
Purpose

Streams live supply chain events.

Event Payload
{
  "supplier_id": "SUP-001",
  "risk_score": 91,
  "risk_level": "HIGH"
}
Internal Testing APIs (Optional)

These endpoints are intended only for development/testing and should be disabled or protected in production.

POST /api/v1/streaming/publish
Purpose

Publishes a test event to a Kafka topic.

Request
{
  "topic": "alerts",
  "payload": {
    "vehicle_id": "EV-001",
    "severity": "HIGH"
  }
}
Response
{
  "success": true,
  "message": "Event Published"
}
GET /api/v1/streaming/topics
Purpose

Returns configured Kafka topics.

Response
{
  "success": true,
  "message": "Topics",
  "data": [
    "telemetry.raw",
    "telemetry.processed",
    "predictions",
    "alerts",
    "maintenance",
    "supplychain"
  ]
}
GET /api/v1/streaming/status
Purpose

Returns streaming infrastructure status.

Response
{
  "success": true,
  "message": "Streaming Status",
  "data": {
    "mqtt": "CONNECTED",
    "kafka": "CONNECTED",
    "websocket_clients": 12
  }
}
Event Schemas
TelemetryEvent
vehicle_id: str
timestamp: datetime
soc: float
voltage: float
current: float
temperature: float
speed: float
PredictionEvent
vehicle_id: str
prediction_type: str
value: float
unit: str
AlertEvent
alert_id: str
vehicle_id: str
severity: str
title: str
description: str
MaintenanceEvent
vehicle_id: str
work_order_id: str
status: str
SupplyChainEvent
supplier_id: str
risk_score: float
risk_level: str
Enumerations
KafkaTopics
telemetry.raw

telemetry.processed

predictions

alerts

maintenance

supplychain
MQTTTopics
ev/telemetry

ev/battery

ev/location

ev/charging

ev/alerts
EventType
TELEMETRY

BATTERY

PREDICTION

ALERT

MAINTENANCE

SUPPLY_CHAIN
Frontend Team Dependencies

The frontend can integrate the following WebSocket endpoints:

WS /api/v1/ws/telemetry
WS /api/v1/ws/battery
WS /api/v1/ws/predictions
WS /api/v1/ws/alerts
WS /api/v1/ws/maintenance
WS /api/v1/ws/supply-chain

Optional development endpoints:

GET  /api/v1/streaming/status
GET  /api/v1/streaming/topics
POST /api/v1/streaming/publish

Primary UI integrations:

Live Fleet Dashboard
Live Battery Widgets
AI Prediction Panels
Alert Notifications
Maintenance Timeline
Supply Chain Risk Dashboard
Infrastructure Team Dependencies

Required services:

Mosquitto MQTT Broker

Kafka Broker

Kafka Consumer Group

Kafka Producer

WebSocket Server

Required Kafka topics:

telemetry.raw

telemetry.processed

predictions

alerts

maintenance

supplychain

Required MQTT topics:

ev/telemetry

ev/battery

ev/location

ev/charging

ev/alerts

Environment variables:

MQTT_BROKER
MQTT_PORT

KAFKA_BOOTSTRAP_SERVERS

KAFKA_GROUP_ID

WEBSOCKET_MAX_CONNECTIONS
ML Team Dependencies

The ML team consumes processed telemetry and publishes prediction events.

Consumes:

telemetry.processed

Publishes:

predictions

Expected prediction event:

{
  "vehicle_id": "EV-001",
  "prediction_type": "THERMAL_RISK",
  "score": 0.92,
  "severity": "HIGH",
  "timestamp": "2026-07-14T18:30:00Z"
}

The backend routes prediction events to:

AI Prediction Service
Alert Service
WebSocket broadcasts
Persistence (if required)
Deliverables
WebSocket APIs
WS /api/v1/ws/telemetry
WS /api/v1/ws/battery
WS /api/v1/ws/predictions
WS /api/v1/ws/alerts
WS /api/v1/ws/maintenance
WS /api/v1/ws/supply-chain
Internal REST APIs
POST /api/v1/streaming/publish
GET  /api/v1/streaming/topics
GET  /api/v1/streaming/status
Event Schemas
TelemetryEvent
PredictionEvent
AlertEvent
MaintenanceEvent
SupplyChainEvent
Kafka Topics
telemetry.raw
telemetry.processed
predictions
alerts
maintenance
supplychain
MQTT Topics
ev/telemetry
ev/battery
ev/location
ev/charging
ev/alerts
Enums
KafkaTopics
MQTTTopics
EventType
```

---

## common_schemas\supply_chain_intelligence

```
Domain 8 — Supply Chain Intelligence
Responsibility

Provides graph-based supply chain intelligence using Neo4j. This module manages suppliers, battery manufacturing networks, material traceability, dependency analysis, critical supplier identification, and supply chain risk propagation.

Directory Structure
backend/app/

models/
├── supplier.py
├── material.py
├── battery_plant.py

schemas/
├── supply_chain.py

api/v1/endpoints/
├── suppliers.py
├── supply_chain.py

services/
├── supplier_service.py
├── graph_service.py
├── risk_service.py

clients/
├── neo4j_client.py
Graph Entities
Supplier

Attributes

supplier_id
supplier_name
country
supplier_type
risk_score
status
Material

Attributes

material_id
material_name
category
source_country
criticality
Mine

Attributes

mine_id
mine_name
country
operator
BatteryPlant

Attributes

plant_id
plant_name
location
manufacturer
capacity
BatteryCell

Attributes

cell_id
cell_name
manufacturer
chemistry
Vehicle

Reference node from Fleet Management

vehicle_id
vehicle_name
Graph Relationships
Mine

│

SUPPLIES

↓

Material

│

USED_BY

↓

Supplier

│

DELIVERS_TO

↓

BatteryPlant

│

PRODUCES

↓

BatteryCell

│

INSTALLED_IN

↓

Vehicle
API Definitions
GET /api/v1/suppliers
Purpose

Returns all registered suppliers.

Query Parameters
country
supplier_type
risk_level
page
limit
Response
{
  "success": true,
  "message": "Supplier List",
  "data": [
    {
      "supplier_id": "SUP-001",
      "supplier_name": "ABC Lithium Ltd",
      "country": "Australia",
      "supplier_type": "Lithium",
      "risk_score": 28
    }
  ]
}
GET /api/v1/suppliers/{supplier_id}
Purpose

Returns supplier details.

Response
{
  "success": true,
  "message": "Supplier Details",
  "data": {
    "supplier_id": "SUP-001",
    "supplier_name": "ABC Lithium Ltd",
    "country": "Australia",
    "supplier_type": "Lithium",
    "risk_score": 28,
    "status": "ACTIVE"
  }
}
GET /api/v1/supply-chain/dependencies
Purpose

Returns upstream and downstream dependency graph for a supplier or material.

Query Parameters
supplier_id

material_id

depth
Response
{
  "success": true,
  "message": "Dependency Graph",
  "data": {
    "nodes": [
      {
        "id": "SUP-001",
        "type": "Supplier",
        "label": "ABC Lithium"
      },
      {
        "id": "PLANT-01",
        "type": "BatteryPlant",
        "label": "Chennai Plant"
      }
    ],
    "edges": [
      {
        "source": "SUP-001",
        "target": "PLANT-01",
        "relationship": "DELIVERS_TO"
      }
    ]
  }
}
GET /api/v1/supply-chain/material-flow
Purpose

Returns material movement across the supply chain.

Query Parameters
material_id
Response
{
  "success": true,
  "message": "Material Flow",
  "data": {
    "material": "Lithium",
    "path": [
      "Mine",
      "Supplier",
      "Battery Plant",
      "Battery Cell",
      "Vehicle"
    ]
  }
}
GET /api/v1/supply-chain/material-traceability
Purpose

Returns complete traceability path for a material.

Query Parameters
material_id
vehicle_id
Response
{
  "success": true,
  "message": "Material Traceability",
  "data": {
    "material": "Lithium",
    "origin": "Green Mine",
    "supplier": "ABC Lithium",
    "battery_plant": "Chennai Plant",
    "vehicle": "EV-001"
  }
}
GET /api/v1/supply-chain/risk
Purpose

Returns calculated supply chain risk for suppliers.

Query Parameters
supplier_id
Response
{
  "success": true,
  "message": "Risk Analysis",
  "data": {
    "supplier_id": "SUP-001",
    "risk_score": 81,
    "risk_level": "HIGH",
    "risk_factors": [
      "Political Instability",
      "Shipping Delay"
    ]
  }
}
GET /api/v1/supply-chain/risk-propagation
Purpose

Returns impacted downstream entities when a supplier becomes unavailable.

Query Parameters
supplier_id
Response
{
  "success": true,
  "message": "Risk Propagation",
  "data": {
    "affected_plants": 2,
    "affected_vehicles": 184,
    "affected_materials": 4
  }
}
GET /api/v1/supply-chain/critical-suppliers
Purpose

Returns suppliers ranked by dependency and risk.

Response
{
  "success": true,
  "message": "Critical Suppliers",
  "data": [
    {
      "supplier_id": "SUP-001",
      "supplier_name": "ABC Lithium",
      "risk_score": 91,
      "dependency_score": 94
    }
  ]
}
GET /api/v1/supply-chain/graph
Purpose

Returns complete graph visualization data.

Query Parameters
depth

entity_id

entity_type
Response
{
    "success":true,
    "message":"Supply Chain Graph",
    "data":{
        "nodes":[],
        "edges":[]
    }
}
GET /api/v1/supply-chain/summary
Purpose

Returns dashboard summary statistics.

Response
{
  "success": true,
  "message": "Supply Chain Summary",
  "data": {
    "suppliers": 124,
    "critical_suppliers": 8,
    "materials": 17,
    "battery_plants": 5
  }
}
Pydantic Schemas
SupplierResponse
supplier_id: str
supplier_name: str
country: str
supplier_type: str
risk_score: float
status: str
DependencyGraphResponse
nodes: list
edges: list
MaterialTraceabilityResponse
material: str
origin: str
supplier: str
battery_plant: str
vehicle: str
RiskResponse
supplier_id: str
risk_score: float
risk_level: str
risk_factors: list[str]
Enumerations
SupplierStatus
ACTIVE
INACTIVE
BLOCKED
RiskLevel
LOW

MEDIUM

HIGH

CRITICAL
SupplierType
Lithium

Nickel

Cobalt

Graphite

Battery Cell

Manufacturer

Logistics

Mining
RelationshipType
SUPPLIES

USED_BY

DELIVERS_TO

PRODUCES

INSTALLED_IN
Neo4j Labels
Supplier

Material

Mine

BatteryPlant

BatteryCell

Vehicle
Frontend Team Dependencies

The frontend can immediately integrate the following endpoints:

GET /api/v1/suppliers
GET /api/v1/suppliers/{supplier_id}

GET /api/v1/supply-chain/dependencies
GET /api/v1/supply-chain/material-flow
GET /api/v1/supply-chain/material-traceability

GET /api/v1/supply-chain/risk
GET /api/v1/supply-chain/risk-propagation

GET /api/v1/supply-chain/critical-suppliers
GET /api/v1/supply-chain/graph

GET /api/v1/supply-chain/summary

Primary UI screens:

Supplier Dashboard
Dependency Graph
Material Flow Visualization
Critical Supplier Heatmap
Risk Propagation View
Material Traceability Explorer
Supply Chain Summary Cards
Infrastructure Team Dependencies

Required services:

Neo4j

Required graph labels:

Supplier
Material
Mine
BatteryPlant
BatteryCell
Vehicle

Required relationship types:

SUPPLIES
USED_BY
DELIVERS_TO
PRODUCES
INSTALLED_IN

Environment variables:

NEO4J_URI
NEO4J_USER
NEO4J_PASSWORD
ML Team Dependencies

The ML team is responsible for computing supplier and supply chain risk scores.

Expected payload from ML/Risk Engine:

{
  "supplier_id": "SUP-001",
  "risk_score": 81,
  "risk_level": "HIGH",
  "risk_factors": [
    "Political Instability",
    "Commodity Price Spike",
    "Shipping Delay"
  ]
}

The backend:

Stores or retrieves graph relationships
Executes Neo4j traversals
Computes dependency paths
Serves graph visualization data

The ML/Risk Engine:

Calculates dynamic risk scores
Evaluates disruption probability
Generates supplier risk assessments
Deliverables
APIs
GET /api/v1/suppliers
GET /api/v1/suppliers/{supplier_id}

GET /api/v1/supply-chain/dependencies
GET /api/v1/supply-chain/material-flow
GET /api/v1/supply-chain/material-traceability

GET /api/v1/supply-chain/risk
GET /api/v1/supply-chain/risk-propagation

GET /api/v1/supply-chain/critical-suppliers
GET /api/v1/supply-chain/graph

GET /api/v1/supply-chain/summary
Schemas
SupplierResponse
DependencyGraphResponse
MaterialTraceabilityResponse
RiskResponse
Neo4j Labels
Supplier
Material
Mine
BatteryPlant
BatteryCell
Vehicle
Relationship Types
SUPPLIES
USED_BY
DELIVERS_TO
PRODUCES
INSTALLED_IN
Enums
SupplierStatus
SupplierType
RiskLevel
RelationshipType
```

---

## common_schemas\sustainablity_carbon_intelligence

```
Domain 9 — Sustainability & Carbon Intelligence
Responsibility

Provides sustainability analytics, carbon emission calculations, fleet electrification readiness assessments, diesel vs EV comparisons, procurement recommendations, and enterprise ESG metrics.

Directory Structure
backend/app/

models/
├── carbon_report.py
├── readiness_assessment.py

schemas/
├── sustainability.py

api/v1/endpoints/
├── sustainability.py

services/
├── carbon_service.py
├── readiness_service.py
├── procurement_service.py
Main Entities
CarbonReport

Stores calculated carbon emission reports.

Attributes
report_id
fleet_id
vehicle_id
report_period
distance_travelled
energy_consumed
diesel_emission
ev_emission
scope1_emission
scope3_emission
carbon_saved
generated_at
ReadinessAssessment

Stores electrification readiness analysis.

Attributes
assessment_id
fleet_id
vehicle_id
route_distance
payload
charging_availability
dwell_time
readiness_score
recommendation
generated_at
API Definitions
POST /api/v1/sustainability/carbon/calculate
Purpose

Calculates carbon emissions for a vehicle or fleet over a specified period.

Request
{
  "vehicle_id": "EV-001",
  "start_date": "2026-07-01",
  "end_date": "2026-07-31"
}
Response
{
  "success": true,
  "message": "Carbon Report Generated",
  "data": {
    "report_id": "CAR-1001",
    "distance_travelled": 2845,
    "energy_consumed_kwh": 652,
    "scope1_emission": 0,
    "scope3_emission": 184.6,
    "carbon_saved": 712.4
  }
}
GET /api/v1/sustainability/carbon/report/{report_id}
Purpose

Returns a previously generated carbon report.

Response
{
  "success": true,
  "message": "Carbon Report",
  "data": {
    "report_id": "CAR-1001",
    "vehicle_id": "EV-001",
    "scope1_emission": 0,
    "scope3_emission": 184.6,
    "carbon_saved": 712.4
  }
}
POST /api/v1/sustainability/diesel-vs-ev
Purpose

Compares emissions between diesel and electric operation.

Request
{
  "distance_km": 350,
  "payload_kg": 1200,
  "diesel_efficiency": 12,
  "ev_efficiency": 0.21
}
Response
{
  "success": true,
  "message": "Comparison Generated",
  "data": {
    "diesel_emission": 92.4,
    "ev_emission": 23.1,
    "carbon_saved": 69.3,
    "reduction_percentage": 75
  }
}
POST /api/v1/sustainability/readiness-assessment
Purpose

Evaluates fleet electrification readiness.

Request
{
  "route_distance": 220,
  "payload": 1500,
  "charging_availability": true,
  "dwell_time": 6
}
Response
{
  "success": true,
  "message": "Assessment Completed",
  "data": {
    "assessment_id": "READ-1001",
    "readiness_score": 86,
    "recommendation": "Suitable for EV migration"
  }
}
GET /api/v1/sustainability/readiness/{assessment_id}
Purpose

Returns readiness assessment details.

Response
{
  "success": true,
  "message": "Readiness Assessment",
  "data": {
    "assessment_id": "READ-1001",
    "readiness_score": 86,
    "recommendation": "Suitable for EV migration"
  }
}
POST /api/v1/sustainability/procurement-recommendation
Purpose

Generates procurement recommendations for EV adoption.

Request
{
  "fleet_size": 120,
  "daily_distance": 180,
  "charging_available": true
}
Response
{
  "success": true,
  "message": "Procurement Recommendation",
  "data": {
    "recommended_vehicle_type": "Medium Duty EV",
    "recommended_quantity": 40,
    "estimated_carbon_saving": 15400
  }
}
GET /api/v1/sustainability/summary
Purpose

Returns dashboard sustainability KPIs.

Response
{
  "success": true,
  "message": "Sustainability Summary",
  "data": {
    "total_carbon_saved": 48520,
    "scope1_emission": 0,
    "scope3_emission": 1542,
    "vehicles_assessed": 132,
    "average_readiness_score": 82
  }
}
GET /api/v1/sustainability/history
Purpose

Returns historical sustainability reports.

Query Parameters
vehicle_id
fleet_id
start_date
end_date
page
limit
Pydantic Schemas
CarbonCalculationRequest
vehicle_id: str
start_date: date
end_date: date
CarbonReportResponse
report_id: str
vehicle_id: str
distance_travelled: float
energy_consumed_kwh: float
scope1_emission: float
scope3_emission: float
carbon_saved: float
DieselVsEVRequest
distance_km: float
payload_kg: float
diesel_efficiency: float
ev_efficiency: float
ReadinessAssessmentRequest
route_distance: float
payload: float
charging_availability: bool
dwell_time: float
ReadinessAssessmentResponse
assessment_id: str
readiness_score: float
recommendation: str
ProcurementRecommendationResponse
recommended_vehicle_type: str
recommended_quantity: int
estimated_carbon_saving: float
Enumerations
ReportPeriod
DAILY
WEEKLY
MONTHLY
YEARLY
CUSTOM
RecommendationLevel
LOW

MEDIUM

HIGH
ReadinessLevel
NOT_READY

PARTIALLY_READY

READY

HIGHLY_READY
Frontend Team Dependencies

The frontend can immediately integrate the following endpoints:

POST /api/v1/sustainability/carbon/calculate
GET  /api/v1/sustainability/carbon/report/{report_id}

POST /api/v1/sustainability/diesel-vs-ev

POST /api/v1/sustainability/readiness-assessment
GET  /api/v1/sustainability/readiness/{assessment_id}

POST /api/v1/sustainability/procurement-recommendation

GET  /api/v1/sustainability/summary
GET  /api/v1/sustainability/history

Primary UI screens:

Carbon Dashboard
Diesel vs EV Comparison
Electrification Readiness Dashboard
Procurement Recommendation Panel
ESG Metrics Dashboard
Sustainability Report History
Infrastructure Team Dependencies

Required database tables:

carbon_report

readiness_assessment

Primary data sources:

Fleet Management

Telemetry & Time-Series

Charging Sessions

Battery Intelligence

Supply Chain Intelligence
ML Team Dependencies

The ML/Analytics team is responsible for generating readiness scores and procurement recommendations.

Expected readiness payload:

{
  "route_distance": 220,
  "payload": 1500,
  "charging_availability": true,
  "dwell_time": 6,
  "readiness_score": 86,
  "recommendation": "Suitable for EV migration"
}

Expected procurement payload:

{
  "recommended_vehicle_type": "Medium Duty EV",
  "recommended_quantity": 40,
  "estimated_carbon_saving": 15400
}

The backend:

Aggregates fleet and telemetry data
Exposes sustainability APIs
Stores reports and assessments
Returns analytics for dashboards

The ML/Analytics engine:

Calculates readiness scores
Estimates procurement recommendations
Provides optimization outputs
Deliverables
APIs
POST /api/v1/sustainability/carbon/calculate
GET  /api/v1/sustainability/carbon/report/{report_id}

POST /api/v1/sustainability/diesel-vs-ev

POST /api/v1/sustainability/readiness-assessment
GET  /api/v1/sustainability/readiness/{assessment_id}

POST /api/v1/sustainability/procurement-recommendation

GET  /api/v1/sustainability/summary
GET  /api/v1/sustainability/history
Schemas
CarbonCalculationRequest
CarbonReportResponse
DieselVsEVRequest
ReadinessAssessmentRequest
ReadinessAssessmentResponse
ProcurementRecommendationResponse
Database Tables
carbon_report

readiness_assessment
Enums
ReportPeriod
RecommendationLevel
ReadinessLevel
```

---

## common_schemas\teleentry_timeseries

```
backend/app/

models/
├── telemetry.py
├── charging_session.py
├── location_history.py

schemas/
├── telemetry.py
├── charging.py
├── location.py

api/v1/endpoints/
├── telemetry.py
├── charging.py
├── location.py

services/
├── telemetry_service.py
├── charging_service.py
├── location_service.py
├── websocket_manager.py

===========================================================================


Main Entities
Telemetry : Stores high-frequency IoT sensor readings.

Attributes
  telemetry_id
  vehicle_id
  timestamp
  state_of_charge
  state_of_health
  voltage
  current
  power
  temperature
  battery_capacity
  battery_cycles
  internal_resistance
  speed
  odometer
  charging_status
  latitude
  longitude

ChargingSession: Represents a complete charging cycle.
Attributes
  session_id
  vehicle_id
  charger_id
  start_time
  end_time
  start_soc
  end_soc
  energy_consumed
  charging_duration
  charging_type
  average_temperature
  status

LocationHistory : Stores GPS tracking data.
Attributes:
  location_id
  vehicle_id
  timestamp
  latitude
  longitude
  speed
  heading
  altitude


Database Relationships : 

Vehicle
1
│
├───────────────┐
│               │
│               │
▼               ▼
Telemetry    ChargingSession
│
▼
LocationHistory


============================================================================

API Definitions
Telemetry APIs
POST /api/v1/telemetry
Purpose: Stores a new telemetry record (primarily used by MQTT/Kafka consumer).
Request
{
  "vehicle_id": "EV-001",
  "timestamp": "2026-07-14T18:30:00Z",
  "state_of_charge": 82,
  "state_of_health": 94,
  "voltage": 387.5,
  "current": 42.3,
  "power": 16.4,
  "temperature": 34.6,
  "battery_capacity": 34.5,
  "battery_cycles": 412,
  "internal_resistance": 0.012,
  "speed": 62,
  "odometer": 15420,
  "charging_status": "DISCHARGING",
  "latitude": 13.0827,
  "longitude": 80.2707
}
Response
{
  "success": true,
  "message": "Telemetry Recorded"
}

GET /api/v1/telemetry/latest
Purpose : Returns the latest telemetry for one or more vehicles.
Query Parameters
  vehicle_id
  fleet_id (optional)
Response
{
  "success": true,
  "message": "Latest Telemetry",
  "data": {
    "vehicle_id": "EV-001",
    "timestamp": "2026-07-14T18:30:00Z",
    "state_of_charge": 82,
    "temperature": 34.6,
    "voltage": 387.5,
    "current": 42.3,
    "speed": 62
  }
}

GET /api/v1/telemetry/history
Purpose: Returns historical telemetry data.
Query Parameters
  vehicle_id
  start_time
  end_time
  page
  limit
Response
{
  "success": true,
  "message": "Telemetry History",
  "data": [
    {
      "timestamp": "2026-07-14T18:20:00Z",
      "state_of_charge": 84,
      "temperature": 33.8
    }
  ]
}


GET /api/v1/telemetry/timeseries
Purpose: Returns aggregated telemetry for visualization.
Query Parameters
  vehicle_id
  metric
  interval
  start_time
  end_time
  Example
  metric=temperature
  interval=5m
Response
{
  "success": true,
  "message": "Time Series Data",
  "data": [
    {
      "timestamp": "2026-07-14T18:00:00Z",
      "value": 31.4
    }
  ]
}


Charging APIs:

POST /api/v1/charging/session
Purpose: Creates a charging session.
Request
{
  "vehicle_id": "EV-001",
  "charger_id": "CH-01",
  "start_soc": 21,
  "charging_type": "FAST"
}
Response
{
  "success": true,
  "message": "Charging Session Started",
  "data": {
    "session_id": "CS-1001"
  }
}

PATCH /api/v1/charging/session/{session_id}
Purpose:Updates charging session on completion.
Request
{
  "end_soc": 96,
  "energy_consumed": 26.2,
  "charging_duration": 72,
  "status": "COMPLETED"
}
Response
{
  "success": true,
  "message": "Charging Session Updated"
}


GET /api/v1/charging/history
Purpose:Returns charging history.
Query Parameters
vehicle_id
start_date
end_date
Response
{
  "success": true,
  "message": "Charging History",
  "data": [
    {
      "session_id": "CS-1001",
      "start_soc": 20,
      "end_soc": 95,
      "energy_consumed": 26.2
    }
  ]
}


Location APIs:

POST /api/v1/location
Purpose: Stores GPS coordinates.
Request
{
  "vehicle_id": "EV-001",
  "timestamp": "2026-07-14T18:30:00Z",
  "latitude": 13.0827,
  "longitude": 80.2707,
  "speed": 62
}
Response
{
  "success": true,
  "message": "Location Recorded"
}


GET /api/v1/location/latest
Purpose: Returns latest GPS position.
Query Parameters
  vehicle_id
Response
{
  "success": true,
  "message": "Latest Location",
  "data": {
    "latitude": 13.0827,
    "longitude": 80.2707,
    "speed": 62
  }
}

GET /api/v1/location/history
Purpose: Returns historical GPS data.
Query Parameters
  vehicle_id
  start_time
  end_time


WebSocket APIs
WS /api/v1/ws/telemetry
Purpose: Streams live telemetry to dashboard.
Event Payload
{
  "vehicle_id": "EV-001",
  "timestamp": "2026-07-14T18:30:00Z",
  "state_of_charge": 82,
  "temperature": 34.6,
  "voltage": 387.5,
  "current": 42.3,
  "speed": 62
}

=========================================================================================

Pydantic Schemas

TelemetryCreate:
  vehicle_id: str
  timestamp: datetime
  state_of_charge: float
  state_of_health: float
  voltage: float
  current: float
  power: float
  temperature: float
  battery_capacity: float
  battery_cycles: int
  internal_resistance: float
  speed: float
  odometer: float
  charging_status: str
  latitude: float
  longitude: float

ChargingSessionCreate
  vehicle_id: str
  charger_id: str
  start_soc: float
  charging_type: str

LocationCreate
  vehicle_id: str
  timestamp: datetime
  latitude: float
  longitude: float
  speed: float


Enumerations:

ChargingStatus
  CHARGING
  DISCHARGING
  IDLE
  FULLY_CHARGED

ChargingType
  AC
  DC_FAST
  WIRELESS
  
MQTT Topics
  ev/telemetry
  ev/charging
  ev/location

Kafka Topics
  telemetry.raw
  telemetry.processed
  charging.events
  location.events


======================================================================

Frontend Team Dependencies

The frontend can integrate the following endpoints immediately:

GET /api/v1/telemetry/latest
GET /api/v1/telemetry/history
GET /api/v1/telemetry/timeseries

GET /api/v1/charging/history

GET /api/v1/location/latest
GET /api/v1/location/history

WS /api/v1/ws/telemetry

Primary UI screens:

Live Fleet Dashboard
Battery Monitoring
Charging History
Vehicle Map
Historical Charts
Infrastructure Team Dependencies

=================================================================================

Infrastructure must provide:

TimescaleDB
MQTT Broker (Mosquitto)
Kafka Broker
Kafka Consumers
Kafka Producers

TimescaleDB Hypertables:

telemetry
charging_session
location_history

Kafka Topics:

telemetry.raw
telemetry.processed
charging.events
location.events

MQTT Topics:

ev/telemetry
ev/charging
ev/location

====================================================================================

ML Team Dependencies

The ML team consumes historical telemetry and publishes prediction requests using the common vehicle_id.

Required telemetry fields:

vehicle_id
timestamp
state_of_charge
state_of_health
voltage
current
power
temperature
battery_capacity
battery_cycles
internal_resistance
charging_status

These fields form the input features for SoH estimation, Remaining Useful Life prediction, anomaly detection, and battery degradation models.


====================================================================================================
Deliverables
APIs
POST   /api/v1/telemetry
GET    /api/v1/telemetry/latest
GET    /api/v1/telemetry/history
GET    /api/v1/telemetry/timeseries

POST   /api/v1/charging/session
PATCH  /api/v1/charging/session/{session_id}
GET    /api/v1/charging/history

POST   /api/v1/location
GET    /api/v1/location/latest
GET    /api/v1/location/history

WS     /api/v1/ws/telemetry

Schemas
TelemetryCreate
ChargingSessionCreate
LocationCreate
Database Tables
telemetry
charging_session
location_history
Kafka Topics
telemetry.raw
telemetry.processed
charging.events
location.events
MQTT Topics
ev/telemetry
ev/charging
ev/location
Enums
ChargingStatus
ChargingType
```

---

## frontend\components.json

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/index.css",
    "baseColor": "slate",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
```

---

## frontend\index.html

```html
<!doctype html>
<html lang="en" class="dark">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Industrial EV AI Platform</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500;600&display=swap" rel="stylesheet">
  </head>
  <body class="bg-background text-foreground antialiased selection:bg-primary/20">
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

---

## frontend\package.json

```json
{
  "name": "ev-industrial-platform-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "clsx": "^2.0.0",
    "lucide-react": "^0.292.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.18.0",
    "recharts": "^2.15.4",
    "tailwind-merge": "^2.0.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.37",
    "@types/react-dom": "^18.2.15",
    "@vitejs/plugin-react": "^4.2.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.31",
    "tailwindcss": "^3.3.5",
    "typescript": "^5.2.2",
    "vite": "^5.0.0"
  }
}
```

---

## frontend\postcss.config.js

```javascript
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

---

## frontend\tailwind.config.js

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [],
}
```

---

## frontend\tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ES2020"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,

    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"]
}
```

---

## frontend\vite.config.ts

```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 3000,
    host: true,
  },
});
```

---

## infrastructure\project_dump.md

```markdown
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
```

---

## ml\project_dump.md

```markdown
# Project Dump

Project: ml

## Directory Tree

```text
ml
├── notebooks
│   └── README.md
├── project_dump.md
├── requirements.txt
├── simulator
│   └── simulator.py
└── src
    └── preprocessing.py
```

# File Contents

---

## project_dump.md

**[Empty File]**

---

## requirements.txt

```text
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.2.0
xgboost>=1.7.0
paho-mqtt>=1.6.0
faker>=19.0.0
jupyter>=1.0.0
```

---

## notebooks\README.md

```markdown
# AI/ML Engineering Notebooks

This folder is designated for exploratory data analysis (EDA), statistical tests, and machine learning model training notebooks (Member 3).

## Recommended Notebook Workflow

### 1. `01_exploratory_data_analysis.ipynb`
- Load and parse datasets: NASA Battery Dataset, Oxford Battery Dataset, NASA C-MAPSS.
- Telemetry profiling: Voltage, Current, Temperature, Capacity Fade, Cycle Count.
- Target derivation: Calculate remaining load cycles before cell capacity hits the 80% degradation threshold.

### 2. `02_model_training_and_evaluation.ipynb`
- Train XGBoost models for Remaining Useful Life (RUL) regression predictions.
- Train Isolation Forest models for real-time anomaly alerts (detecting thermal risks, cell voltage disparities, abnormal charging curves).
- Export trained model weights to production assets (`ml/models/`).
```

---

## simulator\simulator.py

```python
import time
import json
import random
import argparse
from datetime import datetime,timezone
import numpy as np

try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("Warning: paho-mqtt not installed. Run 'pip install paho-mqtt'")
    mqtt = None

VEHICLE_IDS = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]

class TelemetrySimulator:
    def __init__(self, broker_address="localhost", broker_port=1883):
        self.broker = broker_address
        self.port = broker_port
        self.client = None

        # State profiles for vehicles: nominal capacity, current soc, temperature, cycle counts
        self.states = {
            vid: {
                "soc": random.uniform(50, 95),
                "temperature": random.uniform(28, 35),
                "voltage": 400.0,
                "cycles": random.randint(100, 500),
                "degradation_factor": random.uniform(0.01, 0.05)
            } for vid in VEHICLE_IDS
        }

    def connect(self):
        if mqtt is None:
            print("Simulator starting in dry-run mode (MQTT packages missing).")
            return False

        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2 if hasattr(mqtt, 'CallbackAPIVersion') else None)
        try:
            self.client.connect(self.broker, self.port, 60)
            print(f"Connected to Mosquitto MQTT Broker at {self.broker}:{self.port}")
            self.client.loop_start()
            return True
        except Exception as e:
            print(f"Failed to connect to MQTT broker: {e}. Defaulting to terminal log.")
            self.client = None
            return False

    def simulate_step(self):
        for vid in VEHICLE_IDS:
            state = self.states[vid]

            # --- Simulated Physics Engine Logic ---
            is_charging = vid == "EV-HD-002"

            if is_charging:
                state["soc"] = min(100.0, state["soc"] + random.uniform(0.1, 0.4))
                current = random.uniform(-60.0, -20.0)  # negative represents charge
                voltage = 380 + (state["soc"] * 0.3)
                state["temperature"] = min(50.0, state["temperature"] + random.uniform(-0.1, 0.3))
                speed = 0.0
                motor_rpm = 0
                power_output = round(float(voltage * current / 1000.0), 2)  # negative power during charge
            else:
                state["soc"] = max(10.0, state["soc"] - random.uniform(0.05, 0.2))
                current = random.uniform(10.0, 45.0)  # positive represents discharge
                voltage = 400 - ((100 - state["soc"]) * 0.3)
                state["temperature"] = max(25.0, state["temperature"] + random.uniform(-0.2, 0.2))
                speed = round(random.uniform(40.0, 90.0), 2)
                motor_rpm = int(speed * 50 + random.uniform(-100, 100))
                power_output = round(float(voltage * current / 1000.0), 2)

            if vid == "EV-HD-004" and random.random() < 0.15:
                state["temperature"] += random.uniform(2.0, 5.0)
                print(f"[ANOMALY WARNING] Simulated thermal runaway surge on {vid}")

            state["cycles"] += int(random.random() < 0.01)

            # ISO-8601 UTC timestamp format compliance string
            timestamp_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

            # --- Contract Payload 1: General EV Telemetry (Topic: ev/telemetry) ---
            telemetry_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "speed": speed,
                "odometer": round(15000.0 + (state["cycles"] * 2.5), 2),
                "motor_rpm": motor_rpm,
                "power_output": power_output,
                "ambient_temperature": round(random.uniform(20.0, 30.0), 1)
            }

            # --- Contract Payload 2: Battery Telemetry (Topic: ev/battery) ---
            battery_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "soc": round(float(state["soc"]), 1),
                "soh": round(100.0 - (state["cycles"] * 0.015), 2),  # Degrades gradually over cycles
                "voltage": round(float(voltage), 2),
                "current": round(float(current), 2),
                "capacity": 75.0,  # Nominal capacity in kWh
                "cycle_count": state["cycles"],
                "internal_resistance": round(0.01 + (state["cycles"] * 0.00005), 5),
                "cell_temperature": round(float(state["temperature"]), 2)
            }

            # --- Publishing Engine Block ---
            if self.client:
                # Direct match to specifications using flat base paths
                self.client.publish("ev/telemetry", json.dumps(telemetry_payload), qos=1)
                self.client.publish("ev/battery", json.dumps(battery_payload), qos=1)
            else:
                print(f"[SIMULATED STREAM] TOPIC: ev/telemetry | DATA: {telemetry_payload}")
                print(f"[SIMULATED STREAM] TOPIC: ev/battery | DATA: {battery_payload}")

    def run(self, interval=1.0):
        print("Starting EV Telemetry Simulation loop. Press Ctrl+C to terminate.")
        try:
            while True:
                self.simulate_step()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Simulation terminated.")
            if self.client:
                self.client.loop_stop()
                self.client.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EV Battery Telemetry Simulator")
    parser.add_argument("--host", default="localhost", help="MQTT Broker host")
    parser.add_argument("--port", type=int, default=1883, help="MQTT Broker port")
    parser.add_argument("--interval", type=float, default=1.0, help="Stream tick interval in seconds")
    args = parser.parse_args()

    sim = TelemetrySimulator(args.host, args.port)
    sim.connect()
    sim.run(args.interval)
```

---

## src\preprocessing.py

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class TelemetryPreprocessor:
    def __init__(self):
        self.scaler = MinMaxScaler()
        
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handles null values in timeseries telemetry columns via forward/backward fill."""
        fill_cols = ["voltage", "current", "temperature", "soc"]
        df[fill_cols] = df[fill_cols].ffill().bfill()
        return df

    def filter_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Removes physical impossibilities or noise outliers from sensor readings."""
        # E.g., voltage must be positive, temperatures below extreme limits
        df = df[(df["voltage"] > 0) & (df["voltage"] < 1000)]
        df = df[(df["temperature"] > -40) & (df["temperature"] < 150)]
        return df

    def engineer_battery_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Engineers critical battery health predictors:
        - Capacity degradation
        - Thermal variance (rolling cell temp delta)
        - Average discharge slope (dV/dt)
        - Charging efficiency (energy absorbed per cycle)
        """
        # Ensure chronological ordering
        df = df.sort_values("timestamp")
        
        # 1. Thermal Variance
        df["temp_rolling_var"] = df["temperature"].rolling(window=10, min_periods=1).var()
        
        # 2. Discharge Slope (dV/dt)
        df["time_diff_sec"] = df["timestamp"].diff().dt.total_seconds()
        df["voltage_diff"] = df["voltage"].diff()
        
        # Calculate dV/dt, replacing division-by-zero with zero
        df["discharge_slope"] = np.where(
            df["time_diff_sec"] > 0, 
            df["voltage_diff"] / df["time_diff_sec"], 
            0.0
        )
        
        # 3. Capacity Fade approximation (Ah depletion integration)
        # Ah = current * time_hours
        df["current_hours"] = (df["current"] * (df["time_diff_sec"] / 3600.0)).abs()
        df["capacity_fade"] = df["current_hours"].cumsum()
        
        return df

    def scale_features(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """Scales numeric telemetry features for deep learning/regression models."""
        df[columns] = self.scaler.fit_transform(df[columns])
        return df
```
```

---

## ml\requirements.txt

```text
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.2.0
xgboost>=1.7.0
paho-mqtt>=1.6.0
faker>=19.0.0
jupyter>=1.0.0
```

---

## backend\app\main.py

```python
import sys
import os
import asyncio
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

# Windows proactor event loop fix for aiomqtt socket polling
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

    # FIXED: Added missing comma and cleaned out duplicate string literals
    target_domain_topics = [
        "ev.telemetry",
        "ev.battery",
        "ev.location",
        "ev.charging",
        "ev.status",
        "ev.alerts",
        "ev.diagnostics"
    ]
    
    # Register the live debug output print callback across all domain streams
    for domain_topic in target_domain_topics:
        kafka_consumer.register_callback(domain_topic, kafka_to_ws_broadcaster)
        logger.debug(f"Registered WebSocket broadcaster hook for topic: {domain_topic}")

    # Instantiate the new database persistence bridge worker
    telemetry_processor = TelemetryProcessor()

    # Domain specific callback routing matrix mapping
    # Every channel triggers BOTH the real-time WebSocket pipe AND the TimescaleDB storage engine
    kafka_consumer.register_callback("ev.telemetry", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.telemetry", telemetry_processor.process_kinematics)

    kafka_consumer.register_callback("ev.battery", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.battery", telemetry_processor.process_battery)

    kafka_consumer.register_callback("ev.location", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.location", telemetry_processor.process_location)

    kafka_consumer.register_callback("ev.charging", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.charging", telemetry_processor.process_charging)

    # For channels that do not have repositories yet, keep the legacy console broadcast active
    kafka_consumer.register_callback("ev.status", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.alerts", kafka_to_ws_broadcaster)
    kafka_consumer.register_callback("ev.diagnostics", kafka_to_ws_broadcaster)

    # 3. Start Downstream First (Kafka)
    await kafka_producer.start()
    await kafka_consumer.start()
    
    # 4. Start Upstream Last (MQTT Ingestion)
    await mqtt_client.start()
    
    logger.info("Platform streaming layer fully operational.")
    
    yield  # Application runs here

    logger.info("Initiating graceful shutdown sequence...")
    
    # 5. Stop Upstream First (Halt new ingestion)
    await mqtt_client.stop()
    
    # 6. Stop Consumers (Halt internal processing)
    await kafka_consumer.stop()
    
    # 7. Stop Downstream Last (Flush pending producer batches)
    await kafka_producer.stop()
    
    logger.info("Shutdown complete. All connections closed safely.")

# Initialize the FastAPI application
app = FastAPI(title="Industrial EV AI Platform - Streaming Layer", lifespan=lifespan)

# Include core routers
app.include_router(health_router)
app.include_router(ws_router)

app.include_router(rest_router)
```

---

## backend\app\api\health.py

```python
import logging
from fastapi import APIRouter, HTTPException, status
from app.core.container import container

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/health", tags=["Monitoring"])

@router.get("")
async def liveness_check():
    """Basic HTTP liveness probe to verify the API event loop is running."""
    return {"status": "alive", "service": "streaming_layer"}

@router.get("/mqtt")
async def mqtt_readiness_check():
    """Verifies the Mosquitto MQTT broker connection is active."""
    try:
        mqtt = container.mqtt_client
        # Verify the client exists and the background consumption task is actively running
        if mqtt and mqtt._consume_task and not mqtt._consume_task.done():
            return {"status": "connected", "protocol": "mqtt"}
    except RuntimeError:
        # Caught if the DI container hasn't initialized the client yet
        pass
        
    logger.warning("MQTT health check failed.")
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
        detail="MQTT broker connection is not active."
    )

@router.get("/kafka")
async def kafka_readiness_check():
    """Verifies both Kafka Producer and Consumer are active."""
    try:
        producer = container.kafka_producer
        consumer = container.kafka_consumer
        
        is_producer_ok = producer and producer.producer
        is_consumer_ok = consumer and consumer._consume_task and not consumer._consume_task.done()
        
        if is_producer_ok and is_consumer_ok:
            return {"status": "connected", "protocol": "kafka", "components": ["producer", "consumer"]}
            
    except RuntimeError:
        pass
        
    logger.warning("Kafka health check failed.")
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
        detail="Kafka event bus connections are not fully active."
    )
```

---

## backend\app\api\ws_routes.py

```python
# import logging
# from fastapi import APIRouter, WebSocket, WebSocketDisconnect
# from app.streaming.websocket.manager import ws_manager

# logger = logging.getLogger(__name__)
# router = APIRouter()

# @router.websocket("/ws/dashboard")
# async def dashboard_websocket_endpoint(websocket: WebSocket) -> None:
#     """
#     WebSocket endpoint for the React frontend.
#     Expects incoming JSON commands: {"action": "subscribe", "topic": "telemetry.raw"}
#     """
#     await ws_manager.connect(websocket)
    
#     try:
#         while True:
#             # Wait for control commands from the client
#             data = await websocket.receive_json()
#             action = data.get("action")
#             topic = data.get("topic")
            
#             if action == "subscribe" and topic:
#                 await ws_manager.subscribe(websocket, topic)
#             elif action == "unsubscribe" and topic:
#                 await ws_manager.unsubscribe(websocket, topic)
                
#     except WebSocketDisconnect:
#         ws_manager.disconnect(websocket)
#     except Exception as e:
#         logger.error("WebSocket connection error.", exc_info=True)
#         ws_manager.disconnect(websocket)

import logging
import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.streaming.websocket.manager import ws_manager

logger = logging.getLogger(__name__)
router = APIRouter()

@router.websocket("/ws/dashboard")
async def dashboard_websocket_endpoint(websocket: WebSocket) -> None:
    """
    WebSocket endpoint for the React frontend.
    Logs traffic to the terminal for debugging without a UI.
    """
    await ws_manager.connect(websocket)
    logger.info("=== [TESTING] Terminal Client Connected to Dashboard Stream ===")
    
    try:
        while True:
            data = await websocket.receive_json()
            action = data.get("action")
            topic = data.get("topic")
            
            if action == "subscribe" and topic:
                await ws_manager.subscribe(websocket, topic)
                print(f"\n[SUBSCRIPTION] Client listening to Kafka topic: {topic}")
            elif action == "unsubscribe" and topic:
                await ws_manager.unsubscribe(websocket, topic)
                print(f"\n[UNSUBSCRIPTION] Client stopped listening to Kafka topic: {topic}")
                
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
        logger.info("=== [TESTING] Terminal Client Disconnected ===")
    except Exception as e:
        logger.error("WebSocket connection error.", exc_info=True)
        ws_manager.disconnect(websocket)
```

---

## backend\app\contracts\envelope.py

```python
from datetime import datetime, timezone
from typing import Generic, TypeVar, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# Generic Type for payload validation flexibility
T = TypeVar('T', bound=BaseModel)

class EventEnvelope(BaseModel, Generic[T]):
    """Standardized event envelope wrapping all platform domain payloads."""
    
    event_id: UUID = Field(default_factory=uuid4, description="Unique identifier for this specific event instance")
    event_type: str = Field(..., description="The type of event (e.g., 'telemetry.raw', 'battery.alert')")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="UTC timestamp of event generation")
    source: str = Field(..., description="Originating service or simulator node name")
    vehicle_id: str = Field(..., description="Unique immutable ID of the industrial vehicle")
    fleet_id: str = Field(..., description="Identifier for the tracking fleet operational partition")
    correlation_id: UUID = Field(default_factory=uuid4, description="Tracing ID sustained across asynchronous boundaries")
    
    payload: T = Field(..., description="The concrete domain data model matching the event type")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            UUID: lambda v: str(v)
        }
```

---

## backend\app\core\config.py

```python
from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MqttSettings(BaseSettings):
    host: str = Field(default="localhost")
    port: int = Field(default=1883)
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    keepalive: int = Field(default=60)
    client_id: str = Field(default="industrial_ev_streaming_layer")


class KafkaSettings(BaseSettings):
    bootstrap_servers: List[str] = Field(default=["localhost:9092"])
    group_id: str = Field(default="ev_streaming_group")
    auto_offset_reset: str = Field(default="earliest")


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__", extra="ignore")
    database_url: str = "postgresql+asyncpg://ev_admin:ev_password@localhost:5432/ev_platform"
    environment: str = Field(default="development")
    debug: bool = Field(default=False)
    mqtt: MqttSettings = MqttSettings()
    kafka: KafkaSettings = KafkaSettings()


settings = AppSettings()
```

---

## backend\app\core\container.py

```python
import logging
from typing import Any, Optional
from app.core.config import settings

logger = logging.getLogger(__name__)

class ApplicationContainer:
    """Manages system-wide client allocations and lifecycle liftoffs."""
    
    def __init__(self) -> None:
        self.settings = settings
        
        # Placeholders for explicit network clients initialized during app startup
        self._mqtt_client: Optional[Any] = None
        self._kafka_producer: Optional[Any] = None
        self._kafka_consumer: Optional[Any] = None

    def register_mqtt_client(self, client: Any) -> None:
        self._mqtt_client = client
        logger.debug("Async MQTT Client registered to DI container.")

    def register_kafka_producer(self, producer: Any) -> None:
        self._kafka_producer = producer
        logger.debug("Async Kafka Producer registered to DI container.")

    def register_kafka_consumer(self, consumer: Any) -> None:
        self._kafka_consumer = consumer
        logger.debug("Async Kafka Consumer Framework registered to DI container.")

    @property
    def mqtt_client(self) -> Any:
        if not self._mqtt_client:
            raise RuntimeError("MQTT Client requested before initialization.")
        return self._mqtt_client

    @property
    def kafka_producer(self) -> Any:
        if not self._kafka_producer:
            raise RuntimeError("Kafka Producer requested before initialization.")
        return self._kafka_producer
        
    @property
    def kafka_consumer(self) -> Any:
        if not self._kafka_consumer:
            raise RuntimeError("Kafka Consumer requested before initialization.")
        return self._kafka_consumer

    def get_kafka_consumer(self) -> Any:
        """Explicit getter used during startup to wire WebSocket callbacks."""
        if not self._kafka_consumer:
            raise RuntimeError("Kafka Consumer requested before initialization.")
        return self._kafka_consumer


# Global container instance
container = ApplicationContainer()
```

---

## backend\app\core\logging.py

```python
import sys
import logging
import json
from datetime import datetime, timezone
from app.core.config import settings


class JsonFormatter(logging.Formatter):
    """Formats log records as single-line JSON strings for production parsing."""
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        if hasattr(record, "correlation_id"):
            log_data["correlation_id"] = record.correlation_id
        if hasattr(record, "vehicle_id"):
            log_data["vehicle_id"] = record.vehicle_id
            
        return json.dumps(log_data)


import os

def setup_logging() -> None:
    """Initializes global logging configurations."""
    root_logger = logging.getLogger()
    
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        
    handler = logging.StreamHandler(sys.stdout)
    
    # Check for custom LOG_LEVEL env var first
    env_log_level = os.getenv("LOG_LEVEL")
    if env_log_level:
        level = getattr(logging, env_log_level.upper(), logging.INFO)
    else:
        level = logging.DEBUG if getattr(settings, "debug", False) else logging.INFO
    
    if hasattr(settings, "environment") and settings.environment.lower() == "production":
        handler.setFormatter(JsonFormatter())
        root_logger.setLevel(level)
    else:
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        root_logger.setLevel(level)
        
    root_logger.addHandler(handler)
    
    logging.getLogger("aiokafka").setLevel(logging.WARNING)
    logging.getLogger("aiomqtt").setLevel(logging.WARNING)
```

---

## backend\app\db\init_timescale.py

```python
import asyncio
import logging
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings
from app.models.domain import Base

logger = logging.getLogger(__name__)

# Ensure your settings point to asyncpg: "postgresql+asyncpg://user:pass@localhost:5432/ev_platform"
DATABASE_URL = settings.database_url 

async def init_db():
    logger.info("Initializing database and TimescaleDB hypertables...")
    engine = create_async_engine(DATABASE_URL, echo=True)

    async with engine.begin() as conn:
        # 1. Create standard PostgreSQL tables
        await conn.run_sync(Base.metadata.create_all)
        
        logger.info("Standard tables created. Converting time-series tables to TimescaleDB hypertables...")

        # 2. Execute TimescaleDB Hypertable conversion commands
        # The 'IF NOT EXISTS' equivalent in Timescale is handled by checking if it's already a hypertable,
        # but create_hypertable has a 'if_not_exists' flag we can use.
        hypertable_queries = [
            "SELECT create_hypertable('telemetry_records', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('battery_records', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('location_history', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('status_history', 'timestamp', if_not_exists => TRUE);"
        ]

        for query in hypertable_queries:
            try:
                # We use text() wrapper for raw SQL in SQLAlchemy 2.0
                from sqlalchemy import text
                await conn.execute(text(query))
            except Exception as e:
                # If TimescaleDB extension is missing, this will catch and warn you
                logger.warning(f"Failed to create hypertable (ensure TimescaleDB extension is enabled): {e}")

    await engine.dispose()
    logger.info("Database initialization complete.")

if __name__ == "__main__":
    asyncio.run(init_db())
```

---

## backend\app\db\session.py

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

# 1. Create the Async Engine
engine = create_async_engine(
    settings.database_url,
    echo=False,  # Set to True for debugging SQL queries
    pool_size=20, # Connection pool optimized for high-throughput streaming
    max_overflow=10
)

# 2. Create the Async Session Maker
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False # Prevents SQLAlchemy from issuing extra SELECTs after commit
)

# 3. Dependency function for FastAPI routes and Kafka processors
async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session
```

---

## backend\app\models\domain.py

```python
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# ---------------------------------------------------------
# TIME-SERIES HYPERTABLE MODELS (High-Frequency Data)
# ---------------------------------------------------------

class TelemetryRecord(Base):
    __tablename__ = "telemetry_records"

    # TimescaleDB requires the time column in the primary key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    speed_kph = Column(Float, nullable=False)
    odometer_km = Column(Float, nullable=False)
    motor_temperature_c = Column(Float, nullable=False)
    torque_nm = Column(Float, nullable=False)
    inverter_efficiency = Column(Float, nullable=False)

class BatteryRecord(Base):
    __tablename__ = "battery_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    state_of_charge_pct = Column(Float, nullable=False)
    state_of_health_pct = Column(Float, nullable=False)
    voltage = Column(Float, nullable=False)
    current_amps = Column(Float, nullable=False)
    cell_temperature_max_c = Column(Float, nullable=False)
    internal_resistance_ohm = Column(Float, nullable=False)

class LocationHistory(Base):
    __tablename__ = "location_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    altitude_m = Column(Float, nullable=True)
    heading_deg = Column(Integer, nullable=True)
    gps_fix_quality = Column(String(20), nullable=True)

class StatusHistory(Base):
    __tablename__ = "status_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    
    vehicle_id = Column(String(50), nullable=False, index=True)
    operational_status = Column(String(50), nullable=False)
    active_error_codes = Column(JSON, default=list)
    driver_id = Column(String(50), nullable=True)

# ---------------------------------------------------------
# RELATIONAL MODELS (Low-Frequency / State Data)
# ---------------------------------------------------------

class ChargingSession(Base):
    __tablename__ = "charging_sessions"

    # Standard relational table: only ID is the primary key
    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, name="id")
    vehicle_id = Column(String(50), nullable=False, index=True)
    charger_id = Column(String(50), nullable=True)
    
    start_time = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    end_time = Column(DateTime(timezone=True), nullable=True)
    
    status = Column(String(20), nullable=False, default="ACTIVE") # ACTIVE, COMPLETED, FAILED
    energy_consumed_kwh = Column(Float, nullable=True, default=0.0)
```

---

## backend\app\models\relational.py

```python
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, index=True)
    voltage = Column(Float, nullable=False)
    current = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    soc = Column(Float, nullable=False)  # State of Charge (0-100)

class ChargingSession(Base):
    __tablename__ = "charging_sessions"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)
    energy_delivered_kwh = Column(Float, nullable=False)
    starting_soc = Column(Float, nullable=False)
    ending_soc = Column(Float, nullable=True)

class BatteryHealth(Base):
    __tablename__ = "battery_health"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), unique=True, nullable=False, index=True)
    capacity_fade = Column(Float, nullable=False)  # Ah drop
    cycle_count = Column(Integer, nullable=False)
    state_of_health = Column(Float, nullable=False)  # percentage (0-100)
    remaining_useful_life = Column(Integer, nullable=False)  # estimated cycles remaining

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    severity = Column(String(20), nullable=False)  # Critical, Warning, Info
    type = Column(String(50), nullable=False)  # Thermal, Over-voltage, Anomaly
    description = Column(String(255), nullable=False)
    resolved = Column(Boolean, default=False)

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    risk_score = Column(Float, default=0.0)
    material_supplied = Column(String(50), nullable=False)  # Lithium, Cobalt, Nickel, etc.

class MaintenanceLog(Base):
    __tablename__ = "maintenance_logs"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String(255), nullable=False)
    action_taken = Column(String(255), nullable=True)
    status = Column(String(50), default="Pending")  # Pending, In Progress, Completed
```

---

## backend\app\repositories\domain.py

```python
from typing import List, Optional, Dict, Any
from datetime import datetime
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

class TelemetryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: TelemetryRecord) -> None:
        """High-speed async insert for kinematic telemetry."""
        self.session.add(record)
        await self.session.commit()

    async def history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Retrieves raw kinematics history within a time window."""
        stmt = (
            select(TelemetryRecord)
            .where(
                TelemetryRecord.vehicle_id == vehicle_id,
                TelemetryRecord.timestamp >= start_time,
                TelemetryRecord.timestamp <= end_time
            )
            .order_by(desc(TelemetryRecord.timestamp))
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def timeseries_aggregation(self, vehicle_id: str, interval: str = "1 hour", limit: int = 24) -> List[Dict[str, Any]]:
        """
        Uses TimescaleDB's native time_bucket function to aggregate data efficiently.
        Returns the average speed and max motor temperature per time bucket.
        """
        # FIX: Changed FROM ev_telemetry to FROM telemetry_records to match domain.py
        query = text("""
            SELECT 
                time_bucket(CAST(:interval AS INTERVAL), timestamp) AS time_bucket,
                AVG(speed_kph) AS avg_speed,
                MAX(motor_temperature_c) AS max_motor_temp,
                AVG(torque_nm) AS avg_torque
            FROM telemetry_records
            WHERE vehicle_id = :vehicle_id
            GROUP BY time_bucket
            ORDER BY time_bucket DESC
            LIMIT :limit;
        """)
        
        result = await self.session.execute(query, {"interval": interval, "vehicle_id": vehicle_id, "limit": limit})
        
        return [
            {"time": row[0], "avg_speed": round(row[1], 2) if row[1] is not None else 0.0, "max_temp": round(row[2], 2) if row[2] is not None else 0.0} 
            for row in result.fetchall()
        ]


class BatteryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: BatteryRecord) -> None:
        """High-speed async insert for electro-chemical metrics."""
        self.session.add(record)
        await self.session.commit()

    async def latest(self, vehicle_id: str) -> Optional[BatteryRecord]:
        """Fetches the absolute latest battery state."""
        stmt = (
            select(BatteryRecord)
            .where(BatteryRecord.vehicle_id == vehicle_id)
            .order_by(desc(BatteryRecord.timestamp))
            .limit(1)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def degradation_history(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[Dict[str, Any]]:
        """
        Calculates daily State of Health (SoH) degradation and Internal Resistance growth.
        """
        query = text("""
            SELECT
                time_bucket('1 day', timestamp) AS day,
                MIN(state_of_health_pct) as min_soh,
                MAX(internal_resistance_ohm) as max_resistance
            FROM battery_records
            WHERE vehicle_id = :vehicle_id AND timestamp >= :start AND timestamp <= :end
            GROUP BY day
            ORDER BY day ASC;
        """)
        
        result = await self.session.execute(
            query, {"vehicle_id": vehicle_id, "start": start_time, "end": end_time}
        )
        return [{"date": row[0], "soh_pct": float(row[1]), "resistance_ohm": float(row[2])} for row in result.fetchall()]


class LocationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: LocationHistory) -> None:
        self.session.add(record)
        await self.session.commit()

    async def route_playback(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """Retrieves an ordered path of coordinates for map playback."""
        stmt = (
            select(LocationHistory)
            .where(
                LocationHistory.vehicle_id == vehicle_id,
                LocationHistory.timestamp >= start_time,
                LocationHistory.timestamp <= end_time
            )
            .order_by(LocationHistory.timestamp)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()


class ChargingRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_session(self, session_record: ChargingSession) -> ChargingSession:
        """Initializes a new charging session."""
        self.session.add(session_record)
        await self.session.commit()
        await self.session.refresh(session_record)
        return session_record

    async def complete_session(self, session_id: str, end_time: datetime, total_kwh: float) -> Optional[ChargingSession]:
        """Updates an active charging session to COMPLETED."""
        stmt = select(ChargingSession).where(ChargingSession.session_id == session_id)
        result = await self.session.execute(stmt)
        charging_session = result.scalar_one_or_none()
        
        if charging_session:
            charging_session.end_time = end_time
            charging_session.energy_consumed_kwh = total_kwh
            charging_session.status = "COMPLETED"
            await self.session.commit()
            
        return charging_session
```

---

## backend\app\schemas\payloads.py

```python
# from typing import Dict, Any, Optional
# from pydantic import BaseModel, Field

# class TelemetryPayload(BaseModel):
#     """Core kinematic data from the vehicle's engine and operational control units."""
#     speed_kph: float = Field(..., ge=0, le=200)
#     odometer_km: float = Field(..., ge=0)
#     motor_temperature_c: float = Field(..., ge=-40, le=150)
#     torque_nm: float = Field(...)
#     inverter_efficiency: float = Field(..., ge=0, le=1)


# class BatteryPayload(BaseModel):
#     """Real-time electro-chemical battery state statistics."""
#     state_of_charge_pct: float = Field(..., ge=0, le=100)
#     state_of_health_pct: float = Field(..., ge=0, le=100)
#     voltage: float = Field(..., ge=0, le=1000)
#     current_amps: float = Field(...)
#     cell_temperature_max_c: float = Field(..., ge=-40, le=100)
#     internal_resistance_ohm: float = Field(..., ge=0)


# class LocationPayload(BaseModel):
#     """High-precision positional telemetry coordinate data."""
#     latitude: float = Field(..., ge=-90, le=90)
#     longitude: float = Field(..., ge=-180, le=180)
#     altitude_m: float = Field(..., ge=-500, le=9000)
#     heading_deg: float = Field(..., ge=0, le=360)
#     gps_fix_quality: int = Field(..., description="0=Invalid, 1=GPS, 2=DGPS")


# class ChargingPayload(BaseModel):
#     """State management metrics during an active battery charging session."""
#     charger_id: str = Field(...)
#     charging_rate_kw: float = Field(..., ge=0)
#     time_to_full_mins: float = Field(..., ge=0)
#     connector_type: str = Field(..., description="CCS2, Megawatt, etc.")


# class StatusPayload(BaseModel):
#     """High-level operating mode state flags."""
#     operational_status: str = Field(..., description="READY, OPERATIONAL, FAULT, OFFLINE")
#     active_error_codes: list[str] = Field(default_factory=list)
#     driver_id: Optional[str] = Field(default=None)


# class AlertsPayload(BaseModel):
#     """Immediate hardware or safety critical notifications."""
#     alert_code: str = Field(...)
#     severity: str = Field(..., description="INFO, WARNING, CRITICAL")
#     component: str = Field(..., description="BATTERY, MOTOR, BRAKES, POWERTRAIN")
#     description: str = Field(...)


# class HeartbeatPayload(BaseModel):
#     """Lightweight diagnostics asserting infrastructure network health."""
#     uptime_seconds: int = Field(..., ge=0)
#     firmware_version: str = Field(...)
#     signal_strength_dbm: int = Field(..., le=0)



from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field, ConfigDict

# 1. CREATE THE BASE CLASS
class BasePayload(BaseModel):
    """Base configuration allowing both old aliases and new enterprise keys, while keeping extra data."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")

# 2. INHERIT FROM BasePayload (not BaseModel) FOR ALL YOUR SCHEMAS

class TelemetryPayload(BasePayload):
    """Kinematic data mapping simulator inputs to system targets with safe defaults."""
    speed_kph: float = Field(default=0.0, validation_alias="speed", ge=0, le=200)
    odometer_km: float = Field(default=0.0, validation_alias="odometer", ge=0)
    motor_temperature_c: float = Field(default=65.0, validation_alias="ambient_temperature", ge=-40, le=150)
    # Simulator doesn't provide torque or efficiency yet; generate clean platform mock defaults
    torque_nm: float = Field(default=210.5, description="Fallback tracking default")
    inverter_efficiency: float = Field(default=0.94, ge=0, le=1)

class BatteryPayload(BasePayload):
    """Electro-chemical stats providing field transformations for native simulator outputs."""
    state_of_charge_pct: float = Field(..., validation_alias="soc", ge=0, le=100)
    state_of_health_pct: float = Field(..., validation_alias="soh", ge=0, le=100)
    voltage: float = Field(..., ge=0, le=1000)
    current_amps: float = Field(..., validation_alias="current")
    cell_temperature_max_c: float = Field(..., validation_alias="cell_temperature", ge=-40, le=100)
    internal_resistance_ohm: float = Field(..., validation_alias="internal_resistance", ge=0)

class LocationPayload(BasePayload):
    """Positional mapping supporting clean initialization blocks for empty topics."""
    latitude: float = Field(default=39.7392, ge=-90, le=90)
    longitude: float = Field(default=-104.9903, ge=-180, le=180)
    altitude_m: float = Field(default=1609.0, ge=-500, le=9000)
    heading_deg: float = Field(default=0.0, ge=0, le=360)
    gps_fix_quality: int = Field(default=1)

class ChargingPayload(BasePayload):
    """Fallback charging structures for silent initialization loops."""
    charger_id: str = Field(default="CHG-STATION-MOCK")
    charging_rate_kw: float = Field(default=0.0, ge=0)
    time_to_full_mins: float = Field(default=0.0, ge=0)
    connector_type: str = Field(default="CCS2")

class StatusPayload(BasePayload):
    operational_status: str = Field(default="OPERATIONAL")
    active_error_codes: List[str] = Field(default_factory=list)
    driver_id: Optional[str] = Field(default="SYSTEM_AUTO")

class AlertsPayload(BasePayload):
    alert_code: str = Field(default="CLR_00")
    severity: str = Field(default="INFO")
    component: str = Field(default="SYSTEM")
    description: str = Field(default="Healthy baseline initialization status.")

class HeartbeatPayload(BasePayload):
    uptime_seconds: int = Field(default=0, ge=0)
    firmware_version: str = Field(default="v1.0.0-mock")
    signal_strength_dbm: int = Field(default=-50, le=0)
```

---

## backend\app\schemas\telemetry.py

```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class TelemetryBase(BaseModel):
    vehicle_id: str
    voltage: float
    current: float
    temperature: float
    soc: float

class TelemetryCreate(TelemetryBase):
    pass

class TelemetryResponse(TelemetryBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class BatteryHealthResponse(BaseModel):
    vehicle_id: str
    capacity_fade: float
    cycle_count: int
    state_of_health: float
    remaining_useful_life: int

    class Config:
        from_attributes = True

class AlertResponse(BaseModel):
    id: int
    vehicle_id: str
    timestamp: datetime
    severity: str
    type: str
    description: str
    resolved: bool

    class Config:
        from_attributes = True

class SupplierRiskResponse(BaseModel):
    id: int
    name: str
    location: str
    risk_score: float
    material_supplied: str

    class Config:
        from_attributes = True

class DependencyNode(BaseModel):
    id: str
    label: str
    properties: dict

class DependencyEdge(BaseModel):
    source: str
    target: str
    type: str

class GraphDependencyResponse(BaseModel):
    nodes: List[DependencyNode]
    edges: List[DependencyEdge]
```

---

## backend\app\services\telemetry.py

```python
from datetime import datetime
from typing import List, Dict, Any, Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.domain import (
    TelemetryRepository,
    BatteryRepository,
    LocationRepository,
    ChargingRepository
)
from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

# ---------------------------------------------------------
# BUSINESS LOGIC & VALIDATION RULES
# ---------------------------------------------------------

def validate_time_window(start_time: datetime, end_time: datetime, max_days: int = 30) -> None:
    """Enforces strict boundaries on historical queries to prevent database memory exhaustion."""
    if start_time > end_time:
        raise HTTPException(
            status_code=400, 
            detail="Invalid request: start_time cannot be later than end_time."
        )
    
    delta = end_time - start_time
    if delta.days > max_days:
        raise HTTPException(
            status_code=400, 
            detail=f"Query rejected: Requested time range of {delta.days} days exceeds the maximum allowed window of {max_days} days."
        )

# ---------------------------------------------------------
# DOMAIN SERVICES
# ---------------------------------------------------------

class TelemetryService:
    def __init__(self, session: AsyncSession):
        self.repo = TelemetryRepository(session)

    async def get_history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Validates the time window before fetching raw kinematic history."""
        validate_time_window(start_time, end_time, max_days=30)
        return await self.repo.history(vehicle_id, start_time, end_time, limit)

    async def get_timeseries(self, vehicle_id: str, interval: str = "1 hour", limit: int = 24) -> List[Dict[str, Any]]:
        """Pass-through for aggregated time-series data."""
        # TimescaleDB handles intervals safely, but we cap the limit to prevent runaway aggregations
        safe_limit = min(limit, 1000) 
        return await self.repo.timeseries_aggregation(vehicle_id, interval, safe_limit)


class BatteryService:
    def __init__(self, session: AsyncSession):
        self.repo = BatteryRepository(session)

    async def get_latest(self, vehicle_id: str) -> Optional[BatteryRecord]:
        """Fetches the current real-time state of the battery."""
        record = await self.repo.latest(vehicle_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"No battery telemetry found for vehicle {vehicle_id}")
        return record

    async def get_degradation(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[Dict[str, Any]]:
        """
        Battery degradation occurs slowly, so we allow a longer 90-day analytics window 
        specifically for this aggregated query.
        """
        validate_time_window(start_time, end_time, max_days=90)
        return await self.repo.degradation_history(vehicle_id, start_time, end_time)


class LocationService:
    def __init__(self, session: AsyncSession):
        self.repo = LocationRepository(session)

    async def get_route(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """
        GPS route playback queries pull dense datasets. 
        We enforce a strict 7-day maximum window to protect bandwidth and memory.
        """
        validate_time_window(start_time, end_time, max_days=7)
        return await self.repo.route_playback(vehicle_id, start_time, end_time)
```

---

## backend\app\api\v1\api.py

```python
from fastapi import APIRouter
from .endpoints import health, telemetry, ml_inference, supply_chain, sustainability

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(telemetry.router, tags=["telemetry"])
api_router.include_router(ml_inference.router, tags=["ml_inference"])
api_router.include_router(supply_chain.router, tags=["supply_chain"])
api_router.include_router(sustainability.router, tags=["sustainability"])
```

---

## backend\app\api\v1\rest_routes.py

```python
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.db.session import get_db_session
from app.services.telemetry import TelemetryService, BatteryService, LocationService
from app.repositories.domain import ChargingRepository
from app.models.domain import ChargingSession

router = APIRouter(prefix="/api/v1", tags=["Telemetry & Domain Data"])

# ---------------------------------------------------------
# REQUEST SCHEMAS
# ---------------------------------------------------------
class ChargingSessionCreate(BaseModel):
    vehicle_id: str
    charger_id: str

# ---------------------------------------------------------
# TELEMETRY ENDPOINTS
# ---------------------------------------------------------

@router.get("/telemetry/latest")
async def get_latest_telemetry(
    vehicle_id: str,
    session: AsyncSession = Depends(get_db_session)
):
    """Returns the most recent kinematics reading for a specific vehicle."""
    service = TelemetryService(session)
    # We query history with a limit of 1 over the last 24 hours to find the absolute latest
    end = datetime.utcnow()
    start = end - timedelta(days=1)
    
    records = await service.get_history(vehicle_id, start_time=start, end_time=end, limit=1)
    if not records:
        raise HTTPException(status_code=404, detail="No recent telemetry found for this vehicle.")
    return records[0]


@router.get("/telemetry/timeseries")
async def get_telemetry_timeseries(
    vehicle_id: str,
    interval: str = Query("1 hour", description="TimescaleDB interval (e.g., '15 minutes', '1 hour')"),
    limit: int = Query(24, le=1000),
    session: AsyncSession = Depends(get_db_session)
):
    """Returns aggregated kinematic metrics grouped by time buckets for charting."""
    service = TelemetryService(session)
    return await service.get_timeseries(vehicle_id, interval=interval, limit=limit)

# ---------------------------------------------------------
# BATTERY ENDPOINTS
# ---------------------------------------------------------

@router.get("/battery/latest")
async def get_latest_battery(
    vehicle_id: str,
    session: AsyncSession = Depends(get_db_session)
):
    """Returns the absolute real-time State of Charge and Health for the battery."""
    service = BatteryService(session)
    return await service.get_latest(vehicle_id)

# ---------------------------------------------------------
# LOCATION ENDPOINTS
# ---------------------------------------------------------

@router.get("/location/history")
async def get_location_history(
    vehicle_id: str,
    start_time: datetime,
    end_time: datetime,
    session: AsyncSession = Depends(get_db_session)
):
    """Retrieves an ordered array of GPS coordinates for map route playback."""
    service = LocationService(session)
    return await service.get_route(vehicle_id, start_time, end_time)

# ---------------------------------------------------------
# CHARGING ENDPOINTS
# ---------------------------------------------------------

@router.post("/charging/session")
async def start_charging_session(
    payload: ChargingSessionCreate,
    session: AsyncSession = Depends(get_db_session)
):
    """Initializes a new charging session in the database with explicit timestamping."""
    repo = ChargingRepository(session)
    new_session = ChargingSession(
        vehicle_id=payload.vehicle_id,
        charger_id=payload.charger_id,
        start_time=datetime.utcnow(),  # Add this explicit timestamp
        status="ACTIVE",
        energy_consumed_kwh=0.0
    )
    return await repo.create_session(new_session)
```

---

## backend\app\api\v1\endpoints\health.py

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": "2026-07-10T09:05:00Z",
        "version": "1.0.0"
    }
```

---

## backend\app\api\v1\endpoints\ml_inference.py

```python
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException
from ....schemas.telemetry import BatteryHealthResponse
import asyncio
import random
import json

router = APIRouter()

MOCK_BATTERY_HEALTH = {
    "EV-HD-001": {"vehicle_id": "EV-HD-001", "capacity_fade": 5.8, "cycle_count": 260, "state_of_health": 96.0, "remaining_useful_life": 1240},
    "EV-HD-002": {"vehicle_id": "EV-HD-002", "capacity_fade": 9.2, "cycle_count": 410, "state_of_health": 91.0, "remaining_useful_life": 890},
    "EV-HD-003": {"vehicle_id": "EV-HD-003", "capacity_fade": 2.1, "cycle_count": 95, "state_of_health": 98.0, "remaining_useful_life": 1450},
    "EV-HD-004": {"vehicle_id": "EV-HD-004", "capacity_fade": 17.5, "cycle_count": 780, "state_of_health": 83.0, "remaining_useful_life": 430},
}

@router.get("/battery/status", response_model=BatteryHealthResponse)
def get_battery_status(vehicle_id: str = Query(..., description="ID of the EV vehicle asset")):
    if vehicle_id not in MOCK_BATTERY_HEALTH:
        raise HTTPException(status_code=404, detail="Battery status not found for vehicle")
    return MOCK_BATTERY_HEALTH[vehicle_id]

@router.post("/predict/rul")
def predict_rul(payload: dict):
    # Mock ML inference request utilizing temperature, voltage, cycle profiles
    voltage = payload.get("voltage", 380)
    temperature = payload.get("temperature", 35)
    cycle_count = payload.get("cycle_count", 100)
    
    # Simple linear degradation simulation
    base_life = 1500
    degradation = (cycle_count * 1.1) + (temperature * 2.5) + (400 - voltage)
    estimated_rul = max(0, int(base_life - degradation))
    
    return {
        "predicted_rul_cycles": estimated_rul,
        "confidence_interval": [estimated_rul - 50, estimated_rul + 50],
        "model_version": "xgboost-battery-rul-v1.0"
    }

@router.post("/predict/soh")
def predict_soh(payload: dict):
    capacity = payload.get("capacity", 120.0)
    nominal_capacity = payload.get("nominal_capacity", 120.0)
    
    soh = (capacity / nominal_capacity) * 100.0
    return {
        "state_of_health": round(soh, 2),
        "capacity_fade_ah": round(nominal_capacity - capacity, 2),
        "model_version": "regression-degradation-soh-v1.0"
    }

@router.post("/predict/anomaly")
def predict_anomaly(payload: dict):
    temperature = payload.get("temperature", 25.0)
    voltage = payload.get("voltage", 390.0)
    
    # Anomaly indicator: if temp exceeds threshold or voltage is abnormally low
    is_anomaly = False
    anomaly_score = 0.05
    
    if temperature > 45.0 or voltage < 320.0:
        is_anomaly = True
        anomaly_score = 0.89 + (temperature * 0.002)
        
    return {
        "is_anomaly": is_anomaly,
        "anomaly_score": round(anomaly_score, 3),
        "anomalous_features": ["temperature" if temperature > 45.0 else None, "voltage" if voltage < 320.0 else None],
        "model_version": "isolation-forest-anomaly-v1.0"
    }

@router.websocket("/telemetry/ws/{vehicle_id}")
async def websocket_endpoint(websocket: WebSocket, vehicle_id: str):
    await websocket.accept()
    try:
        while True:
            # Generate simulated live streaming data for WebSockets
            data = {
                "vehicle_id": vehicle_id,
                "timestamp": str(asyncio.get_event_loop().time()),
                "voltage": round(random.uniform(370, 410), 2),
                "current": round(random.uniform(-50, 50), 2),
                "temperature": round(random.uniform(30, 48), 2),
                "soc": round(random.uniform(20, 99), 1)
              }
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        pass
```

---

## backend\app\api\v1\endpoints\supply_chain.py

```python
from fastapi import APIRouter
from ....schemas.telemetry import SupplierRiskResponse, GraphDependencyResponse
from typing import List

router = APIRouter()

MOCK_SUPPLIERS = [
    {"id": 1, "name": "Salar de Atacama Minerals", "location": "Chile", "risk_score": 24.5, "material_supplied": "Lithium"},
    {"id": 2, "name": "Tianqi Lithium Refining", "location": "Sichuan, China", "risk_score": 86.2, "material_supplied": "Refined Lithium Hydroxide"},
    {"id": 3, "name": "Democratic Republic of Congo Mining", "location": "Katanga", "risk_score": 68.0, "material_supplied": "Cobalt Ore"},
    {"id": 4, "name": "Sumitomo Metal Mining", "location": "Japan", "risk_score": 15.4, "material_supplied": "Cathode Precursors"},
]

@router.get("/suppliers", response_model=List[SupplierRiskResponse])
def get_suppliers():
    return MOCK_SUPPLIERS

@router.get("/risk")
def get_supply_chain_risk():
    return {
        "global_risk_index": 54.8,
        "critical_vulnerability": "High concentration of refining capacity in Sichuan region.",
        "mitigation_plan": "Diversify sourcing contracts with North American refiners.",
        "last_updated": "2026-07-10T09:05:00Z"
    }

@router.get("/materials")
def get_materials_flow():
    return {
        "materials": [
            {"name": "Lithium", "active_flow_tons": 450, "safety_buffer_days": 45},
            {"name": "Cobalt", "active_flow_tons": 120, "safety_buffer_days": 30},
            {"name": "Nickel", "active_flow_tons": 800, "safety_buffer_days": 60},
        ]
    }

@router.get("/dependencies", response_model=GraphDependencyResponse)
def get_dependencies_graph():
    # Return structured nodes & edges simulating a Neo4j Cypher query response
    return {
        "nodes": [
            {"id": "node_mine_1", "label": "Mine", "properties": {"name": "Salar de Atacama Mine", "country": "Chile"}},
            {"id": "node_refiner_1", "label": "Refiner", "properties": {"name": "Tianqi Refining", "country": "China"}},
            {"id": "node_plant_1", "label": "Battery Plant", "properties": {"name": "CATL Yibin", "capacity_gwh": 20}},
            {"id": "node_fleet_1", "label": "Fleet Vehicle", "properties": {"vehicle_id": "EV-HD-004", "hub": "Denver"}}
        ],
        "edges": [
            {"source": "node_mine_1", "target": "node_refiner_1", "type": "SUPPLIES_RAW_MATERIAL"},
            {"source": "node_refiner_1", "target": "node_plant_1", "type": "DELIVERS_REFINED_LITHIUM"},
            {"source": "node_plant_1", "target": "node_fleet_1", "type": "EQUIP_BATTERY_TO"}
        ]
    }
```

---

## backend\app\api\v1\endpoints\sustainability.py

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/carbon")
def get_carbon_metrics():
    return {
        "co2_savings_ytd_tons": 142.6,
        "diesel_displacement_gallons": 14500,
        "grid_emission_intensity_kwh": 0.32,  # kg CO2/kWh
        "scope_1_direct_displaced_tons": 160.4,
        "scope_3_grid_indirect_tons": 17.8
    }

@router.get("/electrification")
def get_electrification_readiness():
    return {
        "readiness_score": 84,
        "total_active_routes": 195,
        "electrified_routes": 82,
        "recommendations": [
            {
                "route_id": "DEN-BOU-01",
                "name": "Denver - Boulder Corridor",
                "readiness_percentage": 94,
                "reason": "Short length, highly dense public fast chargers, low grade variance."
            },
            {
                "route_id": "HOU-LOC-04",
                "name": "Houston Local Hub Delivery",
                "readiness_percentage": 88,
                "reason": "Repeated stop patterns allow dwell-time depot charging."
            }
        ]
    }
```

---

## backend\app\api\v1\endpoints\telemetry.py

```python
from fastapi import APIRouter, Query, HTTPException
from typing import List
from ....schemas.telemetry import TelemetryResponse
import datetime

router = APIRouter()

MOCK_VEHICLES = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]

MOCK_TELEMETRY = {
    "EV-HD-001": {"vehicle_id": "EV-HD-001", "voltage": 395.2, "current": 12.4, "temperature": 34.5, "soc": 88.0, "id": 1, "timestamp": datetime.datetime.utcnow()},
    "EV-HD-002": {"vehicle_id": "EV-HD-002", "voltage": 380.1, "current": -45.0, "temperature": 38.2, "soc": 42.0, "id": 2, "timestamp": datetime.datetime.utcnow()},
    "EV-HD-003": {"vehicle_id": "EV-HD-003", "voltage": 401.5, "current": 10.1, "temperature": 33.1, "soc": 91.0, "id": 3, "timestamp": datetime.datetime.utcnow()},
    "EV-HD-004": {"vehicle_id": "EV-HD-004", "voltage": 372.4, "current": 115.0, "temperature": 44.8, "soc": 76.0, "id": 4, "timestamp": datetime.datetime.utcnow()},
}

@router.get("/vehicles", response_model=List[str])
def get_vehicles():
    return MOCK_VEHICLES

@router.get("/telemetry/live", response_model=TelemetryResponse)
def get_live_telemetry(vehicle_id: str = Query(..., description="ID of the EV vehicle asset")):
    if vehicle_id not in MOCK_TELEMETRY:
        raise HTTPException(status_code=404, detail="Vehicle telemetry not found")
    # Update timestamp to match current query time
    telemetry = MOCK_TELEMETRY[vehicle_id]
    telemetry["timestamp"] = datetime.datetime.utcnow()
    return telemetry
```

---

## backend\app\streaming\consumers\client.py

```python
import asyncio
import json
import logging
from typing import Callable, Dict, List, Optional, Awaitable, Any

from aiokafka import AIOKafkaConsumer
from app.core.config import settings

logger = logging.getLogger(__name__)

# Define the callback signature: takes a topic (str) and the parsed JSON payload (dict)
ConsumerCallback = Callable[[str, Dict[str, Any]], Awaitable[None]]

class KafkaEventConsumer:
    """Async Kafka consumer framework with an internal callback router."""

    def __init__(self) -> None:
        self.consumer = None
        self._consume_task = None
        
        # UNIFIED NAME: Changed from self.valid_topics to self.ALLOWED_TOPICS
        self.ALLOWED_TOPICS = {
            "ev.telemetry",
            "ev.battery",
            "ev.location",
            "ev.charging",
            "ev.status",
            "ev.alerts",
            "ev.diagnostics"
        }
        
        # Internal router mapping Kafka topics to a list of registered async callbacks
        self._callbacks: Dict[str, List[ConsumerCallback]] = {
            topic: [] for topic in self.ALLOWED_TOPICS
        }

    def register_callback(self, topic: str, callback: ConsumerCallback) -> None:
        """Allows domain services to hook into specific Kafka topics."""
        if topic not in self.ALLOWED_TOPICS:
            logger.warning("Attempted to register callback for unknown topic.", extra={"topic": topic})
            return
            
        self._callbacks[topic].append(callback)
        logger.debug("Registered new callback.", extra={"topic": topic, "callback": callback.__name__})

    async def start(self) -> None:
        """Initializes the Kafka consumer and begins the listening loop."""
        logger.info("Initializing Kafka consumer framework...")
        
        # *self.ALLOWED_TOPICS safely unpacks the set values as independent string arguments
        self.consumer = AIOKafkaConsumer(
            *self.ALLOWED_TOPICS,
            bootstrap_servers=settings.kafka.bootstrap_servers,
            group_id=settings.kafka.group_id,
            auto_offset_reset=settings.kafka.auto_offset_reset,
            enable_auto_commit=True
        )
        
        try:
            await self.consumer.start()
            logger.info("Kafka Consumer successfully connected to brokers.")
            
            # Spin up the background consuming loop
            self._consume_task = asyncio.create_task(self._consume_loop())
        except Exception as e:
            logger.critical("Failed to connect Kafka Consumer.", exc_info=True)
            raise

    async def stop(self) -> None:
        """Gracefully shuts down the consumer task and connection."""
        if self._consume_task:
            self._consume_task.cancel()
            try:
                await self._consume_task
            except asyncio.CancelledError:
                pass
                
        if self.consumer:
            await self.consumer.stop()
            logger.info("Kafka Consumer disconnected cleanly.")

    async def _consume_loop(self) -> None:
        """Background loop retrieving messages and dispatching them to callbacks."""
        if not self.consumer:
            return

        try:
            async for message in self.consumer:
                topic = message.topic
                
                # Check if anyone actually cares about this topic before parsing
                if not self._callbacks.get(topic):
                    continue

                try:
                    # Parse the raw bytes back into the EventEnvelope JSON dictionary
                    payload_dict = json.loads(message.value.decode("utf-8"))
                    
                    # Dispatch to all registered callbacks asynchronously
                    # We use create_task so a slow callback doesn't block the Kafka consumer loop
                    for callback in self._callbacks[topic]:
                        asyncio.create_task(self._execute_callback(callback, topic, payload_dict))
                        
                except json.JSONDecodeError:
                    logger.error("Failed to decode Kafka message as JSON.", extra={"topic": topic})
                except Exception as e:
                    logger.error("Error dispatching Kafka message.", exc_info=True, extra={"topic": topic})

        except asyncio.CancelledError:
            logger.info("Kafka consumption task gracefully cancelled.")
            
    async def _execute_callback(self, callback: ConsumerCallback, topic: str, payload: Dict[str, Any]) -> None:
        """Safely executes a callback, catching any unhandled exceptions."""
        try:
            await callback(topic, payload)
        except Exception as e:
            logger.error(
                "Unhandled exception in consumer callback.", 
                exc_info=True, 
                extra={"topic": topic, "callback": callback.__name__}
            )
```

---

## backend\app\streaming\mqtt\client.py

```python
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
                
                # 1. Subscribe to all fixed data topics
                for topic in self.topics:
                    await client.subscribe(topic)
                    logger.info("Subscribed to MQTT topic", extra={"mqtt_topic": topic})
                
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

        # 1. Structural Schema Validation Check
        validated_model = validate_raw_payload(topic, payload_bytes)
        
        if validated_model:
            # 2. Normalize and extract the target domain channel type
            envelope = normalize_to_envelope(topic, validated_model)
            
            # DYNAMIC ROUTING FIX: Grab the exact destination from the normalizer mapping
            target_kafka_topic = envelope.event_type
            
            # 3. Stream asynchronously straight onto the specific Kafka Topic Bus line
            kafka_producer = container.kafka_producer
            asyncio.create_task(kafka_producer.publish(target_kafka_topic, envelope))
```

---

## backend\app\streaming\processor\telemetry.py

```python
import logging
from typing import Dict, Any
from datetime import datetime
from dateutil.parser import isoparse

from app.db.session import AsyncSessionLocal
from app.repositories.domain import (
    TelemetryRepository, 
    BatteryRepository, 
    LocationRepository, 
    ChargingRepository
)
from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

class TelemetryProcessor:
    """Bridges incoming Kafka EventEnvelope payloads to target domain database repositories."""

    @staticmethod
    def _parse_timestamp(ts_str: str) -> datetime:
        """Safely parses ISO-8601 UTC timestamp strings into Python datetime objects."""
        try:
            return isoparse(ts_str)
        except Exception:
            return datetime.utcnow()

    async def process_kinematics(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.telemetry' streams and persists kinematic vectors."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))

        logger.info(f"[PROCESSOR] Intercepted kinematics for vehicle {vehicle_id}")

        record = TelemetryRecord(
            vehicle_id=vehicle_id,
            timestamp=ts,
            speed_kph=float(payload.get("speed_kph", 0.0)),
            odometer_km=float(payload.get("odometer_km", 0.0)),
            motor_temperature_c=float(payload.get("motor_temperature_c", 0.0)),
            torque_nm=float(payload.get("torque_nm", 0.0)),
            inverter_efficiency=float(payload.get("inverter_efficiency", 1.0))
        )

        async with AsyncSessionLocal() as session:
            repo = TelemetryRepository(session)
            await repo.insert(record)

    async def process_battery(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.battery' streams and persists electro-chemical metrics."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))

        logger.info(f"[PROCESSOR] Intercepted battery diagnostics for vehicle {vehicle_id}")

        record = BatteryRecord(
            vehicle_id=vehicle_id,
            timestamp=ts,
            state_of_charge_pct=float(payload.get("state_of_charge_pct", 0.0)),
            state_of_health_pct=float(payload.get("state_of_health_pct", 100.0)),
            voltage=float(payload.get("voltage", 0.0)),
            current_amps=float(payload.get("current_amps", 0.0)),
            cell_temperature_max_c=float(payload.get("cell_temperature_max_c", 0.0)),
            internal_resistance_ohm=float(payload.get("internal_resistance_ohm", 0.0))
        )

        async with AsyncSessionLocal() as session:
            repo = BatteryRepository(session)
            await repo.insert(record)

    async def process_location(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.location' streams and persists geospatial telemetry chunks."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))

        logger.info(f"[PROCESSOR] Intercepted geospatial logs for vehicle {vehicle_id}")

        record = LocationHistory(
            vehicle_id=vehicle_id,
            timestamp=ts,
            latitude=float(payload.get("latitude", 0.0)),
            longitude=float(payload.get("longitude", 0.0)),
            altitude_m=float(payload.get("altitude_m", 0.0)) if payload.get("altitude_m") else None,
            heading_deg=int(payload.get("heading_deg", 0)) if payload.get("heading_deg") else None,
            gps_fix_quality=payload.get("gps_fix_quality", "UNKNOWN")
        )

        async with AsyncSessionLocal() as session:
            repo = LocationRepository(session)
            await repo.insert(record)

    async def process_charging(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        """Processes 'ev.charging' infrastructure streams to manage session lifecycle state."""
        payload = event_envelope.get("payload", {})
        vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
        ts = self._parse_timestamp(payload.get("timestamp"))
        
        charger_id = payload.get("charger_id")
        connector_type = payload.get("connector_type", "NONE")

        # In a real environment, you would check for an active session to see whether to create or update.
        # For this stage of the bridge ingestion path, we register the event log explicitly.
        if charger_id and connector_type != "NONE":
            logger.info(f"[PROCESSOR] Processing active charging payload for vehicle {vehicle_id}")
            record = ChargingSession(
                vehicle_id=vehicle_id,
                charger_id=charger_id,
                start_time=ts,
                status="ACTIVE",
                energy_consumed_kwh=float(payload.get("charging_rate_kw", 0.0)) / 60.0 # Instantaneous integration approximation
            )
            async with AsyncSessionLocal() as session:
                repo = ChargingRepository(session)
                await repo.create_session(record)
```

---

## backend\app\streaming\producers\client.py

```python
import logging
from typing import Optional
from aiokafka import AIOKafkaProducer

from app.core.config import settings
from app.contracts.envelope import EventEnvelope

logger = logging.getLogger(__name__)

class KafkaEventProducer:
    """Async Kafka producer for routing normalized events to the message bus."""
    
    def __init__(self) -> None:
        self.producer: Optional[AIOKafkaProducer] = None

    async def start(self) -> None:
        """Initializes the Kafka producer connection pool."""
        logger.info("Initializing Kafka producer...", extra={"brokers": settings.kafka.bootstrap_servers})
        
        self.producer = AIOKafkaProducer(
            bootstrap_servers=settings.kafka.bootstrap_servers,
            client_id="ev_streaming_producer",
            # Acknowledge leader write for high throughput, safe enough for telemetry
            acks=1 
        )
        
        try:
            await self.producer.start()
            logger.info("Kafka Producer successfully connected.")
        except Exception as e:
            logger.critical("Failed to connect Kafka Producer.", exc_info=True)
            raise

    async def stop(self) -> None:
        """Flushes pending batches and cleanly disconnects."""
        if self.producer:
            await self.producer.stop()
            logger.info("Kafka Producer disconnected.")

    async def publish(self, target_topic: str, event: EventEnvelope) -> None:
        """Serializes the event envelope and publishes it to the specified topic."""
        if not self.producer:
            logger.error("Attempted to publish without an active Kafka connection.")
            return

        try:
            # Pydantic v2 serialization to JSON bytes
            payload_bytes = event.model_dump_json().encode("utf-8")
            
            # Fire-and-forget for telemetry throughput, though send_and_wait can be used for guarantees
            await self.producer.send(target_topic, value=payload_bytes)
            
        except Exception as e:
            logger.error(
                "Failed to publish event to Kafka.",
                exc_info=True,
                extra={"target_topic": target_topic, "event_id": str(event.event_id)}
            )
```

---

## backend\app\streaming\serializers\normalizer.py

```python
# import logging
# from typing import Dict
# from pydantic import BaseModel
# from app.contracts.envelope import EventEnvelope

# logger = logging.getLogger(__name__)

# # Map incoming MQTT topics to target Kafka topics/event types
# MQTT_TO_KAFKA_ROUTE: Dict[str, str] = {
#     "ev/telemetry": "telemetry.raw",
#     "ev/battery": "telemetry.raw",  # Routing battery data to the same raw firehose for now
#     "ev/location": "telemetry.raw",
#     "ev/charging": "telemetry.raw",
#     "ev/status": "telemetry.raw",
#     "ev/alerts": "alerts",
#     "ev/heartbeat": "telemetry.raw"
# }

# def normalize_to_envelope(mqtt_topic: str, payload: BaseModel) -> EventEnvelope:
#     """
#     Wraps a validated domain payload into the standard Event Envelope.
#     Generates event_id and correlation_id automatically via the schema defaults.
#     """
#     target_event_type = MQTT_TO_KAFKA_ROUTE.get(mqtt_topic, "unknown.raw")
    
#     # In a fully integrated environment, vehicle_id and fleet_id might be extracted
#     # from the MQTT topic structure (e.g., ev/telemetry/{fleet_id}/{vehicle_id}) 
#     # or the payload itself. Since our topics are fixed, we inject placeholders 
#     # for the infrastructure integration phase.
    
#     envelope = EventEnvelope(
#         event_type=target_event_type,
#         source="streaming_ingestion_node",
#         vehicle_id="VEH-SIM-001",
#         fleet_id="FLT-ALPHA-01",
#         payload=payload
#     )
    
#     logger.debug(
#         "Normalized event payload.",
#         extra={
#             "event_id": str(envelope.event_id),
#             "correlation_id": str(envelope.correlation_id),
#             "event_type": target_event_type
#         }
#     )
#     return envelope



import logging
from pydantic import BaseModel
from app.contracts.envelope import EventEnvelope

logger = logging.getLogger(__name__)

# Segmenting the single firehose into clean domain streams
MQTT_TO_KAFKA_ROUTE = {
    "ev/telemetry": "ev.telemetry",
    "ev/battery": "ev.battery",
    "ev/location": "ev.location",
    "ev/charging": "ev.charging",
    "ev/status": "ev.status",
    "ev/alerts": "ev.alerts",
    "ev/heartbeat": "ev.diagnostics"
}

def normalize_to_envelope(mqtt_topic: str, payload: BaseModel) -> EventEnvelope:
    """Wraps the validated payload and dynamically assigns its destination event_type."""
    target_event_type = MQTT_TO_KAFKA_ROUTE.get(mqtt_topic, "ev.unknown")
    
    extracted_vehicle = getattr(payload, "vehicle_id", "VEH-SIM-UNKNOWN")
    
    envelope = EventEnvelope(
        event_type=target_event_type,  # The envelope type now matches the domain stream name
        source="streaming_ingestion_node",
        vehicle_id=extracted_vehicle,
        fleet_id="FLT-ALPHA-01",
        payload=payload
    )
    
    logger.debug(
        "Normalized event payload targeted for domain topic.",
        extra={
            "event_id": str(envelope.event_id),
            "target_topic": target_event_type
        }
    )
    return envelope
```

---

## backend\app\streaming\serializers\validator.py

```python
import json
import logging
from typing import Optional, Dict, Type
from pydantic import BaseModel, ValidationError

from app.schemas.payloads import (
    TelemetryPayload, BatteryPayload, LocationPayload,
    ChargingPayload, StatusPayload, AlertsPayload, HeartbeatPayload
)

logger = logging.getLogger(__name__)

# Map fixed, immutable MQTT topics to their structural validators
TOPIC_SCHEMA_MAP: Dict[str, Type[BaseModel]] = {
    "ev/telemetry": TelemetryPayload,
    "ev/battery": BatteryPayload,
    "ev/location": LocationPayload,
    "ev/charging": ChargingPayload,
    "ev/status": StatusPayload,
    "ev/alerts": AlertsPayload,
    "ev/heartbeat": HeartbeatPayload
}

def validate_raw_payload(topic: str, raw_data: bytes) -> Optional[BaseModel]:
    """
    Parses and structural-checks incoming binary JSON string payloads against domain schemas.
    
    Returns a Pydantic Model instance if valid; returns None if malformed or unknown.
    """
    schema_cls = TOPIC_SCHEMA_MAP.get(topic)
    
    if not schema_cls:
        logger.warning(
            "Received event on unregistered topic. Processing discarded.",
            extra={"mqtt_topic": topic}
        )
        return None

    try:
        # Step 1: Deserialize JSON payload safely
        parsed_json = json.loads(raw_data)
        
        # Step 2: Perform schema enforcement via Pydantic
        validated_model = schema_cls.model_validate(parsed_json)
        return validated_model
        
    except json.JSONDecodeError as jde:
        logger.error(
            "Failed to deserialize payload. Raw input is not clean JSON.",
            exc_info=True,
            extra={"mqtt_topic": topic}
        )
    except ValidationError as ve:
        logger.warning(
            "Payload failed schema compliance assertions. Event dropped.",
            extra={
                "mqtt_topic": topic,
                "validation_errors": ve.errors(include_url=False)
            }
        )
    except Exception as e:
        logger.critical(
            "Unexpected processing failure during validation pipeline.",
            exc_info=True,
            extra={"mqtt_topic": topic}
        )
        
    return None
```

---

## backend\app\streaming\websocket\adapter.py

```python
import logging
from typing import Dict, Any
from app.streaming.websocket.manager import ws_manager

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

async def kafka_to_ws_broadcaster(topic: str, payload: Dict[str, Any]) -> None:
    """
    Standard callback registered with the Kafka Event Consumer.
    Bridges the Kafka bus directly to the WebSocket manager.
    """
    logger.debug("Relaying Kafka event to WebSockets.", extra={"topic": topic})
    await ws_manager.broadcast(topic, payload)
```

---

## backend\app\streaming\websocket\manager.py

```python
import logging
import json
from typing import Dict, Set, Any
from fastapi import WebSocket

logger = logging.getLogger(__name__)

class WebSocketManager:
    """Manages active dashboard WebSocket connections and topic subscriptions."""
    
    def __init__(self) -> None:
        # Maps active WebSocket connections to a set of their subscribed topics
        self.active_connections: Dict[WebSocket, Set[str]] = {}

    async def connect(self, websocket: WebSocket) -> None:
        """Accepts a new connection and initializes an empty subscription set."""
        await websocket.accept()
        self.active_connections[websocket] = set()
        logger.info("New WebSocket dashboard connection established.")

    def disconnect(self, websocket: WebSocket) -> None:
        """Removes a connection from the active pool cleanly."""
        if websocket in self.active_connections:
            del self.active_connections[websocket]
            logger.info("WebSocket dashboard connection removed.")

    async def subscribe(self, websocket: WebSocket, topic: str) -> None:
        """Adds a Kafka topic to the client's subscription list."""
        if websocket in self.active_connections:
            self.active_connections[websocket].add(topic)
            logger.debug("WebSocket subscribed to topic.", extra={"topic": topic})

    async def unsubscribe(self, websocket: WebSocket, topic: str) -> None:
        """Removes a Kafka topic from the client's subscription list."""
        if websocket in self.active_connections and topic in self.active_connections[websocket]:
            self.active_connections[websocket].remove(topic)
            logger.debug("WebSocket unsubscribed from topic.", extra={"topic": topic})

    async def broadcast(self, topic: str, payload: Dict[str, Any]) -> None:
        """Pushes an event payload to all clients subscribed to the topic."""
        
        # print(f"\n--- [LIVE BUS EVENT] Topic: {topic} ---")
        # print(json.dumps(payload, indent=2))
        # print("-" * 40)
        
        # Convert the dictionary payload to a JSON string for transmission
        message = json.dumps({"topic": topic, "data": payload})
        
        stale_connections = []
        
        for websocket, subscriptions in self.active_connections.items():
            if topic in subscriptions:
                try:
                    await websocket.send_text(message)
                except Exception as e:
                    logger.error("Failed to send WebSocket message.", exc_info=True)
                    stale_connections.append(websocket)
                    
        # Cleanup connections that dropped without closing properly
        for stale in stale_connections:
            self.disconnect(stale)

# Global manager instance
ws_manager = WebSocketManager()
```

---

## frontend\src\App.tsx

```tsx
import React from 'react';
import { RouterProvider } from 'react-router-dom';
import { router } from './router';

export default function App() {
  return <RouterProvider router={router} />;
}
```

---

## frontend\src\index.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 224 71% 4%;
    --foreground: 213 31% 91%;

    --muted: 223 47% 11%;
    --muted-foreground: 215.4 16.3% 56.9%;

    --popover: 224 71% 4%;
    --popover-foreground: 215 20.2% 65.1%;

    --card: 222.2 47.4% 11.2%;
    --card-foreground: 213 31% 91%;

    --border: 217 32.6% 16%;
    --input: 217 32.6% 16%;

    --primary: 210 100% 50%;
    --primary-foreground: 210 40% 98%;

    --secondary: 222.2 47.4% 11.2%;
    --secondary-foreground: 210 40% 98%;

    --accent: 216 34% 17%;
    --accent-foreground: 210 40% 98%;

    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;

    --ring: 213 27% 84%;

    --radius: 0.75rem;
  }
}

@layer base {
  * {
    border-color: hsl(var(--border));
  }
  body {
    background-color: hsl(var(--background));
    color: hsl(var(--foreground));
    font-family: 'Outfit', sans-serif;
  }
  code {
    font-family: 'JetBrains Mono', monospace;
  }
}

/* Custom premium UI utilities */
.glass {
  background: rgba(13, 20, 38, 0.45);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.glow-blue {
  box-shadow: 0 0 20px rgba(59, 130, 246, 0.15);
}

.glow-emerald {
  box-shadow: 0 0 20px rgba(16, 185, 129, 0.15);
}
```

---

## frontend\src\main.tsx

```tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

---

## frontend\src\layouts\DashboardLayout.tsx

```tsx
import React, { useState } from "react";
import { Link, Outlet, useLocation } from "react-router-dom";
import {
  Truck,
  BatteryCharging,
  Share2,
  BellRing,
  Leaf,
  Menu,
  X,
  Gauge,
  User,
  SunMoon,
} from "lucide-react";

export default function DashboardLayout() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const location = useLocation();

  const navigation = [
    { name: "Fleet Overview", href: "/", icon: Truck },
    { name: "Battery Analytics", href: "/battery", icon: BatteryCharging },
    { name: "Supply Chain Graph", href: "/supply-chain", icon: Share2 },
    { name: "System Alerts", href: "/alerts", icon: BellRing },
    { name: "Carbon Intelligence", href: "/carbon", icon: Leaf },
  ];

  return (
    <div className="min-h-screen flex bg-background text-foreground font-sans">
      {/* Sidebar Navigation */}
      <aside
        className={`fixed inset-y-0 left-0 z-50 w-64 bg-card border-r border-border transform ${
          sidebarOpen ? "translate-x-0" : "-translate-x-full"
        } lg:translate-x-0 lg:static transition-transform duration-300 ease-in-out flex flex-col justify-between`}
      >
        <div>
          {/* Sidebar Header */}
          <div className="h-16 px-6 border-b border-border flex items-center justify-between">
            <Link
              to="/"
              className="flex items-center gap-2 font-black tracking-wider text-lg uppercase text-blue-500"
            >
              <Gauge className="h-6 w-6" />
              <span>EV AI Platform</span>
            </Link>
            <button
              className="lg:hidden text-muted-foreground hover:text-foreground"
              onClick={() => setSidebarOpen(false)}
            >
              <X className="h-5 w-5" />
            </button>
          </div>

          {/* Navigation Links */}
          <nav className="p-4 space-y-1.5">
            {navigation.map((item) => {
              const active = location.pathname === item.href;
              const Icon = item.icon;
              return (
                <Link
                  key={item.name}
                  to={item.href}
                  onClick={() => setSidebarOpen(false)}
                  className={`flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm font-semibold transition-all ${
                    active
                      ? "bg-blue-500/10 text-blue-400 border-l-2 border-blue-500"
                      : "text-muted-foreground hover:bg-muted/30 hover:text-foreground"
                  }`}
                >
                  <Icon className="h-4.5 w-4.5 shrink-0" />
                  <span>{item.name}</span>
                </Link>
              );
            })}
          </nav>
        </div>

        {/* Sidebar Footer */}
        <div className="p-4 border-t border-border flex items-center justify-between text-xs text-muted-foreground">
          <span>Version 1.0.0-Beta</span>
          <span>© 2026 EV AI Inc.</span>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 overflow-y-auto">
        {/* Top Navbar */}
        <header className="h-16 border-b border-border bg-card/50 backdrop-blur-md sticky top-0 z-40 flex items-center justify-between px-6">
          <div className="flex items-center gap-3">
            <button
              className="lg:hidden text-muted-foreground hover:text-foreground p-1"
              onClick={() => setSidebarOpen(true)}
            >
              <Menu className="h-5 w-5" />
            </button>
            <div className="hidden sm:block text-xs font-semibold text-muted-foreground bg-muted/40 px-2.5 py-1 rounded border border-border">
              Cluster Status:{" "}
              <span className="text-emerald-500">OPERATIONAL</span>
            </div>
          </div>

          <div className="flex items-center gap-4">
            {/* Quick action buttons */}
            <button className="p-2 text-muted-foreground hover:text-foreground hover:bg-muted/50 rounded-lg transition-colors">
              <SunMoon className="h-5 w-5" />
            </button>
            <div className="h-4 w-[1px] bg-border" />
            <div className="flex items-center gap-2.5">
              <div className="h-8 w-8 rounded-lg bg-blue-500/10 border border-blue-500/20 text-blue-500 flex items-center justify-center font-bold text-sm">
                A1
              </div>
              <span className="hidden md:block text-sm font-semibold">
                Hackathon User
              </span>
            </div>
          </div>
        </header>

        {/* Page Inner Container */}
        <main className="p-6 md:p-8 max-w-7xl w-full mx-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
```

---

## frontend\src\pages\Alerts.tsx

```tsx
import React from 'react';
import { AlertCircle, Ban, BellRing, Settings, Info } from 'lucide-react';

export default function Alerts() {
  return (
    <div className="space-y-6 animate-fade-in">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight">Active System Alerts</h1>
          <p className="text-muted-foreground mt-1">Real-time status updates and telemetry anomalies detected on asset networks.</p>
        </div>
        <button className="flex items-center gap-1.5 bg-muted hover:bg-muted/80 text-xs px-3.5 py-2 rounded-lg font-medium border border-border transition-colors">
          <Settings className="h-4 w-4" />
          <span>Config Rules</span>
        </button>
      </div>

      {/* Quick filters */}
      <div className="flex gap-2 text-xs">
        <button className="px-3.5 py-1.5 rounded-full bg-blue-500 text-white font-medium">All Alerts (18)</button>
        <button className="px-3.5 py-1.5 rounded-full bg-muted text-muted-foreground hover:bg-muted/80 font-medium">Critical (4)</button>
        <button className="px-3.5 py-1.5 rounded-full bg-muted text-muted-foreground hover:bg-muted/80 font-medium">Warnings (8)</button>
        <button className="px-3.5 py-1.5 rounded-full bg-muted text-muted-foreground hover:bg-muted/80 font-medium">Resolved (6)</button>
      </div>

      {/* Alert Feed Container */}
      <div className="space-y-3.5">
        {[
          { id: "A-201", type: "Critical", asset: "EV-HD-004", msg: "Voltage delta exceeds 0.2V limit - potential cell imbalance anomaly.", time: "2 mins ago" },
          { id: "A-202", type: "Warning", asset: "EV-HD-002", msg: "Core cell temperature spiked above 42°C during rapid charge sequence.", time: "12 mins ago" },
          { id: "A-203", type: "Critical", asset: "EV-HD-012", msg: "Remaining Useful Life (RUL) regression predictions fell below 10% threshold limit.", time: "1 hour ago" },
          { id: "A-204", type: "Info", asset: "EV-HD-008", msg: "Scheduled filter maintenance completed. Recalibrating health state metrics.", time: "3 hours ago" }
        ].map((alert, i) => (
          <div key={i} className={`glass p-5 rounded-xl border-l-4 flex justify-between items-start gap-4 ${
            alert.type === 'Critical' ? 'border-l-red-500' :
            alert.type === 'Warning' ? 'border-l-yellow-500' :
            'border-l-blue-500'
          }`}>
            <div className="flex gap-3">
              {alert.type === 'Critical' ? (
                <AlertCircle className="h-5 w-5 text-red-500 shrink-0 mt-0.5" />
              ) : alert.type === 'Warning' ? (
                <BellRing className="h-5 w-5 text-yellow-500 shrink-0 mt-0.5" />
              ) : (
                <Info className="h-5 w-5 text-blue-500 shrink-0 mt-0.5" />
              )}
              <div>
                <div className="flex items-center gap-2">
                  <span className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">Asset: <span className="font-mono text-foreground">{alert.asset}</span></span>
                  <span className="h-1 w-1 rounded-full bg-muted-foreground/50" />
                  <span className="text-[11px] text-muted-foreground">{alert.time}</span>
                </div>
                <p className="text-sm font-semibold mt-1.5">{alert.msg}</p>
              </div>
            </div>
            <button className="text-xs text-muted-foreground hover:text-foreground font-semibold px-2 py-1 rounded bg-muted/30 hover:bg-muted/65 transition-colors">
              Mute
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
```

---

## frontend\src\pages\BatteryAnalytics.tsx

```tsx
import React from 'react';
import { BatteryCharging, Flame, Thermometer, ShieldAlert, Cpu } from 'lucide-react';

export default function BatteryAnalytics() {
  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-extrabold tracking-tight">Advanced Battery Intelligence</h1>
        <p className="text-muted-foreground mt-1">Deep analytics on capacity fade, thermal profiles, and degradation predictors.</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Real-time Cell Temp Indicator */}
        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <div className="flex justify-between items-center">
              <h2 className="font-semibold text-lg">Thermal Diagnostics</h2>
              <Thermometer className="h-5 w-5 text-red-400" />
            </div>
            <p className="text-xs text-muted-foreground mt-1">Real-time status of thermal runaways and core gradients.</p>
          </div>
          <div className="my-8 flex justify-center items-center">
            <div className="relative h-32 w-32 rounded-full border-4 border-dashed border-red-500/30 flex flex-col justify-center items-center">
              <span className="text-3xl font-bold">38.4°C</span>
              <span className="text-xs text-red-400 uppercase tracking-wider font-semibold">Healthy Range</span>
            </div>
          </div>
          <div className="space-y-2">
            <div className="flex justify-between text-xs font-semibold text-muted-foreground">
              <span>Upper Threshold Limit</span>
              <span>55.0°C</span>
            </div>
            <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
              <div className="bg-red-500 h-full w-[70%]" />
            </div>
          </div>
        </div>

        {/* Degradation Regression Predictor */}
        <div className="glass p-6 rounded-xl flex flex-col justify-between lg:col-span-2">
          <div>
            <div className="flex justify-between items-center">
              <h2 className="font-semibold text-lg">Capacity Degradation Curve</h2>
              <BatteryCharging className="h-5 w-5 text-emerald-400" />
            </div>
            <p className="text-xs text-muted-foreground mt-1">Calculated capacity fade over consecutive charging/discharging cycles.</p>
          </div>
          <div className="h-44 w-full bg-muted/20 border border-border/50 rounded-lg flex items-center justify-center text-xs text-muted-foreground">
            {/* Chart Placeholder */}
            <div className="flex flex-col items-center gap-1.5">
              <Cpu className="h-8 w-8 text-blue-500/80 animate-pulse" />
              <span>XGBoost degradation curves render here</span>
            </div>
          </div>
          <div className="grid grid-cols-3 gap-4 text-center mt-2">
            <div className="bg-muted/30 p-2 rounded-lg">
              <span className="block text-xs text-muted-foreground">Nominal Cap</span>
              <span className="text-lg font-bold">120 Ah</span>
            </div>
            <div className="bg-muted/30 p-2 rounded-lg">
              <span className="block text-xs text-muted-foreground">Current Cap</span>
              <span className="text-lg font-bold text-emerald-500">114.2 Ah</span>
            </div>
            <div className="bg-muted/30 p-2 rounded-lg">
              <span className="block text-xs text-muted-foreground">SOH State</span>
              <span className="text-lg font-bold text-blue-500">95.1%</span>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Predictive AI Alert Cards */}
        <div className="glass p-6 rounded-xl space-y-4">
          <h2 className="font-semibold text-lg">AI Anomaly Alerts</h2>
          <div className="space-y-3">
            <div className="border-l-4 border-red-500 bg-red-500/5 p-4 rounded-r-lg flex items-start gap-3">
              <ShieldAlert className="h-5 w-5 text-red-500 shrink-0 mt-0.5" />
              <div>
                <h4 className="text-sm font-bold text-red-400">Thermal Runaway Warning (Anomaly Score: 0.98)</h4>
                <p className="text-xs text-muted-foreground mt-0.5">Asset EV-HD-004 showing abnormal discharge slope & cell delta temperature mismatch.</p>
              </div>
            </div>
            <div className="border-l-4 border-yellow-500 bg-yellow-500/5 p-4 rounded-r-lg flex items-start gap-3">
              <ShieldAlert className="h-5 w-5 text-yellow-500 shrink-0 mt-0.5" />
              <div>
                <h4 className="text-sm font-bold text-yellow-400">Micro-short Circuit Indicator</h4>
                <p className="text-xs text-muted-foreground mt-0.5">Asset EV-HD-002 showing slight capacity drop during static charging phase.</p>
              </div>
            </div>
          </div>
        </div>

        {/* SoH Predictor Detail */}
        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <h2 className="font-semibold text-lg">Remaining Useful Life (RUL) Prediction</h2>
            <p className="text-xs text-muted-foreground mt-1">Calculated remaining load cycles before cell capacity dips below 80% (End of Life).</p>
          </div>
          <div className="my-6">
            <div className="text-center">
              <span className="text-4xl font-extrabold text-blue-500">1,120</span>
              <span className="text-sm text-muted-foreground block mt-1">Estimated Remaining Cycles</span>
            </div>
          </div>
          <div className="border-t border-border pt-4 text-xs text-muted-foreground flex justify-between">
            <span>Regression Confidence: 94.2%</span>
            <span>Next inspection: 60 days</span>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## frontend\src\pages\CarbonAnalytics.tsx

```tsx
import React from 'react';
import { Leaf, Award, Compass, Zap, Cpu } from 'lucide-react';

export default function CarbonAnalytics() {
  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-extrabold tracking-tight">Sustainability & Carbon Intelligence</h1>
        <p className="text-muted-foreground mt-1">Scope emissions reporting, electrification metrics, and offset tracking calculations.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Core sustainability cards */}
        <div className="glass p-6 rounded-xl relative overflow-hidden">
          <div className="flex justify-between items-center">
            <span className="text-sm font-semibold text-muted-foreground">CO₂ Savings (YTD)</span>
            <Leaf className="h-5 w-5 text-emerald-400" />
          </div>
          <div className="mt-4">
            <span className="text-3xl font-bold text-emerald-400">142.6 Metric Tons</span>
            <span className="block text-xs text-muted-foreground mt-1.5">Equivalent to planting 5,800 trees</span>
          </div>
        </div>

        <div className="glass p-6 rounded-xl">
          <div className="flex justify-between items-center">
            <span className="text-sm font-semibold text-muted-foreground">Electrification Ratio</span>
            <Zap className="h-5 w-5 text-blue-400" />
          </div>
          <div className="mt-4">
            <span className="text-3xl font-bold text-blue-400">42%</span>
            <span className="block text-xs text-muted-foreground mt-1.5">82 of 195 routes fully converted</span>
          </div>
        </div>

        <div className="glass p-6 rounded-xl">
          <div className="flex justify-between items-center">
            <span className="text-sm font-semibold text-muted-foreground">Readiness Score</span>
            <Award className="h-5 w-5 text-amber-400" />
          </div>
          <div className="mt-4">
            <span className="text-3xl font-bold text-amber-400">84/100</span>
            <span className="block text-xs text-muted-foreground mt-1.5">Based on range suitability & chargers</span>
          </div>
        </div>
      </div>

      {/* Scope analysis section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <h2 className="font-semibold text-lg">Scope-1 & Scope-3 Emission Estimation</h2>
            <p className="text-xs text-muted-foreground mt-1">Calculates diesel displacement emissions relative to charging grid dependencies.</p>
          </div>
          <div className="my-8 h-40 bg-muted/20 border border-border/50 rounded-lg flex items-center justify-center text-xs text-muted-foreground">
            {/* Chart Placeholder */}
            <div className="flex flex-col items-center gap-1.5">
              <Cpu className="h-8 w-8 text-emerald-500/80" />
              <span>Scope emissions tracking graphics render here</span>
            </div>
          </div>
          <div className="border-t border-border pt-4 text-xs text-muted-foreground flex justify-between">
            <span>Grid Emission Factor: 0.32 kg CO₂/kWh</span>
            <span>Last calculated: Today</span>
          </div>
        </div>

        {/* Fleet Route Electrification Roadmap */}
        <div className="glass p-6 rounded-xl space-y-4">
          <h2 className="font-semibold text-lg">Electrification Readiness Scorecard</h2>
          <p className="text-xs text-muted-foreground">Top recommended routes for EV conversion based on distance, payload, and dwell time.</p>
          <div className="space-y-3">
            {[
              { route: "Denver - Boulder Corridor", readiness: "94%", reason: "Excellent charging availability & short route profile" },
              { route: "Houston Local Hub Delivery", readiness: "88%", reason: "Optimized route profile with idle times for dwell charging" },
              { route: "Chicago Regional Logistics", readiness: "54%", reason: "Long hauling requires high-capacity batteries & mega chargers" },
            ].map((route, i) => (
              <div key={i} className="p-3 bg-muted/30 border border-border/50 rounded-lg flex justify-between items-center gap-4">
                <div>
                  <h4 className="text-sm font-bold">{route.route}</h4>
                  <p className="text-[11px] text-muted-foreground mt-0.5">{route.reason}</p>
                </div>
                <span className={`text-sm font-extrabold px-2.5 py-1 rounded-lg ${
                  parseInt(route.readiness) >= 80 ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' :
                  'bg-yellow-500/10 text-yellow-400 border border-yellow-500/20'
                }`}>
                  {route.readiness}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## frontend\src\pages\FleetOverview.tsx

```tsx
import React from 'react';
import { Truck, Battery, AlertTriangle, ShieldCheck, Activity } from 'lucide-react';

export default function FleetOverview() {
  return (
    <div className="space-y-6 animate-fade-in">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight">Fleet Asset Intelligence</h1>
          <p className="text-muted-foreground mt-1">Real-time status, health index, and predictive alerts for industrial EV assets.</p>
        </div>
        <div className="flex items-center gap-2 bg-muted/50 px-3 py-1.5 rounded-lg text-xs font-medium border border-border">
          <Activity className="h-4.5 w-4.5 text-blue-500 animate-pulse" />
          <span>Ingesting: 142 Telemetry msg/sec</span>
        </div>
      </div>

      {/* Metric Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
        <div className="glass p-5 rounded-xl glow-blue">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Active Fleet Assets</span>
            <div className="p-2 bg-blue-500/10 rounded-lg text-blue-500"><Truck className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">124</span>
            <span className="text-xs text-emerald-500 font-medium">96% Active</span>
          </div>
        </div>

        <div className="glass p-5 rounded-xl">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Average SoC</span>
            <div className="p-2 bg-emerald-500/10 rounded-lg text-emerald-500"><Battery className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">78.4%</span>
            <span className="text-xs text-muted-foreground">Healthy Charging</span>
          </div>
        </div>

        <div className="glass p-5 rounded-xl">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Predictive Maintenance Alerts</span>
            <div className="p-2 bg-red-500/10 rounded-lg text-red-500"><AlertTriangle className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">4</span>
            <span className="text-xs text-red-500 font-semibold">Critical Risks</span>
          </div>
        </div>

        <div className="glass p-5 rounded-xl">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Avg Fleet Health Index</span>
            <div className="p-2 bg-emerald-500/10 rounded-lg text-emerald-500"><ShieldCheck className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">92.8%</span>
            <span className="text-xs text-emerald-500 font-medium">+1.2% this week</span>
          </div>
        </div>
      </div>

      {/* Detailed Live Fleet Table */}
      <div className="glass rounded-xl overflow-hidden">
        <div className="px-6 py-5 border-b border-border">
          <h2 className="text-lg font-semibold">Real-Time Vehicle Assets status</h2>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-border bg-muted/30 text-xs uppercase tracking-wider text-muted-foreground">
                <th className="px-6 py-4">Asset ID</th>
                <th className="px-6 py-4">Status</th>
                <th className="px-6 py-4">Battery SoC</th>
                <th className="px-6 py-4">Avg Cell Temp</th>
                <th className="px-6 py-4">State of Health (SoH)</th>
                <th className="px-6 py-4">Remaining Useful Life (RUL)</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border text-sm">
              {[
                { id: "EV-HD-001", status: "Active", soc: "88%", temp: "34.5°C", soh: "96%", rul: "1,240 cycles" },
                { id: "EV-HD-002", status: "Charging", soc: "42%", temp: "38.2°C", soh: "91%", rul: "890 cycles" },
                { id: "EV-HD-003", status: "Active", soc: "91%", temp: "33.1°C", soh: "98%", rul: "1,450 cycles" },
                { id: "EV-HD-004", status: "Warning", soc: "76%", temp: "44.8°C", soh: "83%", rul: "430 cycles" },
              ].map((row, i) => (
                <tr key={i} className="hover:bg-muted/10 transition-colors">
                  <td className="px-6 py-4 font-mono font-medium">{row.id}</td>
                  <td className="px-6 py-4">
                    <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-semibold ${
                      row.status === 'Active' ? 'bg-emerald-500/10 text-emerald-500' :
                      row.status === 'Charging' ? 'bg-blue-500/10 text-blue-500' :
                      'bg-red-500/10 text-red-500'
                    }`}>
                      {row.status}
                    </span>
                  </td>
                  <td className="px-6 py-4">{row.soc}</td>
                  <td className="px-6 py-4">{row.temp}</td>
                  <td className="px-6 py-4">{row.soh}</td>
                  <td className="px-6 py-4">{row.rul}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
```

---

## frontend\src\pages\SupplyChain.tsx

```tsx
import React from 'react';
import { Share2, AlertOctagon, TrendingUp, ShieldAlert, Cpu } from 'lucide-react';

export default function SupplyChain() {
  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-extrabold tracking-tight">Graph-Based Supply Chain Intelligence</h1>
        <p className="text-muted-foreground mt-1">Multi-tier battery material dependencies, supplier risk assessments, and vulnerability tracking.</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Neo4j dependency traversal layout */}
        <div className="glass p-6 rounded-xl lg:col-span-2 flex flex-col justify-between">
          <div>
            <div className="flex justify-between items-center">
              <h2 className="font-semibold text-lg">Multi-Tier Dependency Graph Explorer</h2>
              <Share2 className="h-5 w-5 text-blue-500" />
            </div>
            <p className="text-xs text-muted-foreground mt-1">Neo4j graph representation traversing Mine ➔ Refiner ➔ Battery Plant ➔ Fleet Assembly.</p>
          </div>

          <div className="my-6 h-64 bg-muted/20 border border-border/50 rounded-lg relative overflow-hidden flex items-center justify-center">
            {/* Interactive Graph Node mockups */}
            <div className="absolute top-10 left-10 p-3 glass rounded-lg text-xs flex flex-col items-center">
              <span className="font-bold text-blue-400">Mine</span>
              <span className="text-[10px] text-muted-foreground">Salar de Atacama</span>
            </div>
            <div className="absolute top-36 left-40 p-3 glass rounded-lg text-xs flex flex-col items-center">
              <span className="font-bold text-purple-400">Refinery</span>
              <span className="text-[10px] text-muted-foreground">Tianqi Lithium</span>
            </div>
            <div className="absolute top-12 right-28 p-3 glass rounded-lg text-xs flex flex-col items-center border-amber-500/50">
              <span className="font-bold text-amber-400">Cell Plant</span>
              <span className="text-[10px] text-muted-foreground">CATL Yibin</span>
            </div>
            <div className="absolute top-44 right-10 p-3 glass rounded-lg text-xs flex flex-col items-center">
              <span className="font-bold text-emerald-400">EV Fleet</span>
              <span className="text-[10px] text-muted-foreground">Denver Hub</span>
            </div>

            {/* Connecting SVG lines */}
            <svg className="absolute inset-0 h-full w-full pointer-events-none" xmlns="http://www.w3.org/2000/svg">
              <path d="M 120 70 L 190 145" stroke="rgba(255,255,255,0.15)" strokeWidth="2" strokeDasharray="4" />
              <path d="M 230 160 L 320 80" stroke="rgba(255,255,255,0.15)" strokeWidth="2" strokeDasharray="4" />
              <path d="M 370 80 L 420 170" stroke="rgba(255,255,255,0.15)" strokeWidth="2" strokeDasharray="4" />
            </svg>

            <span className="text-xs text-muted-foreground z-10 bg-background/80 px-2 py-1 rounded">Interactive Cypher queries mapping...</span>
          </div>

          <div className="flex gap-4 text-xs">
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-blue-500" /> Mines</span>
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-purple-500" /> Refiners</span>
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-amber-500" /> Cell Plants</span>
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-emerald-500" /> Fleets</span>
          </div>
        </div>

        {/* Risk Scores Engine */}
        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <h2 className="font-semibold text-lg">Supply Chain Risk Scoring</h2>
            <p className="text-xs text-muted-foreground mt-1">Calculated from supplier concentration, shipping bottle-necks, and geopolitics.</p>
          </div>

          <div className="space-y-4 my-6">
            <div className="space-y-1">
              <div className="flex justify-between text-xs font-semibold">
                <span>Concentration Index</span>
                <span className="text-red-400">High Risk (86/100)</span>
              </div>
              <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
                <div className="bg-red-500 h-full w-[86%]" />
              </div>
            </div>

            <div className="space-y-1">
              <div className="flex justify-between text-xs font-semibold">
                <span>Geopolitical Instability</span>
                <span className="text-yellow-400">Medium Risk (54/100)</span>
              </div>
              <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
                <div className="bg-yellow-500 h-full w-[54%]" />
              </div>
            </div>

            <div className="space-y-1">
              <div className="flex justify-between text-xs font-semibold">
                <span>Shipping Botlenecks</span>
                <span className="text-emerald-400">Low Risk (28/100)</span>
              </div>
              <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
                <div className="bg-emerald-500 h-full w-[28%]" />
              </div>
            </div>
          </div>

          <div className="bg-red-500/5 border border-red-500/20 p-3 rounded-lg flex items-start gap-2.5">
            <AlertOctagon className="h-4.5 w-4.5 text-red-400 shrink-0 mt-0.5" />
            <p className="text-[11px] text-red-300">
              <strong>Dependency Alert:</strong> 85% of Active Cells originate from single-tier refiner. Interruption propagates to Denver Hub assembly within 12 days.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## frontend\src\router\index.tsx

```tsx
import React from 'react';
import { createBrowserRouter } from 'react-router-dom';
import DashboardLayout from '../layouts/DashboardLayout';
import FleetOverview from '../pages/FleetOverview';
import BatteryAnalytics from '../pages/BatteryAnalytics';
import SupplyChain from '../pages/SupplyChain';
import Alerts from '../pages/Alerts';
import CarbonAnalytics from '../pages/CarbonAnalytics';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <DashboardLayout />,
    children: [
      {
        index: true,
        element: <FleetOverview />,
      },
      {
        path: 'battery',
        element: <BatteryAnalytics />,
      },
      {
        path: 'supply-chain',
        element: <SupplyChain />,
      },
      {
        path: 'alerts',
        element: <Alerts />,
      },
      {
        path: 'carbon',
        element: <CarbonAnalytics />,
      },
    ],
  },
]);
```

---

## infrastructure\kafka\mqtt_kafka_bridge.py

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

# Configure logging from env var or default to INFO
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("mqtt_kafka_bridge")

# Configurations from environment variables
MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "ev/#")  

KAFKA_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

# ENTERPRISE ROUTING MAP: Mirroring the domain-split bus design
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
    """Callback when connected to MQTT Broker."""
    logger.info(f"Connected to Mosquitto Broker at {MQTT_HOST}:{MQTT_PORT}")
    client.subscribe(MQTT_TOPIC)
    logger.info(f"Subscribed to MQTT Topic: {MQTT_TOPIC}")

def on_message(client, userdata, msg):
    """Callback when a message is received from MQTT Broker."""
    global producer
    try:
        payload = msg.payload.decode("utf-8")
        logger.debug(f"Received MQTT payload on topic {msg.topic}")

        # Verify JSON validity
        data = json.loads(payload)

        # Enrich data with source MQTT topic trace tag
        data["mqtt_source_topic"] = msg.topic

        # DYNAMIC ROUTING FIX: Map the incoming MQTT topic directly to the target domain stream
        target_kafka_topic = MQTT_TO_KAFKA_ROUTE.get(msg.topic, "ev.unknown")

        if target_kafka_topic == "ev.unknown":
            logger.warning(f"Unmapped MQTT topic received ({msg.topic}). Skipping bridge routing.")
            return

        # Forward dynamically to its explicit Kafka domain channel line
        if producer:
            future = producer.send(target_kafka_topic, value=data)
            # block for a maximum of 10 seconds to confirm send
            record_metadata = future.get(timeout=10)
            logger.debug(f"Forwarded to Kafka stream '{record_metadata.topic}' | Partition [{record_metadata.partition}] | Offset {record_metadata.offset}")
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

## infrastructure\mosquitto\mosquitto.conf

```
listener 1883
allow_anonymous true

listener 9001
protocol websockets
allow_anonymous true

# Logging configuration to reduce spam
log_dest stdout
log_type error
log_type warning
```

---

## infrastructure\neo4j\init_db.py

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

## infrastructure\neo4j\init_graph.cypher

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

## infrastructure\timescaledb\init.sql

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

## infrastructure\kafka\consumers\db_writer.py

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

## infrastructure\kafka\consumers\telemetry_consumer.py

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
    
    # SYSTEM UPGRADE: Listen to all segmented domain topics starting with 'ev.'
    # Instead of 'telemetry.raw', we match 'ev.telemetry', 'ev.battery', etc.
    topic_pattern = "ev\..*"

    print(f"Connecting to Kafka topics matching pattern '{topic_pattern}' at {bootstrap_servers}...")

    consumer = None
    retries = 5
    while retries > 0:
        try:
            # Note: We do NOT pass the positional topic argument here because 
            # we are using consumer.subscribe(pattern=...) instead.
            consumer = KafkaConsumer(
                bootstrap_servers=bootstrap_servers,
                auto_offset_reset='latest',
                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                group_id="infrastructure_telemetry_debug_group"
            )
            
            # Dynamically subscribe to the regex channel configuration
            consumer.subscribe(pattern=topic_pattern)
            print("Successfully connected to Kafka and subscribed to Domain Streams!")
            break
        except Exception as e:
            retries -= 1
            print(f"Kafka not ready, retrying in 5 seconds... ({retries} attempts left). Error: {e}")
            time.sleep(5)

    if not consumer:
        print("Failed to connect to Kafka. Exiting.")
        return

    print("Waiting for messages from segmented streams...\n")
    for message in consumer:
        data = message.value
        # Enhanced output to display exactly which domain channel this payload arrived on
        print(f"─── [BUS EVENT] Received on Topic: {message.topic} ───")
        print(json.dumps(data, indent=2))
        print("─" * 50 + "\n")

if __name__ == "__main__":
    run_consumer()
```

---

## ml\notebooks\README.md

```markdown
# AI/ML Engineering Notebooks

This folder is designated for exploratory data analysis (EDA), statistical tests, and machine learning model training notebooks (Member 3).

## Recommended Notebook Workflow

### 1. `01_exploratory_data_analysis.ipynb`
- Load and parse datasets: NASA Battery Dataset, Oxford Battery Dataset, NASA C-MAPSS.
- Telemetry profiling: Voltage, Current, Temperature, Capacity Fade, Cycle Count.
- Target derivation: Calculate remaining load cycles before cell capacity hits the 80% degradation threshold.

### 2. `02_model_training_and_evaluation.ipynb`
- Train XGBoost models for Remaining Useful Life (RUL) regression predictions.
- Train Isolation Forest models for real-time anomaly alerts (detecting thermal risks, cell voltage disparities, abnormal charging curves).
- Export trained model weights to production assets (`ml/models/`).
```

---

## ml\simulator\simulator.py

```python
# import time
# import json
# import random
# import argparse
# from datetime import datetime,timezone
# import numpy as np

# try:
#     import paho.mqtt.client as mqtt
# except ImportError:
#     print("Warning: paho-mqtt not installed. Run 'pip install paho-mqtt'")
#     mqtt = None

# VEHICLE_IDS = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]

# class TelemetrySimulator:
#     def __init__(self, broker_address="localhost", broker_port=1883):
#         self.broker = broker_address
#         self.port = broker_port
#         self.client = None

#         # State profiles for vehicles: nominal capacity, current soc, temperature, cycle counts
#         self.states = {
#             vid: {
#                 "soc": random.uniform(50, 95),
#                 "temperature": random.uniform(28, 35),
#                 "voltage": 400.0,
#                 "cycles": random.randint(100, 500),
#                 "degradation_factor": random.uniform(0.01, 0.05)
#             } for vid in VEHICLE_IDS
#         }

#     def connect(self):
#         if mqtt is None:
#             print("Simulator starting in dry-run mode (MQTT packages missing).")
#             return False

#         self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2 if hasattr(mqtt, 'CallbackAPIVersion') else None)
#         try:
#             self.client.connect(self.broker, self.port, 60)
#             print(f"Connected to Mosquitto MQTT Broker at {self.broker}:{self.port}")
#             self.client.loop_start()
#             return True
#         except Exception as e:
#             print(f"Failed to connect to MQTT broker: {e}. Defaulting to terminal log.")
#             self.client = None
#             return False

#     def simulate_step(self):
#         for vid in VEHICLE_IDS:
#             state = self.states[vid]

#             # --- Simulated Physics Engine Logic ---
#             is_charging = vid == "EV-HD-002"

#             if is_charging:
#                 state["soc"] = min(100.0, state["soc"] + random.uniform(0.1, 0.4))
#                 current = random.uniform(-60.0, -20.0)  # negative represents charge
#                 voltage = 380 + (state["soc"] * 0.3)
#                 state["temperature"] = min(50.0, state["temperature"] + random.uniform(-0.1, 0.3))
#                 speed = 0.0
#                 motor_rpm = 0
#                 power_output = round(float(voltage * current / 1000.0), 2)  # negative power during charge
#             else:
#                 state["soc"] = max(10.0, state["soc"] - random.uniform(0.05, 0.2))
#                 current = random.uniform(10.0, 45.0)  # positive represents discharge
#                 voltage = 400 - ((100 - state["soc"]) * 0.3)
#                 state["temperature"] = max(25.0, state["temperature"] + random.uniform(-0.2, 0.2))
#                 speed = round(random.uniform(40.0, 90.0), 2)
#                 motor_rpm = int(speed * 50 + random.uniform(-100, 100))
#                 power_output = round(float(voltage * current / 1000.0), 2)

#             if vid == "EV-HD-004" and random.random() < 0.15:
#                 state["temperature"] += random.uniform(2.0, 5.0)
#                 print(f"[ANOMALY WARNING] Simulated thermal runaway surge on {vid}")

#             state["cycles"] += int(random.random() < 0.01)

#             # ISO-8601 UTC timestamp format compliance string
#             timestamp_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

#             # --- Contract Payload 1: General EV Telemetry (Topic: ev/telemetry) ---
#             telemetry_payload = {
#                 "vehicle_id": vid,
#                 "timestamp": timestamp_str,
#                 "speed": speed,
#                 "odometer": round(15000.0 + (state["cycles"] * 2.5), 2),
#                 "motor_rpm": motor_rpm,
#                 "power_output": power_output,
#                 "ambient_temperature": round(random.uniform(20.0, 30.0), 1)
#             }

#             # --- Contract Payload 2: Battery Telemetry (Topic: ev/battery) ---
#             battery_payload = {
#                 "vehicle_id": vid,
#                 "timestamp": timestamp_str,
#                 "soc": round(float(state["soc"]), 1),
#                 "soh": round(100.0 - (state["cycles"] * 0.015), 2),  # Degrades gradually over cycles
#                 "voltage": round(float(voltage), 2),
#                 "current": round(float(current), 2),
#                 "capacity": 75.0,  # Nominal capacity in kWh
#                 "cycle_count": state["cycles"],
#                 "internal_resistance": round(0.01 + (state["cycles"] * 0.00005), 5),
#                 "cell_temperature": round(float(state["temperature"]), 2)
#             }

#             # --- Publishing Engine Block ---
#             if self.client:
#                 # Direct match to specifications using flat base paths
#                 self.client.publish("ev/telemetry", json.dumps(telemetry_payload), qos=1)
#                 self.client.publish("ev/battery", json.dumps(battery_payload), qos=1)
#             else:
#                 print(f"[SIMULATED STREAM] TOPIC: ev/telemetry | DATA: {telemetry_payload}")
#                 print(f"[SIMULATED STREAM] TOPIC: ev/battery | DATA: {battery_payload}")

#     def run(self, interval=1.0):
#         print("Starting EV Telemetry Simulation loop. Press Ctrl+C to terminate.")
#         try:
#             while True:
#                 self.simulate_step()
#                 time.sleep(interval)
#         except KeyboardInterrupt:
#             print("Simulation terminated.")
#             if self.client:
#                 self.client.loop_stop()
#                 self.client.disconnect()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="EV Battery Telemetry Simulator")
#     parser.add_argument("--host", default="localhost", help="MQTT Broker host")
#     parser.add_argument("--port", type=int, default=1883, help="MQTT Broker port")
#     parser.add_argument("--interval", type=float, default=1.0, help="Stream tick interval in seconds")
#     args = parser.parse_args()

#     sim = TelemetrySimulator(args.host, args.port)
#     sim.connect()
#     sim.run(args.interval)


import time
import json
import random
import argparse
import logging
import os
from datetime import datetime, timezone

# Configure logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("simulator")

try:
    import paho.mqtt.client as mqtt
except ImportError:
    logger.warning("paho-mqtt not installed. Run 'pip install paho-mqtt'")
    mqtt = None

VEHICLE_IDS = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]

class TelemetrySimulator:
    def __init__(self, broker_address="localhost", broker_port=1883):
        self.broker = broker_address
        self.port = broker_port
        self.client = None

        # Tracking state vectors for physics modeling
        self.states = {
            vid: {
                "soc": random.uniform(50, 95),
                "temperature": random.uniform(28, 35),
                "voltage": 400.0,
                "cycles": random.randint(100, 500),
                # GPS path initial tracking coordinates (Thiruporur region)
                "lat": 12.7040 + random.uniform(-0.01, 0.01),
                "lon": 80.1930 + random.uniform(-0.01, 0.01),
                "odometer": random.uniform(12000.0, 25000.0),
                "uptime": 0
            } for vid in VEHICLE_IDS
        }

    def connect(self):
        if mqtt is None:
            logger.warning("Simulator starting in dry-run mode (MQTT packages missing).")
            return False

        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2 if hasattr(mqtt, 'CallbackAPIVersion') else None)
        try:
            self.client.connect(self.broker, self.port, 60)
            logger.info(f"Connected to Mosquitto MQTT Broker at {self.broker}:{self.port}")
            self.client.loop_start()
            return True
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}. Defaulting to terminal log.")
            self.client = None
            return False

    def simulate_step(self):
        for vid in VEHICLE_IDS:
            state = self.states[vid]
            state["uptime"] += 1
            timestamp_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            
            # --- Simulated Physics Calculation Tier ---
            is_charging = (vid == "EV-HD-002")
            
            if is_charging:
                state["soc"] = min(100.0, state["soc"] + random.uniform(0.1, 0.4))
                current_amps = random.uniform(-60.0, -20.0)  # Negative denotes absorption
                voltage = 380 + (state["soc"] * 0.3)
                state["temperature"] = min(50.0, state["temperature"] + random.uniform(-0.1, 0.3))
                speed_kph = 0.0
                torque_nm = 0.0
                inverter_efficiency = 0.98
            else:
                state["soc"] = max(10.0, state["soc"] - random.uniform(0.05, 0.2))
                current_amps = random.uniform(10.0, 45.0)   # Positive denotes discharge
                voltage = 400 - ((100 - state["soc"]) * 0.3)
                state["temperature"] = max(25.0, state["temperature"] + random.uniform(-0.2, 0.2))
                speed_kph = round(random.uniform(40.0, 90.0), 2)
                torque_nm = round(random.uniform(120.0, 350.0), 1)
                inverter_efficiency = round(random.uniform(0.91, 0.96), 3)
                # Increment continuous spatial tracking attributes
                state["odometer"] += (speed_kph / 3600.0)
                state["lat"] += random.uniform(-0.0001, 0.0001)
                state["lon"] += random.uniform(-0.0001, 0.0001)

            # Simulated Thermal Anomaly Spike Injector
            if vid == "EV-HD-004" and random.random() < 0.10:
                state["temperature"] += random.uniform(5.0, 12.0)
                logger.warning(f"Thermal boundary breakdown simulation on {vid}")

            # 1. Kinematics Stream (`ev/telemetry`)
            telemetry_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "speed_kph": speed_kph,
                "odometer_km": round(state["odometer"], 2),
                "motor_temperature_c": round(state["temperature"] * 1.1, 1),
                "torque_nm": torque_nm,
                "inverter_efficiency": inverter_efficiency
            }

            # 2. Electro-Chemical Stream (`ev/battery`)
            battery_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "state_of_charge_pct": round(float(state["soc"]), 1),
                "state_of_health_pct": round(98.5 - (state["uptime"] * 0.0001), 2),
                "voltage": round(float(voltage), 2),
                "current_amps": round(float(current_amps), 2),
                "cell_temperature_max_c": round(float(state["temperature"]), 2),
                "internal_resistance_ohm": round(0.012 + (state["uptime"] * 0.000001), 6)
            }

            # 3. Geospatial Stream (`ev/location`)
            location_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "latitude": round(state["lat"], 6),
                "longitude": round(state["lon"], 6),
                "altitude_m": 24.5,
                "heading_deg": random.randint(0, 359),
                "gps_fix_quality": "3D_FIX"
            }

            # 4. Energy Grid Coupling Stream (`ev/charging`)
            charging_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "charger_id": "CHG-TPI-99" if is_charging else None,
                "charging_rate_kw": round(abs(voltage * current_amps) / 1000.0, 2) if is_charging else 0.0,
                "time_to_full_mins": int((100.0 - state["soc"]) * 1.5) if is_charging else 0,
                "connector_type": "CCS_TYPE_2" if is_charging else "NONE"
            }

            # 5. Core Operational Status Stream (`ev/status`)
            status_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "operational_status": "CHARGING" if is_charging else "ACTIVE_DRIVE",
                "active_error_codes": ["ERR_CELL_OVERTEMP"] if state["temperature"] > 48.0 else [],
                "driver_id": f"DRV-{vid[-3:]}"
            }

            # 6. High-Priority Alert Engine (`ev/alerts`)
            alert_payload = None
            if state["temperature"] > 48.0:
                alert_payload = {
                    "vehicle_id": vid,
                    "timestamp": timestamp_str,
                    "alert_code": "ALT_THERMAL_CRITICAL",
                    "severity": "CRITICAL",
                    "component": "BATTERY_PACK_A",
                    "description": f"Core cell temperature hit critical boundary limit: {round(state['temperature'], 2)}C"
                }

            # 7. Diagnostic Diagnostics Base (`ev/heartbeat`)
            heartbeat_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "uptime_seconds": state["uptime"],
                "firmware_version": "v2.4.11-prod",
                "signal_strength_dbm": random.randint(-75, -45)
            }

            # --- Unified Non-Blocking Network Pipeline Transmission ---
            if self.client:
                self.client.publish("ev/telemetry", json.dumps(telemetry_payload), qos=1)
                self.client.publish("ev/battery", json.dumps(battery_payload), qos=1)
                self.client.publish("ev/location", json.dumps(location_payload), qos=1)
                self.client.publish("ev/charging", json.dumps(charging_payload), qos=1)
                self.client.publish("ev/status", json.dumps(status_payload), qos=1)
                self.client.publish("ev/heartbeat", json.dumps(heartbeat_payload), qos=1)
                if alert_payload:
                    self.client.publish("ev/alerts", json.dumps(alert_payload), qos=1)
            else:
                logger.debug(f"[DRY-RUN LOG] Emitting 7 contract streams for {vid}")

    def run(self, interval=1.0):
        logger.info("Starting 7-Channel Enterprise EV Telemetry Simulation loop. Press Ctrl+C to terminate.")
        try:
            while True:
                self.simulate_step()
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("Simulation terminated.")
            if self.client:
                self.client.loop_stop()
                self.client.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enterprise EV Telemetry Multi-Stream Simulator")
    parser.add_argument("--host", default="localhost", help="MQTT Broker host")
    parser.add_argument("--port", type=int, default=1883, help="MQTT Broker port")
    parser.add_argument("--interval", type=float, default=1.0, help="Stream tick interval in seconds")
    args = parser.parse_args()

    sim = TelemetrySimulator(args.host, args.port)
    sim.connect()
    sim.run(args.interval)
```

---

## ml\src\preprocessing.py

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class TelemetryPreprocessor:
    def __init__(self):
        self.scaler = MinMaxScaler()
        
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handles null values in timeseries telemetry columns via forward/backward fill."""
        fill_cols = ["voltage", "current", "temperature", "soc"]
        df[fill_cols] = df[fill_cols].ffill().bfill()
        return df

    def filter_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Removes physical impossibilities or noise outliers from sensor readings."""
        # E.g., voltage must be positive, temperatures below extreme limits
        df = df[(df["voltage"] > 0) & (df["voltage"] < 1000)]
        df = df[(df["temperature"] > -40) & (df["temperature"] < 150)]
        return df

    def engineer_battery_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Engineers critical battery health predictors:
        - Capacity degradation
        - Thermal variance (rolling cell temp delta)
        - Average discharge slope (dV/dt)
        - Charging efficiency (energy absorbed per cycle)
        """
        # Ensure chronological ordering
        df = df.sort_values("timestamp")
        
        # 1. Thermal Variance
        df["temp_rolling_var"] = df["temperature"].rolling(window=10, min_periods=1).var()
        
        # 2. Discharge Slope (dV/dt)
        df["time_diff_sec"] = df["timestamp"].diff().dt.total_seconds()
        df["voltage_diff"] = df["voltage"].diff()
        
        # Calculate dV/dt, replacing division-by-zero with zero
        df["discharge_slope"] = np.where(
            df["time_diff_sec"] > 0, 
            df["voltage_diff"] / df["time_diff_sec"], 
            0.0
        )
        
        # 3. Capacity Fade approximation (Ah depletion integration)
        # Ah = current * time_hours
        df["current_hours"] = (df["current"] * (df["time_diff_sec"] / 3600.0)).abs()
        df["capacity_fade"] = df["current_hours"].cumsum()
        
        return df

    def scale_features(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """Scales numeric telemetry features for deep learning/regression models."""
        df[columns] = self.scaler.fit_transform(df[columns])
        return df
```
