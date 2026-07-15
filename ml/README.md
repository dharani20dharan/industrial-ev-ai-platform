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

## Member 4 Integration Guide

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
