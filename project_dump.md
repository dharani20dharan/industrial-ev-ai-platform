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
│   │   │   ├── ml.py
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
│   ├── migrate.py
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
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.js
│   ├── src
│   │   ├── App.tsx
│   │   ├── hooks
│   │   │   └── useFleetData.ts
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
│   ├── .gitignore
│   ├── 5.+Battery+Data+Set
│   │   ├── 5. Battery Data Set
│   │   │   ├── 1. BatteryAgingARC-FY08Q4.zip
│   │   │   ├── 2. BatteryAgingARC_25_26_27_28_P1.zip
│   │   │   ├── 3. BatteryAgingARC_25-44.zip
│   │   │   ├── 4. BatteryAgingARC_45_46_47_48.zip
│   │   │   ├── 5. BatteryAgingARC_49_50_51_52.zip
│   │   │   └── 6. BatteryAgingARC_53_54_55_56.zip
│   │   └── extracted_1
│   │       ├── B0005.mat
│   │       ├── B0006.mat
│   │       ├── B0007.mat
│   │       ├── B0018.mat
│   │       └── README.txt
│   ├── engines
│   │   ├── __init__.py
│   │   ├── anomaly_detector.py
│   │   ├── battery_predictor.py
│   │   ├── carbon_engine.py
│   │   ├── maintenance_engine.py
│   │   ├── readiness_scorer.py
│   │   └── risk_scorer.py
│   ├── models
│   │   ├── anomaly_detector.joblib
│   │   ├── anomaly_metadata.json
│   │   ├── anomaly_scaler.joblib
│   │   ├── battery_predictor_metadata.json
│   │   ├── rul_model.joblib
│   │   ├── rul_scaler.joblib
│   │   ├── soh_model.joblib
│   │   └── soh_scaler.joblib
│   ├── preprocessing
│   │   ├── __init__.py
│   │   ├── ingest_raw_datasets.py
│   │   └── pipeline.py
│   ├── README.md
│   ├── requirements.txt
│   ├── run_all.py
│   └── simulator
│       └── ev_telemetry_simulator.py
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

# Raw downloaded datasets & zip/tarballs
ml/5.+Battery+Data+Set/
*.mat
*.zip
*.tar.gz
*.tgz
*.rar

# Guideline PDFs and Word Docs (Internal Hackathon assets)
*.pdf
*.docx
*.doc
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

* Continuous state transmission (Voltage, Current, State of Charge, Core temperature) via **MQTT**.
* Buffered event ingestion using **Apache Kafka** partitioned topic distributions.
* Timeseries persistence leveraging **TimescaleDB** hypertables with dynamic temporal indexing and range-partition optimizations.

### 2. Battery & Predictive Maintenance Intelligence

* **State of Health (SoH) Analytics:** Tracks capacity fade using cumulative discharge integration (Ah depletion curves).
* **Remaining Useful Life (RUL) Forecasting:** Predicts cycles remaining until battery capacity falls below the 80% degradation threshold using **XGBoost regression**.
* **Anomaly Diagnostics:** Identifies thermal runaways and cell-level voltage imbalances using unsupervised **Isolation Forest models**.

### 3. Supply Chain Graph Analytics

* Maps multi-tier mineral dependencies (Mine ➔ Refiner ➔ Battery Plant ➔ Assembly Pack ➔ Fleet Vehicle) using **Neo4j Graph Database**.
* Propagates cascading risks (geopolitical instability, shipping bottlenecks, and material shortage) along supply chains utilizing optimized Cypher graph traversal algorithms.

### 4. Carbon & Electrification Analytics

* Displaces direct Scope-1 combustion emissions vs Scope-3 charging grid emissions (based on local carbon intensity coefficients).
* Calculates EV conversion suitability scores for internal combustion engine (ICE) routes based on payload, travel distances, charging station density, and depot dwell times.

---

## 🛠️ Tech Stack Alignment

| Layer | Technologies | Key Functionality |
| --- | --- | --- |
| **Frontend UI** | React 18, TypeScript, TailwindCSS, ShadCN UI, Recharts, React-Leaflet (v4) | Control dashboard views, responsive metrics widgets, live WebSocket visualization, dark-mesh maps |
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
│   ├── components.json             # ShadCN UI components config
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

## 🚀 Environment Launch Instructions

### 1. Infrastructure Setup

Spin up the local containerized databases, brokers, and event pipelines:

```bash
docker-compose up -d

```

*(Optional: Verify Kafka topics are created by checking the setup logs: `docker logs -f kafka_setup`)*

### 2. Initialize TimescaleDB Hypertables

From the backend directory, provision your IoT tracking schemas:

```bash
cd backend
python -m app.db.init_timescale

```

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

### 5. Running the End-to-End Pipeline

Open three separate terminal windows, activate your virtual environment, and execute these components in order to see telemetry route in real-time:

* **Terminal 1 (Destination Database Engine):** `python infrastructure/kafka/consumers/db_writer.py`
* **Terminal 2 (MQTT-to-Kafka Stream Router):** `python infrastructure/kafka/mqtt_kafka_bridge.py`
* **Terminal 3 (Synthetic Sensor Stream Simulator):** `python ml/simulator/simulator.py`

---

## 🖥️ What to Expect: Frontend Live Experience

Once your environment is completely launched and the backend simulators are broadcasting data, the frontend application provides a high-fidelity workspace:

### 📊 Real-Time Telemetry Performance Counters

* **Ingestion Metrics:** The upper banner displays a live processing widget displaying real-time text such as `Ingesting: 4 Telemetry msg/sec`. This guarantees the active telemetry pipeline is communicating correctly.
* **Synchronized States:** The **Active Assets**, **Average SoC**, and **Health Index** panels update instantly as new frames land from the network thread.

### 🗺️ Live Dark-Mesh Geospatial Telemetry Map

* **Automatic Viewport Centering:** The integrated map dynamically handles multi-vehicle tracking bounds via an automated map bounding-box algorithm (`MapUpdater`). It automatically centers and pans around your live active vehicles.
* **Interactive Layer Markers:** Map markers override default legacy graphics with modern glowing DOM circles containing animated custom ping rings indicating live connectivity.
* **Dynamic Status Coloring:** Healthy nodes render in **Emerald Green**, while any asset suffering structural anomalies (e.g., motor temperatures crossing over `40.0°C`) automatically updates its state inside the state engine, instantly rendering as a **Blinking Red Alert Marker** on the canvas. Clicking any marker reveals an analytical diagnostic pop-up block.

### 📋 Fleet Telemetry Data Grid

* The main interface features an exhaustive asset grid logging **Speed**, **Exact Location Coordinates**, **Motor Temperatures**, and **Torque Loads**.
* Columns update dynamically without interface stuttering or full-page rendering cycles, featuring colored indicators mapping back to warning flags.

```
```

---

## backend\migrate.py

```python
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from app.core.config import settings

async def run_migration():
    engine = create_async_engine(settings.database_url, echo=True)
    async with engine.begin() as conn:
        try:
            await conn.execute(text("ALTER TABLE battery_records ADD COLUMN IF NOT EXISTS cycle_count INTEGER DEFAULT 100;"))
            print("Successfully added cycle_count column to battery_records table.")
        except Exception as e:
            print(f"Error during migration: {e}")
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(run_migration())
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
python-dateutil>=2.8.2
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

## frontend\package-lock.json

```json
{
  "name": "ev-industrial-platform-frontend",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "ev-industrial-platform-frontend",
      "version": "1.0.0",
      "dependencies": {
        "clsx": "^2.0.0",
        "leaflet": "^1.9.4",
        "lucide-react": "^0.292.0",
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "react-leaflet": "^4.2.1",
        "react-router-dom": "^6.18.0",
        "recharts": "^2.15.4",
        "tailwind-merge": "^2.0.0"
      },
      "devDependencies": {
        "@types/leaflet": "^1.9.12",
        "@types/react": "^18.2.37",
        "@types/react-dom": "^18.2.15",
        "@vitejs/plugin-react": "^4.2.0",
        "autoprefixer": "^10.4.16",
        "postcss": "^8.4.31",
        "tailwindcss": "^3.3.5",
        "typescript": "^5.2.2",
        "vite": "^5.0.0"
      }
    },
    "node_modules/@alloc/quick-lru": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
      "integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.7.tgz",
      "integrity": "sha512-Aup7aUOfpbAUg2ROOJN6Iw5f9DMBlzu0mIkm/malLQFN/YQgO48wCj0Kxa3sEHJvPVFg7siR+qRInwXd2qhQKw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.29.7",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.7.tgz",
      "integrity": "sha512-locTkQyKvwIEgBzVrn8693ebc97F2U8ZHjbXwDXJ5Fn2TCpNwTlKcaKLkdHop5c/icOFE7qt7Q9JC5hnKNa6Gg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.29.7.tgz",
      "integrity": "sha512-RgHBCvtjbOK2gXSNBNIkNoEc9qoVEtau3hj8gEqKQuL3HZAibKarWFEI3Lfm6EYKkLalOh8eSrj9b+ch9H/VBA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.7",
        "@babel/generator": "^7.29.7",
        "@babel/helper-compilation-targets": "^7.29.7",
        "@babel/helper-module-transforms": "^7.29.7",
        "@babel/helpers": "^7.29.7",
        "@babel/parser": "^7.29.7",
        "@babel/template": "^7.29.7",
        "@babel/traverse": "^7.29.7",
        "@babel/types": "^7.29.7",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.7.tgz",
      "integrity": "sha512-DkXD5OJQaAQIdZ1bt3UZdEnHAn9Imd3IVBdX03UFe+ony9Ojw5pzr9YVKGDY1jt+Gcn/FnGkNf8r+Vj5NOJWtQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.7",
        "@babel/types": "^7.29.7",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.29.7.tgz",
      "integrity": "sha512-wem6WaBj4NaVYVdNhLPPVacES6ZJ+KBBfSkTMD3YZxbP3rm3Di85tJU5ljaUNhaOynt+Aj0xruhYuzQBt8n71g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.29.7",
        "@babel/helper-validator-option": "^7.29.7",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.29.7.tgz",
      "integrity": "sha512-3nQVUAtvkKH9zahfWgw96Jc/uFOmjACE1kQz82E2lqWmHBgjzbNlsC22nuQTfahmWeQtTq5nQ/4Nnd2A1wj4zA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.29.7.tgz",
      "integrity": "sha512-ejHwrQQYcm9xnTivShn2IDOlIzInN34AXskvq9QicvCtEzq1Vzclu/tKF8Jq1Cg8JG2GL6/EmjgsCT7lXepE3g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.29.7",
        "@babel/types": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.29.7.tgz",
      "integrity": "sha512-UPUVSyXbOh627KiCIGQSgwWzGeBKLkaJ9PJEdrngIwMSzxLR4jS4+f1f1jb7VzBbg8nFLaYotvVPFCTqdrmTAg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.29.7",
        "@babel/helper-validator-identifier": "^7.29.7",
        "@babel/traverse": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.29.7.tgz",
      "integrity": "sha512-G7sHYigPY17oO5SYWnfD/0MTBwVR781S/JI643e/JhUYgVgWE/61SoW3NH9KWUKyKq5LVh3npif99Wkt6j86Jw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.29.7.tgz",
      "integrity": "sha512-Pb5ijPrZ89GDH8223L4UP8i6QApWxs04RbPQJTeWDV0/keR2E36MeKnyr6LYmUUvqRRI+Iv87SuF1W6ErINzYw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.29.7.tgz",
      "integrity": "sha512-qehxGkRj55h/ff8EMaJ+cYhyaKlHIxqYDn682wQD7RNp9UujOQsHog2uS0r2vzr4pW+sXf90NeeayjcNaX3fFg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.29.7.tgz",
      "integrity": "sha512-N9ZErrD+yW5geCDtBqnOoxmR8+tNKiGuxKlDpuJxfsqpa2dFcexaziGAE/qoHLiDDreVNMupxGmSoNlyvsA3gw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.29.7.tgz",
      "integrity": "sha512-1k2lAGRMfHTcwuNYcCNUmaUffmQv8KWMfh2iJUUeRlwlwH4FdNG7mfPI10NPfLHJFThE4Tyr4mv7kTNZOiPuBg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.29.7",
        "@babel/types": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.7.tgz",
      "integrity": "sha512-hnORnjP/1P/zFEndoeX+n+t1RwWRJiJpM/jO7FW32Kn9r5+sJB2JWOdYo4L6k78j15eCwY3Gm/7364B1EMwtNg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.7"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.29.7.tgz",
      "integrity": "sha512-TL0hMc9xzy86VD31nUiwzd5otRAcyEPcsegCxolO0PvcXuH1v0kECe/UIznYFihpkvU5wg/jk4v0TTEFfm53fw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.29.7.tgz",
      "integrity": "sha512-06IyK09H3wi4cGbhDBwp5gUGo0IKtnYa8tyTiephirPCK6fbobVGiXMMI5zLQ4aKEYP3wZ3ArU44o+8KMrSG/Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/runtime": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.29.7.tgz",
      "integrity": "sha512-Nq8OhGWiZIZGV6hLHoyAKLLcJihP/xFeBMGJoUrxTX2psI8dCifzLhZISFb+VWS3wFMRDmCGw5R+dOySCqPLhw==",
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.29.7.tgz",
      "integrity": "sha512-puq+Gf35oI24FeN11LkoUQFqv9uwNeWpxXZi/Ji3rRIoKAzKnxRaZ+Gkj0vKS9ZCiTESfng1N9LyOyXvo+m+Gg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.7",
        "@babel/parser": "^7.29.7",
        "@babel/types": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.7.tgz",
      "integrity": "sha512-EhlfNQtZ+NK22w5BM61ciuiq1m58ed33Wr1Xan//ZRTy6hgjnwyCffRYwzsGXdASJSUJ1guZILsErh1eQcl+zw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.7",
        "@babel/generator": "^7.29.7",
        "@babel/helper-globals": "^7.29.7",
        "@babel/parser": "^7.29.7",
        "@babel/template": "^7.29.7",
        "@babel/types": "^7.29.7",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.7.tgz",
      "integrity": "sha512-4zBIxpPzowiZpusoFkyGVwakdRJUyuH5PxQ/PrqghfdFWWasvnCdPfQXHrenDai+gyLARulZjZowCOj6fjT4pA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.29.7",
        "@babel/helper-validator-identifier": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.21.5.tgz",
      "integrity": "sha512-1SDgH6ZSPTlggy1yI6+Dbkiz8xzpHJEVAlF/AM1tHPLsf5STom9rwtjE4hKAF20FfXXNTFqEYXyJNWh1GiZedQ==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.21.5.tgz",
      "integrity": "sha512-vCPvzSjpPHEi1siZdlvAlsPxXl7WbOVUBBAowWug4rJHb68Ox8KualB+1ocNvT5fjv6wpkX6o/iEpbDrf68zcg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.21.5.tgz",
      "integrity": "sha512-c0uX9VAUBQ7dTDCjq+wdyGLowMdtR/GoC2U5IYk/7D1H1JYC0qseD7+11iMP2mRLN9RcCMRcjC4YMclCzGwS/A==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.21.5.tgz",
      "integrity": "sha512-D7aPRUUNHRBwHxzxRvp856rjUHRFW1SdQATKXH2hqA0kAZb1hKmi02OpYRacl0TxIGz/ZmXWlbZgjwWYaCakTA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.21.5.tgz",
      "integrity": "sha512-DwqXqZyuk5AiWWf3UfLiRDJ5EDd49zg6O9wclZ7kUMv2WRFr4HKjXp/5t8JZ11QbQfUS6/cRCKGwYhtNAY88kQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.21.5.tgz",
      "integrity": "sha512-se/JjF8NlmKVG4kNIuyWMV/22ZaerB+qaSi5MdrXtd6R08kvs2qCN4C09miupktDitvh8jRFflwGFBQcxZRjbw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.21.5.tgz",
      "integrity": "sha512-5JcRxxRDUJLX8JXp/wcBCy3pENnCgBR9bN6JsY4OmhfUtIHe3ZW0mawA7+RDAcMLrMIZaf03NlQiX9DGyB8h4g==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.21.5.tgz",
      "integrity": "sha512-J95kNBj1zkbMXtHVH29bBriQygMXqoVQOQYA+ISs0/2l3T9/kj42ow2mpqerRBxDJnmkUDCaQT/dfNXWX/ZZCQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.21.5.tgz",
      "integrity": "sha512-bPb5AHZtbeNGjCKVZ9UGqGwo8EUu4cLq68E95A53KlxAPRmUyYv2D6F0uUI65XisGOL1hBP5mTronbgo+0bFcA==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.21.5.tgz",
      "integrity": "sha512-ibKvmyYzKsBeX8d8I7MH/TMfWDXBF3db4qM6sy+7re0YXya+K1cem3on9XgdT2EQGMu4hQyZhan7TeQ8XkGp4Q==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.21.5.tgz",
      "integrity": "sha512-YvjXDqLRqPDl2dvRODYmmhz4rPeVKYvppfGYKSNGdyZkA01046pLWyRKKI3ax8fbJoK5QbxblURkwK/MWY18Tg==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.21.5.tgz",
      "integrity": "sha512-uHf1BmMG8qEvzdrzAqg2SIG/02+4/DHB6a9Kbya0XDvwDEKCoC8ZRWI5JJvNdUjtciBGFQ5PuBlpEOXQj+JQSg==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.21.5.tgz",
      "integrity": "sha512-IajOmO+KJK23bj52dFSNCMsz1QP1DqM6cwLUv3W1QwyxkyIWecfafnI555fvSGqEKwjMXVLokcV5ygHW5b3Jbg==",
      "cpu": [
        "mips64el"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.21.5.tgz",
      "integrity": "sha512-1hHV/Z4OEfMwpLO8rp7CvlhBDnjsC3CttJXIhBi+5Aj5r+MBvy4egg7wCbe//hSsT+RvDAG7s81tAvpL2XAE4w==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.21.5.tgz",
      "integrity": "sha512-2HdXDMd9GMgTGrPWnJzP2ALSokE/0O5HhTUvWIbD3YdjME8JwvSCnNGBnTThKGEB91OZhzrJ4qIIxk/SBmyDDA==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.21.5.tgz",
      "integrity": "sha512-zus5sxzqBJD3eXxwvjN1yQkRepANgxE9lgOW2qLnmr8ikMTphkjgXu1HR01K4FJg8h1kEEDAqDcZQtbrRnB41A==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.21.5.tgz",
      "integrity": "sha512-1rYdTpyv03iycF1+BhzrzQJCdOuAOtaqHTWJZCWvijKD2N5Xu0TtVC8/+1faWqcP9iBCWOmjmhoH94dH82BxPQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.21.5.tgz",
      "integrity": "sha512-Woi2MXzXjMULccIwMnLciyZH4nCIMpWQAs049KEeMvOcNADVxo0UBIQPfSmxB3CWKedngg7sWZdLvLczpe0tLg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/openbsd-x64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.21.5.tgz",
      "integrity": "sha512-HLNNw99xsvx12lFBUwoT8EVCsSvRNDVxNpjZ7bPn947b8gJPzeHWyNVhFsaerc0n3TsbOINvRP2byTZ5LKezow==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/sunos-x64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.21.5.tgz",
      "integrity": "sha512-6+gjmFpfy0BHU5Tpptkuh8+uw3mnrvgs+dSPQXQOv3ekbordwnzTVEb4qnIvQcYXq6gzkyTnoZ9dZG+D4garKg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "sunos"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/win32-arm64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.21.5.tgz",
      "integrity": "sha512-Z0gOTd75VvXqyq7nsl93zwahcTROgqvuAcYDUr+vOv8uHhNSKROyU961kgtCD1e95IqPKSQKH7tBTslnS3tA8A==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/win32-ia32": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.21.5.tgz",
      "integrity": "sha512-SWXFF1CL2RVNMaVs+BBClwtfZSvDgtL//G/smwAc5oVK/UPu2Gu9tIaRgFmYFFKrmg3SyAjSrElf0TiJ1v8fYA==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/win32-x64": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.21.5.tgz",
      "integrity": "sha512-tQd/1efJuzPC6rCFwEvLtci/xNFcTZknmXs98FYDfGE4wP9ClFV98nyKrzJKVPMhdDnjzLhdUyMX4PsQAPjwIw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
      "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/remapping": {
      "version": "2.3.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/remapping/-/remapping-2.3.5.tgz",
      "integrity": "sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.3.5",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
      "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@react-leaflet/core": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/@react-leaflet/core/-/core-2.1.0.tgz",
      "integrity": "sha512-Qk7Pfu8BSarKGqILj4x7bCSZ1pjuAPZ+qmRwH5S7mDS91VSbVVsJSrW4qA+GPrro8t69gFYVMWb1Zc4yFmPiVg==",
      "license": "Hippocratic-2.1",
      "peerDependencies": {
        "leaflet": "^1.9.0",
        "react": "^18.0.0",
        "react-dom": "^18.0.0"
      }
    },
    "node_modules/@remix-run/router": {
      "version": "1.23.3",
      "resolved": "https://registry.npmjs.org/@remix-run/router/-/router-1.23.3.tgz",
      "integrity": "sha512-4An71tdz9X8+3sI4Qqqd2LWd9vS39J7sqd9EU4Scw7TJE/qB10Flv/UuqbPVgfQV9XoK8Np6jNquZitnZq5i+Q==",
      "license": "MIT",
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@rolldown/pluginutils": {
      "version": "1.0.0-beta.27",
      "resolved": "https://registry.npmjs.org/@rolldown/pluginutils/-/pluginutils-1.0.0-beta.27.tgz",
      "integrity": "sha512-+d0F4MKMCbeVUJwG96uQ4SgAznZNSq93I3V+9NHA4OpvqG8mRCpGdKmK8l/dl02h2CCDHwW2FqilnTyDcAnqjA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@rollup/rollup-android-arm-eabi": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm-eabi/-/rollup-android-arm-eabi-4.62.2.tgz",
      "integrity": "sha512-6o7ZLZK+BeenkZCFNDXqpbjw9bD6nuWonvS/lwQJp7NoVVxm6p3qE7qQ5jGuBjiFsgvqjD8mZAU5oWxTmbOeOg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-android-arm64": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm64/-/rollup-android-arm64-4.62.2.tgz",
      "integrity": "sha512-BaH7BllCACHoH1LguOU56UItGfUWjujlO65kS9LAodViaN4bwIKd7oeW/ZHJ/4ljr/7MIiENnNy3HJ0zXv8Zkw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-darwin-arm64": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-arm64/-/rollup-darwin-arm64-4.62.2.tgz",
      "integrity": "sha512-v39RCCvj4He82I9sFmk+M1VZ0PLM9sfsLVikjfx2hYBNALhrrOR2D3JjQA6AhlaSOgcR+RzrKY7e1+bT6SUO/A==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@rollup/rollup-darwin-x64": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-x64/-/rollup-darwin-x64-4.62.2.tgz",
      "integrity": "sha512-yl0y2vq3S3lHeuXhEdss6TWfKW8vkujImO12tn4ZkG/4oghr09LvdYm2RElVjokTQiUvDUGXLGsYeLqUMCKpGA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@rollup/rollup-freebsd-arm64": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-arm64/-/rollup-freebsd-arm64-4.62.2.tgz",
      "integrity": "sha512-tT4pvt4qXD+vEoezupCWi+a1F0vvDiksiHc+PxRlYTOH1I6/X4id9jPxTP+Fg+545euaFT1jJVs4CEdHZAU1vw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ]
    },
    "node_modules/@rollup/rollup-freebsd-x64": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-x64/-/rollup-freebsd-x64-4.62.2.tgz",
      "integrity": "sha512-6nU5F2wCW+qvCBhTn1pdIU3bzsIoF7EUwsCDRxilWGprQR6yd508YnH9+OKFCwpfS8pjZqDUmnCAr7exax0XCg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm-gnueabihf": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-gnueabihf/-/rollup-linux-arm-gnueabihf-4.62.2.tgz",
      "integrity": "sha512-n1GJHPOvpIfhi3TmrCeh6S6URt9BFCt0KQE3qvexyGCTAKpR4Lg+eWvNZEqu7epxwus/8ElT3hacYEucm49SZg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm-musleabihf": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-musleabihf/-/rollup-linux-arm-musleabihf-4.62.2.tgz",
      "integrity": "sha512-JqgflS8wEB+UXV/vS1RpRbifGBeN4D5lz8D8oOFbFZw4vedvdOgCFAjfBmIMdW3yL10XpQQ0Ambepw6MXrhOnA==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm64-gnu": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-gnu/-/rollup-linux-arm64-gnu-4.62.2.tgz",
      "integrity": "sha512-wnFJkogWvN4jm/hQRF2UBaeUmk20j5+DmHvoyWii2b8HJDyvz1MF2OU/6ynXt2KR63rbZLWkFpoytpdc/yBuSA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm64-musl": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-musl/-/rollup-linux-arm64-musl-4.62.2.tgz",
      "integrity": "sha512-HVu2bp0zhvJ8xHEV9+UUs7S90VadmBSY3LcIMvozbPo4AuMGDWlz3ymHLHZPX4hR67TKTt8Qp5PJ5RBg/i+RMQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-loong64-gnu": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-loong64-gnu/-/rollup-linux-loong64-gnu-4.62.2.tgz",
      "integrity": "sha512-mQqqAV8QaoSgr9I2fKDLY2BAVvmKjWoGiu/cSYQonsLvtqwEn1E4QYfnCOcp5zoEqNhsDYin1s6jx/VJmrxlZg==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-loong64-musl": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-loong64-musl/-/rollup-linux-loong64-musl-4.62.2.tgz",
      "integrity": "sha512-IxKLoxCQ2IWi6bT2akyDUBGsOImDKB+sPp4EsTmwFQ/fMwpCKm8uLSSgP/Kx/QYUgKis6SEZ5/Nlhup0DIA0PQ==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-ppc64-gnu": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-ppc64-gnu/-/rollup-linux-ppc64-gnu-4.62.2.tgz",
      "integrity": "sha512-Mk5ha2RQSgyFfmYYLkBpPnUk8D8FriBxesO1u9O75X0mHgXL1UQcH5Itl2lurWL2tj0RxV9b9tJgipac0hRY9A==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-ppc64-musl": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-ppc64-musl/-/rollup-linux-ppc64-musl-4.62.2.tgz",
      "integrity": "sha512-CjvEnqJL/0/TQ3TXX3OPIJ/kmBellrWd4heXUmHeJlTnmwjKpSJzoehLaL6Xk0ZnMHBu9dZuFADNOrtjF4v+2w==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-riscv64-gnu": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-gnu/-/rollup-linux-riscv64-gnu-4.62.2.tgz",
      "integrity": "sha512-1SiZbzwdkaDURsew/tSOrooKiYy7EQGT6m8ufavAi9NEyQb/6VuIxFXAL1fqa4iZe3g4NbNk4P7J32z2tw5Mgg==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-riscv64-musl": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-musl/-/rollup-linux-riscv64-musl-4.62.2.tgz",
      "integrity": "sha512-nQts12zJ3NQRoE6uYljOH89v7szzLDvG2JD/vsX+vGXU8w/At1GowTZ5/7qeFQ8m7L55rpR8Okugnuo5bgjy2Q==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-s390x-gnu": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-s390x-gnu/-/rollup-linux-s390x-gnu-4.62.2.tgz",
      "integrity": "sha512-E9/ll019jhPIJgpzfZoIkBGhcz+kKNgVWYRY0zr9srBdPPFVpvOKW8VaJKUbeK+eZXyQF9ltME+Kk6affeaPgg==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-x64-gnu": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-gnu/-/rollup-linux-x64-gnu-4.62.2.tgz",
      "integrity": "sha512-5BqxR/pshjey51iliyzTD5Xi3EN0aLmQ2lZ3lvefVV9c82BvrLo2/6OT55iifpWBufs6kdwWbuOKS841DrmK9A==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-x64-musl": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-musl/-/rollup-linux-x64-musl-4.62.2.tgz",
      "integrity": "sha512-uNN83XxQrRAh/w0/pmAfibcwyb6YWt4gP+dpnQKPVJshAloQ785ii8CT8ZCIxkGg9opVsvAlGhFitSm6D1Jjpg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-openbsd-x64": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-openbsd-x64/-/rollup-openbsd-x64-4.62.2.tgz",
      "integrity": "sha512-srjEIxSH3LRnJN6THczDHWQplqEMFiAJrTab0msUryh9kwNpkICf3Ea6q6MN/2cZwRFUNx5w+h6Hpi4QuHS6Zg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ]
    },
    "node_modules/@rollup/rollup-openharmony-arm64": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-openharmony-arm64/-/rollup-openharmony-arm64-4.62.2.tgz",
      "integrity": "sha512-8hOJnxgbyObnCm5AlRA3A931xX19xq80RjVTKgJOvEKWqJruP/Uf12IbAOaDjjEXYRewwHLfmF0YRIdK3OwKWA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ]
    },
    "node_modules/@rollup/rollup-win32-arm64-msvc": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-arm64-msvc/-/rollup-win32-arm64-msvc-4.62.2.tgz",
      "integrity": "sha512-mmF4AY1i0hG/bLWUctUq59gtmgaSIRa3cu/A3JFRp/sCNEme2bgDEiDS22P9FbnJB8NJNF4jPJiSP5RHQpUTDg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-ia32-msvc": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-ia32-msvc/-/rollup-win32-ia32-msvc-4.62.2.tgz",
      "integrity": "sha512-DZgkknc6jhHrk46V25vbAM0zZkyP0nSDkJB8/dRkLTxv470dOmWDqGoEJl/9A0dFfS7yE3REOwNDxpHwSLSt0Q==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-x64-gnu": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-gnu/-/rollup-win32-x64-gnu-4.62.2.tgz",
      "integrity": "sha512-T6xr6ucWSFto+VGajA8YH26LdpHRuP4YLHEKAtCWvJDOlnmWcDZVCI2Jmjr+IFHDlt2zRaTAKE4tfjTaWLgJBg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-x64-msvc": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-msvc/-/rollup-win32-x64-msvc-4.62.2.tgz",
      "integrity": "sha512-BfzEnDJOt9T8M989/lA37EcJgat01wLRnoi5dQf3QzOH7jzpqTAzdDbVfRljVr5r+jzKqpbHeyOfAaXxAd0PAA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@types/babel__core": {
      "version": "7.20.5",
      "resolved": "https://registry.npmjs.org/@types/babel__core/-/babel__core-7.20.5.tgz",
      "integrity": "sha512-qoQprZvz5wQFJwMDqeseRXWv3rqMvhgpbXFfVyWhbx9X47POIA6i/+dXefEmZKoAgOaTdaIgNSMqMIU61yRyzA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.20.7",
        "@babel/types": "^7.20.7",
        "@types/babel__generator": "*",
        "@types/babel__template": "*",
        "@types/babel__traverse": "*"
      }
    },
    "node_modules/@types/babel__generator": {
      "version": "7.27.0",
      "resolved": "https://registry.npmjs.org/@types/babel__generator/-/babel__generator-7.27.0.tgz",
      "integrity": "sha512-ufFd2Xi92OAVPYsy+P4n7/U7e68fex0+Ee8gSG9KX7eo084CWiQ4sdxktvdl0bOPupXtVJPY19zk6EwWqUQ8lg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.0.0"
      }
    },
    "node_modules/@types/babel__template": {
      "version": "7.4.4",
      "resolved": "https://registry.npmjs.org/@types/babel__template/-/babel__template-7.4.4.tgz",
      "integrity": "sha512-h/NUaSyG5EyxBIp8YRxo4RMe2/qQgvyowRwVMzhYhBCONbW8PUsg4lkFMrhgZhUe5z3L3MiLDuvyJ/CaPa2A8A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.1.0",
        "@babel/types": "^7.0.0"
      }
    },
    "node_modules/@types/babel__traverse": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@types/babel__traverse/-/babel__traverse-7.28.0.tgz",
      "integrity": "sha512-8PvcXf70gTDZBgt9ptxJ8elBeBjcLOAcOtoO/mPJjtji1+CdGbHgm77om1GrsPxsiE+uXIpNSK64UYaIwQXd4Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.2"
      }
    },
    "node_modules/@types/d3-array": {
      "version": "3.2.2",
      "resolved": "https://registry.npmjs.org/@types/d3-array/-/d3-array-3.2.2.tgz",
      "integrity": "sha512-hOLWVbm7uRza0BYXpIIW5pxfrKe0W+D5lrFiAEYR+pb6w3N2SwSMaJbXdUfSEv+dT4MfHBLtn5js0LAWaO6otw==",
      "license": "MIT"
    },
    "node_modules/@types/d3-color": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/@types/d3-color/-/d3-color-3.1.3.tgz",
      "integrity": "sha512-iO90scth9WAbmgv7ogoq57O9YpKmFBbmoEoCHDB2xMBY0+/KVrqAaCDyCE16dUspeOvIxFFRI+0sEtqDqy2b4A==",
      "license": "MIT"
    },
    "node_modules/@types/d3-ease": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/@types/d3-ease/-/d3-ease-3.0.2.tgz",
      "integrity": "sha512-NcV1JjO5oDzoK26oMzbILE6HW7uVXOHLQvHshBUW4UMdZGfiY6v5BeQwh9a9tCzv+CeefZQHJt5SRgK154RtiA==",
      "license": "MIT"
    },
    "node_modules/@types/d3-interpolate": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/@types/d3-interpolate/-/d3-interpolate-3.0.4.tgz",
      "integrity": "sha512-mgLPETlrpVV1YRJIglr4Ez47g7Yxjl1lj7YKsiMCb27VJH9W8NVM6Bb9d8kkpG/uAQS5AmbA48q2IAolKKo1MA==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-color": "*"
      }
    },
    "node_modules/@types/d3-path": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/@types/d3-path/-/d3-path-3.1.1.tgz",
      "integrity": "sha512-VMZBYyQvbGmWyWVea0EHs/BwLgxc+MKi1zLDCONksozI4YJMcTt8ZEuIR4Sb1MMTE8MMW49v0IwI5+b7RmfWlg==",
      "license": "MIT"
    },
    "node_modules/@types/d3-scale": {
      "version": "4.0.9",
      "resolved": "https://registry.npmjs.org/@types/d3-scale/-/d3-scale-4.0.9.tgz",
      "integrity": "sha512-dLmtwB8zkAeO/juAMfnV+sItKjlsw2lKdZVVy6LRr0cBmegxSABiLEpGVmSJJ8O08i4+sGR6qQtb6WtuwJdvVw==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-time": "*"
      }
    },
    "node_modules/@types/d3-shape": {
      "version": "3.1.8",
      "resolved": "https://registry.npmjs.org/@types/d3-shape/-/d3-shape-3.1.8.tgz",
      "integrity": "sha512-lae0iWfcDeR7qt7rA88BNiqdvPS5pFVPpo5OfjElwNaT2yyekbM0C9vK+yqBqEmHr6lDkRnYNoTBYlAgJa7a4w==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-path": "*"
      }
    },
    "node_modules/@types/d3-time": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/@types/d3-time/-/d3-time-3.0.4.tgz",
      "integrity": "sha512-yuzZug1nkAAaBlBBikKZTgzCeA+k1uy4ZFwWANOfKw5z5LRhV0gNA7gNkKm7HoK+HRN0wX3EkxGk0fpbWhmB7g==",
      "license": "MIT"
    },
    "node_modules/@types/d3-timer": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/@types/d3-timer/-/d3-timer-3.0.2.tgz",
      "integrity": "sha512-Ps3T8E8dZDam6fUyNiMkekK3XUsaUEik+idO9/YjPtfj2qruF8tFBXS7XhtE4iIXBLxhmLjP3SXpLhVf21I9Lw==",
      "license": "MIT"
    },
    "node_modules/@types/estree": {
      "version": "1.0.9",
      "resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.9.tgz",
      "integrity": "sha512-GhdPgy1el4/ImP05X05Uw4cw2/M93BCUmnEvWZNStlCzEKME4Fkk+YpoA5OiHNQmoS7Cafb8Xa3Pya8m1Qrzeg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/geojson": {
      "version": "7946.0.16",
      "resolved": "https://registry.npmjs.org/@types/geojson/-/geojson-7946.0.16.tgz",
      "integrity": "sha512-6C8nqWur3j98U6+lXDfTUWIfgvZU+EumvpHKcYjujKH7woYyLj2sUmff0tRhrqM7BohUw7Pz3ZB1jj2gW9Fvmg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/leaflet": {
      "version": "1.9.21",
      "resolved": "https://registry.npmjs.org/@types/leaflet/-/leaflet-1.9.21.tgz",
      "integrity": "sha512-TbAd9DaPGSnzp6QvtYngntMZgcRk+igFELwR2N99XZn7RXUdKgsXMR+28bUO0rPsWp8MIu/f47luLIQuSLYv/w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/geojson": "*"
      }
    },
    "node_modules/@types/prop-types": {
      "version": "15.7.15",
      "resolved": "https://registry.npmjs.org/@types/prop-types/-/prop-types-15.7.15.tgz",
      "integrity": "sha512-F6bEyamV9jKGAFBEmlQnesRPGOQqS2+Uwi0Em15xenOxHaf2hv6L8YCVn3rPdPJOiJfPiCnLIRyvwVaqMY3MIw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/react": {
      "version": "18.3.31",
      "resolved": "https://registry.npmjs.org/@types/react/-/react-18.3.31.tgz",
      "integrity": "sha512-vfEqpXTvwT91yhmwdfouStN2hSKwTvyRs8qpLfADyrq/kxDw0hZM7Wk9Ug1FELj8hIby+S/+kQCSRFF32nv2Qw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/prop-types": "*",
        "csstype": "^3.2.2"
      }
    },
    "node_modules/@types/react-dom": {
      "version": "18.3.7",
      "resolved": "https://registry.npmjs.org/@types/react-dom/-/react-dom-18.3.7.tgz",
      "integrity": "sha512-MEe3UeoENYVFXzoXEWsvcpg6ZvlrFNlOQ7EOsvhI3CfAXwzPfO8Qwuxd40nepsYKqyyVQnTdEfv68q91yLcKrQ==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "^18.0.0"
      }
    },
    "node_modules/@vitejs/plugin-react": {
      "version": "4.7.0",
      "resolved": "https://registry.npmjs.org/@vitejs/plugin-react/-/plugin-react-4.7.0.tgz",
      "integrity": "sha512-gUu9hwfWvvEDBBmgtAowQCojwZmJ5mcLn3aufeCsitijs3+f2NsrPtlAWIR6OPiqljl96GVCUbLe0HyqIpVaoA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/core": "^7.28.0",
        "@babel/plugin-transform-react-jsx-self": "^7.27.1",
        "@babel/plugin-transform-react-jsx-source": "^7.27.1",
        "@rolldown/pluginutils": "1.0.0-beta.27",
        "@types/babel__core": "^7.20.5",
        "react-refresh": "^0.17.0"
      },
      "engines": {
        "node": "^14.18.0 || >=16.0.0"
      },
      "peerDependencies": {
        "vite": "^4.2.0 || ^5.0.0 || ^6.0.0 || ^7.0.0"
      }
    },
    "node_modules/any-promise": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/any-promise/-/any-promise-1.3.0.tgz",
      "integrity": "sha512-7UvmKalWRt1wgjL1RrGxoSJW/0QZFIegpeGvZG9kjp8vrRu55XTHbwnqq2GpXm9uLbcuhxm3IqX9OB4MZR1b2A==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/anymatch": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz",
      "integrity": "sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "normalize-path": "^3.0.0",
        "picomatch": "^2.0.4"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/arg": {
      "version": "5.0.2",
      "resolved": "https://registry.npmjs.org/arg/-/arg-5.0.2.tgz",
      "integrity": "sha512-PYjyFOLKQ9y57JvQ6QLo8dAgNqswh8M1RMJYdQduT6xbWSgK36P/Z/v+p888pM69jMMfS8Xd8F6I1kQ/I9HUGg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/autoprefixer": {
      "version": "10.5.4",
      "resolved": "https://registry.npmjs.org/autoprefixer/-/autoprefixer-10.5.4.tgz",
      "integrity": "sha512-MaU0U/za7N3r6brxD4YB/l4NSrFzLPlANv6wEuQVaIPlD3L4W9rFcQPbL/EilY9BHhHvhfcz3gInDLrEtWT4EA==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/autoprefixer"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "browserslist": "^4.28.6",
        "caniuse-lite": "^1.0.30001806",
        "fraction.js": "^5.3.4",
        "picocolors": "^1.1.1",
        "postcss-value-parser": "^4.2.0"
      },
      "bin": {
        "autoprefixer": "bin/autoprefixer"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      },
      "peerDependencies": {
        "postcss": "^8.1.0"
      }
    },
    "node_modules/baseline-browser-mapping": {
      "version": "2.10.43",
      "resolved": "https://registry.npmjs.org/baseline-browser-mapping/-/baseline-browser-mapping-2.10.43.tgz",
      "integrity": "sha512-AjYpR78kDWAY3Efj+cDTFH9t9SCoL7OoTp1BOb0mQV7S+6CiLwnWM3FyxhJtdPufDFKzmCSFoUncKjWgJEZTCQ==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "baseline-browser-mapping": "dist/cli.cjs"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/binary-extensions": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.3.0.tgz",
      "integrity": "sha512-Ceh+7ox5qe7LJuLHoY0feh3pHuUDHAcRUeyL2VYghZwfpkNIy/+8Ocg0a3UuSoYzavmylwuLWQOf3hl0jjMMIw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/browserslist": {
      "version": "4.28.6",
      "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.28.6.tgz",
      "integrity": "sha512-FQBYNK15VMslhLHpA7+n+n1GOlF1kId2xcCg7/j95f24AOF6VDYMNH4mFxF7KuaTdv627faazpOAjFzMrfJOUw==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "baseline-browser-mapping": "^2.10.42",
        "caniuse-lite": "^1.0.30001803",
        "electron-to-chromium": "^1.5.389",
        "node-releases": "^2.0.51",
        "update-browserslist-db": "^1.2.3"
      },
      "bin": {
        "browserslist": "cli.js"
      },
      "engines": {
        "node": "^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7"
      }
    },
    "node_modules/camelcase-css": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/camelcase-css/-/camelcase-css-2.0.1.tgz",
      "integrity": "sha512-QOSvevhslijgYwRx6Rv7zKdMF8lbRmx+uQGx2+vDc+KI/eBnsy9kit5aj23AgGu3pa4t9AgwbnXWqS+iOY+2aA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/caniuse-lite": {
      "version": "1.0.30001806",
      "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001806.tgz",
      "integrity": "sha512-72Cuvd95zbSYPKq6Fhg8eDJRlzgWDf7/mtoZv6Qe/DYNCEBdNxoA3+rZAU2ZhGCpZlns3EssFavaZomckT5Uuw==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/caniuse-lite"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "CC-BY-4.0"
    },
    "node_modules/chokidar": {
      "version": "3.6.0",
      "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-3.6.0.tgz",
      "integrity": "sha512-7VT13fmjotKpGipCW9JEQAusEPE+Ei8nl6/g4FBAmIm0GOOLMua9NDDo/DWp0ZAxCr3cPq5ZpBqmPAQgDda2Pw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "anymatch": "~3.1.2",
        "braces": "~3.0.2",
        "glob-parent": "~5.1.2",
        "is-binary-path": "~2.1.0",
        "is-glob": "~4.0.1",
        "normalize-path": "~3.0.0",
        "readdirp": "~3.6.0"
      },
      "engines": {
        "node": ">= 8.10.0"
      },
      "funding": {
        "url": "https://paulmillr.com/funding/"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/chokidar/node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/clsx": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/clsx/-/clsx-2.1.1.tgz",
      "integrity": "sha512-eYm0QWBtUrBWZWG0d386OGAw16Z995PiOVo2B7bjWSbHedGl5e0ZWaq65kOGgUSNesEIDkB9ISbTg/JK9dhCZA==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/commander": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/commander/-/commander-4.1.1.tgz",
      "integrity": "sha512-NOKm8xhkzAjzFx8B2v5OAHT+u5pRQc2UCa2Vq9jYL/31o2wi9mxBA7LIFs3sV5VSC49z6pEhfbMULvShKj26WA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/convert-source-map": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-2.0.0.tgz",
      "integrity": "sha512-Kvp459HrV2FEJ1CAsi1Ku+MY3kasH19TFykTz2xWmMeq6bk2NU3XXvfJ+Q61m0xktWwt+1HSYf3JZsTms3aRJg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/cssesc": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz",
      "integrity": "sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "cssesc": "bin/cssesc"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/csstype": {
      "version": "3.2.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz",
      "integrity": "sha512-z1HGKcYy2xA8AGQfwrn0PAy+PB7X/GSj3UVJW9qKyn43xWa+gl5nXmU4qqLMRzWVLFC8KusUX8T/0kCiOYpAIQ==",
      "license": "MIT"
    },
    "node_modules/d3-array": {
      "version": "3.2.4",
      "resolved": "https://registry.npmjs.org/d3-array/-/d3-array-3.2.4.tgz",
      "integrity": "sha512-tdQAmyA18i4J7wprpYq8ClcxZy3SC31QMeByyCFyRt7BVHdREQZ5lpzoe5mFEYZUWe+oq8HBvk9JjpibyEV4Jg==",
      "license": "ISC",
      "dependencies": {
        "internmap": "1 - 2"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-color": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-color/-/d3-color-3.1.0.tgz",
      "integrity": "sha512-zg/chbXyeBtMQ1LbD/WSoW2DpC3I0mpmPdW+ynRTj/x2DAWYrIY7qeZIHidozwV24m4iavr15lNwIwLxRmOxhA==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-ease": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-ease/-/d3-ease-3.0.1.tgz",
      "integrity": "sha512-wR/XK3D3XcLIZwpbvQwQ5fK+8Ykds1ip7A2Txe0yxncXSdq1L9skcG7blcedkOX+ZcgxGAmLX1FrRGbADwzi0w==",
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-format": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/d3-format/-/d3-format-3.1.2.tgz",
      "integrity": "sha512-AJDdYOdnyRDV5b6ArilzCPPwc1ejkHcoyFarqlPqT7zRYjhavcT3uSrqcMvsgh2CgoPbK3RCwyHaVyxYcP2Arg==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-interpolate": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-interpolate/-/d3-interpolate-3.0.1.tgz",
      "integrity": "sha512-3bYs1rOD33uo8aqJfKP3JWPAibgw8Zm2+L9vBKEHJ2Rg+viTR7o5Mmv5mZcieN+FRYaAOWX5SJATX6k1PWz72g==",
      "license": "ISC",
      "dependencies": {
        "d3-color": "1 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-path": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-path/-/d3-path-3.1.0.tgz",
      "integrity": "sha512-p3KP5HCf/bvjBSSKuXid6Zqijx7wIfNW+J/maPs+iwR35at5JCbLUT0LzF1cnjbCHWhqzQTIN2Jpe8pRebIEFQ==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-scale": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/d3-scale/-/d3-scale-4.0.2.tgz",
      "integrity": "sha512-GZW464g1SH7ag3Y7hXjf8RoUuAFIqklOAq3MRl4OaWabTFJY9PN/E1YklhXLh+OQ3fM9yS2nOkCoS+WLZ6kvxQ==",
      "license": "ISC",
      "dependencies": {
        "d3-array": "2.10.0 - 3",
        "d3-format": "1 - 3",
        "d3-interpolate": "1.2.0 - 3",
        "d3-time": "2.1.1 - 3",
        "d3-time-format": "2 - 4"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-shape": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/d3-shape/-/d3-shape-3.2.0.tgz",
      "integrity": "sha512-SaLBuwGm3MOViRq2ABk3eLoxwZELpH6zhl3FbAoJ7Vm1gofKx6El1Ib5z23NUEhF9AsGl7y+dzLe5Cw2AArGTA==",
      "license": "ISC",
      "dependencies": {
        "d3-path": "^3.1.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-time": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-time/-/d3-time-3.1.0.tgz",
      "integrity": "sha512-VqKjzBLejbSMT4IgbmVgDjpkYrNWUYJnbCGo874u7MMKIWsILRX+OpX/gTk8MqjpT1A/c6HY2dCA77ZN0lkQ2Q==",
      "license": "ISC",
      "dependencies": {
        "d3-array": "2 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-time-format": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/d3-time-format/-/d3-time-format-4.1.0.tgz",
      "integrity": "sha512-dJxPBlzC7NugB2PDLwo9Q8JiTR3M3e4/XANkreKSUxF8vvXKqm1Yfq4Q5dl8budlunRVlUUaDUgFt7eA8D6NLg==",
      "license": "ISC",
      "dependencies": {
        "d3-time": "1 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-timer": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-timer/-/d3-timer-3.0.1.tgz",
      "integrity": "sha512-ndfJ/JxxMd3nw31uyKoY2naivF+r29V+Lc0svZxe1JvvIRmi8hUsrMvdOwgS1o6uBHmiz91geQ0ylPP0aj1VUA==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/decimal.js-light": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/decimal.js-light/-/decimal.js-light-2.5.1.tgz",
      "integrity": "sha512-qIMFpTMZmny+MMIitAB6D7iVPEorVw6YQRWkvarTkT4tBeSLLiHzcwj6q0MmYSFCiVpiqPJTJEYIrpcPzVEIvg==",
      "license": "MIT"
    },
    "node_modules/didyoumean": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/didyoumean/-/didyoumean-1.2.2.tgz",
      "integrity": "sha512-gxtyfqMg7GKyhQmb056K7M3xszy/myH8w+B4RT+QXBQsvAOdc3XymqDDPHx1BgPgsdAA5SIifona89YtRATDzw==",
      "dev": true,
      "license": "Apache-2.0"
    },
    "node_modules/dlv": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/dlv/-/dlv-1.1.3.tgz",
      "integrity": "sha512-+HlytyjlPKnIG8XuRG8WvmBP8xs8P71y+SKKS6ZXWoEgLuePxtDoUEiH7WkdePWrQ5JBpE6aoVqfZfJUQkjXwA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/dom-helpers": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/dom-helpers/-/dom-helpers-5.2.1.tgz",
      "integrity": "sha512-nRCa7CK3VTrM2NmGkIy4cbK7IZlgBE/PYMn55rrXefr5xXDP0LdtfPnblFDoVdcAfslJ7or6iqAUnx0CCGIWQA==",
      "license": "MIT",
      "dependencies": {
        "@babel/runtime": "^7.8.7",
        "csstype": "^3.0.2"
      }
    },
    "node_modules/electron-to-chromium": {
      "version": "1.5.392",
      "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.392.tgz",
      "integrity": "sha512-1yQq3VQCZRwsnYc67Oc+1fge6Lwtn0hzi6zmEVkB61Zx21kTbwJAW4dFLadl5Rc1tKhG/kSpYXnfiAhu0f0a1g==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/esbuild": {
      "version": "0.21.5",
      "resolved": "https://registry.npmjs.org/esbuild/-/esbuild-0.21.5.tgz",
      "integrity": "sha512-mg3OPMV4hXywwpoDxu3Qda5xCKQi+vCTZq8S9J/EpkhB2HzKXq4SNFZE3+NK93JYxc8VMSep+lOUSC/RVKaBqw==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "bin": {
        "esbuild": "bin/esbuild"
      },
      "engines": {
        "node": ">=12"
      },
      "optionalDependencies": {
        "@esbuild/aix-ppc64": "0.21.5",
        "@esbuild/android-arm": "0.21.5",
        "@esbuild/android-arm64": "0.21.5",
        "@esbuild/android-x64": "0.21.5",
        "@esbuild/darwin-arm64": "0.21.5",
        "@esbuild/darwin-x64": "0.21.5",
        "@esbuild/freebsd-arm64": "0.21.5",
        "@esbuild/freebsd-x64": "0.21.5",
        "@esbuild/linux-arm": "0.21.5",
        "@esbuild/linux-arm64": "0.21.5",
        "@esbuild/linux-ia32": "0.21.5",
        "@esbuild/linux-loong64": "0.21.5",
        "@esbuild/linux-mips64el": "0.21.5",
        "@esbuild/linux-ppc64": "0.21.5",
        "@esbuild/linux-riscv64": "0.21.5",
        "@esbuild/linux-s390x": "0.21.5",
        "@esbuild/linux-x64": "0.21.5",
        "@esbuild/netbsd-x64": "0.21.5",
        "@esbuild/openbsd-x64": "0.21.5",
        "@esbuild/sunos-x64": "0.21.5",
        "@esbuild/win32-arm64": "0.21.5",
        "@esbuild/win32-ia32": "0.21.5",
        "@esbuild/win32-x64": "0.21.5"
      }
    },
    "node_modules/escalade": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
      "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/eventemitter3": {
      "version": "4.0.7",
      "resolved": "https://registry.npmjs.org/eventemitter3/-/eventemitter3-4.0.7.tgz",
      "integrity": "sha512-8guHBZCwKnFhYdHr2ysuRWErTwhoN2X8XELRlrRwpmfeY2jjuUN4taQMsULKUVo1K4DvZl+0pgfyoysHxvmvEw==",
      "license": "MIT"
    },
    "node_modules/fast-equals": {
      "version": "5.4.1",
      "resolved": "https://registry.npmjs.org/fast-equals/-/fast-equals-5.4.1.tgz",
      "integrity": "sha512-DjlFSM5Pk9cGcL0q5QXl66eGzx0N6szNgaswwc5ZphlBohjTVJSnGgI+rJVOgOi65qUoQnDZN4nDqi33udtydQ==",
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/fast-glob": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
      "integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "^2.0.2",
        "@nodelib/fs.walk": "^1.2.3",
        "glob-parent": "^5.1.2",
        "merge2": "^1.3.0",
        "micromatch": "^4.0.8"
      },
      "engines": {
        "node": ">=8.6.0"
      }
    },
    "node_modules/fast-glob/node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/fastq": {
      "version": "1.20.1",
      "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.20.1.tgz",
      "integrity": "sha512-GGToxJ/w1x32s/D2EKND7kTil4n8OVk/9mycTc4VDza13lOvpUZTGX3mFSCtV9ksdGBVzvsyAVLM6mHFThxXxw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "reusify": "^1.0.4"
      }
    },
    "node_modules/fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "to-regex-range": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/fraction.js": {
      "version": "5.3.4",
      "resolved": "https://registry.npmjs.org/fraction.js/-/fraction.js-5.3.4.tgz",
      "integrity": "sha512-1X1NTtiJphryn/uLQz3whtY6jK3fTqoE3ohKs0tT+Ujr1W59oopxmoEh7Lu5p6vBaPbgoM0bzveAW4Qi5RyWDQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "*"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/rawify"
      }
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/gensync": {
      "version": "1.0.0-beta.2",
      "resolved": "https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz",
      "integrity": "sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/glob-parent": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz",
      "integrity": "sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.3"
      },
      "engines": {
        "node": ">=10.13.0"
      }
    },
    "node_modules/hasown": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.4.tgz",
      "integrity": "sha512-T2UbfbBEF32wiepXIsMlTW9+dDYC6wMh/t/vYA4tuOMKqWz/n3vr1NFSxQiyP+zk2mXsoMA/i/7qV6LKut1t1A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/internmap": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/internmap/-/internmap-2.0.3.tgz",
      "integrity": "sha512-5Hh7Y1wQbvY5ooGgPbDaL5iYLAPzMTUrjMulskHLH6wnv/A+1q5rgEaiuqEjB+oxGXIVZs1FF+R/KPN3ZSQYYg==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/is-binary-path": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz",
      "integrity": "sha512-ZMERYes6pDydyuGidse7OsHxtbI7WVeUEozgR/g7rd0xUimYNlvZRE/K2MgZTjWy725IfelLeVcEM97mmtRGXw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "binary-extensions": "^2.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/is-core-module": {
      "version": "2.16.2",
      "resolved": "https://registry.npmjs.org/is-core-module/-/is-core-module-2.16.2.tgz",
      "integrity": "sha512-evOr8xfXKxE6qSR0hSXL2r3sd7ALj8+7jQEUvPYcm5sgZFdJ+AYzT6yNmJenvIYQBgIGwfwz08sL8zoL7yq2BA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "hasown": "^2.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.12.0"
      }
    },
    "node_modules/jiti": {
      "version": "1.21.7",
      "resolved": "https://registry.npmjs.org/jiti/-/jiti-1.21.7.tgz",
      "integrity": "sha512-/imKNG4EbWNrVjoNC/1H5/9GFy+tqjGBHCaSsN+P2RnPqjsLmv6UD3Ej+Kj8nBWaRAwyk7kK5ZUc+OEatnTR3A==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "jiti": "bin/jiti.js"
      }
    },
    "node_modules/js-tokens": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
      "integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==",
      "license": "MIT"
    },
    "node_modules/jsesc": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz",
      "integrity": "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "jsesc": "bin/jsesc"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/json5": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/json5/-/json5-2.2.3.tgz",
      "integrity": "sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "json5": "lib/cli.js"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/leaflet": {
      "version": "1.9.4",
      "resolved": "https://registry.npmjs.org/leaflet/-/leaflet-1.9.4.tgz",
      "integrity": "sha512-nxS1ynzJOmOlHp+iL3FyWqK89GtNL8U8rvlMOsQdTTssxZwCXh8N2NB3GDQOL+YR3XnWyZAxwQixURb+FA74PA==",
      "license": "BSD-2-Clause"
    },
    "node_modules/lilconfig": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/lilconfig/-/lilconfig-3.1.3.tgz",
      "integrity": "sha512-/vlFKAoH5Cgt3Ie+JLhRbwOsCQePABiU3tJ1egGvyQ+33R/vcwM2Zl2QR/LzjsBeItPt3oSVXapn+m4nQDvpzw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=14"
      },
      "funding": {
        "url": "https://github.com/sponsors/antonk52"
      }
    },
    "node_modules/lines-and-columns": {
      "version": "1.2.4",
      "resolved": "https://registry.npmjs.org/lines-and-columns/-/lines-and-columns-1.2.4.tgz",
      "integrity": "sha512-7ylylesZQ/PV29jhEDl3Ufjo6ZX7gCqJr5F7PKrqc93v7fzSymt1BpwEU8nAUXs8qzzvqhbjhK5QZg6Mt/HkBg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/lodash": {
      "version": "4.18.1",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.18.1.tgz",
      "integrity": "sha512-dMInicTPVE8d1e5otfwmmjlxkZoUpiVLwyeTdUsi/Caj/gfzzblBcCE5sRHV/AsjuCmxWrte2TNGSYuCeCq+0Q==",
      "license": "MIT"
    },
    "node_modules/loose-envify": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz",
      "integrity": "sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==",
      "license": "MIT",
      "dependencies": {
        "js-tokens": "^3.0.0 || ^4.0.0"
      },
      "bin": {
        "loose-envify": "cli.js"
      }
    },
    "node_modules/lru-cache": {
      "version": "5.1.1",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz",
      "integrity": "sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "yallist": "^3.0.2"
      }
    },
    "node_modules/lucide-react": {
      "version": "0.292.0",
      "resolved": "https://registry.npmjs.org/lucide-react/-/lucide-react-0.292.0.tgz",
      "integrity": "sha512-rRgUkpEHWpa5VCT66YscInCQmQuPCB1RFRzkkxMxg4b+jaL0V12E3riWWR2Sh5OIiUhCwGW/ZExuEO4Az32E6Q==",
      "license": "ISC",
      "peerDependencies": {
        "react": "^16.5.1 || ^17.0.0 || ^18.0.0"
      }
    },
    "node_modules/merge2": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
      "integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/micromatch": {
      "version": "4.0.8",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
      "integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "braces": "^3.0.3",
        "picomatch": "^2.3.1"
      },
      "engines": {
        "node": ">=8.6"
      }
    },
    "node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/mz": {
      "version": "2.7.0",
      "resolved": "https://registry.npmjs.org/mz/-/mz-2.7.0.tgz",
      "integrity": "sha512-z81GNO7nnYMEhrGh9LeymoE4+Yr0Wn5McHIZMK5cfQCl+NDX08sCZgUc9/6MHni9IWuFLm1Z3HTCXu2z9fN62Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "any-promise": "^1.0.0",
        "object-assign": "^4.0.1",
        "thenify-all": "^1.0.0"
      }
    },
    "node_modules/nanoid": {
      "version": "3.3.16",
      "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.16.tgz",
      "integrity": "sha512-bzlKTyNJ7+LdGIIwy8ijFpIqEQIvafahV7eYykJ8Cvh42EdJeODoJ6gUJXpQJvej1BddH8OqTXZNE/KfbWAu8Q==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "bin": {
        "nanoid": "bin/nanoid.cjs"
      },
      "engines": {
        "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
      }
    },
    "node_modules/node-releases": {
      "version": "2.0.51",
      "resolved": "https://registry.npmjs.org/node-releases/-/node-releases-2.0.51.tgz",
      "integrity": "sha512-wRNIrw4DmVLKQlbgOMdkMx27Wrpzes2hh5Jtbi2bjPd+4wJstWIqP5A+lscnqbm0xxmT5Bpg8Lec5ItEBwx6BQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/normalize-path": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz",
      "integrity": "sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/object-assign": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
      "integrity": "sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/object-hash": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/object-hash/-/object-hash-3.0.0.tgz",
      "integrity": "sha512-RSn9F68PjH9HqtltsSnqYC1XXoWe9Bju5+213R98cNGttag9q9yAOTzdbsqvIa7aNm5WffBZFpWYr2aWrklWAw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/path-parse": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz",
      "integrity": "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/picocolors": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
      "integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/picomatch": {
      "version": "2.3.2",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.2.tgz",
      "integrity": "sha512-V7+vQEJ06Z+c5tSye8S+nHUfI51xoXIXjHQ99cQtKUkQqqO1kO/KCJUfZXuB47h/YBlDhah2H3hdUGXn8ie0oA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/pify": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/pify/-/pify-2.3.0.tgz",
      "integrity": "sha512-udgsAY+fTnvv7kI7aaxbqwWNb0AHiB0qBO89PZKPkoTmGOgdbrHDKD+0B2X4uTfJ/FT1R09r9gTsjUjNJotuog==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/pirates": {
      "version": "4.0.7",
      "resolved": "https://registry.npmjs.org/pirates/-/pirates-4.0.7.tgz",
      "integrity": "sha512-TfySrs/5nm8fQJDcBDuUng3VOUKsd7S+zqvbOTiGXHfxX4wK31ard+hoNuvkicM/2YFzlpDgABOevKSsB4G/FA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/postcss": {
      "version": "8.5.19",
      "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.5.19.tgz",
      "integrity": "sha512-Mz8SaolMd8nB+G13WkORcxQKHZ/NE4xXevtkJHVuG+guo9/wYKlIMTKAqGdEmYOXR2ijPjTYNHssizdaVSUNdQ==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/postcss"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "nanoid": "^3.3.12",
        "picocolors": "^1.1.1",
        "source-map-js": "^1.2.1"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      }
    },
    "node_modules/postcss-import": {
      "version": "15.1.0",
      "resolved": "https://registry.npmjs.org/postcss-import/-/postcss-import-15.1.0.tgz",
      "integrity": "sha512-hpr+J05B2FVYUAXHeK1YyI267J/dDDhMU6B6civm8hSY1jYJnBXxzKDKDswzJmtLHryrjhnDjqqp/49t8FALew==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "postcss-value-parser": "^4.0.0",
        "read-cache": "^1.0.0",
        "resolve": "^1.1.7"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "postcss": "^8.0.0"
      }
    },
    "node_modules/postcss-js": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/postcss-js/-/postcss-js-4.1.0.tgz",
      "integrity": "sha512-oIAOTqgIo7q2EOwbhb8UalYePMvYoIeRY2YKntdpFQXNosSu3vLrniGgmH9OKs/qAkfoj5oB3le/7mINW1LCfw==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "camelcase-css": "^2.0.1"
      },
      "engines": {
        "node": "^12 || ^14 || >= 16"
      },
      "peerDependencies": {
        "postcss": "^8.4.21"
      }
    },
    "node_modules/postcss-load-config": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/postcss-load-config/-/postcss-load-config-6.0.1.tgz",
      "integrity": "sha512-oPtTM4oerL+UXmx+93ytZVN82RrlY/wPUV8IeDxFrzIjXOLF1pN+EmKPLbubvKHT2HC20xXsCAH2Z+CKV6Oz/g==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "lilconfig": "^3.1.1"
      },
      "engines": {
        "node": ">= 18"
      },
      "peerDependencies": {
        "jiti": ">=1.21.0",
        "postcss": ">=8.0.9",
        "tsx": "^4.8.1",
        "yaml": "^2.4.2"
      },
      "peerDependenciesMeta": {
        "jiti": {
          "optional": true
        },
        "postcss": {
          "optional": true
        },
        "tsx": {
          "optional": true
        },
        "yaml": {
          "optional": true
        }
      }
    },
    "node_modules/postcss-nested": {
      "version": "6.2.0",
      "resolved": "https://registry.npmjs.org/postcss-nested/-/postcss-nested-6.2.0.tgz",
      "integrity": "sha512-HQbt28KulC5AJzG+cZtj9kvKB93CFCdLvog1WFLf1D+xmMvPGlBstkpTEZfK5+AN9hfJocyBFCNiqyS48bpgzQ==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "postcss-selector-parser": "^6.1.1"
      },
      "engines": {
        "node": ">=12.0"
      },
      "peerDependencies": {
        "postcss": "^8.2.14"
      }
    },
    "node_modules/postcss-selector-parser": {
      "version": "6.1.4",
      "resolved": "https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.1.4.tgz",
      "integrity": "sha512-bIoJLOmjCO1S9XdY/DcnR5hJxvrDir1PbGChrzXG3vw0/FOliy/fA3dmdhQ441kah4gKv+TwckGzex6wNS5cnQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "cssesc": "^3.0.0",
        "util-deprecate": "^1.0.2"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/postcss-value-parser": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz",
      "integrity": "sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/prop-types": {
      "version": "15.8.1",
      "resolved": "https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz",
      "integrity": "sha512-oj87CgZICdulUohogVAR7AjlC0327U4el4L6eAvOqCeudMDVU0NThNaV+b9Df4dXgSP1gXMTnPdhfe/2qDH5cg==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.4.0",
        "object-assign": "^4.1.1",
        "react-is": "^16.13.1"
      }
    },
    "node_modules/prop-types/node_modules/react-is": {
      "version": "16.13.1",
      "resolved": "https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz",
      "integrity": "sha512-24e6ynE2H+OKt4kqsOvNd8kBpV65zoxbA4BVsEOB3ARVWQki/DHzaUoC5KuON/BiccDaCCTZBuOcfZs70kR8bQ==",
      "license": "MIT"
    },
    "node_modules/queue-microtask": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
      "integrity": "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/react": {
      "version": "18.3.1",
      "resolved": "https://registry.npmjs.org/react/-/react-18.3.1.tgz",
      "integrity": "sha512-wS+hAgJShR0KhEvPJArfuPVN1+Hz1t0Y6n5jLrGQbkb4urgPE/0Rve+1kMB1v/oWgHgm4WIcV+i7F2pTVj+2iQ==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.1.0"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-dom": {
      "version": "18.3.1",
      "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-18.3.1.tgz",
      "integrity": "sha512-5m4nQKp+rZRb09LNH59GM4BxTh9251/ylbKIbpe7TpGxfJ+9kv6BLkLBXIjjspbgbnIBNqlI23tRnTWT0snUIw==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.1.0",
        "scheduler": "^0.23.2"
      },
      "peerDependencies": {
        "react": "^18.3.1"
      }
    },
    "node_modules/react-is": {
      "version": "18.3.1",
      "resolved": "https://registry.npmjs.org/react-is/-/react-is-18.3.1.tgz",
      "integrity": "sha512-/LLMVyas0ljjAtoYiPqYiL8VWXzUUdThrmU5+n20DZv+a+ClRoevUzw5JxU+Ieh5/c87ytoTBV9G1FiKfNJdmg==",
      "license": "MIT"
    },
    "node_modules/react-leaflet": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/react-leaflet/-/react-leaflet-4.2.1.tgz",
      "integrity": "sha512-p9chkvhcKrWn/H/1FFeVSqLdReGwn2qmiobOQGO3BifX+/vV/39qhY8dGqbdcPh1e6jxh/QHriLXr7a4eLFK4Q==",
      "license": "Hippocratic-2.1",
      "dependencies": {
        "@react-leaflet/core": "^2.1.0"
      },
      "peerDependencies": {
        "leaflet": "^1.9.0",
        "react": "^18.0.0",
        "react-dom": "^18.0.0"
      }
    },
    "node_modules/react-refresh": {
      "version": "0.17.0",
      "resolved": "https://registry.npmjs.org/react-refresh/-/react-refresh-0.17.0.tgz",
      "integrity": "sha512-z6F7K9bV85EfseRCp2bzrpyQ0Gkw1uLoCel9XBVWPg/TjRj94SkJzUTGfOa4bs7iJvBWtQG0Wq7wnI0syw3EBQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-router": {
      "version": "6.30.4",
      "resolved": "https://registry.npmjs.org/react-router/-/react-router-6.30.4.tgz",
      "integrity": "sha512-SVUsDe+DybHM/WmYKIVYhZh1o5Dcuf16yM6WjG02Q9XVFMZIJyHYhwrr6bFBXZkVP6z69kNkMyBCujt8FaFLJA==",
      "license": "MIT",
      "dependencies": {
        "@remix-run/router": "1.23.3"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "react": ">=16.8"
      }
    },
    "node_modules/react-router-dom": {
      "version": "6.30.4",
      "resolved": "https://registry.npmjs.org/react-router-dom/-/react-router-dom-6.30.4.tgz",
      "integrity": "sha512-q4HvNl+mmDdkS0g+MqiBZNteQJCuimWoOyHMy4T/RQLAn9Z29+E91QXRaxOujeMl2HTzRSS0KFPd7lxX3PjV0Q==",
      "license": "MIT",
      "dependencies": {
        "@remix-run/router": "1.23.3",
        "react-router": "6.30.4"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "react": ">=16.8",
        "react-dom": ">=16.8"
      }
    },
    "node_modules/react-smooth": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/react-smooth/-/react-smooth-4.0.4.tgz",
      "integrity": "sha512-gnGKTpYwqL0Iii09gHobNolvX4Kiq4PKx6eWBCYYix+8cdw+cGo3do906l1NBPKkSWx1DghC1dlWG9L2uGd61Q==",
      "license": "MIT",
      "dependencies": {
        "fast-equals": "^5.0.1",
        "prop-types": "^15.8.1",
        "react-transition-group": "^4.4.5"
      },
      "peerDependencies": {
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0",
        "react-dom": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/react-transition-group": {
      "version": "4.4.5",
      "resolved": "https://registry.npmjs.org/react-transition-group/-/react-transition-group-4.4.5.tgz",
      "integrity": "sha512-pZcd1MCJoiKiBR2NRxeCRg13uCXbydPnmB4EOeRrY7480qNWO8IIgQG6zlDkm6uRMsURXPuKq0GWtiM59a5Q6g==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "@babel/runtime": "^7.5.5",
        "dom-helpers": "^5.0.1",
        "loose-envify": "^1.4.0",
        "prop-types": "^15.6.2"
      },
      "peerDependencies": {
        "react": ">=16.6.0",
        "react-dom": ">=16.6.0"
      }
    },
    "node_modules/read-cache": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/read-cache/-/read-cache-1.0.0.tgz",
      "integrity": "sha512-Owdv/Ft7IjOgm/i0xvNDZ1LrRANRfew4b2prF3OWMQLxLfu3bS8FVhCsrSCMK4lR56Y9ya+AThoTpDCTxCmpRA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "pify": "^2.3.0"
      }
    },
    "node_modules/readdirp": {
      "version": "3.6.0",
      "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz",
      "integrity": "sha512-hOS089on8RduqdbhvQ5Z37A0ESjsqz6qnRcffsMU3495FuTdqSm+7bhJ29JvIOsBDEEnan5DPu9t3To9VRlMzA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "picomatch": "^2.2.1"
      },
      "engines": {
        "node": ">=8.10.0"
      }
    },
    "node_modules/recharts": {
      "version": "2.15.4",
      "resolved": "https://registry.npmjs.org/recharts/-/recharts-2.15.4.tgz",
      "integrity": "sha512-UT/q6fwS3c1dHbXv2uFgYJ9BMFHu3fwnd7AYZaEQhXuYQ4hgsxLvsUXzGdKeZrW5xopzDCvuA2N41WJ88I7zIw==",
      "deprecated": "1.x and 2.x branches are no longer active. Bump to Recharts v3 to receive latest features and bugfixes. See https://github.com/recharts/recharts/wiki/3.0-migration-guide",
      "license": "MIT",
      "dependencies": {
        "clsx": "^2.0.0",
        "eventemitter3": "^4.0.1",
        "lodash": "^4.17.21",
        "react-is": "^18.3.1",
        "react-smooth": "^4.0.4",
        "recharts-scale": "^0.4.4",
        "tiny-invariant": "^1.3.1",
        "victory-vendor": "^36.6.8"
      },
      "engines": {
        "node": ">=14"
      },
      "peerDependencies": {
        "react": "^16.0.0 || ^17.0.0 || ^18.0.0 || ^19.0.0",
        "react-dom": "^16.0.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/recharts-scale": {
      "version": "0.4.5",
      "resolved": "https://registry.npmjs.org/recharts-scale/-/recharts-scale-0.4.5.tgz",
      "integrity": "sha512-kivNFO+0OcUNu7jQquLXAxz1FIwZj8nrj+YkOKc5694NbjCvcT6aSZiIzNzd2Kul4o4rTto8QVR9lMNtxD4G1w==",
      "license": "MIT",
      "dependencies": {
        "decimal.js-light": "^2.4.1"
      }
    },
    "node_modules/resolve": {
      "version": "1.22.12",
      "resolved": "https://registry.npmjs.org/resolve/-/resolve-1.22.12.tgz",
      "integrity": "sha512-TyeJ1zif53BPfHootBGwPRYT1RUt6oGWsaQr8UyZW/eAm9bKoijtvruSDEmZHm92CwS9nj7/fWttqPCgzep8CA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "is-core-module": "^2.16.1",
        "path-parse": "^1.0.7",
        "supports-preserve-symlinks-flag": "^1.0.0"
      },
      "bin": {
        "resolve": "bin/resolve"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/reusify": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
      "integrity": "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "iojs": ">=1.0.0",
        "node": ">=0.10.0"
      }
    },
    "node_modules/rollup": {
      "version": "4.62.2",
      "resolved": "https://registry.npmjs.org/rollup/-/rollup-4.62.2.tgz",
      "integrity": "sha512-RFnrW4lhXA3s3eqHDZvN654g8OTjzRfqpIRJYczCGB6HzphckVAi/Qh4tbPUbRuDi7s1Llv8g/NspLkttY3gTA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/estree": "1.0.9"
      },
      "bin": {
        "rollup": "dist/bin/rollup"
      },
      "engines": {
        "node": ">=18.0.0",
        "npm": ">=8.0.0"
      },
      "optionalDependencies": {
        "@rollup/rollup-android-arm-eabi": "4.62.2",
        "@rollup/rollup-android-arm64": "4.62.2",
        "@rollup/rollup-darwin-arm64": "4.62.2",
        "@rollup/rollup-darwin-x64": "4.62.2",
        "@rollup/rollup-freebsd-arm64": "4.62.2",
        "@rollup/rollup-freebsd-x64": "4.62.2",
        "@rollup/rollup-linux-arm-gnueabihf": "4.62.2",
        "@rollup/rollup-linux-arm-musleabihf": "4.62.2",
        "@rollup/rollup-linux-arm64-gnu": "4.62.2",
        "@rollup/rollup-linux-arm64-musl": "4.62.2",
        "@rollup/rollup-linux-loong64-gnu": "4.62.2",
        "@rollup/rollup-linux-loong64-musl": "4.62.2",
        "@rollup/rollup-linux-ppc64-gnu": "4.62.2",
        "@rollup/rollup-linux-ppc64-musl": "4.62.2",
        "@rollup/rollup-linux-riscv64-gnu": "4.62.2",
        "@rollup/rollup-linux-riscv64-musl": "4.62.2",
        "@rollup/rollup-linux-s390x-gnu": "4.62.2",
        "@rollup/rollup-linux-x64-gnu": "4.62.2",
        "@rollup/rollup-linux-x64-musl": "4.62.2",
        "@rollup/rollup-openbsd-x64": "4.62.2",
        "@rollup/rollup-openharmony-arm64": "4.62.2",
        "@rollup/rollup-win32-arm64-msvc": "4.62.2",
        "@rollup/rollup-win32-ia32-msvc": "4.62.2",
        "@rollup/rollup-win32-x64-gnu": "4.62.2",
        "@rollup/rollup-win32-x64-msvc": "4.62.2",
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/run-parallel": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
      "integrity": "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "queue-microtask": "^1.2.2"
      }
    },
    "node_modules/scheduler": {
      "version": "0.23.2",
      "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.23.2.tgz",
      "integrity": "sha512-UOShsPwz7NrMUqhR6t0hWjFduvOzbtv7toDH1/hIrfRNIDBnnBWd0CwJTGvTpngVlmwGCdP9/Zl/tVrDqcuYzQ==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.1.0"
      }
    },
    "node_modules/semver": {
      "version": "6.3.1",
      "resolved": "https://registry.npmjs.org/semver/-/semver-6.3.1.tgz",
      "integrity": "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA==",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      }
    },
    "node_modules/source-map-js": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz",
      "integrity": "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==",
      "dev": true,
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/sucrase": {
      "version": "3.35.1",
      "resolved": "https://registry.npmjs.org/sucrase/-/sucrase-3.35.1.tgz",
      "integrity": "sha512-DhuTmvZWux4H1UOnWMB3sk0sbaCVOoQZjv8u1rDoTV0HTdGem9hkAZtl4JZy8P2z4Bg0nT+YMeOFyVr4zcG5Tw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.3.2",
        "commander": "^4.0.0",
        "lines-and-columns": "^1.1.6",
        "mz": "^2.7.0",
        "pirates": "^4.0.1",
        "tinyglobby": "^0.2.11",
        "ts-interface-checker": "^0.1.9"
      },
      "bin": {
        "sucrase": "bin/sucrase",
        "sucrase-node": "bin/sucrase-node"
      },
      "engines": {
        "node": ">=16 || 14 >=14.17"
      }
    },
    "node_modules/supports-preserve-symlinks-flag": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
      "integrity": "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/tailwind-merge": {
      "version": "2.6.1",
      "resolved": "https://registry.npmjs.org/tailwind-merge/-/tailwind-merge-2.6.1.tgz",
      "integrity": "sha512-Oo6tHdpZsGpkKG88HJ8RR1rg/RdnEkQEfMoEk2x1XRI3F1AxeU+ijRXpiVUF4UbLfcxxRGw6TbUINKYdWVsQTQ==",
      "license": "MIT",
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/dcastil"
      }
    },
    "node_modules/tailwindcss": {
      "version": "3.4.19",
      "resolved": "https://registry.npmjs.org/tailwindcss/-/tailwindcss-3.4.19.tgz",
      "integrity": "sha512-3ofp+LL8E+pK/JuPLPggVAIaEuhvIz4qNcf3nA1Xn2o/7fb7s/TYpHhwGDv1ZU3PkBluUVaF8PyCHcm48cKLWQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@alloc/quick-lru": "^5.2.0",
        "arg": "^5.0.2",
        "chokidar": "^3.6.0",
        "didyoumean": "^1.2.2",
        "dlv": "^1.1.3",
        "fast-glob": "^3.3.2",
        "glob-parent": "^6.0.2",
        "is-glob": "^4.0.3",
        "jiti": "^1.21.7",
        "lilconfig": "^3.1.3",
        "micromatch": "^4.0.8",
        "normalize-path": "^3.0.0",
        "object-hash": "^3.0.0",
        "picocolors": "^1.1.1",
        "postcss": "^8.4.47",
        "postcss-import": "^15.1.0",
        "postcss-js": "^4.0.1",
        "postcss-load-config": "^4.0.2 || ^5.0 || ^6.0",
        "postcss-nested": "^6.2.0",
        "postcss-selector-parser": "^6.1.2",
        "resolve": "^1.22.8",
        "sucrase": "^3.35.0"
      },
      "bin": {
        "tailwind": "lib/cli.js",
        "tailwindcss": "lib/cli.js"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/thenify": {
      "version": "3.3.1",
      "resolved": "https://registry.npmjs.org/thenify/-/thenify-3.3.1.tgz",
      "integrity": "sha512-RVZSIV5IG10Hk3enotrhvz0T9em6cyHBLkH/YAZuKqd8hRkKhSfCGIcP2KUY0EPxndzANBmNllzWPwak+bheSw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "any-promise": "^1.0.0"
      }
    },
    "node_modules/thenify-all": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/thenify-all/-/thenify-all-1.6.0.tgz",
      "integrity": "sha512-RNxQH/qI8/t3thXJDwcstUO4zeqo64+Uy/+sNVRBx4Xn2OX+OZ9oP+iJnNFqplFra2ZUVeKCSa2oVWi3T4uVmA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "thenify": ">= 3.1.0 < 4"
      },
      "engines": {
        "node": ">=0.8"
      }
    },
    "node_modules/tiny-invariant": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/tiny-invariant/-/tiny-invariant-1.3.3.tgz",
      "integrity": "sha512-+FbBPE1o9QAYvviau/qC5SE3caw21q3xkvWKBtja5vgqOWIHHJ3ioaq1VPfn/Szqctz2bU/oYeKd9/z5BL+PVg==",
      "license": "MIT"
    },
    "node_modules/tinyglobby": {
      "version": "0.2.17",
      "resolved": "https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.17.tgz",
      "integrity": "sha512-wXR/dYpcqKmfWpEdZjiKJOwCNFndD0DMnrW/cYjVGttEkBfVgcLFHoNrlj47mjOVic9yyNu65alsgF4NQyTa2g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fdir": "^6.5.0",
        "picomatch": "^4.0.4"
      },
      "engines": {
        "node": ">=12.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/SuperchupuDev"
      }
    },
    "node_modules/tinyglobby/node_modules/fdir": {
      "version": "6.5.0",
      "resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
      "integrity": "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12.0.0"
      },
      "peerDependencies": {
        "picomatch": "^3 || ^4"
      },
      "peerDependenciesMeta": {
        "picomatch": {
          "optional": true
        }
      }
    },
    "node_modules/tinyglobby/node_modules/picomatch": {
      "version": "4.0.5",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.5.tgz",
      "integrity": "sha512-RvwwcruNjI1ncT5xRakeyS9Lf8lcItv34KD+aif+VH9kduAyfYBipGh12274xtenIPZ119/R9BdTBa8gAwSh0A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-number": "^7.0.0"
      },
      "engines": {
        "node": ">=8.0"
      }
    },
    "node_modules/ts-interface-checker": {
      "version": "0.1.13",
      "resolved": "https://registry.npmjs.org/ts-interface-checker/-/ts-interface-checker-0.1.13.tgz",
      "integrity": "sha512-Y/arvbn+rrz3JCKl9C4kVNfTfSm2/mEp5FSz5EsZSANGPSlQrpRI5M4PKF+mJnE52jOO90PnPSc3Ur3bTQw0gA==",
      "dev": true,
      "license": "Apache-2.0"
    },
    "node_modules/typescript": {
      "version": "5.9.3",
      "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz",
      "integrity": "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "tsc": "bin/tsc",
        "tsserver": "bin/tsserver"
      },
      "engines": {
        "node": ">=14.17"
      }
    },
    "node_modules/update-browserslist-db": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.2.3.tgz",
      "integrity": "sha512-Js0m9cx+qOgDxo0eMiFGEueWztz+d4+M3rGlmKPT+T4IS/jP4ylw3Nwpu6cpTTP8R1MAC1kF4VbdLt3ARf209w==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "escalade": "^3.2.0",
        "picocolors": "^1.1.1"
      },
      "bin": {
        "update-browserslist-db": "cli.js"
      },
      "peerDependencies": {
        "browserslist": ">= 4.21.0"
      }
    },
    "node_modules/util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/victory-vendor": {
      "version": "36.9.2",
      "resolved": "https://registry.npmjs.org/victory-vendor/-/victory-vendor-36.9.2.tgz",
      "integrity": "sha512-PnpQQMuxlwYdocC8fIJqVXvkeViHYzotI+NJrCuav0ZYFoq912ZHBk3mCeuj+5/VpodOjPe1z0Fk2ihgzlXqjQ==",
      "license": "MIT AND ISC",
      "dependencies": {
        "@types/d3-array": "^3.0.3",
        "@types/d3-ease": "^3.0.0",
        "@types/d3-interpolate": "^3.0.1",
        "@types/d3-scale": "^4.0.2",
        "@types/d3-shape": "^3.1.0",
        "@types/d3-time": "^3.0.0",
        "@types/d3-timer": "^3.0.0",
        "d3-array": "^3.1.6",
        "d3-ease": "^3.0.1",
        "d3-interpolate": "^3.0.1",
        "d3-scale": "^4.0.2",
        "d3-shape": "^3.1.0",
        "d3-time": "^3.0.0",
        "d3-timer": "^3.0.1"
      }
    },
    "node_modules/vite": {
      "version": "5.4.21",
      "resolved": "https://registry.npmjs.org/vite/-/vite-5.4.21.tgz",
      "integrity": "sha512-o5a9xKjbtuhY6Bi5S3+HvbRERmouabWbyUcpXXUA1u+GNUKoROi9byOJ8M0nHbHYHkYICiMlqxkg1KkYmm25Sw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "esbuild": "^0.21.3",
        "postcss": "^8.4.43",
        "rollup": "^4.20.0"
      },
      "bin": {
        "vite": "bin/vite.js"
      },
      "engines": {
        "node": "^18.0.0 || >=20.0.0"
      },
      "funding": {
        "url": "https://github.com/vitejs/vite?sponsor=1"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.3"
      },
      "peerDependencies": {
        "@types/node": "^18.0.0 || >=20.0.0",
        "less": "*",
        "lightningcss": "^1.21.0",
        "sass": "*",
        "sass-embedded": "*",
        "stylus": "*",
        "sugarss": "*",
        "terser": "^5.4.0"
      },
      "peerDependenciesMeta": {
        "@types/node": {
          "optional": true
        },
        "less": {
          "optional": true
        },
        "lightningcss": {
          "optional": true
        },
        "sass": {
          "optional": true
        },
        "sass-embedded": {
          "optional": true
        },
        "stylus": {
          "optional": true
        },
        "sugarss": {
          "optional": true
        },
        "terser": {
          "optional": true
        }
      }
    },
    "node_modules/yallist": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz",
      "integrity": "sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g==",
      "dev": true,
      "license": "ISC"
    }
  }
}
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
    "tailwind-merge": "^2.0.0",
    "leaflet": "^1.9.4",
    "react-leaflet": "^4.2.1"
  },
  "devDependencies": {
    "@types/leaflet": "^1.9.12",
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

## mosquitto\mosquitto.conf

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
    charger_id VARCHAR(50),
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ,
    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    energy_consumed_kwh DOUBLE PRECISION DEFAULT 0.0,
    starting_soc DOUBLE PRECISION DEFAULT 0.0,
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
```

---

## ml\.gitignore

```
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
*.log
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

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

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
#   For a library or app, you might want to share your .python-version.
#   For a library or app, you might want to share your .python-version.
#   For a library or app, you might want to share your .python-version.
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if delegates have different system versions of python,
#   this may cause dependency resolution issues.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, poetry.lock contains specific versions of dependencies
#   poetry.lock

# pdm
#   Similar to Pipfile.lock, pdm.lock contains specific versions of dependencies
#pdm.lock
#   pdm local configuration
.pdm-python.path
.pdm-build/

# PEP 582; used by e.g. github.com/lincolnloop/layman and pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

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

# pytype static analyzer
.pytype/

# Cython debug symbols
cython_debug/

# IDE files
.vscode/
.idea/
.project
.pydevproject
.settings/

# Large Datasets and Models (Optional but recommended for clean Git repos)
# If you want to force users to generate data/models locally instead of pulling large binary files:
# ai_ml/data/raw/*.csv
# ai_ml/data/processed/*.csv
# ai_ml/data/processed/*.json
# ai_ml/models/*.joblib

# Raw Downloaded Battery Data
ai_ml/5.+Battery+Data+Set/
```

---

## ml\README.md

```markdown
# AI/ML Module — Industrial EV Intelligence Platform

## Overview

This module contains all AI/ML components for the Industrial EV Supply Chain & Asset Intelligence platform (Member 3 deliverables).

## Project Structure

```
ai_ml/
|-- data/
|   |-- raw/                            # Raw datasets
|   |   |-- battery/                    # NASA Battery PCoE format data
|   |   |-- cmapss/                     # NASA C-MAPSS format data
|   |   |-- dataset_metadata.json       # Dataset documentation
|   |-- processed/                      # Processed outputs
|       |-- battery_features_*.csv      # Engineered features
|       |-- battery_anomaly_scores.csv  # Anomaly detection results
|       |-- battery_predictions.csv     # SoH + RUL predictions
|       |-- supply_chain_*.json/csv     # Supply chain risk scores
|       |-- carbon_analysis.json        # Carbon intelligence results
|       |-- maintenance_*.json          # Maintenance recommendations
|       |-- fleet_readiness_*.json      # Electrification readiness
|       |-- simulated_telemetry.json    # Simulator output
|
|-- models/                             # Trained ML models
|   |-- anomaly_detector.joblib         # Isolation Forest model
|   |-- soh_model.joblib                # XGBoost SoH model
|   |-- rul_model.joblib                # XGBoost RUL model
|   |-- *_scaler.joblib                 # Feature scalers
|   |-- *_metadata.json                 # Model metadata
|
|-- preprocessing/
|   |-- generate_datasets.py            # NASA-format data generator
|   |-- pipeline.py                     # Data cleaning & feature engineering
|
|-- simulator/
|   |-- ev_telemetry_simulator.py       # Real-time EV fleet simulator
|
|-- engines/
|   |-- anomaly_detector.py             # Isolation Forest anomaly detection
|   |-- battery_predictor.py            # XGBoost SoH + RUL prediction
|   |-- risk_scorer.py                  # Supply chain risk scoring
|   |-- carbon_engine.py                # CO2 emission calculations
|   |-- maintenance_engine.py           # Maintenance recommendations
|   |-- readiness_scorer.py             # Fleet electrification readiness
|
|-- run_all.py                          # Master pipeline runner
|-- requirements.txt                    # Python dependencies
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the entire pipeline (generates data, trains models, runs all engines)
python run_all.py

# Or run individual components:
python preprocessing/generate_datasets.py    # Generate datasets
python preprocessing/pipeline.py             # Preprocess data
python engines/anomaly_detector.py           # Train anomaly detector
python engines/battery_predictor.py          # Train battery predictor
python engines/risk_scorer.py                # Run risk scoring
python engines/carbon_engine.py              # Run carbon analysis
python engines/maintenance_engine.py         # Run maintenance engine
python engines/readiness_scorer.py           # Run readiness scorer

# Run the telemetry simulator
python simulator/ev_telemetry_simulator.py --vehicles 10 --duration 30
python simulator/ev_telemetry_simulator.py --mode file --vehicles 50 --duration 60
python simulator/ev_telemetry_simulator.py --mode mqtt --mqtt-host localhost
```

## AI Models Summary

| Model | Algorithm | Target | Accuracy |
|-------|-----------|--------|----------|
| Anomaly Detector | Isolation Forest | Anomalous battery behavior | ~95% detection |
| SoH Predictor | XGBoost | Battery State of Health (%) | R2 > 0.99 |
| RUL Predictor | XGBoost | Remaining Useful Life (cycles) | RMSE < 15 cycles |

## Engines Summary

| Engine | Purpose | Output |
|--------|---------|--------|
| Anomaly Detector | Detect thermal spikes, voltage anomalies | Anomaly scores, alert types |
| Battery Predictor | Predict SoH and RUL | Health %, remaining cycles |
| Risk Scorer | Score supply chain risk | Risk scores 0-100 per supplier |
| Carbon Engine | Calculate CO2 savings | Diesel vs EV emission comparison |
| Maintenance Engine | Recommend maintenance | Priority actions, scheduling |
| Readiness Scorer | Score fleet EV readiness | Readiness score per route |

---

## Backend Integration Guide

### What Member 4 needs to set up:

#### 1. Docker Compose Infrastructure

```yaml
# docker-compose.yml
version: '3.8'
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: ev_intelligence
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin123
    ports:
      - "5432:5432"

  timescaledb:
    image: timescale/timescaledb:latest-pg15
    environment:
      POSTGRES_DB: ev_telemetry
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin123
    ports:
      - "5433:5432"

  neo4j:
    image: neo4j:5
    environment:
      NEO4J_AUTH: neo4j/password123
    ports:
      - "7474:7474"
      - "7687:7687"

  zookeeper:
    image: confluentinc/cp-zookeeper:7.5.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka:7.5.0
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1

  mosquitto:
    image: eclipse-mosquitto:2
    ports:
      - "1883:1883"
    volumes:
      - ./mosquitto/config:/mosquitto/config
```

#### 2. Kafka Topics to Create

```bash
# Battery telemetry
kafka-topics --create --topic ev.battery --bootstrap-server localhost:9092

# Charging sessions
kafka-topics --create --topic ev.charging --bootstrap-server localhost:9092

# Vehicle location
kafka-topics --create --topic ev.location --bootstrap-server localhost:9092

# Temperature data
kafka-topics --create --topic ev.temperature --bootstrap-server localhost:9092

# Alerts & anomalies
kafka-topics --create --topic ev.alerts --bootstrap-server localhost:9092
```

#### 3. TimescaleDB Schema

```sql
-- Create hypertable for telemetry
CREATE TABLE telemetry (
    time        TIMESTAMPTZ NOT NULL,
    vehicle_id  TEXT NOT NULL,
    soc         DOUBLE PRECISION,
    voltage     DOUBLE PRECISION,
    current     DOUBLE PRECISION,
    temperature DOUBLE PRECISION,
    soh         DOUBLE PRECISION,
    speed       DOUBLE PRECISION,
    latitude    DOUBLE PRECISION,
    longitude   DOUBLE PRECISION,
    is_charging BOOLEAN,
    anomaly_score DOUBLE PRECISION
);

SELECT create_hypertable('telemetry', 'time');
```

#### 4. Neo4j Graph Setup

```cypher
// Create supply chain graph
// Load from ai_ml/data/processed/supply_chain_graph.json

// Create supplier nodes
CREATE (s:Supplier {id: 'S001', name: 'CobaltCo DRC', type: 'mine', country: 'DRC'})
CREATE (s:Supplier {id: 'S002', name: 'LithiumEx Chile', type: 'mine', country: 'CHL'})
// ... (load all nodes from supply_chain_graph.json)

// Create relationships
MATCH (a:Supplier {id: 'S001'}), (b:Supplier {id: 'R001'})
CREATE (a)-[:SUPPLIES {material: 'cobalt'}]->(b)
// ... (load all edges from supply_chain_graph.json)
```

#### 5. Connecting the Simulator to MQTT/Kafka

Once Mosquitto is running, use the simulator in MQTT mode:

```bash
# Start simulator with MQTT output
python simulator/ev_telemetry_simulator.py --mode mqtt --mqtt-host localhost --mqtt-port 1883 --vehicles 50 --duration 3600
```

The simulator publishes to these MQTT topics:
- `ev/battery/{vehicle_id}` - Battery telemetry
- `ev/vehicle/{vehicle_id}` - Vehicle status
- `ev/charging/{vehicle_id}` - Charging sessions
- `ev/alerts/{vehicle_id}` - Anomaly alerts

Member 4 should create a Kafka consumer that:
1. Subscribes to MQTT topics
2. Forwards messages to Kafka topics
3. Kafka consumers write to TimescaleDB

#### 6. Storing ML Predictions in PostgreSQL

```sql
-- Battery predictions table
CREATE TABLE battery_predictions (
    id SERIAL PRIMARY KEY,
    vehicle_id TEXT NOT NULL,
    predicted_at TIMESTAMPTZ DEFAULT NOW(),
    soh_percent DOUBLE PRECISION,
    rul_cycles DOUBLE PRECISION,
    health_status TEXT,
    urgency TEXT,
    anomaly_score DOUBLE PRECISION,
    is_anomaly BOOLEAN
);

-- Supply chain risk scores
CREATE TABLE supply_chain_risk (
    supplier_id TEXT PRIMARY KEY,
    supplier_name TEXT,
    risk_score DOUBLE PRECISION,
    risk_level TEXT,
    political_risk DOUBLE PRECISION,
    concentration_risk DOUBLE PRECISION,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Maintenance recommendations
CREATE TABLE maintenance_schedule (
    id SERIAL PRIMARY KEY,
    vehicle_id TEXT NOT NULL,
    priority TEXT,
    scheduled_date DATE,
    actions JSONB,
    estimated_cost DOUBLE PRECISION,
    reasoning TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### What to Change in AI/ML Code for Integration:

1. **Simulator**: Change `--mode console` to `--mode mqtt` once Mosquitto is running
2. **Anomaly Detector**: Load model from `models/` directory and run `.predict()` on incoming telemetry
3. **Battery Predictor**: Load model and run `.predict_full()` for each vehicle
4. **Risk Scorer**: Load supply chain graph from Neo4j instead of hardcoded data
5. **All Engines**: Member 2 (Backend) will wrap these engines in FastAPI endpoints

### API Integration Points for Member 2 (Backend):

```python
# Example FastAPI integration
from engines.anomaly_detector import AnomalyDetector
from engines.battery_predictor import BatteryHealthPredictor
from engines.risk_scorer import SupplyChainRiskScorer
from engines.carbon_engine import CarbonIntelligenceEngine
from engines.maintenance_engine import MaintenanceRecommendationEngine
from engines.readiness_scorer import FleetReadinessScorer

# Load trained models
anomaly = AnomalyDetector()
anomaly.load('models/')

predictor = BatteryHealthPredictor()
predictor.load('models/')

# Use in API endpoints
@app.post("/predict/soh")
def predict_soh(data: dict):
    return predictor.predict_soh(data)

@app.post("/predict/rul")
def predict_rul(data: dict):
    return predictor.predict_rul(data)

@app.post("/predict/anomaly")
def predict_anomaly(data: dict):
    return anomaly.predict(data)
```

## Using Real NASA Datasets

To replace synthetic data with real NASA datasets:

1. Download from https://ti.arc.nasa.gov/c/5/ (Battery PCoE)
2. Download from https://ti.arc.nasa.gov/c/6/ (C-MAPSS)
3. For .mat files, use this conversion:

```python
from scipy.io import loadmat
import pandas as pd

data = loadmat('battery_data.mat')
# Extract and convert to DataFrame
# Save as CSV to data/raw/battery/nasa_battery_data.csv
```

4. Re-run `python run_all.py` to retrain models with real data
```

---

## ml\requirements.txt

```text
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
xgboost>=2.0.0
joblib>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
paho-mqtt>=1.6.0
faker>=19.0.0
scipy>=1.11.0
```

---

## ml\run_all.py

```python
"""
Master Pipeline Runner
======================
Runs the entire AI/ML pipeline end-to-end:
1. Generate datasets
2. Preprocess data
3. Train anomaly detector
4. Train battery predictor (SoH + RUL)
5. Run supply chain risk scoring
6. Run carbon intelligence analysis
7. Run maintenance recommendations
8. Run fleet readiness assessment
9. Run telemetry simulator demo

Usage: python run_all.py
"""

import os
import sys
import time
import json
from datetime import datetime

# Set base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)


def run_step(step_num, title, func):
    """Run a pipeline step with timing."""
    print(f"\n{'#' * 70}")
    print(f"# STEP {step_num}: {title}")
    print(f"{'#' * 70}")
    start = time.time()
    try:
        result = func()
        elapsed = time.time() - start
        print(f"\n[STEP {step_num} COMPLETE] {title} ({elapsed:.1f}s)")
        return result
    except Exception as e:
        elapsed = time.time() - start
        print(f"\n[STEP {step_num} FAILED] {title} ({elapsed:.1f}s)")
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
        return None





def step2_preprocess():
    """Run preprocessing pipeline."""
    from preprocessing.pipeline import BatteryPreprocessor, CMAPSSPreprocessor
    
    raw_dir = os.path.join(BASE_DIR, 'data', 'raw')
    processed_dir = os.path.join(BASE_DIR, 'data', 'processed')
    os.makedirs(processed_dir, exist_ok=True)
    
    # Battery preprocessing
    battery_proc = BatteryPreprocessor()
    battery_path = os.path.join(raw_dir, 'battery', 'nasa_battery_data.csv')
    battery_proc.process(battery_path, processed_dir)
    
    # C-MAPSS preprocessing
    cmapss_path = os.path.join(raw_dir, 'cmapss', 'cmapss_fd001.csv')
    if os.path.exists(cmapss_path):
        cmapss_proc = CMAPSSPreprocessor()
        cmapss_proc.process(cmapss_path, processed_dir)
    else:
        print("\n  [INFO] C-MAPSS dataset (cmapss_fd001.csv) not found in data/raw/cmapss/. Skipping C-MAPSS preprocessing.")


def step3_train_anomaly_detector():
    """Train Isolation Forest anomaly detector."""
    from engines.anomaly_detector import train_and_save
    
    data_path = os.path.join(BASE_DIR, 'data', 'processed', 'battery_features_unscaled.csv')
    model_dir = os.path.join(BASE_DIR, 'models')
    return train_and_save(data_path, model_dir)


def step4_train_battery_predictor():
    """Train XGBoost SoH and RUL models."""
    from engines.battery_predictor import train_and_save
    
    data_path = os.path.join(BASE_DIR, 'data', 'processed', 'battery_features_unscaled.csv')
    model_dir = os.path.join(BASE_DIR, 'models')
    return train_and_save(data_path, model_dir)


def step5_supply_chain_risk():
    """Run supply chain risk scoring."""
    from engines.risk_scorer import SupplyChainRiskScorer
    
    output_dir = os.path.join(BASE_DIR, 'data', 'processed')
    scorer = SupplyChainRiskScorer()
    scorer.save_results(output_dir)


def step6_carbon_intelligence():
    """Run carbon intelligence analysis."""
    from engines.carbon_engine import CarbonIntelligenceEngine
    
    output_dir = os.path.join(BASE_DIR, 'data', 'processed')
    engine = CarbonIntelligenceEngine(grid_region='india')
    engine.save_analysis(output_dir)


def step7_maintenance_recommendations():
    """Run maintenance recommendation engine."""
    from engines.maintenance_engine import MaintenanceRecommendationEngine
    
    output_dir = os.path.join(BASE_DIR, 'data', 'processed')
    engine = MaintenanceRecommendationEngine()
    engine.save_analysis(output_dir)


def step8_fleet_readiness():
    """Run fleet electrification readiness assessment."""
    from engines.readiness_scorer import FleetReadinessScorer
    
    output_dir = os.path.join(BASE_DIR, 'data', 'processed')
    scorer = FleetReadinessScorer()
    scorer.save_assessment(output_dir)


def step9_simulator_demo():
    """Run a short telemetry simulator demo."""
    from simulator.ev_telemetry_simulator import EVFleetSimulator
    
    sim = EVFleetSimulator(num_vehicles=5, output_mode='file')
    sim.run(duration_seconds=6, interval=2.0)


def print_final_summary():
    """Print final summary of all outputs."""
    print(f"\n{'=' * 70}")
    print(f"{'=' * 70}")
    print("   AI/ML PIPELINE COMPLETE - Industrial EV Intelligence Platform")
    print(f"{'=' * 70}")
    print(f"{'=' * 70}")
    
    # List all outputs
    processed_dir = os.path.join(BASE_DIR, 'data', 'processed')
    model_dir = os.path.join(BASE_DIR, 'models')
    
    print(f"\n  PROCESSED DATA ({processed_dir}):")
    if os.path.exists(processed_dir):
        for f in sorted(os.listdir(processed_dir)):
            size = os.path.getsize(os.path.join(processed_dir, f)) / 1024
            print(f"    {f:50s} {size:8.1f} KB")
    
    print(f"\n  TRAINED MODELS ({model_dir}):")
    if os.path.exists(model_dir):
        for f in sorted(os.listdir(model_dir)):
            size = os.path.getsize(os.path.join(model_dir, f)) / 1024
            print(f"    {f:50s} {size:8.1f} KB")
    
    print(f"\n  PIPELINE OUTPUTS:")
    key_outputs = [
        ('Anomaly Scores', 'battery_anomaly_scores.csv'),
        ('Battery Predictions', 'battery_predictions.csv'),
        ('Supply Chain Risk', 'supply_chain_risk_scores.json'),
        ('Cascading Failure', 'cascading_failure_analysis.json'),
        ('Carbon Analysis', 'carbon_analysis.json'),
        ('Maintenance Recs', 'maintenance_recommendations.json'),
        ('Fleet Readiness', 'fleet_readiness_assessment.json'),
        ('Supply Chain Graph', 'supply_chain_graph.json'),
        ('Simulated Telemetry', 'simulated_telemetry.json'),
    ]
    
    for name, filename in key_outputs:
        path = os.path.join(processed_dir, filename)
        status = "OK" if os.path.exists(path) else "MISSING"
        print(f"    [{status:7s}] {name:25s} -> {filename}")
    
    print(f"\n  Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """Run the complete AI/ML pipeline."""
    print("=" * 70)
    print("  Industrial EV AI Platform - Complete AI/ML Pipeline")
    print("  Member 3 Deliverables")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    total_start = time.time()
    
    run_step(1, "Preprocess & Feature Engineering", step2_preprocess)
    run_step(2, "Train Anomaly Detector (Isolation Forest)", step3_train_anomaly_detector)
    run_step(3, "Train Battery Predictor (XGBoost SoH + RUL)", step4_train_battery_predictor)
    run_step(4, "Supply Chain Risk Scoring", step5_supply_chain_risk)
    run_step(5, "Carbon Intelligence Analysis", step6_carbon_intelligence)
    run_step(6, "Maintenance Recommendations", step7_maintenance_recommendations)
    run_step(7, "Fleet Electrification Readiness", step8_fleet_readiness)
    run_step(8, "Telemetry Simulator Demo", step9_simulator_demo)
    
    total_elapsed = time.time() - total_start
    
    print_final_summary()
    print(f"\n  Total pipeline time: {total_elapsed:.1f} seconds")
    print("\n  All Member 3 deliverables complete!")


if __name__ == '__main__':
    main()
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
from pydantic import BaseModel, Field, ConfigDict

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

    # FIX: Updated old custom encoder blocks to Pydantic V2 model_config structure
    model_config = ConfigDict(
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            UUID: lambda v: str(v)
        }
    )
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
from sqlalchemy import text
from app.core.config import settings
from app.models.domain import Base

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

DATABASE_URL = settings.database_url

async def init_db():
    engine = create_async_engine(DATABASE_URL, echo=False)

    async with engine.begin() as conn:
        # Step 1: Initialize standardized base schemas
        await conn.run_sync(Base.metadata.create_all)

        # Step 2: Convert structural physical logs to partitioned hypertables
        hypertable_queries = [
            "ALTER TABLE battery_records ADD COLUMN IF NOT EXISTS cycle_count INTEGER DEFAULT 100;",
            "SELECT create_hypertable('telemetry', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('battery_records', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('location_history', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('alert_records', 'timestamp', if_not_exists => TRUE);"
        ]

        for query in hypertable_queries:
            try:
                await conn.execute(text(query))
            except Exception:
                pass

    await engine.dispose()
    print(">>> TimescaleDB Initialization Matrix Complete <<<")

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
from sqlalchemy import Column, String, Float, DateTime, Integer, JSON, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID  # Required for the UUID column type

Base = declarative_base()

# ---------------------------------------------------------
# TIME-SERIES HYPERTABLE MODELS (High-Frequency Data)
# ---------------------------------------------------------

class TelemetryRecord(Base):
    __tablename__ = "telemetry"

    # Partitioned hypertable composite layout
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    vehicle_id = Column(String(50), nullable=False, index=True)

    # Real kinematic signatures
    speed_kph = Column(Float, nullable=False, name="voltage")  # Map to existing DB column shapes
    odometer_km = Column(Float, nullable=False, name="current")
    motor_temperature_c = Column(Float, nullable=False, name="temperature")
    torque_nm = Column(Float, nullable=False, name="soc")

class BatteryRecord(Base):
    __tablename__ = "battery_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    vehicle_id = Column(String(50), nullable=False, index=True)
    state_of_charge_pct = Column(Float, nullable=False)
    state_of_health_pct = Column(Float, nullable=False)
    voltage = Column(Float, nullable=False)
    current_amps = Column(Float, nullable=False)
    cell_temperature_max_c = Column(Float, nullable=False)
    internal_resistance_ohm = Column(Float, nullable=False)
    cycle_count = Column(Integer, nullable=False, default=100)

class LocationHistory(Base):
    __tablename__ = "location_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)
    vehicle_id = Column(String(50), nullable=False, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    altitude_m = Column(Float, nullable=True)
    heading_deg = Column(Integer, nullable=True)
    gps_fix_quality = Column(String(20), nullable=True)

# ---------------------------------------------------------
# RELATIONAL MODELS (Low-Frequency State Tables)
# ---------------------------------------------------------

class ChargingSession(Base):
    __tablename__ = "charging_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    charger_id = Column(String(50), nullable=True)
    start_time = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    end_time = Column(DateTime(timezone=True), nullable=True)
    status = Column(String(20), nullable=False, default="ACTIVE")
    energy_consumed_kwh = Column(Float, nullable=True, default=0.0)
    starting_soc = Column(Float, nullable=True, default=0.0)
    ending_soc = Column(Float, nullable=True)

class AlertRecord(Base):
    __tablename__ = "alert_records"

    # TimescaleDB requires the time column (timestamp) to be part of the primary key configuration
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow)

    vehicle_id = Column(String(50), nullable=False, index=True)
    severity = Column(String(20), nullable=False, index=True)  # CRITICAL, WARNING, INFO
    alert_type = Column(String(50), nullable=False, index=True)  # THERMAL_RUNAWAY, OVER_VOLTAGE, ANOMALY
    description = Column(String(255), nullable=False)
    resolved = Column(Boolean, default=False, nullable=False)
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
from sqlalchemy import select, desc, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession , AlertRecord

class TelemetryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: TelemetryRecord) -> TelemetryRecord:
        """Stores a single telemetry record."""
        self.session.add(record)
        await self.session.commit()
        return record

    async def bulk_insert(self, records: List[TelemetryRecord]) -> None:
        """Handles high-throughput batch writes efficiently (Requirement 8)."""
        self.session.add_all(records)
        await self.session.commit()

    async def timeseries_aggregation(self, vehicle_id: str, interval: str = "1 minute", limit: int = 24) -> List[Dict[str, Any]]:
        """Uses TimescaleDB's native time_bucket function to aggregate data efficiently."""
        query = text("""
            SELECT
                time_bucket(CAST(CAST(:bucket_interval AS TEXT) AS INTERVAL), timestamp) AS time_bucket,
                AVG(voltage) AS avg_speed,
                MAX(temperature) AS max_motor_temp,
                AVG(soc) AS avg_torque
            FROM telemetry
            WHERE vehicle_id = :vehicle_id
            GROUP BY time_bucket
            ORDER BY time_bucket DESC
            LIMIT :limit;
        """)

        result = await self.session.execute(
            query,
            {
                "bucket_interval": str(interval),
                "vehicle_id": str(vehicle_id),
                "limit": int(limit)
            }
        )

        return [
            {
                "time": row[0].isoformat() if hasattr(row[0], "isoformat") else str(row[0]),
                "avg_speed": round(row[1], 2) if row[1] is not None else 0.0,
                "max_temp": round(row[2], 2) if row[2] is not None else 0.0
            }
            for row in result.fetchall()
        ]

    async def history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Retrieves raw telemetry history lines within an explicit time window."""
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
        return list(result.scalars().all())


class BatteryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: BatteryRecord) -> None:
        self.session.add(record)
        await self.session.commit()

    async def latest(self, vehicle_id: str) -> Optional[BatteryRecord]:
        stmt = (
            select(BatteryRecord)
            .where(BatteryRecord.vehicle_id == vehicle_id)
            .order_by(desc(BatteryRecord.timestamp))
            .limit(1)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()


class LocationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: LocationHistory) -> LocationHistory:
        """High-speed async insert for vehicle coordinates."""
        self.session.add(record)
        await self.session.commit()
        return record

    async def get_latest(self, vehicle_id: str) -> Optional[LocationHistory]:
        """Fetches absolute latest geographic trace coordinate node (Requirement 8)."""
        stmt = (
            select(LocationHistory)
            .where(LocationHistory.vehicle_id == vehicle_id)
            .order_by(desc(LocationHistory.timestamp))
            .limit(1)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def route_playback(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """Retrieves an ordered array of coordinates for spatial path tracking."""
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
        return list(result.scalars().all())


class ChargingRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_session(self, session_record: ChargingSession) -> ChargingSession:
        self.session.add(session_record)
        await self.session.commit()
        await self.session.refresh(session_record)
        return session_record

    async def update_session(self, session_id: int, updates: Dict[str, Any]) -> Optional[ChargingSession]:
        """Applies dynamic PATCH field changes to an active charging entity (Requirement 8)."""
        stmt = (
            update(ChargingSession)
            .where(ChargingSession.id == session_id)
            .values(**updates)
        )
        await self.session.execute(stmt)
        await self.session.commit()

        # Retrieve the updated model record cleanly
        fetch_stmt = select(ChargingSession).where(ChargingSession.id == session_id)
        result = await self.session.execute(fetch_stmt)
        return result.scalar_one_or_none()

    async def get_history(self, vehicle_id: str) -> List[ChargingSession]:
        """Returns historical tracking elements collection sorted chronologically (Requirement 8)."""
        stmt = (
            select(ChargingSession)
            .where(ChargingSession.vehicle_id == vehicle_id)
            .order_by(desc(ChargingSession.start_time))
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

class AlertRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, record: AlertRecord) -> None:
        """High-speed async insert for structured system alerts."""
        self.session.add(record)
        await self.session.commit()

    async def get_active_alerts(self, limit: int = 50) -> List[AlertRecord]:
        """Retrieves currently unresolved critical warnings and failures across the ecosystem."""
        stmt = (
            select(AlertRecord)
            .where(AlertRecord.resolved == False)
            .order_by(desc(AlertRecord.timestamp))
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
```

---

## backend\app\schemas\payloads.py

```python
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field, ConfigDict

class BasePayload(BaseModel):
    """Base configuration allowing both old aliases and new enterprise keys, while keeping extra data."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    # FIX: Added top-level vehicle string tracking requirement to clean up extraction
    vehicle_id: str = Field(default="VEH-SIM-UNKNOWN")

class TelemetryPayload(BasePayload):
    """Kinematic data mapping simulator inputs to system targets with safe defaults."""
    speed_kph: float = Field(default=0.0, validation_alias="speed", ge=0, le=2000.0)
    odometer_km: float = Field(default=0.0, validation_alias="odometer", ge=0)
    # FIX: Increased upper boundary check to 5000.0 to allow extreme thermal anomalies through
    motor_temperature_c: float = Field(default=25.0, validation_alias="ambient_temperature", ge=-40, le=5000.0)
    torque_nm: float = Field(default=0.0, validation_alias="power_output")
    inverter_efficiency: float = Field(default=0.94, ge=0, le=1)

class BatteryPayload(BasePayload):
    """Electro-chemical stats providing field transformations for native simulator outputs."""
    state_of_charge_pct: float = Field(default=0.0, validation_alias="soc", ge=0, le=100)
    state_of_health_pct: float = Field(default=100.0, validation_alias="soh", ge=0, le=100)
    voltage: float = Field(default=0.0, ge=0, le=1000)
    current_amps: float = Field(default=0.0, validation_alias="current")
    # FIX: Relax constraints further to ensure packets aren't dropped during runtime anomalies
    cell_temperature_max_c: float = Field(default=25.0, validation_alias="cell_temperature", ge=-40, le=5000.0)
    internal_resistance_ohm: float = Field(default=0.01, validation_alias="internal_resistance", ge=0)
    cycle_count: int = Field(default=100, validation_alias="cycle_count", ge=0)

class LocationPayload(BasePayload):
    latitude: float = Field(default=39.7392, ge=-90, le=90)
    longitude: float = Field(default=-104.9903, ge=-180, le=180)
    altitude_m: Optional[float] = Field(default=1609.0, ge=-500, le=9000)
    heading_deg: Optional[float] = Field(default=0.0, ge=0, le=360)
    # FIX: Change to str to cleanly capture status strings like '3D_FIX'
    gps_fix_quality: str = Field(default="UNKNOWN")

class ChargingPayload(BasePayload):
    # FIX: Make Optional to safely handle payloads when the EV is discharging instead of charging
    charger_id: Optional[str] = Field(default="CHG-STATION-MOCK")
    charging_rate_kw: float = Field(default=0.0, ge=-200, le=500) # Accept negative numbers during charge state physics
    time_to_full_mins: float = Field(default=0.0, ge=0)
    connector_type: Optional[str] = Field(default="CCS2")

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
from pydantic import BaseModel, ConfigDict
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
    # FIX: Replaced old class Config with Pydantic V2 model_config property
    model_config = ConfigDict(from_attributes=True)

class BatteryHealthResponse(BaseModel):
    vehicle_id: str
    capacity_fade: float
    cycle_count: int
    state_of_health: float
    remaining_useful_life: int
    model_config = ConfigDict(from_attributes=True)

class AlertResponse(BaseModel):
    id: int
    vehicle_id: str
    timestamp: datetime
    severity: str
    type: str
    description: str
    resolved: bool
    model_config = ConfigDict(from_attributes=True)

class SupplierRiskResponse(BaseModel):
    id: int
    name: str
    location: str
    risk_score: float
    material_supplied: str
    model_config = ConfigDict(from_attributes=True)

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

## backend\app\services\ml.py

```python
import os
import sys
import logging
from typing import Dict, Any, List, Optional
import numpy as np

# Resolve paths
# Current file: backend/app/services/ml.py
# Root directory: industrial-ev-ai-platform
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
ML_DIR = os.path.join(ROOT_DIR, "ml")
MODELS_DIR = os.path.join(ML_DIR, "models")

# Add ml folder to sys.path
if ML_DIR not in sys.path:
    sys.path.append(ML_DIR)

logger = logging.getLogger(__name__)

# Lazy initialization placeholders
_anomaly_detector = None
_battery_predictor = None

def get_anomaly_detector():
    """Lazily load and return the pre-trained AnomalyDetector."""
    global _anomaly_detector
    if _anomaly_detector is None:
        try:
            from engines.anomaly_detector import AnomalyDetector
            _anomaly_detector = AnomalyDetector()
            _anomaly_detector.load(MODELS_DIR)
            logger.info("AnomalyDetector engine successfully loaded from models directory.")
        except Exception as e:
            logger.error(f"Critical error loading pre-trained AnomalyDetector: {e}")
            # Fallback mock detector if loading fails
            class FallbackAnomalyDetector:
                def __init__(self):
                    self.is_trained = False
                def predict(self, data: dict):
                    temp = data.get('temperature', 35.0)
                    voltage = data.get('voltage', 380.0)
                    is_anomaly = temp > 45.0 or voltage < 320.0
                    return {
                        'is_anomaly': is_anomaly,
                        'anomaly_score': 0.89 if is_anomaly else 0.05,
                        'anomaly_types': ['thermal_warning' if temp > 45.0 else 'under_voltage'] if is_anomaly else [],
                        'severity': 'high' if is_anomaly else 'normal',
                        'alerts': [f"Fallback: Temp {temp}C exceeds threshold"] if is_anomaly else [],
                        'recommendations': ["Cool battery"] if is_anomaly else []
                    }
            _anomaly_detector = FallbackAnomalyDetector()
    return _anomaly_detector

def get_battery_predictor():
    """Lazily load and return the pre-trained BatteryHealthPredictor."""
    global _battery_predictor
    if _battery_predictor is None:
        try:
            from engines.battery_predictor import BatteryHealthPredictor
            _battery_predictor = BatteryHealthPredictor()
            _battery_predictor.load(MODELS_DIR)
            logger.info("BatteryHealthPredictor engine successfully loaded from models directory.")
        except Exception as e:
            logger.error(f"Critical error loading pre-trained BatteryHealthPredictor: {e}")
            # Fallback mock predictor if loading fails
            class FallbackBatteryPredictor:
                def __init__(self):
                    self.soh_trained = False
                    self.rul_trained = False
                def predict_soh(self, data: dict):
                    capacity = data.get('capacity_ah', 114.0)
                    soh = (capacity / 120.0) * 100.0
                    return {
                        'soh_percent': round(soh, 2),
                        'health_status': 'good' if soh >= 85 else 'fair',
                        'recommendation': 'Fallback prediction: Battery is healthy.',
                        'confidence': 90.0
                    }
                def predict_rul(self, data: dict):
                    cycle = data.get('cycle', 100)
                    rul = max(0, 1500 - cycle)
                    return {
                        'rul_cycles': rul,
                        'estimated_days': round(rul / 2),
                        'urgency': 'low' if rul > 200 else 'medium',
                        'action': 'Fallback prediction: No actions required.',
                        'confidence': 90.0
                    }
                def predict_full(self, data: dict):
                    return {
                        'soh': self.predict_soh(data),
                        'rul': self.predict_rul(data)
                    }
            _battery_predictor = FallbackBatteryPredictor()
    return _battery_predictor

def prepare_features_from_records(records: List[Any], current_payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Constructs a complete ML feature dictionary mapping the 26 statistical/rolling features 
    expected by the pre-trained models from database records and/or active payload.
    """
    # Default/Baseline feature values
    data = {
        'cycle': 100,
        'capacity_ah': 114.0,
        'avg_voltage_v': 380.0,
        'voltage_charged_v': 400.0,
        'voltage_discharged_v': 350.0,
        'charge_current_a': 0.0,
        'discharge_current_a': 10.0,
        'avg_temperature_c': 35.0,
        'max_temperature_c': 38.0,
        'internal_resistance_ohm': 0.04,
        'charge_transfer_resistance_ohm': 0.05,
        'discharge_time_s': 3600.0,
        'charge_efficiency_percent': 95.0,
        'discharge_slope_v_per_s': -0.001,
        'capacity_degradation_rate': -0.005,
        'cumulative_capacity_loss': 6.0,
        'resistance_growth_rate': 0.0001,
        'temp_rolling_mean': 35.0,
        'temp_rolling_std': 1.0,
        'thermal_variance': 1.0,
        'voltage_spread': 50.0,
        'capacity_rolling_std': 0.5,
        'efficiency_drop': 0.0,
        'discharge_rate': 114.0,
        'impedance_ratio': 1.25,
        'cycle_age_normalized': 0.1
    }
    
    if current_payload:
        data['cycle'] = current_payload.get('cycle_count', current_payload.get('cycle', data['cycle']))
        data['avg_voltage_v'] = current_payload.get('voltage', data['avg_voltage_v'])
        data['avg_temperature_c'] = current_payload.get('temperature', data['avg_temperature_c'])
        data['internal_resistance_ohm'] = current_payload.get('internal_resistance', data['internal_resistance_ohm'])
        
        soh_val = current_payload.get('soh', current_payload.get('state_of_health', current_payload.get('state_of_health_pct', 95.0)))
        data['capacity_ah'] = (soh_val / 100.0) * 120.0
        
        current_val = current_payload.get('current', current_payload.get('current_amps', 0.0))
        if current_val > 0:
            data['charge_current_a'] = current_val
            data['discharge_current_a'] = 0.0
        else:
            data['charge_current_a'] = 0.0
            data['discharge_current_a'] = abs(current_val)
            
    if not records:
        return data

    # Extract historical fields from timeseries BatteryRecords
    voltages = [r.voltage for r in records]
    temps = [r.cell_temperature_max_c for r in records]
    currents = [r.current_amps for r in records]
    resistances = [r.internal_resistance_ohm for r in records]
    sohs = [r.state_of_health_pct for r in records]
    cycles = [getattr(r, 'cycle_count', 100) for r in records]
    
    # Calculate rolling features
    data['cycle'] = cycles[0]
    data['capacity_ah'] = (sohs[0] / 100.0) * 120.0
    data['avg_voltage_v'] = sum(voltages) / len(voltages)
    data['voltage_charged_v'] = max(voltages)
    data['voltage_discharged_v'] = min(voltages)
    
    pos_currents = [c for c in currents if c > 0]
    neg_currents = [c for c in currents if c < 0]
    data['charge_current_a'] = max(pos_currents) if pos_currents else 0.0
    data['discharge_current_a'] = abs(min(neg_currents)) if neg_currents else 10.0
    
    data['avg_temperature_c'] = sum(temps) / len(temps)
    data['max_temperature_c'] = max(temps)
    data['internal_resistance_ohm'] = resistances[0]
    data['charge_transfer_resistance_ohm'] = resistances[0] * 1.2
    
    if len(temps) > 1:
        data['temp_rolling_mean'] = sum(temps) / len(temps)
        data['temp_rolling_std'] = float(np.std(temps))
        data['thermal_variance'] = float(np.var(temps))
    
    data['voltage_spread'] = max(voltages) - min(voltages)
    
    if len(sohs) > 1:
        capacities = [(s / 100.0) * 120.0 for s in sohs]
        data['capacity_rolling_std'] = float(np.std(capacities))
        
        cycle_diff = max(1, cycles[0] - cycles[-1])
        data['capacity_degradation_rate'] = (capacities[0] - capacities[-1]) / cycle_diff
        data['cumulative_capacity_loss'] = 120.0 - capacities[0]
        data['resistance_growth_rate'] = (resistances[0] - resistances[-1]) / cycle_diff
        
    data['discharge_rate'] = data['capacity_ah'] / (data['discharge_time_s'] / 3600.0)
    data['impedance_ratio'] = data['charge_transfer_resistance_ohm'] / max(0.001, data['internal_resistance_ohm'])
    data['cycle_age_normalized'] = min(1.0, data['cycle'] / 1000.0)
    
    return data
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

    async def store_telemetry(self, record: TelemetryRecord) -> TelemetryRecord:
        """Stores a raw manual telemetry record (Requirement 9)."""
        return await self.repo.insert(record)

    async def get_history(self, vehicle_id: str, start_time: datetime, end_time: datetime, limit: int = 100) -> List[TelemetryRecord]:
        """Validates the time window before fetching raw kinematic history."""
        validate_time_window(start_time, end_time, max_days=30)
        return await self.repo.history(vehicle_id, start_time, end_time, limit)

    async def get_timeseries(self, vehicle_id: str, interval: str = "1 hour", limit: int = 24) -> List[Dict[str, Any]]:
        """Pass-through for aggregated time-series data."""
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
        """Battery degradation analytics window over a longer timeframe."""
        validate_time_window(start_time, end_time, max_days=90)
        return await self.repo.degradation_history(vehicle_id, start_time, end_time)


class LocationService:
    def __init__(self, session: AsyncSession):
        self.repo = LocationRepository(session)

    async def store_location(self, record: LocationHistory) -> LocationHistory:
        """Stores a manual GPS coordinate update (Requirement 9)."""
        return await self.repo.insert(record)

    async def get_latest_location(self, vehicle_id: str) -> Optional[LocationHistory]:
        """Retrieves the latest known vehicle position (Requirement 9)."""
        record = await self.repo.get_latest(vehicle_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"No location metrics found for vehicle {vehicle_id}")
        return record

    async def get_route(self, vehicle_id: str, start_time: datetime, end_time: datetime) -> List[LocationHistory]:
        """GPS route playback engine tracking sequence loops."""
        validate_time_window(start_time, end_time, max_days=7)
        return await self.repo.route_playback(vehicle_id, start_time, end_time)

class ChargingService:
    def __init__(self, session: AsyncSession):
        self.repo = ChargingRepository(session)

    async def create_charging_session(self, session_record: ChargingSession) -> ChargingSession:
        return await self.repo.create_session(session_record)

    async def update_charging_session(self, session_id: int, updates: Dict[str, Any]) -> ChargingSession:
        """Applies updates to an active session, raising a clean 404 if the target ID is missing."""
        updated = await self.repo.update_session(session_id, updates)
        if not updated:
            raise HTTPException(
                status_code=404, 
                detail=f"Active tracking session ID {session_id} does not exist in the database system."
            )
        return updated

    async def get_charging_history(self, vehicle_id: str) -> List[ChargingSession]:
        """Pulls comprehensive charging history arrays, safely returning empty arrays if none exist."""
        records = await self.repo.get_history(vehicle_id)
        return records if records is not None else []
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
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, Query, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.db.session import get_db_session
# FIX: Added ChargingService to the explicit imports list
from app.services.telemetry import TelemetryService, BatteryService, LocationService, ChargingService
from app.models.domain import TelemetryRecord, LocationHistory, ChargingSession

router = APIRouter(prefix="/api/v1", tags=["Telemetry & Domain Data"])

# ---------------------------------------------------------
# PYDANTIC INGESTION SCHEMAS
# ---------------------------------------------------------
class TelemetryManualInput(BaseModel):
    vehicle_id: str
    speed_kph: float
    odometer_km: float
    motor_temperature_c: float
    torque_nm: float

class LocationManualInput(BaseModel):
    vehicle_id: str
    latitude: float
    longitude: float
    altitude_m: float
    heading_deg: float
    gps_fix_quality: str

class ChargingSessionCreate(BaseModel):
    vehicle_id: str
    charger_id: str
    starting_soc: float = 0.0

class ChargingSessionUpdate(BaseModel):
    end_time: datetime
    energy_consumed_kwh: float
    ending_soc: float
    status: str = "COMPLETED"

# ---------------------------------------------------------
# WEBSOCKET BROADCAST MANAGER
# ---------------------------------------------------------
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast_event(self, message: Dict[str, Any]):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                pass

ws_manager = ConnectionManager()

@router.websocket("/ws/telemetry")
async def ws_telemetry_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)

# ---------------------------------------------------------
# 1. TELEMETRY APIS
# ---------------------------------------------------------
@router.post("/telemetry", status_code=201)
async def manual_telemetry_ingestion(payload: TelemetryManualInput, session: AsyncSession = Depends(get_db_session)):
    """Manual telemetry debug ingestion endpoint."""
    service = TelemetryService(session)
    record = TelemetryRecord(
        vehicle_id=payload.vehicle_id,
        timestamp=datetime.now(timezone.utc),
        speed_kph=payload.speed_kph,
        odometer_km=payload.odometer_km,
        motor_temperature_c=payload.motor_temperature_c,
        torque_nm=payload.torque_nm
    )
    await service.store_telemetry(record)
    
    await ws_manager.broadcast_event({
        "topic": "ev.telemetry",
        "vehicle_id": payload.vehicle_id,
        "payload": payload.model_dump()
    })
    # FIX: Return a clear status block instead of relying on unpopulated auto-increment hypertable fields
    return {"status": "SUCCESS", "vehicle_id": payload.vehicle_id}

@router.get("/telemetry/latest")
async def get_latest_telemetry(vehicle_id: str, session: AsyncSession = Depends(get_db_session)):
    service = TelemetryService(session)
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=1)
    
    records = await service.get_history(vehicle_id, start_time=start, end_time=end, limit=1)
    if not records:
        raise HTTPException(status_code=404, detail="No recent telemetry found for this vehicle.")
    return records[0]

@router.get("/telemetry/history")
async def get_telemetry_history(
    vehicle_id: str, 
    start_time: datetime, 
    end_time: datetime, 
    limit: int = Query(100, le=1000), 
    session: AsyncSession = Depends(get_db_session)
):
    service = TelemetryService(session)
    return await service.get_history(vehicle_id, start_time, end_time, limit)

@router.get("/telemetry/timeseries")
async def get_telemetry_timeseries(
    vehicle_id: str,
    interval: str = Query("1 minute", description="TimescaleDB interval block"),
    limit: int = Query(24, le=1000),
    session: AsyncSession = Depends(get_db_session)
):
    service = TelemetryService(session)
    return await service.get_timeseries(vehicle_id, interval=interval, limit=limit)

# ---------------------------------------------------------
# 2. CHARGING APIS
# ---------------------------------------------------------
@router.post("/charging/session", status_code=201)
async def start_charging_session(payload: ChargingSessionCreate, session: AsyncSession = Depends(get_db_session)):
    service = ChargingService(session)
    new_session = ChargingSession(
        vehicle_id=payload.vehicle_id,
        charger_id=payload.charger_id,
        start_time=datetime.now(timezone.utc),
        starting_soc=payload.starting_soc,
        status="ACTIVE",
        energy_consumed_kwh=0.0
    )
    return await service.create_charging_session(new_session)

@router.patch("/charging/session/{session_id}")
async def patch_charging_session(session_id: int, payload: ChargingSessionUpdate, session: AsyncSession = Depends(get_db_session)):
    service = ChargingService(session)
    # FIX: Converts returning updated object cleanly to prevent dictionary unpacking visualization errors
    result = await service.update_charging_session(session_id, payload.model_dump(exclude_unset=True))
    return result

@router.get("/charging/history")
async def get_charging_history(vehicle_id: str, session: AsyncSession = Depends(get_db_session)):
    service = ChargingService(session)
    return await service.get_charging_history(vehicle_id)

# ---------------------------------------------------------
# 3. LOCATION & BATTERY APIS
# ---------------------------------------------------------
@router.post("/location", status_code=201)
async def manual_location_ingestion(payload: LocationManualInput, session: AsyncSession = Depends(get_db_session)):
    service = LocationService(session)
    record = LocationHistory(
        vehicle_id=payload.vehicle_id,
        timestamp=datetime.now(timezone.utc),
        latitude=payload.latitude,
        longitude=payload.longitude,
        altitude_m=payload.altitude_m,
        heading_deg=payload.heading_deg,
        gps_fix_quality=payload.gps_fix_quality
    )
    await service.store_location(record)
    # FIX: Clean static layout response dictionary target
    return {"status": "SUCCESS", "vehicle_id": payload.vehicle_id}

@router.get("/location/latest")
async def get_latest_location(vehicle_id: str, session: AsyncSession = Depends(get_db_session)):
    service = LocationService(session)
    # FIX: Gracefully evaluate fallback range checks to prevent driver crashes
    try:
        return await service.get_latest_location(vehicle_id)
    except Exception:
        # Fallback to standard range tracking if direct lookup encounters layout limitations
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=1)
        records = await service.get_route(vehicle_id, start, end)
        if not records:
            raise HTTPException(status_code=404, detail="No recent location found for this vehicle.")
        return records[0]

@router.get("/location/history")
async def get_location_history(vehicle_id: str, start_time: datetime, end_time: datetime, session: AsyncSession = Depends(get_db_session)):
    service = LocationService(session)
    return await service.get_route(vehicle_id, start_time, end_time)

@router.get("/battery/latest")
async def get_latest_battery(vehicle_id: str, session: AsyncSession = Depends(get_db_session)):
    service = BatteryService(session)
    return await service.get_latest(vehicle_id)
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
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException, Depends
from ....schemas.telemetry import BatteryHealthResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db_session
from app.models.domain import BatteryRecord
from sqlalchemy import select
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
async def get_battery_status(
    vehicle_id: str = Query(..., description="ID of the EV vehicle asset"),
    session: AsyncSession = Depends(get_db_session)
):
    from app.services.ml import get_battery_predictor, prepare_features_from_records
    
    # 1. Fetch latest 20 database entries to compile history for rolling features
    stmt = select(BatteryRecord).where(BatteryRecord.vehicle_id == vehicle_id).order_by(BatteryRecord.timestamp.desc()).limit(20)
    result = await session.execute(stmt)
    records = result.scalars().all()
    
    if records:
        features = prepare_features_from_records(records)
        predictor = get_battery_predictor()
        
        soh_res = predictor.predict_soh(features)
        rul_res = predictor.predict_rul(features)
        
        return {
            "vehicle_id": vehicle_id,
            "capacity_fade": round(120.0 - features['capacity_ah'], 2),
            "cycle_count": int(features['cycle']),
            "state_of_health": soh_res['soh_percent'],
            "remaining_useful_life": int(rul_res['rul_cycles'])
        }
        
    # 2. Fallback to mock data if no DB records found
    if vehicle_id in MOCK_BATTERY_HEALTH:
        return MOCK_BATTERY_HEALTH[vehicle_id]
        
    raise HTTPException(status_code=404, detail="Battery status not found for vehicle")

@router.post("/predict/rul")
def predict_rul(payload: dict):
    from app.services.ml import get_battery_predictor, prepare_features_from_records
    features = prepare_features_from_records([], payload)
    predictor = get_battery_predictor()
    res = predictor.predict_rul(features)
    return {
        "predicted_rul_cycles": int(res['rul_cycles']),
        "confidence_interval": [max(0, int(res['rul_cycles']) - 50), int(res['rul_cycles']) + 50],
        "model_version": "xgboost-battery-rul-v1.0",
        "urgency": res['urgency'],
        "action": res['action']
    }

@router.post("/predict/soh")
def predict_soh(payload: dict):
    from app.services.ml import get_battery_predictor, prepare_features_from_records
    features = prepare_features_from_records([], payload)
    predictor = get_battery_predictor()
    res = predictor.predict_soh(features)
    return {
        "state_of_health": res['soh_percent'],
        "capacity_fade_ah": round(120.0 - features['capacity_ah'], 2),
        "health_status": res['health_status'],
        "recommendation": res['recommendation'],
        "model_version": "xgboost-battery-soh-v1.0"
    }

@router.post("/predict/anomaly")
def predict_anomaly(payload: dict):
    from app.services.ml import get_anomaly_detector, prepare_features_from_records
    features = prepare_features_from_records([], payload)
    detector = get_anomaly_detector()
    res = detector.predict(features)
    return {
        "is_anomaly": res['is_anomaly'],
        "anomaly_score": res['anomaly_score'],
        "severity": res['severity'],
        "anomaly_types": res['anomaly_types'],
        "alerts": res['alerts'],
        "recommendations": res['recommendations'],
        "model_version": "isolation-forest-anomaly-v1.0"
    }

@router.websocket("/telemetry/ws/{vehicle_id}")
async def websocket_endpoint(websocket: WebSocket, vehicle_id: str):
    await websocket.accept()
    try:
        while True:
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
from datetime import datetime
import sys
import os

# Append ML directory to sys.path
from app.services.ml import ML_DIR
if ML_DIR not in sys.path:
    sys.path.append(ML_DIR)

from engines.risk_scorer import SupplyChainRiskScorer

router = APIRouter()

@router.get("/suppliers", response_model=List[SupplierRiskResponse])
def get_suppliers():
    scorer = SupplyChainRiskScorer()
    scores = scorer.score_all_suppliers()
    
    response = []
    for idx, s in enumerate(scores):
        num_id = idx + 1
        try:
            # Try parsing digits out of S001 etc.
            digits = "".join(filter(str.isdigit, s['supplier_id']))
            if digits:
                num_id = int(digits)
        except Exception:
            pass
            
        response.append({
            "id": num_id,
            "name": s['supplier_name'],
            "location": s['country'],
            "risk_score": s['risk_score'],
            "material_supplied": s['mineral'].capitalize() if s['mineral'] else s['type'].capitalize()
        })
    return response

@router.get("/risk")
def get_supply_chain_risk():
    scorer = SupplyChainRiskScorer()
    scores = scorer.score_all_suppliers()
    
    global_risk = round(sum(s['risk_score'] for s in scores) / len(scores), 1)
    highest = max(scores, key=lambda x: x['risk_score'])
    critical_vuln = f"High risk concentration from supplier {highest['supplier_name']} ({highest['risk_score']}/100) in {highest['country']}."
    mitigation = highest['recommendations'][0] if highest['recommendations'] else "Diversify sourcing contracts."
    
    return {
        "global_risk_index": global_risk,
        "critical_vulnerability": critical_vuln,
        "mitigation_plan": mitigation,
        "last_updated": datetime.now().isoformat()
    }

@router.get("/materials")
def get_materials_flow():
    scorer = SupplyChainRiskScorer()
    materials = []
    for name, info in scorer.commodity_data.items():
        materials.append({
            "name": name.capitalize(),
            "active_flow_tons": int(info['price_usd_ton'] / 100),
            "safety_buffer_days": int((1.0 - info['supply_risk']) * 100)
        })
    return {"materials": materials}

@router.get("/dependencies", response_model=GraphDependencyResponse)
def get_dependencies_graph():
    scorer = SupplyChainRiskScorer()
    graph = scorer.get_supply_chain_graph()
    
    nodes = []
    for n in graph['nodes']:
        nodes.append({
            "id": n['id'],
            "label": n['type'].capitalize(),
            "properties": {
                "name": n['label'],
                "country": n['country'] or "Unknown",
                "risk_score": n['risk_score'],
                "risk_level": n['risk_level']
            }
        })
        
    edges = []
    for e in graph['edges']:
        edges.append({
            "source": e['source'],
            "target": e['target'],
            "type": e['material'].upper().replace(' ', '_')
        })
        
    return {
        "nodes": nodes,
        "edges": edges
    }
```

---

## backend\app\api\v1\endpoints\sustainability.py

```python
from fastapi import APIRouter
import sys
import os

# Append ML directory to sys.path
from app.services.ml import ML_DIR
if ML_DIR not in sys.path:
    sys.path.append(ML_DIR)

from engines.carbon_engine import CarbonIntelligenceEngine
from engines.readiness_scorer import FleetReadinessScorer

router = APIRouter()

@router.get("/carbon")
def get_carbon_metrics():
    engine = CarbonIntelligenceEngine(grid_region='india')
    fleet = engine.generate_sample_fleet(50)
    summary = engine.analyze_fleet(fleet)
    
    co2_saved_tons = summary['savings']['co2_saved_tons']
    # 2.68 kg CO2 per liter diesel. 0.264172 gallons per liter.
    diesel_displacement_gallons = (co2_saved_tons * 1000.0 / 2.68) * 0.264172
    
    return {
        "co2_savings_ytd_tons": round(co2_saved_tons, 1),
        "diesel_displacement_gallons": round(diesel_displacement_gallons, 1),
        "grid_emission_intensity_kwh": round(engine.grid_emission_factor, 3),  # kg CO2/kWh
        "scope_1_direct_displaced_tons": round(summary['diesel_scenario']['total_co2_tons'], 1),
        "scope_3_grid_indirect_tons": round(summary['ev_scenario']['total_co2_tons'], 1)
    }

@router.get("/electrification")
def get_electrification_readiness():
    scorer = FleetReadinessScorer()
    routes = scorer.generate_sample_routes(30)
    summary = scorer.assess_fleet(routes)
    
    recommendations = []
    for r in summary['route_assessments']:
        reason = r['recommendation']
        if r['improvements_needed']:
            reason += ". Required: " + "; ".join(r['improvements_needed'])
        recommendations.append({
            "route_id": r['route_id'],
            "name": r['route_name'],
            "readiness_percentage": int(r['readiness_score']),
            "reason": reason
        })
        
    return {
        "readiness_score": int(summary['overall_readiness_score']),
        "total_active_routes": summary['total_routes'],
        "electrified_routes": len(summary['recommended_for_immediate_ev']),
        "recommendations": recommendations
    }
```

---

## backend\app\api\v1\endpoints\telemetry.py

```python
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import datetime
import json
import asyncio
import logging

logger = logging.getLogger("app.streaming.processor.telemetry")
router = APIRouter()

MOCK_VEHICLES = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]
MOCK_TELEMETRY = {
    "EV-HD-001": {"vehicle_id": "EV-HD-001", "voltage": 395.2, "current": 12.4, "temperature": 34.5, "soc": 88.0, "id": 1},
    "EV-HD-002": {"vehicle_id": "EV-HD-002", "voltage": 380.1, "current": -45.0, "temperature": 38.2, "soc": 42.0, "id": 2},
    "EV-HD-003": {"vehicle_id": "EV-HD-003", "voltage": 401.5, "current": 10.1, "temperature": 33.1, "soc": 91.0, "id": 3},
    "EV-HD-004": {"vehicle_id": "EV-HD-004", "voltage": 372.4, "current": 115.0, "temperature": 44.8, "soc": 76.0, "id": 4},
}

@router.websocket("/telemetry/live")
async def get_live_telemetry_websocket(websocket: WebSocket):
    await websocket.accept()
    logger.info("Live telemetry matrix stream connection initialized.")
    try:
        while True:
            for vehicle_id in MOCK_VEHICLES:
                # Use a fallback baseline to avoid missing key schema crashes
                raw_telemetry = MOCK_TELEMETRY.get(vehicle_id, {
                    "vehicle_id": vehicle_id, "voltage": 0.0, "current": 0.0, "temperature": 0.0, "soc": 0.0, "id": 0
                }).copy()

                # Format to adhere strictly to your TelemetryResponse schema fields
                payload = {
                    "id": raw_telemetry.get("id"),
                    "vehicle_id": raw_telemetry.get("vehicle_id"),
                    "voltage": float(raw_telemetry.get("voltage")),
                    "current": float(raw_telemetry.get("current")),
                    "temperature": float(raw_telemetry.get("temperature")),
                    "soc": float(raw_telemetry.get("soc")),
                    "timestamp": datetime.datetime.utcnow().isoformat()
                }

                await websocket.send_text(json.dumps(payload))

            # Keep heartbeat frequency high enough to prevent engine drops
            await asyncio.sleep(1.0)

    except WebSocketDisconnect:
        logger.info("Client disconnected cleanly from live telemetry matrix stream.")
    except Exception as e:
        logger.error(f"Stream exception intercepted: {str(e)}")
    finally:
        # Ensure socket state cleanly unmounts even during hard crashes
        try:
            await websocket.close()
        except Exception:
            pass
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
    ChargingRepository,
    AlertRepository
)
from app.models.domain import TelemetryRecord, BatteryRecord, LocationHistory, ChargingSession , AlertRecord
from app.streaming.websocket.adapter import kafka_to_ws_broadcaster

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

        # Instantiates using the explicit kinematic parameter names
        record = TelemetryRecord(
            vehicle_id=vehicle_id,
            timestamp=ts,
            speed_kph=float(payload.get("speed_kph", 0.0)),
            odometer_km=float(payload.get("odometer_km", 0.0)),
            motor_temperature_c=float(payload.get("motor_temperature_c", 0.0)),
            torque_nm=float(payload.get("torque_nm", 0.0))
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
            internal_resistance_ohm=float(payload.get("internal_resistance_ohm", 0.0)),
            cycle_count=int(payload.get("cycle_count", 100))
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

    async def process_alerts(self, topic: str, event_envelope: Dict[str, Any]) -> None:
            """Processes 'ev.alerts' diagnostic streams, pushes live to WebSockets, and logs to hypertable."""
            payload = event_envelope.get("payload", {})
            vehicle_id = event_envelope.get("vehicle_id", payload.get("vehicle_id", "UNKNOWN"))
            ts = self._parse_timestamp(payload.get("timestamp"))

            logger.warning(f"[ALERT ENGINE] Intercepted system event fault payload for vehicle {vehicle_id}")

            # Parse from the AlertsPayload structural fields
            record = AlertRecord(
                vehicle_id=vehicle_id,
                timestamp=ts,
                severity=payload.get("severity", "INFO"),
                alert_type=payload.get("alert_code", "GEN_ERR"),
                description=payload.get("description", "Unhandled internal system status anomaly."),
                resolved=False
            )

            # Route A: High-performance async database safe persistence
            async with AsyncSessionLocal() as session:
                repo = AlertRepository(session)
                await repo.insert(record)

            # Route B: Direct visual broadcast frame to active web sockets UI clients
            # ADD THIS BLOCK:
            # Route B: Direct visual broadcast frame to active web sockets UI clients
            await kafka_to_ws_broadcaster(
                topic="ev.alerts",
                payload={
                    "vehicle_id": vehicle_id,
                    "timestamp": ts.isoformat(),
                    "severity": record.severity,
                    "alert_type": record.alert_type,
                    "description": record.description,
                    "resolved": record.resolved
                }
            )
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

# FIX: Changed level to WARNING to prevent logs bleeding into execution terminals
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

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
    schema_cls = TOPIC_SCHEMA_MAP.get(topic)
    if not schema_cls:
        return None

    try:
        parsed_json = json.loads(raw_data)
        validated_model = schema_cls.model_validate(parsed_json)
        return validated_model
    except (json.JSONDecodeError, ValidationError, Exception) as e:
        # Crucial processing errors fallback quietly to system logs without flooding stdout
        logger.error(f"Ingestion structural exception caught on topic {topic}: {e}")
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

/* Fix styling context inside leaflet popup component arrays */
.leaflet-popup-content-wrapper, .leaflet-popup-tip {
  background: #0f172a !important;
  color: #f8fafc !important;
  border: 1px solid #334155 !important;
  border-radius: 8px !important;
}
.leaflet-container a.leaflet-popup-close-button {
  color: #94a3b8 !important;
  padding: 4px 6px 0 0 !important;
}

/* Force compiler tracking for Leaflet DivIcon styles */
.custom-leaflet-marker {
  background: transparent !important;
  border: none !important;
}

/* Fallback layer guaranteeing visibility for your live map tracking nodes */
.bg-emerald-400 { background-color: #34d399 !important; }
.bg-red-500     { background-color: #ef4444 !important; }
.bg-amber-400   { background-color: #fbbf24 !important; }
.bg-blue-400    { background-color: #60a5fa !important; }

.ring-emerald-500\/30 { box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.3); }
.ring-red-500\/50     { box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.5); }
.ring-amber-500\/30   { box-shadow: 0 0 0 4px rgba(245, 158, 11, 0.3); }
.ring-blue-500\/30    { box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.3); }
```

---

## frontend\src\main.tsx

```tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';
import 'leaflet/dist/leaflet.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

---

## frontend\src\hooks\useFleetData.ts

```typescript
import { useState, useEffect, useRef } from 'react';

export function useFleetData() {
  const [fleet, setFleet] = useState<Record<string, any>>({});
  const [alerts, setAlerts] = useState<any[]>([]);
  const [msgPerSec, setMsgPerSec] = useState(0);

  const socketRef = useRef<WebSocket | null>(null);
  const reconnectRef = useRef<NodeJS.Timeout | null>(null);
  const counterRef = useRef(0);

  useEffect(() => {
    let isMounted = true;

    function connect() {
      // Don't build a new socket if one is already connecting or fully open
      if (
        socketRef.current &&
        (socketRef.current.readyState === WebSocket.CONNECTING || socketRef.current.readyState === WebSocket.OPEN)
      ) {
        return;
      }

      const socket = new WebSocket('ws://localhost:8000/api/v1/telemetry/live');
      socketRef.current = socket;

      socket.onopen = () => {
        if (!isMounted) {
          socket.close();
          return;
        }
        console.log('📡 Telemetry matrix connection established successfully.');
      };

      socket.onmessage = (event) => {
        if (!isMounted) return;
        counterRef.current++;
        try {
          const data = JSON.parse(event.data);
          const vId = data.vehicle_id;
          if (!vId) return;

          // 1. Detect temperature using both payload variants
          const temp = data.motor_temperature_c || data.temperature;

          // 2. Dynamically assign the status flag so the Map and Table UI can read it
          let assetStatus = data.status || "Active";
          if (temp > 40.0) {
            assetStatus = "Critical";
          }

          // 3. Save the modified object with the updated status flag
          const updatedData = { ...data, status: assetStatus };
          setFleet((prev) => ({ ...prev, [vId]: updatedData }));

          // 4. Handle Alert Stack
          if (temp > 40.0) {
            setAlerts((prev) => [
              {
                asset: vId,
                type: 'Critical', // Changed to match your critical check
                msg: `High operational anomaly detected: ${temp.toFixed(1)}°C`,
                timestamp: new Date().toLocaleTimeString()
              },
              ...prev.slice(0, 9)
            ]);
          }
        } catch (e) {
          console.error('Failed to parse frame payload:', e);
        }
      };

      socket.onclose = (event) => {
        // If the component was unmounted, ignore drop notices and drop retry scheduling
        if (!isMounted) return;

        socketRef.current = null;
        console.warn(`Connection dropped (Code: ${event.code}). Retrying downstream handshake...`);

        if (reconnectRef.current) clearTimeout(reconnectRef.current);
        reconnectRef.current = setTimeout(connect, 3000);
      };

      socket.onerror = (error) => {
        // Suppress noisy trace logging if it's just the clean strict-mode teardown drop
        if (!isMounted) return;
        console.error('WebSocket connection error intercepted:', error);
      };
    }

    connect();

    const interval = setInterval(() => {
      if (isMounted) {
        setMsgPerSec(counterRef.current);
        counterRef.current = 0;
      }
    }, 1000);

    return () => {
      isMounted = false;
      clearInterval(interval);
      if (reconnectRef.current) clearTimeout(reconnectRef.current);
      if (socketRef.current) {
        // Clean up the instance cleanly
        const ws = socketRef.current;
        ws.onopen = null;
        ws.onmessage = null;
        ws.onclose = null;
        ws.onerror = null;
        if (ws.readyState === WebSocket.CONNECTING || ws.readyState === WebSocket.OPEN) {
          ws.close();
        }
        socketRef.current = null;
      }
    };
  }, []);

  return { fleet, alerts, msgPerSec };
}
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
import React, { useState, useEffect } from 'react';
import { useFleetData } from '../hooks/useFleetData';

interface SystemAlert {
  id: string; // Dynamic ID to prevent duplicate key warning
  asset: string;
  type: 'Warning' | 'Critical';
  msg: string;
  timestamp: string;
}

export default function Alerts() {
  // 1. Grab incoming stream alerts from our custom hook
  const { alerts: incomingAlerts } = useFleetData();

  // 2. Maintain a local state so we can actually delete or acknowledge them on screen
  const [localAlerts, setLocalAlerts] = useState<SystemAlert[]>([]);

  // Sync incoming live updates with local state, assigning a bulletproof ID
  useEffect(() => {
    if (incomingAlerts && incomingAlerts.length > 0) {
      setLocalAlerts((prev) => {
        // Create an array of fresh entries with robust keys
        const formattedIncoming = incomingAlerts.map((alert, index) => ({
          ...alert,
          // Generate a truly unique composite key string
          id: `${alert.asset}-${alert.timestamp}-${index}-${alert.msg.substring(0, 5)}`
        }));

        // Deduplicate incoming vs existing to prevent view pop duplicates
        const existingKeys = new Set(prev.map(a => a.id));
        const newUniqueAlerts = formattedIncoming.filter(a => !existingKeys.has(a.id));

        return [...newUniqueAlerts, ...prev].slice(0, 50);
      });
    }
  }, [incomingAlerts]);

  // FIX: This now safely mutates the correct local state array!
  const clearAlert = (idToRemove: string) => {
    setLocalAlerts((prev) => prev.filter((alert) => alert.id !== idToRemove));
  };

  const clearAllAlerts = () => {
    setLocalAlerts([]);
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-800">System Activity Fault Logs</h2>
        {localAlerts.length > 0 && (
          <button
            onClick={clearAllAlerts}
            className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded text-sm transition"
          >
            Clear All Logs
          </button>
        )}
      </div>

      {localAlerts.length === 0 ? (
        <div className="p-8 text-center bg-gray-50 border border-dashed rounded text-gray-500">
          🟢 All vehicle assets running within nominal thresholds. No faults detected.
        </div>
      ) : (
        <div className="space-y-3">
          {localAlerts.map((alert) => (
            // FIX: Explicitly passing down our absolute unique dynamic ID key
            <div
              key={alert.id}
              className={`p-4 rounded border flex justify-between items-start transition ${
                alert.type === 'Critical' ? 'bg-red-50 border-red-200' : 'bg-amber-50 border-amber-200'
              }`}
            >
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <span className={`px-2 py-0.5 rounded text-xs font-semibold ${
                    alert.type === 'Critical' ? 'bg-red-200 text-red-800' : 'bg-amber-200 text-amber-800'
                  }`}>
                    {alert.type}
                  </span>
                  <strong className="text-gray-900">{alert.asset}</strong>
                  <span className="text-xs text-gray-500 font-mono">{alert.timestamp}</span>
                </div>
                <p className="text-sm text-gray-700">{alert.msg}</p>
              </div>

              <button
                onClick={() => clearAlert(alert.id)}
                className="text-gray-400 hover:text-gray-600 ml-4 font-bold text-lg leading-none"
                title="Acknowledge fault"
              >
                &times;
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

---

## frontend\src\pages\BatteryAnalytics.tsx

```tsx
import React from 'react';
import { BatteryCharging, Thermometer, ShieldAlert, Cpu } from 'lucide-react';
import { useFleetData } from '../hooks/useFleetData';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

export default function BatteryAnalytics() {
  const { fleet, alerts } = useFleetData();

  // Focus primarily on EV-HD-004 as our primary telemetry streaming unit
  const targetAssetId = "EV-HD-004";
  const liveData = fleet[targetAssetId];

  // Dynamic values pulled from WebSocket or falling back to static seeds
  const currentTemp = liveData?.motor_temperature_c !== undefined ? liveData.motor_temperature_c : 38.4;
  const tempPercentage = Math.min(100, (currentTemp / 55) * 100);
  const isOverheating = currentTemp > 100;

  // Mocking an XGBoost degradation calculation array based on real-world cell health
  const mockDegradationData = [
    { cycle: 0, nominal: 120, predicted: 120 },
    { cycle: 200, nominal: 120, predicted: 118.5 },
    { cycle: 400, nominal: 120, predicted: 116.8 },
    { cycle: 600, nominal: 120, predicted: 115.2 },
    { cycle: 800, nominal: 120, predicted: 114.2 },
    { cycle: 1000, nominal: 120, predicted: liveData ? 114.2 - (currentTemp * 0.005) : 112.1 },
  ];

  // Dynamic filter looking for high-scoring AI anomalies in the hook's logs
  const targetedCriticalAlerts = alerts.filter(a => a.asset === targetAssetId || a.type === 'Critical');

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
              <Thermometer className={`h-5 w-5 ${isOverheating ? 'text-red-500 animate-bounce' : 'text-red-400'}`} />
            </div>
            <p className="text-xs text-muted-foreground mt-1">Real-time status of thermal runaways and core gradients.</p>
          </div>

          <div className="my-8 flex justify-center items-center">
            <div className={`relative h-32 w-32 rounded-full border-4 border-dashed flex flex-col justify-center items-center transition-all ${
              isOverheating ? 'border-red-500 bg-red-500/10 animate-pulse' : 'border-red-500/30'
            }`}>
              <span className="text-2xl font-bold font-mono">{currentTemp.toFixed(1)}°C</span>
              <span className={`text-[10px] uppercase tracking-wider font-semibold ${isOverheating ? 'text-red-400' : 'text-emerald-400'}`}>
                {isOverheating ? 'Thermal Overload' : 'Healthy Range'}
              </span>
            </div>
          </div>

          <div className="space-y-2">
            <div className="flex justify-between text-xs font-semibold text-muted-foreground">
              <span>Upper Safety Threshold</span>
              <span>55.0°C</span>
            </div>
            <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
              <div
                className={`h-full transition-all duration-300 ${isOverheating ? 'bg-red-500' : 'bg-amber-500'}`}
                style={{ width: `${tempPercentage}%` }}
              />
            </div>
          </div>
        </div>

        {/* Degradation Regression Predictor (Recharts Integration) */}
        <div className="glass p-6 rounded-xl flex flex-col justify-between lg:col-span-2">
          <div>
            <div className="flex justify-between items-center">
              <h2 className="font-semibold text-lg">Capacity Degradation Curve</h2>
              <BatteryCharging className="h-5 w-5 text-emerald-400" />
            </div>
            <p className="text-xs text-muted-foreground mt-1">Calculated capacity fade over consecutive charging/discharging cycles.</p>
          </div>

          <div className="h-48 w-full bg-muted/10 border border-border/40 rounded-lg p-2 mt-4">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={mockDegradationData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#2e2e2e" />
                <XAxis dataKey="cycle" stroke="#888888" fontSize={11} tickLine={false} />
                <YAxis domain={[100, 125]} stroke="#888888" fontSize={11} tickLine={false} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#1e1b4b', borderColor: '#312e81', borderRadius: '8px' }}
                  labelStyle={{ color: '#94a3b8', fontSize: '11px' }}
                  itemStyle={{ fontSize: '12px' }}
                />
                <Line type="monotone" dataKey="nominal" stroke="#64748b" strokeDasharray="5 5" name="Nominal Limit" dot={false} />
                <Line type="monotone" dataKey="predicted" stroke="#3b82f6" strokeWidth={2.5} name="XGBoost Prediction" dot={true} />
              </LineChart>
            </ResponsiveContainer>
          </div>

          <div className="grid grid-cols-3 gap-4 text-center mt-4">
            <div className="bg-muted/30 p-2 rounded-lg">
              <span className="block text-xs text-muted-foreground">Nominal Cap</span>
              <span className="text-base font-bold font-mono">120 Ah</span>
            </div>
            <div className="bg-muted/30 p-2 rounded-lg">
              <span className="block text-xs text-muted-foreground">Current Cap</span>
              <span className="text-base font-bold font-mono text-emerald-500">
                {liveData ? (114.2 - (currentTemp * 0.002)).toFixed(1) : '114.2'} Ah
              </span>
            </div>
            <div className="bg-muted/30 p-2 rounded-lg">
              <span className="block text-xs text-muted-foreground">SOH State</span>
              <span className="text-base font-bold font-mono text-blue-500">
                {liveData && isOverheating ? '83.4%' : '95.1%'}
              </span>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Predictive AI Alert Cards */}
        <div className="glass p-6 rounded-xl space-y-4">
          <div className="flex items-center gap-2">
            <Cpu className="h-5 w-5 text-blue-400" />
            <h2 className="font-semibold text-lg">AI Anomaly Alerts</h2>
          </div>

          <div className="space-y-3 max-h-[180px] overflow-y-auto pr-1">
            {targetedCriticalAlerts.length > 0 ? (
              targetedCriticalAlerts.map((alert, idx) => (
                <div key={idx} className="border-l-4 border-red-500 bg-red-500/5 p-4 rounded-r-lg flex items-start gap-3">
                  <ShieldAlert className="h-5 w-5 text-red-500 shrink-0 mt-0.5 animate-pulse" />
                  <div>
                    <h4 className="text-sm font-bold text-red-400">Critical Thermal Delta Excursion</h4>
                    <p className="text-xs text-muted-foreground mt-0.5">{alert.msg}</p>
                  </div>
                </div>
              ))
            ) : (
              <>
                <div className="border-l-4 border-red-500 bg-red-500/5 p-4 rounded-r-lg flex items-start gap-3">
                  <ShieldAlert className="h-5 w-5 text-red-500 shrink-0 mt-0.5" />
                  <div>
                    <h4 className="text-sm font-bold text-red-400">Thermal Runaway Baseline (Anomaly Score: 0.98)</h4>
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
              </>
            )}
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
              <span className="text-4xl font-extrabold text-blue-500 font-mono">
                {liveData && isOverheating ? '430' : '1,120'}
              </span>
              <span className="text-sm text-muted-foreground block mt-1">Estimated Remaining Cycles</span>
            </div>
          </div>
          <div className="border-t border-border pt-4 text-xs text-muted-foreground flex justify-between">
            <span>Regression Confidence: 94.2%</span>
            <span>Next inspection: {liveData && isOverheating ? 'Immediate' : '60 days'}</span>
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
import { Truck, Battery, AlertTriangle, ShieldCheck, Activity, Navigation } from 'lucide-react';
import { useFleetData } from '../hooks/useFleetData';

// Leaflet UI Engine Components
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';

// 1. Core Map Controller Component to smoothly pan the camera to the main cluster
function MapUpdater({ coordinates }: { coordinates: [number, number][] }) {
  const map = useMap();
  React.useEffect(() => {
    if (coordinates.length > 0) {
      // Create bounds based on current live tracking data matrices
      const bounds = L.latLngBounds(coordinates);
      map.fitBounds(bounds, { padding: [40, 40], maxZoom: 14 });
    }
  }, [coordinates, map]);
  return null;
}

// 2. Factory function to build custom DOM-styled markers that bypass Leaflet's blue legacy images
const createCustomMarker = (status: string) => {
  let colorClass = "bg-emerald-400 ring-emerald-500/30";
  if (status === "Critical") colorClass = "bg-red-500 ring-red-500/50 animate-pulse";
  if (status === "Warning") colorClass = "bg-amber-400 ring-amber-500/30";
  if (status === "Charging") colorClass = "bg-blue-400 ring-blue-500/30 animate-pulse";

  return L.divIcon({
    className: 'custom-leaflet-marker',
    html: `
      <div class="relative flex items-center justify-center w-6 h-6">
        <div class="absolute w-6 h-6 rounded-full ring-4 opacity-40 animate-ping ${colorClass}"></div>
        <div class="w-3 h-3 rounded-full border-2 border-slate-900 shadow-md ${colorClass}"></div>
      </div>
    `,
    iconSize: [24, 24],
    iconAnchor: [12, 12]
  });
};

export default function FleetOverview() {
  const { fleet, alerts, msgPerSec } = useFleetData();

  const activeAssets = Object.values(fleet);
  const criticalCount = alerts.filter(a => a.type === 'Critical').length;

  const defaultFleet = [
    { id: "EV-HD-001", fallbackStatus: "Active", defaultLat: 37.7749, defaultLng: -122.4194 },
    { id: "EV-HD-002", fallbackStatus: "Charging", defaultLat: 37.7833, defaultLng: -122.4167 },
    { id: "EV-HD-003", fallbackStatus: "Active", defaultLat: 37.7699, defaultLng: -122.4468 },
    { id: "EV-HD-004", fallbackStatus: "Warning", defaultLat: 37.7599, defaultLng: -122.4368 },
  ];

  // Compile active coordinates array dynamically to feed the automated viewport framing calculations
  const mapCoordinates: [number, number][] = defaultFleet.map(v => {
    const liveData = fleet[v.id];
    return [liveData?.latitude || v.defaultLat, liveData?.longitude || v.defaultLng];
  });

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header View Row */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight">Fleet Asset Intelligence</h1>
          <p className="text-muted-foreground mt-1">Real-time status, health index, and predictive alerts for industrial EV assets.</p>
        </div>
        <div className="flex items-center gap-2 bg-muted/50 px-3 py-1.5 rounded-lg text-xs font-medium border border-border">
          <Activity className="h-4.5 w-4.5 text-blue-500 animate-pulse" />
          <span>Ingesting: {msgPerSec || 1} Telemetry msg/sec</span>
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
            <span className="text-3xl font-bold">{Math.max(4, activeAssets.length)}</span>
            <span className="text-xs text-emerald-500 font-medium">100% Monitored</span>
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
            <span className="text-3xl font-bold">{criticalCount}</span>
            <span className="text-xs text-red-500 font-semibold">Critical Risks Active</span>
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

      {/* Live Geospatial Real Map Layer Section */}
      <div className="glass rounded-xl overflow-hidden p-5">
        <div className="flex items-center gap-2 mb-4">
          <Navigation className="h-5 w-5 text-blue-400" />
          <h2 className="text-lg font-semibold">Live Geospatial Telemetry Layer</h2>
        </div>

        {/* Physical Map Canvas Box Container */}
        <div className="h-96 w-full rounded-lg overflow-hidden border border-border bg-slate-900 z-10 relative">
          <MapContainer
            center={[37.7749, -122.4194]}
            zoom={13}
            className="h-full w-full"
            style={{ background: '#0f172a' }}
          >
            {/* Dark Mode Cartographic Mesh Tiles */}
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
              url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
            />

            {/* Rendered directly inside separate fragment blocks to prevent context-consumer mismatch */}
            {defaultFleet.map((v) => {
              const liveData = fleet[v.id];
              const lat = liveData?.latitude || v.defaultLat;
              const lng = liveData?.longitude || v.defaultLng;
              const currentStatus = liveData ? liveData.status : v.fallbackStatus;

              return (
                <Marker
                  key={`real-map-${v.id}`}
                  position={[lat, lng]}
                  icon={createCustomMarker(currentStatus)}
                >
                  <Popup className="custom-map-popup">
                    <div className="p-1 font-mono text-xs text-slate-200">
                      <strong className="text-blue-400 block mb-1">{v.id}</strong>
                      <div className="space-y-0.5">
                        <div>Speed: {liveData?.speed_kph !== undefined ? `${liveData.speed_kph.toFixed(1)} kph` : '72.0 kph'}</div>
                        <div>Temp: {liveData?.motor_temperature_c !== undefined ? `${liveData.motor_temperature_c.toFixed(1)}°C` : '38.5°C'}</div>
                        <div>Status: <span className="font-bold uppercase text-[10px]">{currentStatus}</span></div>
                      </div>
                    </div>
                  </Popup>
                </Marker>
              );
            })}

            <MapUpdater coordinates={mapCoordinates} />
          </MapContainer>
        </div>
      </div>

      {/* Detailed Live Fleet Table */}
      <div className="glass rounded-xl overflow-hidden">
        <div className="px-6 py-5 border-b border-border">
          <h2 className="text-lg font-semibold">Real-Time Vehicle Assets Status</h2>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-border bg-muted/30 text-xs uppercase tracking-wider text-muted-foreground">
                <th className="px-6 py-4">Asset ID</th>
                <th className="px-6 py-4">Speed</th>
                <th className="px-6 py-4">Live Location (Lat, Lon)</th>
                <th className="px-6 py-4">Avg Motor Temp</th>
                <th className="px-6 py-4">Torque Load</th>
                <th className="px-6 py-4">Status Flag</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border text-sm">
              {defaultFleet.map((v) => {
                const liveData = fleet[v.id];

                const speedDisplay = liveData?.speed_kph !== undefined ? `${liveData.speed_kph.toFixed(1)} kph` : '72.0 kph';
                const tempDisplay = liveData?.motor_temperature_c !== undefined ? `${liveData.motor_temperature_c.toFixed(1)}°C` : '38.5°C';
                const torqueDisplay = liveData?.torque_nm !== undefined ? `${liveData.torque_nm.toFixed(1)} Nm` : '210 Nm';

                const locationDisplay = liveData?.latitude && liveData?.longitude
                  ? `${liveData.latitude.toFixed(4)}, ${liveData.longitude.toFixed(4)}`
                  : `${v.defaultLat.toFixed(4)}, ${v.defaultLng.toFixed(4)}`;

                const currentStatus = liveData ? liveData.status : v.fallbackStatus;
                const isCritical = currentStatus === 'Critical';
                const isWarning = currentStatus === 'Warning';

                return (
                  <tr key={v.id} className="hover:bg-muted/10 transition-colors">
                    <td className="px-6 py-4 font-mono font-medium">{v.id}</td>
                    <td className="px-6 py-4 font-mono">{speedDisplay}</td>
                    <td className="px-6 py-4 font-mono text-xs text-blue-400 font-semibold">
                      {locationDisplay}
                    </td>
                    <td className={`px-6 py-4 font-mono font-semibold ${isCritical ? 'text-red-400 animate-pulse' : isWarning ? 'text-yellow-400' : ''}`}>
                      {tempDisplay}
                    </td>
                    <td className="px-6 py-4 font-mono">{torqueDisplay}</td>
                    <td className="px-6 py-4">
                      <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-semibold ${
                        isCritical ? 'bg-red-500/10 text-red-500 animate-pulse' :
                        isWarning ? 'bg-yellow-500/10 text-yellow-500' :
                        'bg-emerald-500/10 text-emerald-500'
                      }`}>
                        {currentStatus}
                      </span>
                    </td>
                  </tr>
                );
              })}
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
    charger_id VARCHAR(50),
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ,
    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    energy_consumed_kwh DOUBLE PRECISION DEFAULT 0.0,
    starting_soc DOUBLE PRECISION DEFAULT 0.0,
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
```

---

## infrastructure\kafka\consumers\telemetry_consumer.py

```python
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
```

---

## ml\engines\anomaly_detector.py

```python
"""
Anomaly Detection Engine
========================
Uses Isolation Forest to detect anomalous battery behavior in real-time.
Detects: thermal spikes, voltage anomalies, current surges, SoC inconsistencies.
"""

import numpy as np
import pandas as pd
import os
import json
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class AnomalyDetector:
    """
    Isolation Forest-based anomaly detection for EV battery telemetry.
    
    How Isolation Forest works:
    - Builds random trees by randomly selecting features and split values
    - Anomalies are isolated in fewer splits (shorter path length)
    - Normal points need more splits to be isolated (longer path length)
    - Score: -1 = anomaly, 1 = normal (or continuous score)
    """
    
    def __init__(self, contamination: float = 0.05):
        """
        Args:
            contamination: Expected proportion of anomalies (0.01-0.1)
        """
        self.model = IsolationForest(
            n_estimators=200,
            contamination=contamination,
            max_features=0.8,
            bootstrap=True,
            random_state=42,
            n_jobs=-1
        )
        self.scaler = StandardScaler()
        self.is_trained = False
        self.feature_columns = []
        self.thresholds = {}
        
        # Physical limit thresholds for rule-based detection
        self.physical_limits = {
            'temperature_max': 55.0,       # Celsius - critical thermal
            'temperature_warning': 45.0,    # Celsius - warning
            'voltage_min': 300.0,           # Volts - pack level
            'voltage_max': 420.0,           # Volts - pack level
            'current_max': 250.0,           # Amps - max discharge
            'soc_drop_max': 15.0,           # % per reading - impossible drop
            'soc_min': 3.0,                 # % - deep discharge danger
        }
    
    def _get_training_features(self, df: pd.DataFrame) -> List[str]:
        """Get feature columns for anomaly detection."""
        candidate_features = [
            'capacity_ah', 'avg_voltage_v', 'voltage_charged_v', 'voltage_discharged_v',
            'avg_temperature_c', 'max_temperature_c', 'internal_resistance_ohm',
            'charge_transfer_resistance_ohm', 'discharge_time_s',
            'charge_efficiency_percent', 'discharge_slope_v_per_s',
            'capacity_degradation_rate', 'thermal_variance', 'voltage_spread',
            'resistance_growth_rate', 'temp_rolling_std'
        ]
        return [c for c in candidate_features if c in df.columns]
    
    def train(self, df: pd.DataFrame) -> dict:
        """
        Train the Isolation Forest on battery telemetry data.
        
        Args:
            df: DataFrame with battery features (from preprocessing pipeline)
        
        Returns:
            Training summary with metrics
        """
        print("\n" + "=" * 50)
        print("Training Anomaly Detection Model")
        print("=" * 50)
        
        self.feature_columns = self._get_training_features(df)
        X = df[self.feature_columns].values
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        print(f"[TRAIN] Features: {len(self.feature_columns)}")
        print(f"[TRAIN] Samples: {len(X_scaled)}")
        
        # Train Isolation Forest
        self.model.fit(X_scaled)
        self.is_trained = True
        
        # Get anomaly scores for training data
        scores = self.model.decision_function(X_scaled)
        predictions = self.model.predict(X_scaled)
        
        num_anomalies = (predictions == -1).sum()
        anomaly_rate = num_anomalies / len(predictions) * 100
        
        # Compute threshold statistics
        self.thresholds = {
            'score_mean': float(np.mean(scores)),
            'score_std': float(np.std(scores)),
            'score_min': float(np.min(scores)),
            'score_max': float(np.max(scores)),
            'anomaly_threshold': float(np.percentile(scores, 5)),  # Bottom 5%
            'warning_threshold': float(np.percentile(scores, 10)),  # Bottom 10%
        }
        
        summary = {
            'total_samples': len(X_scaled),
            'anomalies_detected': int(num_anomalies),
            'anomaly_rate_percent': round(anomaly_rate, 2),
            'features_used': self.feature_columns,
            'thresholds': self.thresholds,
            'trained_at': datetime.now().isoformat()
        }
        
        print(f"[TRAIN] Anomalies detected: {num_anomalies} ({anomaly_rate:.1f}%)")
        print(f"[TRAIN] Score range: [{scores.min():.3f}, {scores.max():.3f}]")
        print(f"[TRAIN] Anomaly threshold: {self.thresholds['anomaly_threshold']:.3f}")
        
        return summary
    
    def predict(self, data: Dict) -> Dict:
        """
        Predict anomaly for a single telemetry reading.
        
        Combines:
        1. Isolation Forest ML score
        2. Rule-based physical limit checks
        
        Args:
            data: Dict with battery telemetry values
        
        Returns:
            Dict with anomaly score, type, severity, and recommendations
        """
        result = {
            'is_anomaly': False,
            'anomaly_score': 0.0,
            'anomaly_types': [],
            'severity': 'normal',
            'severity_score': 0.0,
            'alerts': [],
            'recommendations': []
        }
        
        # --- Rule-based detection (always active) ---
        self._check_physical_limits(data, result)
        
        # --- ML-based detection (if trained) ---
        if self.is_trained:
            ml_result = self._ml_predict(data)
            result['ml_anomaly_score'] = ml_result['score']
            result['ml_is_anomaly'] = ml_result['is_anomaly']
            
            if ml_result['is_anomaly']:
                result['is_anomaly'] = True
                result['anomaly_types'].append('ml_detected')
                result['alerts'].append(f"ML anomaly score: {ml_result['score']:.3f}")
        
        # --- Combine scores ---
        rule_severity = result['severity_score']
        ml_severity = (1 - result.get('ml_anomaly_score', 0.5)) if self.is_trained else 0
        result['anomaly_score'] = max(rule_severity, ml_severity)
        
        # Determine overall severity
        score = result['anomaly_score']
        if score >= 0.8:
            result['severity'] = 'critical'
        elif score >= 0.5:
            result['severity'] = 'high'
        elif score >= 0.3:
            result['severity'] = 'medium'
        elif score > 0:
            result['severity'] = 'low'
        else:
            result['severity'] = 'normal'
        
        return result
    
    def _check_physical_limits(self, data: Dict, result: Dict):
        """Check against physical limits and thresholds."""
        temp = data.get('temperature', data.get('avg_temperature_c', 0))
        voltage = data.get('voltage', data.get('avg_voltage_v', 0))
        current = data.get('current', 0)
        soc = data.get('soc', data.get('soc_percent', 50))
        
        # Temperature checks
        if temp > self.physical_limits['temperature_max']:
            result['is_anomaly'] = True
            result['anomaly_types'].append('critical_thermal')
            result['severity_score'] = max(result['severity_score'], 0.95)
            result['alerts'].append(f"CRITICAL: Temperature {temp:.1f}C exceeds {self.physical_limits['temperature_max']}C")
            result['recommendations'].append("IMMEDIATE: Shut down vehicle and cool battery")
        elif temp > self.physical_limits['temperature_warning']:
            result['is_anomaly'] = True
            result['anomaly_types'].append('thermal_warning')
            result['severity_score'] = max(result['severity_score'], 0.6)
            result['alerts'].append(f"WARNING: Temperature {temp:.1f}C approaching critical")
            result['recommendations'].append("Reduce load and monitor temperature closely")
        
        # Voltage checks (pack level)
        if voltage > 0:  # Only check if voltage data exists
            if voltage < self.physical_limits['voltage_min']:
                result['is_anomaly'] = True
                result['anomaly_types'].append('under_voltage')
                result['severity_score'] = max(result['severity_score'], 0.7)
                result['alerts'].append(f"Under-voltage: {voltage:.1f}V")
                result['recommendations'].append("Stop discharging immediately")
            elif voltage > self.physical_limits['voltage_max']:
                result['is_anomaly'] = True
                result['anomaly_types'].append('over_voltage')
                result['severity_score'] = max(result['severity_score'], 0.8)
                result['alerts'].append(f"Over-voltage: {voltage:.1f}V")
                result['recommendations'].append("Disconnect charger immediately")
        
        # Current checks
        if abs(current) > self.physical_limits['current_max']:
            result['is_anomaly'] = True
            result['anomaly_types'].append('current_surge')
            result['severity_score'] = max(result['severity_score'], 0.75)
            result['alerts'].append(f"Current surge: {current:.1f}A")
            result['recommendations'].append("Check for short circuit or load issues")
        
        # SoC checks
        if soc < self.physical_limits['soc_min']:
            result['is_anomaly'] = True
            result['anomaly_types'].append('deep_discharge')
            result['severity_score'] = max(result['severity_score'], 0.6)
            result['alerts'].append(f"Deep discharge: SoC at {soc:.1f}%")
            result['recommendations'].append("Charge immediately to prevent damage")
    
    def _ml_predict(self, data: Dict) -> Dict:
        """Run Isolation Forest prediction on a single sample."""
        # Map input data to feature columns
        feature_values = []
        for col in self.feature_columns:
            # Handle both raw telemetry and preprocessed data formats
            key_mapping = {
                'avg_temperature_c': data.get('temperature', data.get('avg_temperature_c', 30)),
                'max_temperature_c': data.get('max_temperature', data.get('max_temperature_c', 35)),
                'avg_voltage_v': data.get('voltage', data.get('avg_voltage_v', 3.5)),
                'capacity_ah': data.get('capacity', data.get('capacity_ah', 1.8)),
                'internal_resistance_ohm': data.get('internal_resistance', data.get('internal_resistance_ohm', 0.04)),
            }
            value = key_mapping.get(col, data.get(col, 0))
            feature_values.append(value)
        
        X = np.array(feature_values).reshape(1, -1)
        X_scaled = self.scaler.transform(X)
        
        score = self.model.decision_function(X_scaled)[0]
        prediction = self.model.predict(X_scaled)[0]
        
        return {
            'score': float(score),
            'is_anomaly': prediction == -1
        }
    
    def predict_batch(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Run anomaly detection on a batch of data.
        
        Returns DataFrame with anomaly scores and labels.
        """
        if not self.is_trained:
            raise RuntimeError("Model not trained. Call train() first.")
        
        X = df[self.feature_columns].values
        X_scaled = self.scaler.transform(X)
        
        scores = self.model.decision_function(X_scaled)
        predictions = self.model.predict(X_scaled)
        
        df = df.copy()
        df['anomaly_score'] = scores
        df['is_anomaly'] = predictions == -1
        df['anomaly_severity'] = df['anomaly_score'].apply(
            lambda s: 'critical' if s < self.thresholds.get('anomaly_threshold', -0.1) else
                      'warning' if s < self.thresholds.get('warning_threshold', 0) else 'normal'
        )
        
        return df
    
    def save(self, model_dir: str):
        """Save the trained model and scaler."""
        os.makedirs(model_dir, exist_ok=True)
        
        joblib.dump(self.model, os.path.join(model_dir, 'anomaly_detector.joblib'))
        joblib.dump(self.scaler, os.path.join(model_dir, 'anomaly_scaler.joblib'))
        
        metadata = {
            'feature_columns': self.feature_columns,
            'thresholds': self.thresholds,
            'physical_limits': self.physical_limits,
            'saved_at': datetime.now().isoformat()
        }
        with open(os.path.join(model_dir, 'anomaly_metadata.json'), 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"[SAVE] Anomaly detector saved to {model_dir}")
    
    def load(self, model_dir: str):
        """Load a trained model."""
        self.model = joblib.load(os.path.join(model_dir, 'anomaly_detector.joblib'))
        self.scaler = joblib.load(os.path.join(model_dir, 'anomaly_scaler.joblib'))
        
        with open(os.path.join(model_dir, 'anomaly_metadata.json'), 'r') as f:
            metadata = json.load(f)
        
        self.feature_columns = metadata['feature_columns']
        self.thresholds = metadata['thresholds']
        self.physical_limits = metadata['physical_limits']
        self.is_trained = True
        
        print(f"[LOAD] Anomaly detector loaded from {model_dir}")


def train_and_save(data_path: str, model_dir: str):
    """Convenience function to train and save the anomaly detector."""
    df = pd.read_csv(data_path)
    
    detector = AnomalyDetector(contamination=0.05)
    summary = detector.train(df)
    
    # Run batch prediction on training data
    df_scored = detector.predict_batch(df)
    anomalies = df_scored[df_scored['is_anomaly']]
    
    print(f"\n[RESULT] Found {len(anomalies)} anomalous readings in training data")
    if len(anomalies) > 0:
        print(f"[RESULT] Anomaly distribution by battery:")
        for bid, group in anomalies.groupby('battery_id'):
            print(f"  {bid}: {len(group)} anomalies")
    
    detector.save(model_dir)
    
    # Save scored data
    scored_path = os.path.join(os.path.dirname(data_path), 'battery_anomaly_scores.csv')
    df_scored.to_csv(scored_path, index=False)
    print(f"[SAVE] Scored data: {scored_path}")
    
    return detector, summary


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'processed', 'battery_features_unscaled.csv')
    model_dir = os.path.join(base_dir, 'models')
    
    if os.path.exists(data_path):
        train_and_save(data_path, model_dir)
    else:
        print(f"[ERROR] Data not found: {data_path}")
        print("Run preprocessing/pipeline.py first!")
```

---

## ml\engines\battery_predictor.py

```python
"""
Battery Health Predictor
========================
Uses XGBoost to predict:
1. State of Health (SoH) - Current battery health percentage
2. Remaining Useful Life (RUL) - Cycles remaining before failure

Trained on NASA Battery PCoE format data.
"""

import numpy as np
import pandas as pd
import os
import json
import joblib
from datetime import datetime
from typing import Dict, Tuple, Optional

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler


class BatteryHealthPredictor:
    """
    XGBoost-based battery health prediction engine.
    
    Two models:
    1. SoH Model: Predicts current State of Health (%)
    2. RUL Model: Predicts Remaining Useful Life (cycles)
    """
    
    def __init__(self):
        self.soh_model = XGBRegressor(
            n_estimators=300,
            max_depth=6,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            reg_alpha=0.1,
            reg_lambda=1.0,
            random_state=42,
            n_jobs=-1
        )
        
        self.rul_model = XGBRegressor(
            n_estimators=400,
            max_depth=7,
            learning_rate=0.03,
            subsample=0.8,
            colsample_bytree=0.8,
            reg_alpha=0.5,
            reg_lambda=2.0,
            min_child_weight=3,
            random_state=42,
            n_jobs=-1
        )
        
        self.soh_scaler = StandardScaler()
        self.rul_scaler = StandardScaler()
        self.feature_columns = []
        self.soh_trained = False
        self.rul_trained = False
        self.training_metrics = {}
    
    def _get_features(self, df: pd.DataFrame) -> list:
        """Select features for prediction models."""
        candidate_features = [
            'cycle', 'capacity_ah', 'avg_voltage_v', 'voltage_charged_v',
            'voltage_discharged_v', 'charge_current_a', 'discharge_current_a',
            'avg_temperature_c', 'max_temperature_c', 'internal_resistance_ohm',
            'charge_transfer_resistance_ohm', 'discharge_time_s',
            'charge_efficiency_percent', 'discharge_slope_v_per_s',
            'capacity_degradation_rate', 'cumulative_capacity_loss',
            'resistance_growth_rate', 'temp_rolling_mean', 'temp_rolling_std',
            'thermal_variance', 'voltage_spread', 'capacity_rolling_std',
            'efficiency_drop', 'discharge_rate', 'impedance_ratio',
            'cycle_age_normalized'
        ]
        return [c for c in candidate_features if c in df.columns]
    
    def train_soh(self, df: pd.DataFrame) -> Dict:
        """
        Train SoH prediction model.
        
        Target: soh_percent (0-100)
        """
        print("\n" + "=" * 50)
        print("Training SoH Prediction Model (XGBoost)")
        print("=" * 50)
        
        self.feature_columns = self._get_features(df)
        
        # Exclude SoH-correlated features that would be "cheating"
        soh_features = [f for f in self.feature_columns 
                       if f not in ['soh_percent', 'rul_cycles']]
        
        X = df[soh_features].values
        y = df['soh_percent'].values
        
        # Scale
        X_scaled = self.soh_scaler.fit_transform(X)
        
        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        
        print(f"[TRAIN] Features: {len(soh_features)}")
        print(f"[TRAIN] Train: {len(X_train)} | Test: {len(X_test)}")
        
        # Train
        self.soh_model.fit(
            X_train, y_train,
            eval_set=[(X_test, y_test)],
            verbose=False
        )
        
        # Evaluate
        y_pred = self.soh_model.predict(X_test)
        
        metrics = {
            'rmse': float(np.sqrt(mean_squared_error(y_test, y_pred))),
            'mae': float(mean_absolute_error(y_test, y_pred)),
            'r2': float(r2_score(y_test, y_pred)),
            'features': soh_features,
            'train_size': len(X_train),
            'test_size': len(X_test),
        }
        
        self.soh_trained = True
        self.training_metrics['soh'] = metrics
        self._soh_features = soh_features
        
        print(f"[RESULT] RMSE: {metrics['rmse']:.3f}")
        print(f"[RESULT] MAE:  {metrics['mae']:.3f}")
        print(f"[RESULT] R2:   {metrics['r2']:.4f}")
        
        # Feature importance
        importances = self.soh_model.feature_importances_
        top_features = sorted(zip(soh_features, importances), 
                            key=lambda x: x[1], reverse=True)[:5]
        print("\n[FEATURES] Top 5 most important:")
        for feat, imp in top_features:
            print(f"  {feat}: {imp:.4f}")
        
        return metrics
    
    def train_rul(self, df: pd.DataFrame) -> Dict:
        """
        Train RUL prediction model.
        
        Target: rul_cycles (remaining cycles to failure)
        """
        print("\n" + "=" * 50)
        print("Training RUL Prediction Model (XGBoost)")
        print("=" * 50)
        
        # RUL features - exclude RUL itself and direct SoH
        rul_features = [f for f in self._get_features(df) 
                       if f not in ['rul_cycles', 'soh_percent']]
        
        X = df[rul_features].values
        y = df['rul_cycles'].values
        
        # Clip RUL to reasonable range
        y = np.clip(y, 0, 1000)
        
        # Scale
        X_scaled = self.rul_scaler.fit_transform(X)
        
        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        
        print(f"[TRAIN] Features: {len(rul_features)}")
        print(f"[TRAIN] Train: {len(X_train)} | Test: {len(X_test)}")
        
        # Train
        self.rul_model.fit(
            X_train, y_train,
            eval_set=[(X_test, y_test)],
            verbose=False
        )
        
        # Evaluate
        y_pred = self.rul_model.predict(X_test)
        y_pred = np.maximum(y_pred, 0)  # RUL can't be negative
        
        metrics = {
            'rmse': float(np.sqrt(mean_squared_error(y_test, y_pred))),
            'mae': float(mean_absolute_error(y_test, y_pred)),
            'r2': float(r2_score(y_test, y_pred)),
            'features': rul_features,
            'train_size': len(X_train),
            'test_size': len(X_test),
        }
        
        self.rul_trained = True
        self.training_metrics['rul'] = metrics
        self._rul_features = rul_features
        
        print(f"[RESULT] RMSE: {metrics['rmse']:.3f} cycles")
        print(f"[RESULT] MAE:  {metrics['mae']:.3f} cycles")
        print(f"[RESULT] R2:   {metrics['r2']:.4f}")
        
        # Feature importance
        importances = self.rul_model.feature_importances_
        top_features = sorted(zip(rul_features, importances),
                            key=lambda x: x[1], reverse=True)[:5]
        print("\n[FEATURES] Top 5 most important:")
        for feat, imp in top_features:
            print(f"  {feat}: {imp:.4f}")
        
        return metrics
    
    def predict_soh(self, data: Dict) -> Dict:
        """Predict SoH for a single battery reading."""
        if not self.soh_trained:
            raise RuntimeError("SoH model not trained")
        
        features = []
        for col in self._soh_features:
            features.append(data.get(col, 0))
        
        X = np.array(features).reshape(1, -1)
        X_scaled = self.soh_scaler.transform(X)
        soh = float(self.soh_model.predict(X_scaled)[0])
        soh = max(0, min(100, soh))
        
        # Health category
        if soh >= 85:
            health_status = 'good'
            recommendation = 'Battery in good condition. Continue normal operation.'
        elif soh >= 70:
            health_status = 'fair'
            recommendation = 'Battery showing wear. Monitor closely and plan replacement.'
        elif soh >= 50:
            health_status = 'poor'
            recommendation = 'Battery significantly degraded. Schedule replacement soon.'
        else:
            health_status = 'critical'
            recommendation = 'Battery near end of life. Replace immediately.'
        
        return {
            'soh_percent': round(soh, 2),
            'health_status': health_status,
            'recommendation': recommendation,
            'confidence': round(self.training_metrics['soh']['r2'] * 100, 1)
        }
    
    def predict_rul(self, data: Dict) -> Dict:
        """Predict RUL for a single battery reading."""
        if not self.rul_trained:
            raise RuntimeError("RUL model not trained")
        
        features = []
        for col in self._rul_features:
            features.append(data.get(col, 0))
        
        X = np.array(features).reshape(1, -1)
        X_scaled = self.rul_scaler.transform(X)
        rul = float(self.rul_model.predict(X_scaled)[0])
        rul = max(0, rul)
        
        # Urgency level
        if rul > 200:
            urgency = 'low'
            action = 'No immediate action required.'
        elif rul > 100:
            urgency = 'medium'
            action = 'Begin planning battery replacement.'
        elif rul > 30:
            urgency = 'high'
            action = 'Order replacement battery. Schedule within 2 weeks.'
        else:
            urgency = 'critical'
            action = 'URGENT: Battery replacement needed immediately.'
        
        # Estimate days (assuming ~2 cycles per day for industrial EVs)
        estimated_days = round(rul / 2)
        
        return {
            'rul_cycles': round(rul, 1),
            'estimated_days': estimated_days,
            'urgency': urgency,
            'action': action,
            'confidence': round(self.training_metrics['rul']['r2'] * 100, 1)
        }
    
    def predict_full(self, data: Dict) -> Dict:
        """Get both SoH and RUL predictions."""
        result = {
            'timestamp': datetime.now().isoformat(),
            'battery_id': data.get('battery_id', 'unknown')
        }
        
        if self.soh_trained:
            result['soh'] = self.predict_soh(data)
        
        if self.rul_trained:
            result['rul'] = self.predict_rul(data)
        
        return result
    
    def predict_batch(self, df: pd.DataFrame) -> pd.DataFrame:
        """Run predictions on a batch of data."""
        df = df.copy()
        
        if self.soh_trained:
            X_soh = df[self._soh_features].values
            X_soh_scaled = self.soh_scaler.transform(X_soh)
            df['predicted_soh'] = self.soh_model.predict(X_soh_scaled)
            df['predicted_soh'] = df['predicted_soh'].clip(0, 100)
        
        if self.rul_trained:
            X_rul = df[self._rul_features].values
            X_rul_scaled = self.rul_scaler.transform(X_rul)
            df['predicted_rul'] = self.rul_model.predict(X_rul_scaled)
            df['predicted_rul'] = df['predicted_rul'].clip(0)
        
        return df
    
    def save(self, model_dir: str):
        """Save all models and metadata."""
        os.makedirs(model_dir, exist_ok=True)
        
        if self.soh_trained:
            joblib.dump(self.soh_model, os.path.join(model_dir, 'soh_model.joblib'))
            joblib.dump(self.soh_scaler, os.path.join(model_dir, 'soh_scaler.joblib'))
        
        if self.rul_trained:
            joblib.dump(self.rul_model, os.path.join(model_dir, 'rul_model.joblib'))
            joblib.dump(self.rul_scaler, os.path.join(model_dir, 'rul_scaler.joblib'))
        
        metadata = {
            'soh_features': getattr(self, '_soh_features', []),
            'rul_features': getattr(self, '_rul_features', []),
            'training_metrics': self.training_metrics,
            'soh_trained': self.soh_trained,
            'rul_trained': self.rul_trained,
            'saved_at': datetime.now().isoformat()
        }
        with open(os.path.join(model_dir, 'battery_predictor_metadata.json'), 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"[SAVE] Battery predictor saved to {model_dir}")
    
    def load(self, model_dir: str):
        """Load trained models."""
        with open(os.path.join(model_dir, 'battery_predictor_metadata.json'), 'r') as f:
            metadata = json.load(f)
        
        self._soh_features = metadata['soh_features']
        self._rul_features = metadata['rul_features']
        self.training_metrics = metadata['training_metrics']
        
        if metadata['soh_trained']:
            self.soh_model = joblib.load(os.path.join(model_dir, 'soh_model.joblib'))
            self.soh_scaler = joblib.load(os.path.join(model_dir, 'soh_scaler.joblib'))
            self.soh_trained = True
        
        if metadata['rul_trained']:
            self.rul_model = joblib.load(os.path.join(model_dir, 'rul_model.joblib'))
            self.rul_scaler = joblib.load(os.path.join(model_dir, 'rul_scaler.joblib'))
            self.rul_trained = True
        
        print(f"[LOAD] Battery predictor loaded from {model_dir}")
        print(f"  SoH model: {'loaded' if self.soh_trained else 'not available'}")
        print(f"  RUL model: {'loaded' if self.rul_trained else 'not available'}")


def train_and_save(data_path: str, model_dir: str):
    """Convenience: train both models and save."""
    df = pd.read_csv(data_path)
    
    predictor = BatteryHealthPredictor()
    
    # Train SoH model
    soh_metrics = predictor.train_soh(df)
    
    # Train RUL model
    rul_metrics = predictor.train_rul(df)
    
    # Save
    predictor.save(model_dir)
    
    # Run batch predictions and save
    df_predicted = predictor.predict_batch(df)
    pred_path = os.path.join(os.path.dirname(data_path), 'battery_predictions.csv')
    df_predicted.to_csv(pred_path, index=False)
    print(f"\n[SAVE] Predictions saved: {pred_path}")
    
    # Print example predictions
    print("\n" + "=" * 50)
    print("Example Predictions")
    print("=" * 50)
    sample = df.iloc[0].to_dict()
    full_pred = predictor.predict_full(sample)
    print(json.dumps(full_pred, indent=2))
    
    return predictor


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'processed', 'battery_features_unscaled.csv')
    model_dir = os.path.join(base_dir, 'models')
    
    if os.path.exists(data_path):
        train_and_save(data_path, model_dir)
    else:
        print(f"[ERROR] Data not found: {data_path}")
        print("Run preprocessing/pipeline.py first!")
```

---

## ml\engines\carbon_engine.py

```python
"""
Carbon Intelligence Engine
===========================
Calculates CO2 emissions, diesel vs EV comparisons,
Scope-1/Scope-3 estimation, and fleet sustainability metrics.

Based on EPA GHG emission factors and OWID CO2 datasets.
"""

import numpy as np
import pandas as pd
import os
import json
from datetime import datetime
from typing import Dict, List, Optional


# ============================================================
# EPA/Standard Emission Factors
# ============================================================

# Source: EPA GHG Emission Factors Hub 2025
EMISSION_FACTORS = {
    # Fuel emission factors (kg CO2 per unit)
    'diesel_kg_co2_per_liter': 2.68,       # EPA: 2.68 kg CO2/liter diesel
    'gasoline_kg_co2_per_liter': 2.31,     # EPA: 2.31 kg CO2/liter gasoline
    'cng_kg_co2_per_kg': 2.75,             # Compressed natural gas
    
    # Electricity grid emission factors (kg CO2 per kWh)
    # Varies by region - using common values
    'grid_india_kg_co2_per_kwh': 0.708,     # India grid average
    'grid_us_avg_kg_co2_per_kwh': 0.386,    # US national average
    'grid_eu_avg_kg_co2_per_kwh': 0.276,    # EU average
    'grid_china_kg_co2_per_kwh': 0.555,     # China grid average
    'grid_renewable_kg_co2_per_kwh': 0.020, # Renewable/solar
    
    # Vehicle consumption defaults
    'diesel_truck_l_per_100km': 32.0,       # Medium/heavy duty diesel truck
    'diesel_van_l_per_100km': 12.0,         # Delivery van
    'ev_truck_kwh_per_km': 1.2,             # EV truck consumption
    'ev_van_kwh_per_km': 0.25,              # EV van consumption
    'ev_bus_kwh_per_km': 1.5,               # Electric bus
}

# Vehicle categories
VEHICLE_CATEGORIES = {
    'heavy_truck': {
        'diesel_l_per_100km': 35.0,
        'ev_kwh_per_km': 1.4,
        'payload_tons': 20,
        'annual_km': 80000,
    },
    'medium_truck': {
        'diesel_l_per_100km': 25.0,
        'ev_kwh_per_km': 0.8,
        'payload_tons': 10,
        'annual_km': 60000,
    },
    'delivery_van': {
        'diesel_l_per_100km': 12.0,
        'ev_kwh_per_km': 0.25,
        'payload_tons': 2,
        'annual_km': 40000,
    },
    'bus': {
        'diesel_l_per_100km': 30.0,
        'ev_kwh_per_km': 1.3,
        'payload_tons': 8,
        'annual_km': 70000,
    }
}


class CarbonIntelligenceEngine:
    """
    Calculates and compares carbon emissions between diesel and EV fleets.
    
    Provides:
    - Per-vehicle emission calculations
    - Fleet-wide carbon savings
    - Scope-1 and Scope-3 estimates
    - Sustainability metrics and equivalents
    """
    
    def __init__(self, grid_region: str = 'india'):
        """
        Args:
            grid_region: Electricity grid region for emission factors
                         Options: 'india', 'us', 'eu', 'china', 'renewable'
        """
        grid_key = f'grid_{grid_region}_kg_co2_per_kwh'
        if grid_key not in EMISSION_FACTORS:
            grid_key = 'grid_india_kg_co2_per_kwh'
        
        self.grid_emission_factor = EMISSION_FACTORS[grid_key]
        self.grid_region = grid_region
        self.diesel_factor = EMISSION_FACTORS['diesel_kg_co2_per_liter']
    
    def calculate_diesel_emissions(self, 
                                    distance_km: float,
                                    vehicle_type: str = 'medium_truck',
                                    custom_consumption: Optional[float] = None) -> Dict:
        """
        Calculate CO2 emissions for a diesel vehicle.
        
        Args:
            distance_km: Total distance driven
            vehicle_type: Type of vehicle
            custom_consumption: Override fuel consumption (L/100km)
        """
        category = VEHICLE_CATEGORIES.get(vehicle_type, VEHICLE_CATEGORIES['medium_truck'])
        consumption = custom_consumption or category['diesel_l_per_100km']
        
        # Fuel used
        fuel_liters = distance_km * consumption / 100
        
        # CO2 emissions (Scope 1 - direct combustion)
        co2_kg = fuel_liters * self.diesel_factor
        
        # Well-to-tank emissions (Scope 3 upstream) ~20% additional
        scope3_upstream = co2_kg * 0.20
        
        return {
            'distance_km': distance_km,
            'vehicle_type': vehicle_type,
            'fuel_type': 'diesel',
            'fuel_consumed_liters': round(fuel_liters, 2),
            'consumption_l_per_100km': consumption,
            'scope_1_co2_kg': round(co2_kg, 2),
            'scope_3_upstream_co2_kg': round(scope3_upstream, 2),
            'total_co2_kg': round(co2_kg + scope3_upstream, 2),
            'co2_per_km_kg': round((co2_kg + scope3_upstream) / max(distance_km, 1), 4),
        }
    
    def calculate_ev_emissions(self,
                                distance_km: float,
                                vehicle_type: str = 'medium_truck',
                                custom_consumption: Optional[float] = None,
                                renewable_fraction: float = 0.0) -> Dict:
        """
        Calculate CO2 emissions for an EV.
        
        Args:
            distance_km: Total distance driven
            vehicle_type: Type of vehicle
            custom_consumption: Override energy consumption (kWh/km)
            renewable_fraction: Fraction of charging from renewables (0-1)
        """
        category = VEHICLE_CATEGORIES.get(vehicle_type, VEHICLE_CATEGORIES['medium_truck'])
        consumption = custom_consumption or category['ev_kwh_per_km']
        
        # Energy used
        energy_kwh = distance_km * consumption
        
        # Grid emissions (Scope 2)
        grid_energy = energy_kwh * (1 - renewable_fraction)
        renewable_energy = energy_kwh * renewable_fraction
        
        scope2_co2 = grid_energy * self.grid_emission_factor
        scope2_co2 += renewable_energy * EMISSION_FACTORS['grid_renewable_kg_co2_per_kwh']
        
        # Scope 3: Battery manufacturing lifecycle (~30-40 kg CO2/kWh battery capacity)
        # Amortized over battery life (~200,000 km)
        battery_lifecycle_co2_per_km = 0.05  # kg CO2/km (amortized)
        scope3_co2 = distance_km * battery_lifecycle_co2_per_km
        
        return {
            'distance_km': distance_km,
            'vehicle_type': vehicle_type,
            'fuel_type': 'electric',
            'energy_consumed_kwh': round(energy_kwh, 2),
            'consumption_kwh_per_km': consumption,
            'grid_region': self.grid_region,
            'grid_emission_factor': self.grid_emission_factor,
            'renewable_fraction': renewable_fraction,
            'scope_1_co2_kg': 0,  # EVs have zero direct emissions
            'scope_2_co2_kg': round(scope2_co2, 2),
            'scope_3_battery_co2_kg': round(scope3_co2, 2),
            'total_co2_kg': round(scope2_co2 + scope3_co2, 2),
            'co2_per_km_kg': round((scope2_co2 + scope3_co2) / max(distance_km, 1), 4),
        }
    
    def compare_diesel_vs_ev(self,
                              distance_km: float,
                              vehicle_type: str = 'medium_truck',
                              renewable_fraction: float = 0.0) -> Dict:
        """
        Compare emissions between diesel and EV for the same journey.
        """
        diesel = self.calculate_diesel_emissions(distance_km, vehicle_type)
        ev = self.calculate_ev_emissions(distance_km, vehicle_type, 
                                          renewable_fraction=renewable_fraction)
        
        savings_kg = diesel['total_co2_kg'] - ev['total_co2_kg']
        savings_percent = (savings_kg / max(diesel['total_co2_kg'], 0.001)) * 100
        
        return {
            'diesel': diesel,
            'ev': ev,
            'savings': {
                'co2_saved_kg': round(savings_kg, 2),
                'co2_saved_percent': round(savings_percent, 1),
                'equivalent_trees_year': round(savings_kg / 22, 1),  # 1 tree absorbs ~22kg CO2/year
                'equivalent_gallons_gasoline': round(savings_kg / 8.89, 1),
            }
        }
    
    def analyze_fleet(self, fleet: List[Dict]) -> Dict:
        """
        Analyze carbon impact for an entire fleet.
        
        Args:
            fleet: List of vehicle dicts with keys:
                   'vehicle_id', 'vehicle_type', 'annual_km', 
                   'fuel_type' ('diesel' or 'electric'),
                   'renewable_fraction' (optional)
        """
        results = []
        total_diesel_co2 = 0
        total_ev_co2 = 0
        total_savings = 0
        total_distance = 0
        
        for vehicle in fleet:
            vid = vehicle.get('vehicle_id', 'unknown')
            vtype = vehicle.get('vehicle_type', 'medium_truck')
            annual_km = vehicle.get('annual_km', VEHICLE_CATEGORIES.get(vtype, {}).get('annual_km', 50000))
            fuel_type = vehicle.get('fuel_type', 'electric')
            renewable = vehicle.get('renewable_fraction', 0.0)
            
            comparison = self.compare_diesel_vs_ev(annual_km, vtype, renewable)
            
            results.append({
                'vehicle_id': vid,
                'vehicle_type': vtype,
                'annual_km': annual_km,
                'current_fuel': fuel_type,
                'diesel_co2_tons': round(comparison['diesel']['total_co2_kg'] / 1000, 3),
                'ev_co2_tons': round(comparison['ev']['total_co2_kg'] / 1000, 3),
                'savings_tons': round(comparison['savings']['co2_saved_kg'] / 1000, 3),
                'savings_percent': comparison['savings']['co2_saved_percent'],
            })
            
            total_diesel_co2 += comparison['diesel']['total_co2_kg']
            total_ev_co2 += comparison['ev']['total_co2_kg']
            total_savings += comparison['savings']['co2_saved_kg']
            total_distance += annual_km
        
        fleet_summary = {
            'fleet_size': len(fleet),
            'total_annual_km': total_distance,
            'diesel_scenario': {
                'total_co2_tons': round(total_diesel_co2 / 1000, 2),
                'co2_per_km_g': round(total_diesel_co2 / max(total_distance, 1) * 1000, 1),
            },
            'ev_scenario': {
                'total_co2_tons': round(total_ev_co2 / 1000, 2),
                'co2_per_km_g': round(total_ev_co2 / max(total_distance, 1) * 1000, 1),
            },
            'savings': {
                'co2_saved_tons': round(total_savings / 1000, 2),
                'co2_saved_percent': round(total_savings / max(total_diesel_co2, 1) * 100, 1),
                'equivalent_trees': round(total_savings / 22),
                'equivalent_homes_electricity': round(total_savings / 4000),  # ~4 tons CO2/home/year
                'equivalent_flights_nyc_london': round(total_savings / 1000),  # ~1 ton/flight
            },
            'scope_summary': {
                'scope_1_tons': round(total_diesel_co2 / 1000, 2) if any(v.get('fuel_type') == 'diesel' for v in fleet) else 0,
                'scope_2_tons': round(total_ev_co2 * 0.85 / 1000, 2),
                'scope_3_tons': round(total_ev_co2 * 0.15 / 1000, 2),
            },
            'vehicle_details': results,
            'grid_region': self.grid_region,
            'calculated_at': datetime.now().isoformat()
        }
        
        return fleet_summary
    
    def generate_sample_fleet(self, size: int = 50) -> List[Dict]:
        """Generate a sample fleet for analysis."""
        fleet = []
        vehicle_types = ['heavy_truck', 'medium_truck', 'delivery_van', 'bus']
        weights = [0.2, 0.4, 0.3, 0.1]
        
        for i in range(size):
            vtype = np.random.choice(vehicle_types, p=weights)
            category = VEHICLE_CATEGORIES[vtype]
            
            fleet.append({
                'vehicle_id': f'EV-{i+1:03d}',
                'vehicle_type': vtype,
                'annual_km': int(category['annual_km'] * np.random.uniform(0.7, 1.3)),
                'fuel_type': 'electric',
                'renewable_fraction': np.random.uniform(0.0, 0.3)
            })
        
        return fleet
    
    def save_analysis(self, output_dir: str, fleet: Optional[List[Dict]] = None):
        """Run full analysis and save results."""
        os.makedirs(output_dir, exist_ok=True)
        
        if fleet is None:
            fleet = self.generate_sample_fleet(50)
        
        print("\n" + "=" * 60)
        print("Carbon Intelligence Analysis")
        print("=" * 60)
        
        # Fleet analysis
        summary = self.analyze_fleet(fleet)
        
        print(f"\n  Fleet Size: {summary['fleet_size']}")
        print(f"  Total Annual KM: {summary['total_annual_km']:,}")
        print(f"  Grid Region: {summary['grid_region']}")
        print(f"\n  DIESEL SCENARIO: {summary['diesel_scenario']['total_co2_tons']:.1f} tons CO2/year")
        print(f"  EV SCENARIO:     {summary['ev_scenario']['total_co2_tons']:.1f} tons CO2/year")
        print(f"  CO2 SAVED:       {summary['savings']['co2_saved_tons']:.1f} tons/year ({summary['savings']['co2_saved_percent']:.1f}%)")
        print(f"\n  Equivalents:")
        print(f"    Trees planted: {summary['savings']['equivalent_trees']:,}")
        print(f"    Homes powered: {summary['savings']['equivalent_homes_electricity']}")
        print(f"    NYC-London flights: {summary['savings']['equivalent_flights_nyc_london']}")
        
        # Save results
        with open(os.path.join(output_dir, 'carbon_analysis.json'), 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Save vehicle details as CSV
        df = pd.DataFrame(summary['vehicle_details'])
        df.to_csv(os.path.join(output_dir, 'carbon_vehicle_details.csv'), index=False)
        
        # Example comparison
        print(f"\n  Single Vehicle Comparison (medium_truck, 60,000 km/year):")
        comparison = self.compare_diesel_vs_ev(60000, 'medium_truck')
        print(f"    Diesel: {comparison['diesel']['total_co2_kg']:.0f} kg CO2")
        print(f"    EV:     {comparison['ev']['total_co2_kg']:.0f} kg CO2")
        print(f"    Saved:  {comparison['savings']['co2_saved_kg']:.0f} kg CO2 ({comparison['savings']['co2_saved_percent']:.0f}%)")
        
        with open(os.path.join(output_dir, 'carbon_comparison_example.json'), 'w') as f:
            json.dump(comparison, f, indent=2)
        
        print(f"\n[SAVE] Results saved to {output_dir}")
        
        return summary


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'data', 'processed')
    
    engine = CarbonIntelligenceEngine(grid_region='india')
    engine.save_analysis(output_dir)
```

---

## ml\engines\maintenance_engine.py

```python
"""
Maintenance Recommendation Engine
==================================
Combines anomaly scores, battery degradation trends, and operational data
to generate maintenance recommendations for each vehicle.

Priority levels: CRITICAL > HIGH > MEDIUM > LOW > ROUTINE
"""

import numpy as np
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class MaintenanceRecommendationEngine:
    """
    Generates smart maintenance recommendations by combining:
    1. Anomaly detection scores
    2. Battery SoH and RUL predictions
    3. Temperature trends
    4. Charging efficiency trends
    5. Operational patterns
    """
    
    # Maintenance action catalog
    MAINTENANCE_ACTIONS = {
        'battery_replacement': {
            'description': 'Full battery pack replacement',
            'estimated_hours': 8,
            'estimated_cost_usd': 15000,
            'category': 'battery'
        },
        'battery_inspection': {
            'description': 'Detailed battery pack inspection and diagnostics',
            'estimated_hours': 2,
            'estimated_cost_usd': 500,
            'category': 'battery'
        },
        'thermal_system_check': {
            'description': 'Battery thermal management system inspection',
            'estimated_hours': 3,
            'estimated_cost_usd': 800,
            'category': 'thermal'
        },
        'cooling_system_service': {
            'description': 'Coolant flush, pump check, fan inspection',
            'estimated_hours': 4,
            'estimated_cost_usd': 1200,
            'category': 'thermal'
        },
        'charging_system_diagnostic': {
            'description': 'Onboard charger and charging port diagnostics',
            'estimated_hours': 2,
            'estimated_cost_usd': 400,
            'category': 'charging'
        },
        'bms_recalibration': {
            'description': 'Battery Management System recalibration',
            'estimated_hours': 1,
            'estimated_cost_usd': 200,
            'category': 'software'
        },
        'cell_balancing': {
            'description': 'Cell voltage balancing procedure',
            'estimated_hours': 6,
            'estimated_cost_usd': 600,
            'category': 'battery'
        },
        'contactor_inspection': {
            'description': 'High-voltage contactor and relay inspection',
            'estimated_hours': 2,
            'estimated_cost_usd': 300,
            'category': 'electrical'
        },
        'routine_service': {
            'description': 'Standard scheduled maintenance check',
            'estimated_hours': 3,
            'estimated_cost_usd': 350,
            'category': 'general'
        },
    }
    
    def __init__(self):
        self.recommendation_history = []
    
    def generate_recommendation(self, vehicle_data: Dict) -> Dict:
        """
        Generate maintenance recommendation for a single vehicle.
        
        Args:
            vehicle_data: Dict containing:
                - vehicle_id: str
                - anomaly_score: float (0-1, from anomaly detector)
                - anomaly_types: list of detected anomaly types
                - soh_percent: float (State of Health)
                - rul_cycles: float (Remaining Useful Life)
                - avg_temperature: float (recent average temperature)
                - temperature_trend: str ('rising', 'stable', 'falling')
                - charging_efficiency: float (%)
                - last_maintenance_days: int (days since last service)
                - odometer_km: float
        """
        vehicle_id = vehicle_data.get('vehicle_id', 'unknown')
        anomaly_score = vehicle_data.get('anomaly_score', 0)
        anomaly_types = vehicle_data.get('anomaly_types', [])
        soh = vehicle_data.get('soh_percent', 100)
        rul = vehicle_data.get('rul_cycles', 500)
        avg_temp = vehicle_data.get('avg_temperature', 30)
        temp_trend = vehicle_data.get('temperature_trend', 'stable')
        charge_eff = vehicle_data.get('charging_efficiency', 95)
        days_since_maint = vehicle_data.get('last_maintenance_days', 30)
        odometer = vehicle_data.get('odometer_km', 0)
        
        actions = []
        priority = 'routine'
        urgency_days = 90  # Default: within 90 days
        
        # ===== Rule-based decision logic =====
        
        # Rule 1: Critical battery condition
        if anomaly_score > 0.8 and soh < 70:
            priority = 'critical'
            urgency_days = 0  # Immediate
            actions.append('battery_replacement')
            actions.append('thermal_system_check')
        
        # Rule 2: High anomaly with thermal issue
        elif anomaly_score > 0.5 and (temp_trend == 'rising' or avg_temp > 45):
            priority = 'high'
            urgency_days = 2
            actions.append('thermal_system_check')
            actions.append('cooling_system_service')
            if 'thermal_spike' in anomaly_types or 'critical_thermal' in anomaly_types:
                actions.append('battery_inspection')
        
        # Rule 3: Low RUL
        elif rul < 30:
            priority = 'critical'
            urgency_days = 1
            actions.append('battery_replacement')
            actions.append('battery_inspection')
        
        elif rul < 100:
            priority = 'high'
            urgency_days = 14
            actions.append('battery_inspection')
            actions.append('bms_recalibration')
        
        # Rule 4: Moderate SoH degradation
        elif soh < 75:
            priority = 'high'
            urgency_days = 7
            actions.append('battery_inspection')
            actions.append('cell_balancing')
        
        elif soh < 85:
            priority = 'medium'
            urgency_days = 30
            actions.append('bms_recalibration')
            actions.append('cell_balancing')
        
        # Rule 5: Charging issues
        elif charge_eff < 80:
            priority = 'high'
            urgency_days = 7
            actions.append('charging_system_diagnostic')
            actions.append('bms_recalibration')
        
        elif charge_eff < 90:
            priority = 'medium'
            urgency_days = 14
            actions.append('charging_system_diagnostic')
        
        # Rule 6: Anomaly detected but no specific pattern
        elif anomaly_score > 0.3:
            priority = 'medium'
            urgency_days = 7
            actions.append('battery_inspection')
            
            if 'voltage_anomaly' in anomaly_types or 'under_voltage' in anomaly_types:
                actions.append('contactor_inspection')
            if 'current_surge' in anomaly_types:
                actions.append('contactor_inspection')
        
        # Rule 7: Overdue routine maintenance
        elif days_since_maint > 60:
            priority = 'low'
            urgency_days = 14
            actions.append('routine_service')
        
        # Rule 8: Everything OK
        else:
            priority = 'routine'
            urgency_days = 90
            actions.append('routine_service')
        
        # Deduplicate actions
        actions = list(dict.fromkeys(actions))
        
        # Build recommendation
        scheduled_date = datetime.now() + timedelta(days=urgency_days)
        
        total_hours = sum(self.MAINTENANCE_ACTIONS[a]['estimated_hours'] for a in actions)
        total_cost = sum(self.MAINTENANCE_ACTIONS[a]['estimated_cost_usd'] for a in actions)
        
        recommendation = {
            'vehicle_id': vehicle_id,
            'priority': priority,
            'urgency_days': urgency_days,
            'scheduled_date': scheduled_date.strftime('%Y-%m-%d'),
            'actions': [
                {
                    'action_id': action,
                    **self.MAINTENANCE_ACTIONS[action]
                } for action in actions
            ],
            'estimated_total_hours': total_hours,
            'estimated_total_cost_usd': total_cost,
            'reasoning': self._generate_reasoning(vehicle_data, priority, actions),
            'vehicle_status': {
                'soh_percent': soh,
                'rul_cycles': rul,
                'anomaly_score': anomaly_score,
                'avg_temperature': avg_temp,
                'charging_efficiency': charge_eff,
                'odometer_km': odometer,
            },
            'generated_at': datetime.now().isoformat()
        }
        
        self.recommendation_history.append(recommendation)
        return recommendation
    
    def _generate_reasoning(self, data: Dict, priority: str, actions: list) -> str:
        """Generate human-readable reasoning for the recommendation."""
        reasons = []
        
        soh = data.get('soh_percent', 100)
        rul = data.get('rul_cycles', 500)
        anomaly_score = data.get('anomaly_score', 0)
        avg_temp = data.get('avg_temperature', 30)
        charge_eff = data.get('charging_efficiency', 95)
        
        if soh < 70:
            reasons.append(f"Battery health critically low at {soh:.0f}%")
        elif soh < 85:
            reasons.append(f"Battery health degraded to {soh:.0f}%")
        
        if rul < 30:
            reasons.append(f"Only {rul:.0f} cycles remaining before end of life")
        elif rul < 100:
            reasons.append(f"Battery approaching end of life ({rul:.0f} cycles remaining)")
        
        if anomaly_score > 0.5:
            reasons.append(f"High anomaly score ({anomaly_score:.2f}) detected")
        
        if avg_temp > 45:
            reasons.append(f"Elevated battery temperature ({avg_temp:.1f}C)")
        
        if charge_eff < 85:
            reasons.append(f"Reduced charging efficiency ({charge_eff:.0f}%)")
        
        if not reasons:
            reasons.append("Routine scheduled maintenance")
        
        return ". ".join(reasons) + "."
    
    def analyze_fleet(self, fleet_data: List[Dict]) -> Dict:
        """
        Generate maintenance schedule for entire fleet.
        
        Args:
            fleet_data: List of vehicle data dicts
        
        Returns:
            Fleet maintenance summary with schedule
        """
        recommendations = []
        for vehicle in fleet_data:
            rec = self.generate_recommendation(vehicle)
            recommendations.append(rec)
        
        # Sort by priority
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3, 'routine': 4}
        recommendations.sort(key=lambda r: priority_order.get(r['priority'], 5))
        
        # Summary
        summary = {
            'fleet_size': len(fleet_data),
            'analysis_date': datetime.now().isoformat(),
            'priority_breakdown': {
                'critical': sum(1 for r in recommendations if r['priority'] == 'critical'),
                'high': sum(1 for r in recommendations if r['priority'] == 'high'),
                'medium': sum(1 for r in recommendations if r['priority'] == 'medium'),
                'low': sum(1 for r in recommendations if r['priority'] == 'low'),
                'routine': sum(1 for r in recommendations if r['priority'] == 'routine'),
            },
            'total_estimated_cost_usd': sum(r['estimated_total_cost_usd'] for r in recommendations),
            'total_estimated_hours': sum(r['estimated_total_hours'] for r in recommendations),
            'immediate_attention_required': sum(1 for r in recommendations if r['urgency_days'] <= 1),
            'this_week': sum(1 for r in recommendations if r['urgency_days'] <= 7),
            'this_month': sum(1 for r in recommendations if r['urgency_days'] <= 30),
            'recommendations': recommendations,
        }
        
        return summary
    
    def generate_sample_fleet_data(self, num_vehicles: int = 50) -> List[Dict]:
        """Generate sample vehicle data for testing."""
        fleet = []
        for i in range(num_vehicles):
            # Vary conditions realistically
            soh = np.random.uniform(55, 100)
            rul = max(0, (soh - 60) / 40 * 500 + np.random.normal(0, 50))
            anomaly_score = max(0, min(1, (100 - soh) / 50 + np.random.normal(0, 0.15)))
            
            vehicle = {
                'vehicle_id': f'EV-{i+1:03d}',
                'anomaly_score': round(anomaly_score, 3),
                'anomaly_types': [],
                'soh_percent': round(soh, 1),
                'rul_cycles': round(rul, 0),
                'avg_temperature': round(np.random.uniform(25, 50), 1),
                'temperature_trend': np.random.choice(['rising', 'stable', 'falling'], p=[0.2, 0.6, 0.2]),
                'charging_efficiency': round(max(70, 99 - (100 - soh) * 0.5 + np.random.normal(0, 2)), 1),
                'last_maintenance_days': np.random.randint(5, 90),
                'odometer_km': np.random.randint(10000, 150000),
            }
            
            # Add anomaly types based on score
            if vehicle['anomaly_score'] > 0.5:
                vehicle['anomaly_types'] = np.random.choice(
                    ['thermal_spike', 'voltage_anomaly', 'current_surge', 'soc_inconsistency'],
                    size=np.random.randint(1, 3), replace=False
                ).tolist()
            
            fleet.append(vehicle)
        
        return fleet
    
    def save_analysis(self, output_dir: str, fleet_data: Optional[List[Dict]] = None):
        """Run full fleet analysis and save results."""
        os.makedirs(output_dir, exist_ok=True)
        
        if fleet_data is None:
            fleet_data = self.generate_sample_fleet_data(50)
        
        print("\n" + "=" * 60)
        print("Maintenance Recommendation Analysis")
        print("=" * 60)
        
        summary = self.analyze_fleet(fleet_data)
        
        print(f"\n  Fleet Size: {summary['fleet_size']}")
        print(f"  Priority Breakdown:")
        for level, count in summary['priority_breakdown'].items():
            print(f"    {level.upper():10s}: {count}")
        print(f"\n  Immediate attention: {summary['immediate_attention_required']} vehicles")
        print(f"  This week: {summary['this_week']} vehicles")
        print(f"  This month: {summary['this_month']} vehicles")
        print(f"  Total estimated cost: ${summary['total_estimated_cost_usd']:,.0f}")
        print(f"  Total estimated hours: {summary['total_estimated_hours']}")
        
        # Show top critical/high recommendations
        critical_high = [r for r in summary['recommendations'] 
                        if r['priority'] in ('critical', 'high')][:5]
        if critical_high:
            print(f"\n  Top Priority Vehicles:")
            for r in critical_high:
                print(f"    {r['vehicle_id']}: [{r['priority'].upper()}] - {r['reasoning'][:80]}")
        
        # Save
        with open(os.path.join(output_dir, 'maintenance_recommendations.json'), 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print(f"\n[SAVE] Results saved to {output_dir}")
        return summary


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'data', 'processed')
    
    engine = MaintenanceRecommendationEngine()
    engine.save_analysis(output_dir)
```

---

## ml\engines\readiness_scorer.py

```python
"""
Fleet Electrification Readiness Scorer
=======================================
Scores how ready each route/vehicle in a fleet is to transition 
from diesel to electric, based on:
- Route distance vs EV range
- Charging infrastructure availability
- Payload impact on range
- Dwell time at depots (charging opportunity)
- Duty cycle intensity
"""

import numpy as np
import json
import os
from datetime import datetime
from typing import Dict, List, Optional


# EV specifications for different vehicle types
EV_SPECS = {
    'heavy_truck': {
        'battery_kwh': 300,
        'range_km': 300,
        'charge_rate_kw': 150,  # DC fast
        'range_reduction_per_ton': 5,  # km lost per ton payload
        'min_soc_threshold': 15,  # Don't go below 15%
    },
    'medium_truck': {
        'battery_kwh': 150,
        'range_km': 250,
        'charge_rate_kw': 100,
        'range_reduction_per_ton': 8,
        'min_soc_threshold': 15,
    },
    'delivery_van': {
        'battery_kwh': 75,
        'range_km': 200,
        'charge_rate_kw': 50,
        'range_reduction_per_ton': 15,
        'min_soc_threshold': 10,
    },
    'bus': {
        'battery_kwh': 200,
        'range_km': 250,
        'charge_rate_kw': 120,
        'range_reduction_per_ton': 6,
        'min_soc_threshold': 15,
    }
}


class FleetReadinessScorer:
    """
    Scores fleet electrification readiness using multiple factors.
    
    Score 0-100:
    - 80-100: Immediately ready for electrification
    - 60-79:  Ready with minor infrastructure additions
    - 40-59:  Feasible with planning and investment
    - 20-39:  Challenging, requires significant changes
    - 0-19:   Not currently feasible
    """
    
    # Factor weights
    WEIGHTS = {
        'range_feasibility': 0.25,
        'charging_availability': 0.25,
        'payload_impact': 0.20,
        'dwell_time': 0.15,
        'duty_cycle': 0.15,
    }
    
    def __init__(self):
        self.assessments = []
    
    def score_route(self, route: Dict) -> Dict:
        """
        Score electrification readiness for a single route.
        
        Args:
            route: Dict with:
                - route_id: str
                - route_name: str (optional)
                - total_distance_km: float
                - vehicle_type: str
                - avg_payload_tons: float
                - max_payload_tons: float
                - charging_stations_along_route: int
                - has_depot_charging: bool
                - depot_dwell_hours: float (time spent at depot)
                - stops_count: int
                - avg_stop_duration_hours: float
                - daily_trips: int
                - terrain: str ('flat', 'hilly', 'mountainous')
                - temperature_extreme: bool (hot/cold climate)
        """
        route_id = route.get('route_id', 'unknown')
        distance = route.get('total_distance_km', 100)
        vehicle_type = route.get('vehicle_type', 'medium_truck')
        payload = route.get('avg_payload_tons', 5)
        max_payload = route.get('max_payload_tons', 10)
        charging_stations = route.get('charging_stations_along_route', 0)
        has_depot_charging = route.get('has_depot_charging', False)
        dwell_hours = route.get('depot_dwell_hours', 8)
        stops = route.get('stops_count', 3)
        avg_stop_hours = route.get('avg_stop_duration_hours', 0.5)
        daily_trips = route.get('daily_trips', 1)
        terrain = route.get('terrain', 'flat')
        temp_extreme = route.get('temperature_extreme', False)
        
        specs = EV_SPECS.get(vehicle_type, EV_SPECS['medium_truck'])
        
        # ===== Factor 1: Range Feasibility (0-100) =====
        # Can the EV complete the route on a single charge?
        effective_range = specs['range_km']
        
        # Payload reduces range
        effective_range -= payload * specs['range_reduction_per_ton']
        
        # Terrain impact
        terrain_factor = {'flat': 1.0, 'hilly': 0.85, 'mountainous': 0.70}.get(terrain, 1.0)
        effective_range *= terrain_factor
        
        # Temperature impact
        if temp_extreme:
            effective_range *= 0.85  # HVAC load reduces range
        
        # Usable range (accounting for min SoC)
        usable_range = effective_range * (1 - specs['min_soc_threshold'] / 100)
        
        daily_distance = distance * daily_trips
        
        if usable_range >= daily_distance:
            range_score = 100  # Can do full day on single charge
        elif usable_range >= distance:
            # Can do one trip, might need mid-day charge for multiple trips
            range_score = max(40, 100 - (daily_distance - usable_range) / usable_range * 60)
        else:
            # Can't even complete one trip
            range_score = max(0, usable_range / distance * 40)
        
        # ===== Factor 2: Charging Availability (0-100) =====
        charge_score = 0
        
        if has_depot_charging:
            charge_score += 50  # Depot charging is most important
        
        # En-route charging
        if distance > usable_range * 0.7:
            # Need en-route charging
            needed_stations = max(1, int(distance / usable_range))
            if charging_stations >= needed_stations:
                charge_score += 50
            elif charging_stations > 0:
                charge_score += 25 * (charging_stations / needed_stations)
        else:
            # Short route, depot charging is sufficient
            charge_score += 40
        
        charge_score = min(100, charge_score)
        
        # ===== Factor 3: Payload Impact (0-100) =====
        # How much does payload reduce EV viability?
        range_with_max_payload = specs['range_km'] - max_payload * specs['range_reduction_per_ton']
        range_with_max_payload *= terrain_factor
        
        if range_with_max_payload >= distance:
            payload_score = 100  # Even max payload works
        elif range_with_max_payload >= distance * 0.7:
            payload_score = 70  # Works most days
        elif range_with_max_payload >= distance * 0.5:
            payload_score = 40  # Marginal
        else:
            payload_score = max(0, range_with_max_payload / distance * 40)
        
        # ===== Factor 4: Dwell Time / Charging Opportunity (0-100) =====
        # Is there enough dwell time at depots/stops to charge?
        charge_time_needed = specs['battery_kwh'] * 0.8 / specs['charge_rate_kw']  # Hours for 80% charge
        
        total_available_charge_time = dwell_hours  # Depot time
        total_available_charge_time += stops * avg_stop_hours * 0.5  # Partial use of stop time
        
        if total_available_charge_time >= charge_time_needed:
            dwell_score = 100
        elif total_available_charge_time >= charge_time_needed * 0.5:
            dwell_score = 60
        else:
            dwell_score = max(10, total_available_charge_time / charge_time_needed * 60)
        
        # ===== Factor 5: Duty Cycle Intensity (0-100) =====
        # How intense is the driving pattern?
        intensity = daily_distance / specs['range_km']  # >1 means multi-charge needed
        
        if intensity <= 0.5:
            duty_score = 100  # Light duty, easy EV
        elif intensity <= 0.8:
            duty_score = 80
        elif intensity <= 1.0:
            duty_score = 60
        elif intensity <= 1.5:
            duty_score = 35  # Heavy, but possible with charging
        else:
            duty_score = max(5, 100 - intensity * 40)
        
        # ===== Weighted Overall Score =====
        overall_score = (
            range_score * self.WEIGHTS['range_feasibility'] +
            charge_score * self.WEIGHTS['charging_availability'] +
            payload_score * self.WEIGHTS['payload_impact'] +
            dwell_score * self.WEIGHTS['dwell_time'] +
            duty_score * self.WEIGHTS['duty_cycle']
        )
        
        # Readiness level
        if overall_score >= 80:
            level = 'excellent'
            recommendation = 'Immediately suitable for electrification'
            color = 'green'
        elif overall_score >= 60:
            level = 'good'
            recommendation = 'Ready with minor infrastructure additions'
            color = 'blue'
        elif overall_score >= 40:
            level = 'moderate'
            recommendation = 'Feasible with planning and investment in charging'
            color = 'yellow'
        elif overall_score >= 20:
            level = 'challenging'
            recommendation = 'Requires significant infrastructure and operational changes'
            color = 'orange'
        else:
            level = 'not_ready'
            recommendation = 'Not currently feasible. Consider hybrid or wait for better range.'
            color = 'red'
        
        # Limiting factor
        factor_scores = {
            'range_feasibility': range_score,
            'charging_availability': charge_score,
            'payload_impact': payload_score,
            'dwell_time': dwell_score,
            'duty_cycle': duty_score
        }
        limiting_factor = min(factor_scores, key=factor_scores.get)
        
        # Estimated ROI
        annual_km = daily_distance * 260  # Working days
        diesel_cost_per_km = 0.15  # USD (fuel + maintenance)
        ev_cost_per_km = 0.06  # USD (electricity + maintenance)
        savings_per_year = annual_km * (diesel_cost_per_km - ev_cost_per_km)
        ev_premium = {'heavy_truck': 80000, 'medium_truck': 40000, 
                      'delivery_van': 15000, 'bus': 60000}.get(vehicle_type, 40000)
        roi_years = ev_premium / max(savings_per_year, 1)
        
        # Improvements needed
        improvements = []
        if range_score < 50:
            improvements.append("Consider extended-range battery option or route splitting")
        if charge_score < 50:
            improvements.append("Install depot charging infrastructure")
            if charging_stations < 2 and distance > 100:
                improvements.append("Add en-route fast charging stations")
        if payload_score < 50:
            improvements.append("Consider lighter payload distribution or multiple trips")
        if dwell_score < 50:
            improvements.append("Adjust schedules to allow more charging time at depots")
        if duty_score < 50:
            improvements.append("Consider route optimization to reduce daily distance")
        
        result = {
            'route_id': route_id,
            'route_name': route.get('route_name', f'Route {route_id}'),
            'readiness_score': round(overall_score, 1),
            'readiness_level': level,
            'readiness_color': color,
            'recommendation': recommendation,
            'limiting_factor': limiting_factor.replace('_', ' ').title(),
            'factor_scores': {k: round(v, 1) for k, v in factor_scores.items()},
            'vehicle_type': vehicle_type,
            'route_details': {
                'total_distance_km': distance,
                'daily_distance_km': daily_distance,
                'effective_ev_range_km': round(usable_range, 1),
                'terrain': terrain,
            },
            'financial': {
                'estimated_roi_years': round(roi_years, 1),
                'annual_fuel_savings_usd': round(savings_per_year, 0),
                'ev_premium_usd': ev_premium,
            },
            'improvements_needed': improvements,
            'assessed_at': datetime.now().isoformat()
        }
        
        self.assessments.append(result)
        return result
    
    def assess_fleet(self, routes: List[Dict]) -> Dict:
        """Assess all routes in a fleet for electrification readiness."""
        results = []
        for route in routes:
            result = self.score_route(route)
            results.append(result)
        
        # Sort by readiness score
        results.sort(key=lambda r: r['readiness_score'], reverse=True)
        
        scores = [r['readiness_score'] for r in results]
        
        summary = {
            'total_routes': len(routes),
            'assessment_date': datetime.now().isoformat(),
            'overall_readiness_score': round(np.mean(scores), 1),
            'readiness_distribution': {
                'excellent': sum(1 for s in scores if s >= 80),
                'good': sum(1 for s in scores if 60 <= s < 80),
                'moderate': sum(1 for s in scores if 40 <= s < 60),
                'challenging': sum(1 for s in scores if 20 <= s < 40),
                'not_ready': sum(1 for s in scores if s < 20),
            },
            'total_annual_savings_usd': sum(r['financial']['annual_fuel_savings_usd'] for r in results),
            'avg_roi_years': round(np.mean([r['financial']['estimated_roi_years'] for r in results]), 1),
            'recommended_for_immediate_ev': [
                r['route_id'] for r in results if r['readiness_score'] >= 70
            ],
            'route_assessments': results,
        }
        
        return summary
    
    def generate_sample_routes(self, num_routes: int = 30) -> List[Dict]:
        """Generate sample routes for testing."""
        routes = []
        vehicle_types = ['heavy_truck', 'medium_truck', 'delivery_van', 'bus']
        terrains = ['flat', 'hilly', 'mountainous']
        
        for i in range(num_routes):
            vtype = np.random.choice(vehicle_types, p=[0.2, 0.35, 0.35, 0.1])
            distance = np.random.uniform(30, 350)
            
            route = {
                'route_id': f'R-{i+1:03d}',
                'route_name': f'Route {chr(65 + i % 26)}{i // 26 + 1}',
                'total_distance_km': round(distance, 1),
                'vehicle_type': vtype,
                'avg_payload_tons': round(np.random.uniform(1, 15), 1),
                'max_payload_tons': round(np.random.uniform(5, 20), 1),
                'charging_stations_along_route': np.random.randint(0, 5),
                'has_depot_charging': np.random.choice([True, False], p=[0.6, 0.4]),
                'depot_dwell_hours': round(np.random.uniform(4, 12), 1),
                'stops_count': np.random.randint(1, 8),
                'avg_stop_duration_hours': round(np.random.uniform(0.25, 2.0), 2),
                'daily_trips': np.random.randint(1, 4),
                'terrain': np.random.choice(terrains, p=[0.5, 0.35, 0.15]),
                'temperature_extreme': np.random.choice([True, False], p=[0.2, 0.8]),
            }
            routes.append(route)
        
        return routes
    
    def save_assessment(self, output_dir: str, routes: Optional[List[Dict]] = None):
        """Run full assessment and save results."""
        os.makedirs(output_dir, exist_ok=True)
        
        if routes is None:
            routes = self.generate_sample_routes(30)
        
        print("\n" + "=" * 60)
        print("Fleet Electrification Readiness Assessment")
        print("=" * 60)
        
        summary = self.assess_fleet(routes)
        
        print(f"\n  Total Routes: {summary['total_routes']}")
        print(f"  Overall Readiness: {summary['overall_readiness_score']}/100")
        print(f"\n  Readiness Distribution:")
        for level, count in summary['readiness_distribution'].items():
            bar = '#' * count
            print(f"    {level:12s}: {count:3d} {bar}")
        
        print(f"\n  Recommended for immediate EV: {len(summary['recommended_for_immediate_ev'])} routes")
        print(f"  Annual fuel savings potential: ${summary['total_annual_savings_usd']:,.0f}")
        print(f"  Average ROI: {summary['avg_roi_years']:.1f} years")
        
        # Top ready routes
        print(f"\n  Top 5 Readiest Routes:")
        for r in summary['route_assessments'][:5]:
            print(f"    {r['route_id']} ({r['route_name']}): {r['readiness_score']:.0f}/100 [{r['readiness_level']}]")
        
        # Save
        with open(os.path.join(output_dir, 'fleet_readiness_assessment.json'), 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print(f"\n[SAVE] Results saved to {output_dir}")
        return summary


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'data', 'processed')
    
    scorer = FleetReadinessScorer()
    scorer.save_assessment(output_dir)
```

---

## ml\engines\risk_scorer.py

```python
"""
Supply Chain Risk Scoring Engine
================================
Scores supply chain risk for EV battery suppliers based on:
- Political stability of source countries
- Commodity price volatility
- Supplier concentration
- Logistics performance
- Historical disruption patterns

Also implements cascading failure detection through the supply chain graph.
"""

import numpy as np
import pandas as pd
import os
import json
from datetime import datetime
from typing import Dict, List, Optional


# ============================================================
# Simulated Reference Data (replace with real data from datasets)
# ============================================================

# Country risk data (based on World Governance Indicators patterns)
COUNTRY_RISK_DATA = {
    'DRC': {'name': 'DR Congo', 'political_stability': 0.15, 'logistics_score': 2.1,
            'minerals': ['cobalt', 'lithium'], 'region': 'Africa'},
    'AUS': {'name': 'Australia', 'political_stability': 0.90, 'logistics_score': 3.8,
            'minerals': ['lithium', 'nickel'], 'region': 'Oceania'},
    'CHL': {'name': 'Chile', 'political_stability': 0.72, 'logistics_score': 3.3,
            'minerals': ['lithium', 'copper'], 'region': 'South America'},
    'CHN': {'name': 'China', 'political_stability': 0.55, 'logistics_score': 3.6,
            'minerals': ['graphite', 'rare_earths', 'lithium'], 'region': 'Asia'},
    'IDN': {'name': 'Indonesia', 'political_stability': 0.45, 'logistics_score': 3.0,
            'minerals': ['nickel'], 'region': 'Asia'},
    'ARG': {'name': 'Argentina', 'political_stability': 0.50, 'logistics_score': 2.8,
            'minerals': ['lithium'], 'region': 'South America'},
    'PHL': {'name': 'Philippines', 'political_stability': 0.40, 'logistics_score': 2.7,
            'minerals': ['nickel'], 'region': 'Asia'},
    'RUS': {'name': 'Russia', 'political_stability': 0.25, 'logistics_score': 2.5,
            'minerals': ['nickel', 'cobalt'], 'region': 'Europe'},
    'CAN': {'name': 'Canada', 'political_stability': 0.92, 'logistics_score': 3.7,
            'minerals': ['nickel', 'cobalt', 'lithium'], 'region': 'North America'},
    'BRA': {'name': 'Brazil', 'political_stability': 0.48, 'logistics_score': 2.9,
            'minerals': ['graphite', 'nickel'], 'region': 'South America'},
    'IND': {'name': 'India', 'political_stability': 0.45, 'logistics_score': 3.2,
            'minerals': ['graphite'], 'region': 'Asia'},
    'USA': {'name': 'United States', 'political_stability': 0.85, 'logistics_score': 3.9,
            'minerals': ['lithium'], 'region': 'North America'},
}

# Commodity price volatility (based on World Bank data patterns)
COMMODITY_VOLATILITY = {
    'lithium': {'price_usd_ton': 25000, 'volatility_30d': 0.35, 'volatility_90d': 0.52,
                'trend': 'declining', 'supply_risk': 0.6},
    'cobalt': {'price_usd_ton': 35000, 'volatility_30d': 0.28, 'volatility_90d': 0.45,
               'trend': 'stable', 'supply_risk': 0.8},
    'nickel': {'price_usd_ton': 18000, 'volatility_30d': 0.22, 'volatility_90d': 0.38,
               'trend': 'rising', 'supply_risk': 0.5},
    'graphite': {'price_usd_ton': 1200, 'volatility_30d': 0.15, 'volatility_90d': 0.25,
                 'trend': 'stable', 'supply_risk': 0.4},
    'copper': {'price_usd_ton': 8500, 'volatility_30d': 0.18, 'volatility_90d': 0.30,
               'trend': 'rising', 'supply_risk': 0.3},
    'manganese': {'price_usd_ton': 4500, 'volatility_30d': 0.12, 'volatility_90d': 0.22,
                  'trend': 'stable', 'supply_risk': 0.35},
    'rare_earths': {'price_usd_ton': 45000, 'volatility_30d': 0.40, 'volatility_90d': 0.55,
                    'trend': 'rising', 'supply_risk': 0.85},
}

# Sample supply chain graph
SAMPLE_SUPPLY_CHAIN = [
    # Mines → Refineries → Battery Plants → Battery Packs → Fleet Vehicles
    {
        'supplier_id': 'S001', 'name': 'CobaltCo DRC', 'type': 'mine',
        'country': 'DRC', 'mineral': 'cobalt', 'capacity_tons_year': 5000,
        'downstream': ['R001'], 'failure_rate': 0.15
    },
    {
        'supplier_id': 'S002', 'name': 'LithiumEx Chile', 'type': 'mine',
        'country': 'CHL', 'mineral': 'lithium', 'capacity_tons_year': 8000,
        'downstream': ['R001', 'R002'], 'failure_rate': 0.05
    },
    {
        'supplier_id': 'S003', 'name': 'NickelPro Indonesia', 'type': 'mine',
        'country': 'IDN', 'mineral': 'nickel', 'capacity_tons_year': 12000,
        'downstream': ['R002'], 'failure_rate': 0.10
    },
    {
        'supplier_id': 'S004', 'name': 'GraphiteCorp China', 'type': 'mine',
        'country': 'CHN', 'mineral': 'graphite', 'capacity_tons_year': 15000,
        'downstream': ['R001', 'R002'], 'failure_rate': 0.08
    },
    {
        'supplier_id': 'S005', 'name': 'LithiumOz Australia', 'type': 'mine',
        'country': 'AUS', 'mineral': 'lithium', 'capacity_tons_year': 10000,
        'downstream': ['R002'], 'failure_rate': 0.03
    },
    {
        'supplier_id': 'R001', 'name': 'CathodeRefine Shanghai', 'type': 'refinery',
        'country': 'CHN', 'mineral': 'cathode_materials', 'capacity_tons_year': 20000,
        'downstream': ['P001'], 'failure_rate': 0.06
    },
    {
        'supplier_id': 'R002', 'name': 'BattMat Korea', 'type': 'refinery',
        'country': 'KOR', 'mineral': 'cathode_materials', 'capacity_tons_year': 18000,
        'downstream': ['P001', 'P002'], 'failure_rate': 0.04
    },
    {
        'supplier_id': 'P001', 'name': 'GigaCell Shenzhen', 'type': 'battery_plant',
        'country': 'CHN', 'mineral': 'battery_cells', 'capacity_tons_year': 50000,
        'downstream': ['F001', 'F002'], 'failure_rate': 0.05
    },
    {
        'supplier_id': 'P002', 'name': 'BatteryWorks USA', 'type': 'battery_plant',
        'country': 'USA', 'mineral': 'battery_cells', 'capacity_tons_year': 30000,
        'downstream': ['F002', 'F003'], 'failure_rate': 0.03
    },
    {
        'supplier_id': 'F001', 'name': 'Fleet Alpha', 'type': 'fleet',
        'country': 'IND', 'mineral': None, 'capacity_tons_year': None,
        'downstream': [], 'failure_rate': 0
    },
    {
        'supplier_id': 'F002', 'name': 'Fleet Beta', 'type': 'fleet',
        'country': 'IND', 'mineral': None, 'capacity_tons_year': None,
        'downstream': [], 'failure_rate': 0
    },
    {
        'supplier_id': 'F003', 'name': 'Fleet Gamma', 'type': 'fleet',
        'country': 'USA', 'mineral': None, 'capacity_tons_year': None,
        'downstream': [], 'failure_rate': 0
    },
]


class SupplyChainRiskScorer:
    """
    Scores supply chain risk using multiple weighted factors.
    
    Risk Score = weighted combination of:
    - Political stability of source country
    - Supplier concentration (single source = high risk)
    - Commodity price volatility
    - Logistics performance
    - Shipping disruption probability
    - Historical failure rate
    """
    
    # Risk factor weights
    WEIGHTS = {
        'political_risk': 0.25,
        'concentration_risk': 0.20,
        'price_volatility_risk': 0.20,
        'logistics_risk': 0.15,
        'shipping_risk': 0.10,
        'historical_risk': 0.10,
    }
    
    def __init__(self):
        self.supply_chain = SAMPLE_SUPPLY_CHAIN
        self.country_data = COUNTRY_RISK_DATA
        self.commodity_data = COMMODITY_VOLATILITY
        self.risk_cache = {}
    
    def score_supplier(self, supplier: Dict) -> Dict:
        """
        Calculate comprehensive risk score for a single supplier.
        
        Returns dict with overall score, breakdown, and recommendations.
        """
        country_code = supplier.get('country', 'UNK')
        mineral = supplier.get('mineral')
        country_info = self.country_data.get(country_code, {})
        
        # 1. Political Risk (0-1, higher = more risky)
        political_stability = country_info.get('political_stability', 0.5)
        political_risk = 1 - political_stability
        
        # 2. Concentration Risk
        # How many alternative suppliers exist for this mineral?
        if mineral and mineral not in ['cathode_materials', 'battery_cells']:
            alternatives = sum(1 for s in self.supply_chain 
                             if s.get('mineral') == mineral and s['supplier_id'] != supplier['supplier_id'])
            concentration_risk = max(0, 1 - (alternatives / 3))  # 3+ alternatives = low risk
        else:
            concentration_risk = 0.3  # Default for non-mineral suppliers
        
        # 3. Price Volatility Risk
        commodity_info = self.commodity_data.get(mineral, {})
        price_volatility_risk = commodity_info.get('volatility_90d', 0.3)
        
        # 4. Logistics Risk
        logistics_score = country_info.get('logistics_score', 3.0)
        logistics_risk = max(0, 1 - (logistics_score / 5))  # 5 = perfect logistics
        
        # 5. Shipping Disruption Risk
        # Higher for distant/conflict regions
        shipping_risk_map = {
            'Africa': 0.6, 'Asia': 0.4, 'South America': 0.5,
            'Europe': 0.3, 'North America': 0.2, 'Oceania': 0.3
        }
        shipping_risk = shipping_risk_map.get(country_info.get('region', ''), 0.4)
        
        # 6. Historical Failure Rate
        historical_risk = supplier.get('failure_rate', 0.05) * 5  # Scale to 0-1
        historical_risk = min(1, historical_risk)
        
        # Weighted overall score (0-100)
        overall_score = (
            political_risk * self.WEIGHTS['political_risk'] +
            concentration_risk * self.WEIGHTS['concentration_risk'] +
            price_volatility_risk * self.WEIGHTS['price_volatility_risk'] +
            logistics_risk * self.WEIGHTS['logistics_risk'] +
            shipping_risk * self.WEIGHTS['shipping_risk'] +
            historical_risk * self.WEIGHTS['historical_risk']
        ) * 100
        
        # Risk level
        if overall_score <= 25:
            level = 'low'
            color = 'green'
            action = 'Monitor quarterly'
        elif overall_score <= 50:
            level = 'medium'
            color = 'yellow'
            action = 'Monitor monthly, identify alternatives'
        elif overall_score <= 75:
            level = 'high'
            color = 'orange'
            action = 'Actively source alternatives, build inventory buffer'
        else:
            level = 'critical'
            color = 'red'
            action = 'Immediate diversification required'
        
        # Recommendations
        recommendations = []
        if political_risk > 0.6:
            recommendations.append(f"HIGH political risk in {country_info.get('name', country_code)}. Diversify sourcing.")
        if concentration_risk > 0.7:
            recommendations.append(f"Single-source dependency for {mineral}. Add alternative suppliers.")
        if price_volatility_risk > 0.4:
            recommendations.append(f"High price volatility for {mineral}. Consider long-term contracts.")
        if logistics_risk > 0.5:
            recommendations.append(f"Weak logistics infrastructure in {country_info.get('name', country_code)}.")
        
        result = {
            'supplier_id': supplier['supplier_id'],
            'supplier_name': supplier['name'],
            'type': supplier['type'],
            'country': country_code,
            'country_name': country_info.get('name', country_code),
            'mineral': mineral,
            'risk_score': round(overall_score, 2),
            'risk_level': level,
            'risk_color': color,
            'action': action,
            'breakdown': {
                'political_risk': round(political_risk * 100, 1),
                'concentration_risk': round(concentration_risk * 100, 1),
                'price_volatility_risk': round(price_volatility_risk * 100, 1),
                'logistics_risk': round(logistics_risk * 100, 1),
                'shipping_risk': round(shipping_risk * 100, 1),
                'historical_risk': round(historical_risk * 100, 1),
            },
            'recommendations': recommendations
        }
        
        self.risk_cache[supplier['supplier_id']] = result
        return result
    
    def score_all_suppliers(self) -> List[Dict]:
        """Score all suppliers in the supply chain."""
        print("\n" + "=" * 60)
        print("Supply Chain Risk Assessment")
        print("=" * 60)
        
        results = []
        for supplier in self.supply_chain:
            result = self.score_supplier(supplier)
            results.append(result)
            
            print(f"\n  {result['supplier_name']} ({result['supplier_id']})")
            print(f"  Type: {result['type']} | Country: {result['country_name']}")
            print(f"  Risk Score: {result['risk_score']:.1f}/100 [{result['risk_level'].upper()}]")
            if result['recommendations']:
                for rec in result['recommendations']:
                    print(f"    -> {rec}")
        
        # Summary
        scores = [r['risk_score'] for r in results]
        print(f"\n{'='*60}")
        print(f"Supply Chain Risk Summary")
        print(f"{'='*60}")
        print(f"  Total suppliers: {len(results)}")
        print(f"  Average risk: {np.mean(scores):.1f}/100")
        print(f"  Highest risk: {max(scores):.1f}/100")
        print(f"  Critical: {sum(1 for r in results if r['risk_level'] == 'critical')}")
        print(f"  High: {sum(1 for r in results if r['risk_level'] == 'high')}")
        print(f"  Medium: {sum(1 for r in results if r['risk_level'] == 'medium')}")
        print(f"  Low: {sum(1 for r in results if r['risk_level'] == 'low')}")
        
        return results
    
    def detect_cascading_failures(self, failed_supplier_id: str) -> Dict:
        """
        Detect cascading failure impact when a supplier fails.
        
        Traces the supply chain graph downstream to find all affected entities.
        
        Example: If a cobalt mine in DRC fails ->
          -> Refinery loses input ->
            -> Battery plant can't produce ->
              -> Fleet vehicles affected
        """
        print(f"\n{'='*60}")
        print(f"Cascading Failure Analysis: {failed_supplier_id}")
        print(f"{'='*60}")
        
        # Find the failed supplier
        failed = None
        supplier_map = {s['supplier_id']: s for s in self.supply_chain}
        failed = supplier_map.get(failed_supplier_id)
        
        if not failed:
            return {'error': f'Supplier {failed_supplier_id} not found'}
        
        print(f"\n  FAILURE ORIGIN: {failed['name']} ({failed['type']})")
        print(f"  Country: {failed.get('country', 'N/A')}")
        print(f"  Material: {failed.get('mineral', 'N/A')}")
        
        # BFS to find all downstream affected entities
        affected = []
        queue = [failed_supplier_id]
        visited = set()
        level = 0
        levels = {}
        
        while queue:
            next_queue = []
            for sid in queue:
                if sid in visited:
                    continue
                visited.add(sid)
                supplier = supplier_map.get(sid)
                if supplier:
                    levels[sid] = level
                    if sid != failed_supplier_id:
                        affected.append({
                            'supplier_id': sid,
                            'name': supplier['name'],
                            'type': supplier['type'],
                            'impact_level': level,
                            'risk_amplification': round(1.5 ** level, 2)
                        })
                    for downstream_id in supplier.get('downstream', []):
                        if downstream_id not in visited:
                            next_queue.append(downstream_id)
            queue = next_queue
            level += 1
        
        # Impact assessment
        affected_fleets = [a for a in affected if supplier_map.get(a['supplier_id'], {}).get('type') == 'fleet']
        affected_plants = [a for a in affected if supplier_map.get(a['supplier_id'], {}).get('type') == 'battery_plant']
        
        result = {
            'failed_supplier': {
                'id': failed_supplier_id,
                'name': failed['name'],
                'type': failed['type'],
                'mineral': failed.get('mineral'),
                'country': failed.get('country')
            },
            'total_affected': len(affected),
            'affected_entities': affected,
            'impact_summary': {
                'refineries_affected': sum(1 for a in affected if supplier_map.get(a['supplier_id'], {}).get('type') == 'refinery'),
                'plants_affected': len(affected_plants),
                'fleets_affected': len(affected_fleets),
                'max_cascade_depth': max(levels.values()) if levels else 0
            },
            'severity': 'critical' if len(affected_fleets) > 1 else 'high' if len(affected_fleets) == 1 else 'medium',
            'mitigation': []
        }
        
        # Mitigation recommendations
        if failed['type'] == 'mine':
            alt_suppliers = [s for s in self.supply_chain 
                           if s.get('mineral') == failed.get('mineral') 
                           and s['supplier_id'] != failed_supplier_id]
            if alt_suppliers:
                result['mitigation'].append(
                    f"Redirect to alternative supplier(s): {', '.join(s['name'] for s in alt_suppliers)}")
            else:
                result['mitigation'].append("CRITICAL: No alternative suppliers for this mineral!")
        
        result['mitigation'].append(f"Activate strategic reserve for {failed.get('mineral', 'materials')}")
        result['mitigation'].append("Notify downstream partners of potential delays")
        
        # Print cascading failure chain
        print(f"\n  IMPACT CHAIN:")
        for a in sorted(affected, key=lambda x: x['impact_level']):
            indent = "  " * (a['impact_level'] + 1)
            print(f"  {indent}-> {a['name']} (Level {a['impact_level']}, amplification: {a['risk_amplification']}x)")
        
        print(f"\n  TOTAL IMPACT: {result['total_affected']} entities affected")
        print(f"  FLEETS AT RISK: {len(affected_fleets)}")
        print(f"  SEVERITY: {result['severity'].upper()}")
        
        return result
    
    def get_supply_chain_graph(self) -> Dict:
        """Return the supply chain as a graph structure for visualization."""
        nodes = []
        edges = []
        
        for supplier in self.supply_chain:
            risk = self.risk_cache.get(supplier['supplier_id'], {})
            nodes.append({
                'id': supplier['supplier_id'],
                'label': supplier['name'],
                'type': supplier['type'],
                'country': supplier.get('country'),
                'risk_score': risk.get('risk_score', 0),
                'risk_level': risk.get('risk_level', 'unknown')
            })
            
            for downstream_id in supplier.get('downstream', []):
                edges.append({
                    'source': supplier['supplier_id'],
                    'target': downstream_id,
                    'material': supplier.get('mineral', 'components')
                })
        
        return {'nodes': nodes, 'edges': edges}
    
    def save_results(self, output_dir: str):
        """Save risk assessment results."""
        os.makedirs(output_dir, exist_ok=True)
        
        results = self.score_all_suppliers()
        
        # Save as JSON
        with open(os.path.join(output_dir, 'supply_chain_risk_scores.json'), 'w') as f:
            json.dump(results, f, indent=2)
        
        # Save as CSV
        df = pd.DataFrame(results)
        df.to_csv(os.path.join(output_dir, 'supply_chain_risk_scores.csv'), index=False)
        
        # Save graph
        graph = self.get_supply_chain_graph()
        with open(os.path.join(output_dir, 'supply_chain_graph.json'), 'w') as f:
            json.dump(graph, f, indent=2)
        
        # Run cascading failure analysis for highest-risk supplier
        highest_risk = max(results, key=lambda x: x['risk_score'])
        cascade = self.detect_cascading_failures(highest_risk['supplier_id'])
        with open(os.path.join(output_dir, 'cascading_failure_analysis.json'), 'w') as f:
            json.dump(cascade, f, indent=2)
        
        print(f"\n[SAVE] Results saved to {output_dir}")


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'data', 'processed')
    
    scorer = SupplyChainRiskScorer()
    scorer.save_results(output_dir)
```

---

## ml\engines\__init__.py

```python
# AI/ML Engines for EV Intelligence Platform
```

---

## ml\models\anomaly_detector.joblib

**[Skipped - File Too Large (2314.4 KB)]**

---

## ml\models\anomaly_metadata.json

```json
{
  "feature_columns": [
    "capacity_ah",
    "avg_voltage_v",
    "voltage_charged_v",
    "voltage_discharged_v",
    "avg_temperature_c",
    "max_temperature_c",
    "internal_resistance_ohm",
    "charge_transfer_resistance_ohm",
    "discharge_time_s",
    "charge_efficiency_percent",
    "discharge_slope_v_per_s",
    "capacity_degradation_rate",
    "thermal_variance",
    "voltage_spread",
    "resistance_growth_rate",
    "temp_rolling_std"
  ],
  "thresholds": {
    "score_mean": 0.07490448308004012,
    "score_std": 0.040329323618395196,
    "score_min": -0.14127468862902748,
    "score_max": 0.12420221863504877,
    "anomaly_threshold": 5.551115123125783e-17,
    "warning_threshold": 0.013478784003670197
  },
  "physical_limits": {
    "temperature_max": 55.0,
    "temperature_warning": 45.0,
    "voltage_min": 300.0,
    "voltage_max": 420.0,
    "current_max": 250.0,
    "soc_drop_max": 15.0,
    "soc_min": 3.0
  },
  "saved_at": "2026-07-15T13:26:00.434910"
}
```

---

## ml\models\anomaly_scaler.joblib

**[Binary File]**

---

## ml\models\battery_predictor_metadata.json

```json
{
  "soh_features": [
    "cycle",
    "capacity_ah",
    "avg_voltage_v",
    "voltage_charged_v",
    "voltage_discharged_v",
    "charge_current_a",
    "discharge_current_a",
    "avg_temperature_c",
    "max_temperature_c",
    "internal_resistance_ohm",
    "charge_transfer_resistance_ohm",
    "discharge_time_s",
    "charge_efficiency_percent",
    "discharge_slope_v_per_s",
    "capacity_degradation_rate",
    "cumulative_capacity_loss",
    "resistance_growth_rate",
    "temp_rolling_mean",
    "temp_rolling_std",
    "thermal_variance",
    "voltage_spread",
    "capacity_rolling_std",
    "efficiency_drop",
    "discharge_rate",
    "impedance_ratio",
    "cycle_age_normalized"
  ],
  "rul_features": [
    "cycle",
    "capacity_ah",
    "avg_voltage_v",
    "voltage_charged_v",
    "voltage_discharged_v",
    "charge_current_a",
    "discharge_current_a",
    "avg_temperature_c",
    "max_temperature_c",
    "internal_resistance_ohm",
    "charge_transfer_resistance_ohm",
    "discharge_time_s",
    "charge_efficiency_percent",
    "discharge_slope_v_per_s",
    "capacity_degradation_rate",
    "cumulative_capacity_loss",
    "resistance_growth_rate",
    "temp_rolling_mean",
    "temp_rolling_std",
    "thermal_variance",
    "voltage_spread",
    "capacity_rolling_std",
    "efficiency_drop",
    "discharge_rate",
    "impedance_ratio",
    "cycle_age_normalized"
  ],
  "training_metrics": {
    "soh": {
      "rmse": 0.18657092046829346,
      "mae": 0.13451298594474875,
      "r2": 0.9995985269480547,
      "features": [
        "cycle",
        "capacity_ah",
        "avg_voltage_v",
        "voltage_charged_v",
        "voltage_discharged_v",
        "charge_current_a",
        "discharge_current_a",
        "avg_temperature_c",
        "max_temperature_c",
        "internal_resistance_ohm",
        "charge_transfer_resistance_ohm",
        "discharge_time_s",
        "charge_efficiency_percent",
        "discharge_slope_v_per_s",
        "capacity_degradation_rate",
        "cumulative_capacity_loss",
        "resistance_growth_rate",
        "temp_rolling_mean",
        "temp_rolling_std",
        "thermal_variance",
        "voltage_spread",
        "capacity_rolling_std",
        "efficiency_drop",
        "discharge_rate",
        "impedance_ratio",
        "cycle_age_normalized"
      ],
      "train_size": 508,
      "test_size": 128
    },
    "rul": {
      "rmse": 2.026349185725761,
      "mae": 1.1672186851501465,
      "r2": 0.997903048992157,
      "features": [
        "cycle",
        "capacity_ah",
        "avg_voltage_v",
        "voltage_charged_v",
        "voltage_discharged_v",
        "charge_current_a",
        "discharge_current_a",
        "avg_temperature_c",
        "max_temperature_c",
        "internal_resistance_ohm",
        "charge_transfer_resistance_ohm",
        "discharge_time_s",
        "charge_efficiency_percent",
        "discharge_slope_v_per_s",
        "capacity_degradation_rate",
        "cumulative_capacity_loss",
        "resistance_growth_rate",
        "temp_rolling_mean",
        "temp_rolling_std",
        "thermal_variance",
        "voltage_spread",
        "capacity_rolling_std",
        "efficiency_drop",
        "discharge_rate",
        "impedance_ratio",
        "cycle_age_normalized"
      ],
      "train_size": 508,
      "test_size": 128
    }
  },
  "soh_trained": true,
  "rul_trained": true,
  "saved_at": "2026-07-15T13:26:01.494759"
}
```

---

## ml\models\rul_model.joblib

**[Binary File]**

---

## ml\models\rul_scaler.joblib

**[Binary File]**

---

## ml\models\soh_model.joblib

**[Binary File]**

---

## ml\models\soh_scaler.joblib

**[Binary File]**

---

## ml\preprocessing\ingest_raw_datasets.py

```python
"""
Raw NASA Dataset Ingestion Script
=================================
Converts downloaded raw NASA datasets (MATLAB .mat files for Battery PCoE,
and space-separated text files for C-MAPSS) into the CSV formats expected by the pipeline.

Ensure you have downloaded:
1. NASA Battery Dataset: https://ti.arc.nasa.gov/c/5/ (e.g. B0005.mat, B0006.mat, etc.)
2. NASA C-MAPSS Dataset: https://ti.arc.nasa.gov/c/6/ (e.g. train_FD001.txt)

Usage:
  python preprocessing/ingest_raw_datasets.py --battery_dir /path/to/mat_files --cmapss_file /path/to/train_FD001.txt
"""

import os
import argparse
import pandas as pd
import numpy as np
import scipy.io
from datetime import datetime

def parse_battery_mat(mat_path):
    """
    Parses a single NASA battery .mat file (e.g., B0005.mat) and extracts cycle-by-cycle summary features.
    """
    mat_dict = scipy.io.loadmat(mat_path)
    # The filename (without extension) is the key to the nested struct
    battery_id = os.path.basename(mat_path).split('.')[0]
    
    # Extract structural contents
    # Structure path: mat_dict[battery_id][0, 0]['cycle'][0]
    cycle_structs = mat_dict[battery_id][0, 0]['cycle'][0]
    
    cycles_data = []
    
    # Track the last seen values to link charge, discharge, and impedance cycles
    current_capacity = None
    current_impedance_re = None
    current_impedance_rct = None
    
    discharge_cycle_counter = 1
    
    # Temporary lists to align charge/discharge characteristics per cycle
    temp_charge_data = {}
    
    for i, cyc in enumerate(cycle_structs):
        cycle_type = cyc['type'][0]
        
        # Datetime conversion (handles formatting variations in .mat files)
        try:
            dt_tuple = cyc['time'][0]
            dt = datetime(
                year=int(dt_tuple[0]),
                month=int(dt_tuple[1]),
                day=int(dt_tuple[2]),
                hour=int(dt_tuple[3]),
                minute=int(dt_tuple[4]),
                second=int(round(dt_tuple[5]))
            )
        except Exception:
            dt = None
            
        data = cyc['data'][0, 0]
        
        if cycle_type == 'charge':
            try:
                # Voltage measured during charge
                v_meas = data['Voltage_measured'][0]
                # Current measured during charge
                c_meas = data['Current_measured'][0]
                # Temp measured during charge
                t_meas = data['Temperature_measured'][0]
                # Charge time
                time_arr = data['Time'][0]
                
                # Compute charge statistics
                temp_charge_data = {
                    'voltage_charged_v': float(np.max(v_meas)),
                    'charge_current_a': float(np.mean(c_meas)),
                    'charge_time_s': float(time_arr[-1] if len(time_arr) > 0 else 0)
                }
            except (KeyError, IndexError, ValueError):
                pass
                
        elif cycle_type == 'impedance':
            try:
                # Extract impedance measurements if present
                r_est = data['Estimated_electrolyte_resistance'][0, 0]
                r_ct = data['Estimated_charge_transfer_resistance'][0, 0]
                current_impedance_re = float(r_est)
                current_impedance_rct = float(r_ct)
            except (KeyError, IndexError, ValueError):
                pass
                
        elif cycle_type == 'discharge':
            try:
                # Capacity is the key performance target in Ampere-hours
                capacity = float(data['Capacity'][0, 0])
                current_capacity = capacity
                
                v_meas = data['Voltage_measured'][0]
                c_meas = data['Current_measured'][0]
                t_meas = data['Temperature_measured'][0]
                time_arr = data['Time'][0]
                
                # Calculate metrics for discharge
                voltage_charged = float(np.max(v_meas))
                voltage_discharged = float(np.min(v_meas))
                avg_voltage = float(np.mean(v_meas))
                avg_temp = float(np.mean(t_meas))
                max_temp = float(np.max(t_meas))
                discharge_current = float(np.mean(c_meas))
                discharge_time = float(time_arr[-1] if len(time_arr) > 0 else 0)
                
                # Compute voltage slope
                if len(time_arr) > 1 and len(v_meas) > 1:
                    slope = (v_meas[-1] - v_meas[0]) / (time_arr[-1] - time_arr[0])
                else:
                    slope = 0.0
                    
                # Recover charge features if they were stored in the previous step
                charge_current = temp_charge_data.get('charge_current_a', 1.5)
                voltage_chg = temp_charge_data.get('voltage_charged_v', 4.2)
                charge_time = temp_charge_data.get('charge_time_s', 3600)
                
                # Calculate charge efficiency
                # Ah discharged / Ah charged
                charge_efficiency = 100.0
                if charge_time > 0 and discharge_time > 0:
                    ah_charged = abs(charge_current) * (charge_time / 3600)
                    ah_discharged = abs(discharge_current) * (discharge_time / 3600)
                    if ah_charged > 0:
                        charge_efficiency = min(100.0, (ah_discharged / ah_charged) * 100)
                
                # SOH calculation: capacity relative to nominal capacity (2.0 Ah)
                soh = (capacity / 2.0) * 100
                
                # Set default resistances if impedance cycle was missing
                re_ohm = current_impedance_re if current_impedance_re is not None else 0.05
                rct_ohm = current_impedance_rct if current_impedance_rct is not None else 0.08
                
                cycles_data.append({
                    'battery_id': battery_id,
                    'cycle': discharge_cycle_counter,
                    'datetime': dt.isoformat() if dt else '',
                    'type': 'summary',
                    'capacity_ah': round(capacity, 4),
                    'soh_percent': round(soh, 2),
                    'voltage_charged_v': round(voltage_chg, 4),
                    'voltage_discharged_v': round(voltage_discharged, 4),
                    'avg_voltage_v': round(avg_voltage, 4),
                    'charge_current_a': round(charge_current, 4),
                    'discharge_current_a': round(discharge_current, 4),
                    'avg_temperature_c': round(avg_temp, 2),
                    'max_temperature_c': round(max_temp, 2),
                    'internal_resistance_ohm': round(re_ohm, 5),
                    'charge_transfer_resistance_ohm': round(rct_ohm, 5),
                    'discharge_time_s': round(discharge_time, 1),
                    'charge_efficiency_percent': round(charge_efficiency, 2),
                    'discharge_slope_v_per_s': round(slope, 6)
                })
                
                discharge_cycle_counter += 1
            except (KeyError, IndexError, ValueError) as e:
                print(f"  [WARN] Skipping a discharge cycle due to read error: {e}")
                
    # Compute Remaining Useful Life (RUL) in cycles back-propagated
    total_cycles = len(cycles_data)
    for idx, item in enumerate(cycles_data):
        item['rul_cycles'] = total_cycles - item['cycle']
        
    return pd.DataFrame(cycles_data)


def ingest_battery_datasets(battery_dir, output_file):
    """
    Ingests all battery .mat files in a directory and consolidates them into a single CSV.
    """
    print(f"\nScanning directory '{battery_dir}' for battery .mat files...")
    
    mat_files = [f for f in os.listdir(battery_dir) if f.lower().endswith('.mat')]
    if not mat_files:
        print("  [ERROR] No .mat files found in the directory!")
        return False
        
    print(f"Found {len(mat_files)} files: {mat_files}")
    all_dfs = []
    
    for f in mat_files:
        path = os.path.join(battery_dir, f)
        print(f"Processing '{f}'...")
        try:
            df = parse_battery_mat(path)
            if not df.empty:
                all_dfs.append(df)
                print(f"  [OK] Extracted {len(df)} cycles for battery {df['battery_id'].iloc[0]}")
            else:
                print(f"  [WARN] Battery file '{f}' returned no cycles.")
        except Exception as e:
            print(f"  [ERROR] Failed to parse '{f}': {e}")
            
    if not all_dfs:
        print("  [ERROR] No battery data could be extracted.")
        return False
        
    combined_df = pd.concat(all_dfs, ignore_index=True)
    
    # Save output CSV
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    combined_df.to_csv(output_file, index=False)
    print(f"\n[SUCCESS] Consolidate battery CSV saved to: {output_file}")
    print(f"Total records: {len(combined_df)}")
    return True


def ingest_cmapss_dataset(txt_file, output_file):
    """
    Ingests the raw space-separated train_FD001.txt C-MAPSS file and converts it to a standard CSV.
    """
    print(f"\nIngesting C-MAPSS dataset from '{txt_file}'...")
    
    if not os.path.exists(txt_file):
        print(f"  [ERROR] File '{txt_file}' does not exist!")
        return False
        
    # Columns definition matching the NASA standard
    columns = ['unit_id', 'cycle', 'op_setting_1', 'op_setting_2', 'op_setting_3']
    for s_idx in range(1, 22):
        columns.append(f's{s_idx}')
        
    try:
        # Read whitespace-delimited file
        df = pd.read_csv(txt_file, sep=r'\s+', header=None)
        
        # The file might have extra trailing empty columns due to trailing spaces, slice first 26 columns
        df = df.iloc[:, :26]
        df.columns = columns
        
        # Add RUL column based on maximum cycles for each unit
        # Real engines in CMAPSS run to failure, so RUL = max_cycles_of_unit - current_cycle
        rul_dict = {}
        for unit_id, group in df.groupby('unit_id'):
            rul_dict[unit_id] = group['cycle'].max()
            
        df['rul'] = df.apply(lambda row: int(rul_dict[row['unit_id']] - row['cycle']), axis=1)
        
        # Save output CSV
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df.to_csv(output_file, index=False)
        print(f"[SUCCESS] Converted C-MAPSS CSV saved to: {output_file}")
        print(f"Total records: {len(df)} engines: {df['unit_id'].nunique()}")
        return True
    except Exception as e:
        print(f"  [ERROR] Failed to ingest C-MAPSS data: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Ingest NASA raw datasets into EV Platform standard formats.")
    parser.add_argument('--battery_dir', type=str, help="Directory containing B0005.mat, B0006.mat, etc.")
    parser.add_argument('--cmapss_file', type=str, help="Path to raw train_FD001.txt file")
    args = parser.parse_args()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    if args.battery_dir:
        output_battery_csv = os.path.join(base_dir, 'data', 'raw', 'battery', 'nasa_battery_data.csv')
        ingest_battery_datasets(args.battery_dir, output_battery_csv)
        
    if args.cmapss_file:
        output_cmapss_csv = os.path.join(base_dir, 'data', 'raw', 'cmapss', 'cmapss_fd001.csv')
        ingest_cmapss_dataset(args.cmapss_file, output_cmapss_csv)
        
    if not args.battery_dir and not args.cmapss_file:
        print("\n[INFO] No arguments provided. To ingest files, specify options.")
        print("Example:")
        print("  python preprocessing/ingest_raw_datasets.py --battery_dir /path/to/extracted/matfiles --cmapss_file /path/to/train_FD001.txt")


if __name__ == '__main__':
    main()
```

---

## ml\preprocessing\pipeline.py

```python
"""
Preprocessing Pipeline
=====================
Cleans raw NASA battery and C-MAPSS data, engineers features, 
and produces ML-ready datasets.
"""

import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import joblib
import json


class BatteryPreprocessor:
    """Preprocesses NASA Battery PCoE data for ML models."""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.feature_columns = []
    
    def load_data(self, filepath: str) -> pd.DataFrame:
        """Load raw battery CSV data."""
        df = pd.read_csv(filepath)
        print(f"[LOAD] Battery data: {len(df)} records, {df['battery_id'].nunique()} batteries")
        return df
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values, outliers, and data quality issues."""
        original_len = len(df)
        
        # Drop rows with NaN in critical columns
        critical_cols = ['capacity_ah', 'soh_percent', 'avg_voltage_v', 
                        'avg_temperature_c', 'internal_resistance_ohm']
        df = df.dropna(subset=critical_cols)
        
        # Remove physically impossible values
        df = df[df['capacity_ah'] > 0]
        df = df[df['soh_percent'] > 0]
        df = df[df['soh_percent'] <= 110]  # Allow slight over 100 for measurement noise
        df = df[df['avg_temperature_c'] > -20]  # Realistic temp range
        df = df[df['avg_temperature_c'] < 80]
        df = df[df['internal_resistance_ohm'] > 0]
        df = df[df['avg_voltage_v'] > 2.0]
        df = df[df['avg_voltage_v'] < 5.0]
        
        dropped = original_len - len(df)
        if dropped > 0:
            print(f"[CLEAN] Dropped {dropped} invalid rows ({dropped/original_len*100:.1f}%)")
        else:
            print("[CLEAN] No invalid rows found")
        
        return df.reset_index(drop=True)
    
    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create derived features for ML models."""
        print("[FEATURES] Engineering battery features...")
        
        # Per-battery rolling features
        engineered = []
        for battery_id, group in df.groupby('battery_id'):
            group = group.sort_values('cycle').copy()
            
            # 1. Capacity degradation rate (capacity loss per cycle)
            group['capacity_degradation_rate'] = group['capacity_ah'].diff() / group['cycle'].diff()
            
            # 2. Cumulative capacity loss
            initial_capacity = group['capacity_ah'].iloc[0]
            group['cumulative_capacity_loss'] = initial_capacity - group['capacity_ah']
            
            # 3. Resistance growth rate
            group['resistance_growth_rate'] = group['internal_resistance_ohm'].diff() / group['cycle'].diff()
            
            # 4. Rolling temperature statistics (window=10 cycles)
            group['temp_rolling_mean'] = group['avg_temperature_c'].rolling(10, min_periods=1).mean()
            group['temp_rolling_std'] = group['avg_temperature_c'].rolling(10, min_periods=1).std().fillna(0)
            group['thermal_variance'] = group['avg_temperature_c'].rolling(20, min_periods=1).var().fillna(0)
            
            # 5. Voltage spread (charged - discharged)
            group['voltage_spread'] = group['voltage_charged_v'] - group['voltage_discharged_v']
            
            # 6. Rolling capacity statistics
            group['capacity_rolling_std'] = group['capacity_ah'].rolling(10, min_periods=1).std().fillna(0)
            
            # 7. Efficiency trend
            group['efficiency_drop'] = group['charge_efficiency_percent'].iloc[0] - group['charge_efficiency_percent']
            
            # 8. Discharge rate (capacity / time)
            group['discharge_rate'] = group['capacity_ah'] / (group['discharge_time_s'] / 3600)
            
            # 9. Impedance ratio (charge transfer / internal)
            group['impedance_ratio'] = group['charge_transfer_resistance_ohm'] / group['internal_resistance_ohm']
            
            # 10. Cycle age (normalized 0-1)
            max_cycle = group['cycle'].max()
            group['cycle_age_normalized'] = group['cycle'] / max_cycle
            
            engineered.append(group)
        
        result = pd.concat(engineered, ignore_index=True)
        
        # Fill NaN from diff operations
        result = result.fillna(0)
        
        print(f"[FEATURES] Created {len(result.columns) - len(df.columns)} new features")
        return result
    
    def get_ml_features(self) -> list:
        """Return the list of features used for ML training."""
        return [
            'cycle', 'capacity_ah', 'avg_voltage_v', 'voltage_charged_v',
            'voltage_discharged_v', 'charge_current_a', 'discharge_current_a',
            'avg_temperature_c', 'max_temperature_c', 'internal_resistance_ohm',
            'charge_transfer_resistance_ohm', 'discharge_time_s',
            'charge_efficiency_percent', 'discharge_slope_v_per_s',
            'capacity_degradation_rate', 'cumulative_capacity_loss',
            'resistance_growth_rate', 'temp_rolling_mean', 'temp_rolling_std',
            'thermal_variance', 'voltage_spread', 'capacity_rolling_std',
            'efficiency_drop', 'discharge_rate', 'impedance_ratio',
            'cycle_age_normalized'
        ]
    
    def scale_features(self, df: pd.DataFrame, fit: bool = True) -> pd.DataFrame:
        """Scale features using StandardScaler."""
        feature_cols = self.get_ml_features()
        self.feature_columns = feature_cols
        
        available_cols = [c for c in feature_cols if c in df.columns]
        
        if fit:
            df[available_cols] = self.scaler.fit_transform(df[available_cols])
        else:
            df[available_cols] = self.scaler.transform(df[available_cols])
        
        print(f"[SCALE] Scaled {len(available_cols)} features")
        return df
    
    def process(self, filepath: str, output_dir: str) -> pd.DataFrame:
        """Full preprocessing pipeline."""
        print("\n" + "=" * 50)
        print("Battery Data Preprocessing Pipeline")
        print("=" * 50)
        
        df = self.load_data(filepath)
        df = self.clean(df)
        df = self.engineer_features(df)
        
        # Save unscaled version (for visualization)
        unscaled_path = os.path.join(output_dir, 'battery_features_unscaled.csv')
        df.to_csv(unscaled_path, index=False)
        print(f"[SAVE] Unscaled features: {unscaled_path}")
        
        # Save scaled version (for ML)
        df_scaled = df.copy()
        df_scaled = self.scale_features(df_scaled, fit=True)
        scaled_path = os.path.join(output_dir, 'battery_features_scaled.csv')
        df_scaled.to_csv(scaled_path, index=False)
        print(f"[SAVE] Scaled features: {scaled_path}")
        
        # Save scaler
        scaler_path = os.path.join(output_dir, 'battery_scaler.joblib')
        joblib.dump(self.scaler, scaler_path)
        print(f"[SAVE] Scaler: {scaler_path}")
        
        return df  # Return unscaled


class CMAPSSPreprocessor:
    """Preprocesses NASA C-MAPSS data for RUL prediction."""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.sensor_columns = [f's{i}' for i in range(1, 22)]
        self.op_columns = ['op_setting_1', 'op_setting_2', 'op_setting_3']
    
    def load_data(self, filepath: str) -> pd.DataFrame:
        """Load raw C-MAPSS CSV data."""
        df = pd.read_csv(filepath)
        print(f"[LOAD] C-MAPSS data: {len(df)} records, {df['unit_id'].nunique()} engines")
        return df
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove constant sensors and clean data."""
        # Identify constant or near-constant sensors (std < 0.001)
        constant_sensors = []
        for col in self.sensor_columns:
            if df[col].std() < 0.001:
                constant_sensors.append(col)
        
        if constant_sensors:
            print(f"[CLEAN] Removing {len(constant_sensors)} near-constant sensors: {constant_sensors}")
            self.sensor_columns = [s for s in self.sensor_columns if s not in constant_sensors]
        
        return df
    
    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Engineer features from C-MAPSS sensor data."""
        print("[FEATURES] Engineering C-MAPSS features...")
        
        engineered = []
        for unit_id, group in df.groupby('unit_id'):
            group = group.sort_values('cycle').copy()
            
            # Rolling statistics for each sensor
            for sensor in self.sensor_columns:
                group[f'{sensor}_rolling_mean'] = group[sensor].rolling(5, min_periods=1).mean()
                group[f'{sensor}_rolling_std'] = group[sensor].rolling(5, min_periods=1).std().fillna(0)
            
            # Normalized cycle (0-1 progress through life)
            group['cycle_normalized'] = group['cycle'] / group['cycle'].max()
            
            engineered.append(group)
        
        result = pd.concat(engineered, ignore_index=True).fillna(0)
        new_features = len(result.columns) - len(df.columns)
        print(f"[FEATURES] Created {new_features} new features")
        return result
    
    def process(self, filepath: str, output_dir: str) -> pd.DataFrame:
        """Full C-MAPSS preprocessing pipeline."""
        print("\n" + "=" * 50)
        print("C-MAPSS Data Preprocessing Pipeline")
        print("=" * 50)
        
        df = self.load_data(filepath)
        df = self.clean(df)
        df = self.engineer_features(df)
        
        # Save processed data
        output_path = os.path.join(output_dir, 'cmapss_processed.csv')
        df.to_csv(output_path, index=False)
        print(f"[SAVE] Processed C-MAPSS: {output_path}")
        
        return df


def main():
    """Run all preprocessing pipelines."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(base_dir, 'data', 'raw')
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    os.makedirs(processed_dir, exist_ok=True)
    
    # Process Battery Data
    battery_proc = BatteryPreprocessor()
    battery_path = os.path.join(raw_dir, 'battery', 'nasa_battery_data.csv')
    battery_df = battery_proc.process(battery_path, processed_dir)
    
    # Process C-MAPSS Data
    cmapss_path = os.path.join(raw_dir, 'cmapss', 'cmapss_fd001.csv')
    if os.path.exists(cmapss_path):
        cmapss_proc = CMAPSSPreprocessor()
        cmapss_df = cmapss_proc.process(cmapss_path, processed_dir)
    else:
        print("\n[INFO] C-MAPSS dataset (cmapss_fd001.csv) not found. Skipping CMAPSS preprocessing.")
    
    print("\n" + "=" * 50)
    print("[DONE] All preprocessing complete!")
    print("=" * 50)
    print(f"\nProcessed files in: {processed_dir}")
    for f in os.listdir(processed_dir):
        fpath = os.path.join(processed_dir, f)
        size_kb = os.path.getsize(fpath) / 1024
        print(f"  - {f} ({size_kb:.1f} KB)")


if __name__ == '__main__':
    main()
```

---

## ml\preprocessing\__init__.py

```python
# Preprocessing Pipeline for EV AI Platform
```

---

## ml\simulator\ev_telemetry_simulator.py

```python
"""
EV Telemetry Simulator
======================
Simulates real-time sensor data from a fleet of electric vehicles.
Generates battery telemetry, vehicle status, charging sessions, and anomalies.

Modes:
  - Console: Prints telemetry to stdout (default, no dependencies)
  - File: Writes to JSON files for batch processing
  - MQTT: Publishes to MQTT broker (requires Mosquitto/Member 4 setup)
"""

import numpy as np
import json
import time
import os
import sys
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import threading

# Try to import MQTT, but don't fail if not available
try:
    import paho.mqtt.client as mqtt
    MQTT_AVAILABLE = True
except ImportError:
    MQTT_AVAILABLE = False


class EVVehicle:
    """Simulates a single EV with realistic battery behavior."""
    
    def __init__(self, vehicle_id: str, battery_age_cycles: int = None):
        self.vehicle_id = vehicle_id
        self.battery_age_cycles = battery_age_cycles or np.random.randint(50, 600)
        
        # Battery characteristics
        self.initial_capacity = 75.0  # kWh (typical industrial EV)
        self.soh = max(65, 100 - (self.battery_age_cycles / 800) * 35 + np.random.normal(0, 2))
        self.soc = np.random.uniform(20, 95)  # Current charge level
        self.voltage_nominal = 400.0  # Volts (pack level)
        self.temperature = np.random.uniform(25, 35)
        
        # Vehicle state
        self.is_charging = False
        self.is_moving = np.random.choice([True, False], p=[0.7, 0.3])
        self.speed = np.random.uniform(30, 80) if self.is_moving else 0
        self.odometer = np.random.randint(10000, 100000)
        self.latitude = 28.6139 + np.random.uniform(-0.5, 0.5)  # Delhi area
        self.longitude = 77.2090 + np.random.uniform(-0.5, 0.5)
        
        # Internal resistance (increases with age)
        self.internal_resistance = 0.04 + (self.battery_age_cycles / 800) * 0.03
        
        # Anomaly probability increases with age
        self.anomaly_base_prob = 0.01 + (self.battery_age_cycles / 800) * 0.05
    
    def update(self, dt_seconds: float = 2.0) -> Dict:
        """Generate next telemetry reading."""
        
        # --- Update vehicle state ---
        # Randomly transition between driving/stopped/charging
        if np.random.random() < 0.02:  # 2% chance of state change
            if self.is_moving:
                self.is_moving = False
                self.speed = 0
                if self.soc < 30 and np.random.random() < 0.7:
                    self.is_charging = True
            elif self.is_charging:
                if self.soc > 85:
                    self.is_charging = False
                    self.is_moving = True
                    self.speed = np.random.uniform(30, 80)
            else:
                self.is_moving = True
                self.speed = np.random.uniform(30, 80)
        
        # --- Battery simulation ---
        # SoC changes
        if self.is_charging:
            # Charging: SoC increases (~50kW charger)
            charge_rate = 50.0 / self.initial_capacity * 100 / 3600 * dt_seconds  # %/second
            self.soc = min(100, self.soc + charge_rate + np.random.normal(0, 0.1))
            current = 125.0 + np.random.normal(0, 5)  # Positive = charging
        elif self.is_moving:
            # Driving: SoC decreases
            consumption = (0.2 + self.speed / 500) * dt_seconds / 3600 * 100  # % per dt
            self.soc = max(5, self.soc - consumption + np.random.normal(0, 0.05))
            current = -(80 + self.speed * 0.5 + np.random.normal(0, 10))  # Negative = discharging
        else:
            # Parked: minimal drain
            self.soc = max(5, self.soc - 0.001 + np.random.normal(0, 0.01))
            current = -0.5 + np.random.normal(0, 0.1)
        
        # Voltage (depends on SoC and load)
        voltage = self.voltage_nominal * (0.85 + 0.15 * (self.soc / 100))
        voltage += np.random.normal(0, 1.5)
        
        # Temperature (affected by current, ambient, and battery health)
        ambient_temp = 30 + np.random.normal(0, 2)
        heat_from_current = abs(current) * self.internal_resistance * 0.01
        self.temperature = 0.95 * self.temperature + 0.05 * (ambient_temp + heat_from_current)
        self.temperature += np.random.normal(0, 0.3)
        
        # Movement
        if self.is_moving:
            self.speed += np.random.normal(0, 2)
            self.speed = max(0, min(120, self.speed))
            distance = self.speed * dt_seconds / 3600  # km
            self.odometer += distance
            # Update position
            self.latitude += np.random.normal(0, 0.001)
            self.longitude += np.random.normal(0, 0.001)
        
        # --- Anomaly injection ---
        anomaly_type = None
        anomaly_severity = 0
        
        if np.random.random() < self.anomaly_base_prob:
            anomaly_choices = ['thermal_spike', 'voltage_anomaly', 'current_surge', 
                             'soc_inconsistency', 'charging_fault']
            anomaly_type = np.random.choice(anomaly_choices)
            
            if anomaly_type == 'thermal_spike':
                self.temperature += np.random.uniform(8, 20)
                anomaly_severity = min(1.0, (self.temperature - 45) / 20)
            elif anomaly_type == 'voltage_anomaly':
                voltage += np.random.choice([-30, 30]) + np.random.normal(0, 5)
                anomaly_severity = 0.6
            elif anomaly_type == 'current_surge':
                current *= np.random.uniform(2.0, 3.0)
                anomaly_severity = 0.8
            elif anomaly_type == 'soc_inconsistency':
                # SoC jumps unrealistically
                self.soc += np.random.choice([-15, -10])
                anomaly_severity = 0.5
            elif anomaly_type == 'charging_fault':
                if self.is_charging:
                    current = np.random.uniform(-5, 5)  # Near zero despite "charging"
                    anomaly_severity = 0.7
        
        # Build telemetry packet
        telemetry = {
            'vehicle_id': self.vehicle_id,
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'battery': {
                'soc': round(self.soc, 2),
                'voltage': round(voltage, 2),
                'current': round(current, 2),
                'temperature': round(self.temperature, 2),
                'soh': round(self.soh, 2),
                'cycle_count': self.battery_age_cycles,
                'internal_resistance': round(self.internal_resistance, 5),
                'capacity_kwh': round(self.initial_capacity * self.soh / 100, 2)
            },
            'vehicle': {
                'speed_kmh': round(self.speed, 1),
                'odometer_km': round(self.odometer, 1),
                'is_moving': bool(self.is_moving),
                'location': {
                    'latitude': round(self.latitude, 6),
                    'longitude': round(self.longitude, 6)
                }
            },
            'charging': {
                'is_charging': bool(self.is_charging),
                'charger_type': 'DC_FAST' if self.is_charging else None,
                'power_kw': round(abs(current) * voltage / 1000, 2) if self.is_charging else 0
            },
            'anomaly': {
                'detected': bool(anomaly_type is not None),
                'type': anomaly_type,
                'severity': round(anomaly_severity, 3)
            }
        }
        
        return telemetry


class EVFleetSimulator:
    """Simulates an entire fleet of EVs generating telemetry."""
    
    def __init__(self, num_vehicles: int = 50, output_mode: str = 'console'):
        """
        Args:
            num_vehicles: Number of EVs to simulate
            output_mode: 'console', 'file', or 'mqtt'
        """
        self.num_vehicles = num_vehicles
        self.output_mode = output_mode
        self.vehicles: List[EVVehicle] = []
        self.mqtt_client = None
        self.running = False
        self.telemetry_log = []
        
        # Create fleet
        for i in range(num_vehicles):
            vid = f"EV-{i+1:03d}"
            self.vehicles.append(EVVehicle(vid))
        
        print(f"[INIT] Fleet simulator: {num_vehicles} vehicles, mode={output_mode}")
    
    def setup_mqtt(self, broker_host: str = 'localhost', broker_port: int = 1883):
        """Connect to MQTT broker (requires Mosquitto from Member 4)."""
        if not MQTT_AVAILABLE:
            print("[WARN] paho-mqtt not installed. Use: pip install paho-mqtt")
            return False
        
        try:
            # Handles paho-mqtt compatibility for both v1 and v2 APIs
            self.mqtt_client = mqtt.Client(
                callback_api_version=mqtt.CallbackAPIVersion.VERSION2 if hasattr(mqtt, 'CallbackAPIVersion') else None
            )
            self.mqtt_client.connect(broker_host, broker_port, 60)
            self.mqtt_client.loop_start()
            print(f"[MQTT] Connected to {broker_host}:{broker_port}")
            return True
        except Exception as e:
            print(f"[MQTT] Connection failed: {e}")
            print("[MQTT] Falling back to console mode")
            self.output_mode = 'console'
            return False
    
    def publish_telemetry(self, telemetry: Dict):
        """Publish telemetry to the configured output."""
        vehicle_id = telemetry['vehicle_id']
        
        if self.output_mode == 'mqtt' and self.mqtt_client:
            # Match the exact flat payload and topic required by the backend developer for Kafka
            payload = {
                "vehicle_id": vehicle_id,
                "timestamp": telemetry['timestamp'],
                "voltage": telemetry['battery']['voltage'],
                "current": telemetry['battery']['current'],
                "temperature": telemetry['battery']['temperature'],
                "soc": telemetry['battery']['soc'],
                "cycle_count": telemetry['battery']['cycle_count']
            }
            self.mqtt_client.publish(f"ev/battery/{vehicle_id}", json.dumps(payload))
        
        elif self.output_mode == 'file':
            self.telemetry_log.append(telemetry)
        
        elif self.output_mode == 'console':
            # Compact console output
            bat = telemetry['battery']
            veh = telemetry['vehicle']
            anomaly = telemetry['anomaly']
            
            status = "CHRG" if telemetry['charging']['is_charging'] else (
                     "MOVE" if veh['is_moving'] else "PARK")
            
            line = (f"  {vehicle_id} | SoC:{bat['soc']:5.1f}% | "
                   f"V:{bat['voltage']:6.1f} | I:{bat['current']:7.1f}A | "
                   f"T:{bat['temperature']:5.1f}C | SoH:{bat['soh']:5.1f}% | "
                   f"{status} {veh['speed_kmh']:5.1f}km/h")
            
            if anomaly['detected']:
                line += f" | !! {anomaly['type']} (sev:{anomaly['severity']:.2f})"
            
            print(line)
    
    def run(self, duration_seconds: int = 30, interval: float = 2.0):
        """Run the simulator for a given duration."""
        self.running = True
        iterations = int(duration_seconds / interval)
        
        print(f"\n{'='*80}")
        print(f"EV Fleet Simulator - {self.num_vehicles} vehicles, {duration_seconds}s duration")
        print(f"{'='*80}\n")
        
        try:
            for i in range(iterations):
                if not self.running:
                    break
                
                timestamp = datetime.utcnow().strftime('%H:%M:%S')
                print(f"\n[{timestamp}] Tick {i+1}/{iterations}")
                
                for vehicle in self.vehicles:
                    telemetry = vehicle.update(interval)
                    self.publish_telemetry(telemetry)
                
                if i < iterations - 1:
                    time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n[STOP] Simulator interrupted")
        
        self.running = False
        
        # Save file output
        if self.output_mode == 'file' and self.telemetry_log:
            output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                      'data', 'processed')
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, 'simulated_telemetry.json')
            with open(output_path, 'w') as f:
                json.dump(self.telemetry_log, f, indent=2)
            print(f"\n[SAVE] {len(self.telemetry_log)} records saved to {output_path}")
        
        # Generate summary
        self._print_summary()
    
    def generate_batch(self, num_ticks: int = 100, interval: float = 2.0) -> list:
        """Generate a batch of telemetry without real-time delays (for training data)."""
        all_telemetry = []
        for tick in range(num_ticks):
            for vehicle in self.vehicles:
                telemetry = vehicle.update(interval)
                all_telemetry.append(telemetry)
        return all_telemetry
    
    def _print_summary(self):
        """Print fleet status summary."""
        print(f"\n{'='*80}")
        print("Fleet Summary")
        print(f"{'='*80}")
        
        socs = [v.soc for v in self.vehicles]
        sohs = [v.soh for v in self.vehicles]
        temps = [v.temperature for v in self.vehicles]
        
        print(f"  SoC   - Min: {min(socs):.1f}% | Avg: {np.mean(socs):.1f}% | Max: {max(socs):.1f}%")
        print(f"  SoH   - Min: {min(sohs):.1f}% | Avg: {np.mean(sohs):.1f}% | Max: {max(sohs):.1f}%")
        print(f"  Temp  - Min: {min(temps):.1f}C | Avg: {np.mean(temps):.1f}C | Max: {max(temps):.1f}C")
        
        moving = sum(1 for v in self.vehicles if v.is_moving)
        charging = sum(1 for v in self.vehicles if v.is_charging)
        parked = self.num_vehicles - moving - charging
        print(f"  Status - Moving: {moving} | Charging: {charging} | Parked: {parked}")


def main():
    """Run the simulator with default settings."""
    import argparse
    
    parser = argparse.ArgumentParser(description='EV Fleet Telemetry Simulator')
    parser.add_argument('--vehicles', type=int, default=10, help='Number of vehicles (default: 10)')
    parser.add_argument('--duration', type=int, default=20, help='Duration in seconds (default: 20)')
    parser.add_argument('--interval', type=float, default=2.0, help='Update interval in seconds')
    parser.add_argument('--mode', choices=['console', 'file', 'mqtt'], default='console',
                       help='Output mode (default: console)')
    parser.add_argument('--mqtt-host', default='localhost', help='MQTT broker host')
    parser.add_argument('--mqtt-port', type=int, default=1883, help='MQTT broker port')
    
    args = parser.parse_args()
    
    sim = EVFleetSimulator(num_vehicles=args.vehicles, output_mode=args.mode)
    
    if args.mode == 'mqtt':
        sim.setup_mqtt(args.mqtt_host, args.mqtt_port)
    
    sim.run(duration_seconds=args.duration, interval=args.interval)


if __name__ == '__main__':
    main()
```

---

## ml\5.+Battery+Data+Set\5. Battery Data Set\1. BatteryAgingARC-FY08Q4.zip

**[Skipped - File Too Large (55192.7 KB)]**

---

## ml\5.+Battery+Data+Set\5. Battery Data Set\2. BatteryAgingARC_25_26_27_28_P1.zip

**[Skipped - File Too Large (10862.7 KB)]**

---

## ml\5.+Battery+Data+Set\5. Battery Data Set\3. BatteryAgingARC_25-44.zip

**[Skipped - File Too Large (91467.4 KB)]**

---

## ml\5.+Battery+Data+Set\5. Battery Data Set\4. BatteryAgingARC_45_46_47_48.zip

**[Skipped - File Too Large (14370.2 KB)]**

---

## ml\5.+Battery+Data+Set\5. Battery Data Set\5. BatteryAgingARC_49_50_51_52.zip

**[Skipped - File Too Large (8512.9 KB)]**

---

## ml\5.+Battery+Data+Set\5. Battery Data Set\6. BatteryAgingARC_53_54_55_56.zip

**[Skipped - File Too Large (24339.3 KB)]**

---

## ml\5.+Battery+Data+Set\extracted_1\B0005.mat

**[Skipped - File Too Large (15582.9 KB)]**

---

## ml\5.+Battery+Data+Set\extracted_1\B0006.mat

**[Skipped - File Too Large (15652.5 KB)]**

---

## ml\5.+Battery+Data+Set\extracted_1\B0007.mat

**[Skipped - File Too Large (15673.3 KB)]**

---

## ml\5.+Battery+Data+Set\extracted_1\B0018.mat

**[Skipped - File Too Large (8302.9 KB)]**

---

## ml\5.+Battery+Data+Set\extracted_1\README.txt

```text
Data Description:
A set of four Li-ion batteries (# 5, 6, 7 and 18) were run through 3 different operational profiles (charge, discharge and impedance) at room temperature. Charging was carried out in a constant current (CC) mode at 1.5A until the battery voltage reached 4.2V and then continued in a constant voltage (CV) mode until the charge current dropped to 20mA. Discharge was carried out at a constant current (CC) level of 2A until the battery voltage fell to 2.7V, 2.5V, 2.2V and 2.5V for batteries 5 6 7 and 18 respectively. Impedance measurement was carried out through an electrochemical impedance spectroscopy (EIS) frequency sweep from 0.1Hz to 5kHz. Repeated charge and discharge cycles result in accelerated aging of the batteries while impedance measurements provide insight into the internal battery parameters that change as aging progresses. The experiments were stopped when the batteries reached end-of-life (EOL) criteria, which was a 30% fade in rated capacity (from 2Ahr to 1.4Ahr). This dataset can be used for the prediction of both remaining charge (for a given discharge cycle) and remaining useful life (RUL).

Files:
B0005.mat	Data for Battery #5
B0006.mat	Data for Battery #6
B0007.mat	Data for Battery #7
B0018.mat	Data for Battery #18

Data Structure:
cycle:	top level structure array containing the charge, discharge and impedance operations
	type: 	operation  type, can be charge, discharge or impedance
	ambient_temperature:	ambient temperature (degree C)
	time: 	the date and time of the start of the cycle, in MATLAB  date vector format
	data:	data structure containing the measurements
	   for charge the fields are:
		Voltage_measured: 	Battery terminal voltage (Volts)
		Current_measured:	Battery output current (Amps)
		Temperature_measured: 	Battery temperature (degree C)
		Current_charge:		Current measured at charger (Amps)
		Voltage_charge:		Voltage measured at charger (Volts)
		Time:			Time vector for the cycle (secs)
	   for discharge the fields are:
		Voltage_measured: 	Battery terminal voltage (Volts)
		Current_measured:	Battery output current (Amps)
		Temperature_measured: 	Battery temperature (degree C)
		Current_charge:		Current measured at load (Amps)
		Voltage_charge:		Voltage measured at load (Volts)
		Time:			Time vector for the cycle (secs)
		Capacity:		Battery capacity (Ahr) for discharge till 2.7V 
	   for impedance the fields are:
		Sense_current:		Current in sense branch (Amps)
		Battery_current:	Current in battery branch (Amps)
		Current_ratio:		Ratio of the above currents 
		Battery_impedance:	Battery impedance (Ohms) computed from raw data
		Rectified_impedance:	Calibrated and smoothed battery impedance (Ohms) 
		Re:			Estimated electrolyte resistance (Ohms)
		Rct:			Estimated charge transfer resistance (Ohms)
```
