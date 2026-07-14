# Industrial EV AI Platform

An enterprise-grade platform for EV Supply Chain & Asset Intelligence. Designed for industrial IoT architectures, real-time telemetry streaming, battery degradation intelligence, Neo4j supply chain graph analytics, predictive maintenance systems, and carbon & sustainability reporting.

This project was bootstrapped to align with a **2-Week Hackathon** implementation guide.

---

## 🛠️ Repository & Architecture Layout

The repository is structured as a mono-repo to facilitate seamless collaboration across different members:

```
├── .gitignore                      # Python, Node, environment configurations ignore
├── docker-compose.yml              # Local infrastructure stack (TimescaleDB, Neo4j, MQTT, Kafka)
├── README.md                       # This document
├── frontend/                       # React + TS + TailwindCSS + ShadCN UI (Member 1)
│   ├── package.json                # Frontend package dependencies
│   ├── tsconfig.json               # TypeScript config
│   ├── tailwind.config.js          # Tailwind styling configuration
│   ├── src/
│   │   ├── components/             # Reusable widgets (gauges, charts, panels)
│   │   ├── layouts/                # Sidebar, Navbar, page containers (Shell)
│   │   └── pages/                  # Dashboard pages (Fleet, Battery, Supply Chain, Alerts, Carbon)
├── backend/                        # FastAPI REST/WebSocket Server (Member 2)
│   ├── requirements.txt            # Backend Python dependencies
│   ├── app/
│   │   ├── main.py                 # FastAPI entrance & configurations
│   │   ├── models/                 # SQLAlchemy schemas (telemetry, alerts, logs)
│   │   ├── schemas/                # Pydantic schemas
│   │   └── api/                    # Routers (health, telemetry, ML, supply chain, sustainability)
├── ml/                             # AI/ML & Telemetry Simulator (Member 3)
│   ├── requirements.txt            # Data science packages
│   ├── notebooks/                  # Exploratory Data Analysis & training
│   ├── src/                        # Preprocessing and model inference scripts
│   └── simulator/                  # Paho-MQTT based synthetic telemetry stream simulator
└── infrastructure/                 # Databases, brokers, and streaming (Member 4)
    ├── timescaledb/                # Init SQL, partitions, hypertable setups
    ├── neo4j/                      # Cypher query imports & relationship setup
    ├── kafka/                      # Kafka producers & consumers
    └── mosquitto/                  # MQTT broker configurations
```

---

## 🗓️ 2-Week Hackathon Execution Plan

### Day 1 — Project Foundation & System Design
- **Member 1 (Frontend):** Initialize React + TS project, install Tailwind + ShadCN UI, set up routing.
- **Member 2 (Backend):** Initialize FastAPI backend, Swagger/OpenAPI docs, health checks, CORS.
- **Member 3 (AI/ML):** Download datasets (NASA Battery, Oxford, C-MAPSS), start exploratory analysis.
- **Member 4 (Infrastructure):** Setup Docker Compose, PostgreSQL + TimescaleDB, Neo4j, Kafka, Mosquitto.

### Day 2 — Databases & Streaming Foundation
- **Member 1 (Frontend):** Design wireframes for Fleet, Battery, Supply Chain, Alerts, and Carbon.
- **Member 2 (Backend):** Define SQLAlchemy schemas (telemetry, charging_sessions, battery_health, alerts, etc.).
- **Member 3 (AI/ML):** Build preprocessing pipelines (normalization, capacity fade, thermal variance).
- **Member 4 (Infrastructure):** Set up MQTT and Kafka topics (`ev/battery`, `ev/charging`, etc.).

### Day 3 — Telemetry Simulation & Live Pipelines
- **Member 1 (Frontend):** Build live widgets (gauges, cards, Apache ECharts/Recharts).
- **Member 2 (Backend):** Develop REST APIs for `/telemetry/live`, `/battery/status`, etc.
- **Member 3 (AI/ML):** Build Telemetry Simulator (simulating SoC, thermal spikes, battery degradation).
- **Member 4 (Infrastructure):** Deploy end-to-end telemetry pipeline (MQTT ➔ Kafka ➔ FastAPI).

### Day 4-5 — AI & Predictive Maintenance
- **Member 1 (Frontend):** Build Remaining Useful Life (RUL) charts and anomaly warning notifications.
- **Member 2 (Backend):** Create ML inference APIs (`/predict/rul`, `/predict/soh`, etc.) & WebSockets.
- **Member 3 (AI/ML):** Train XGBoost (RUL), Isolation Forest (anomalies), and regression models.
- **Member 4 (Infrastructure):** Optimize TimescaleDB storage (indexing, partitioning, hypertables).

### Day 6-7 — Supply Chain Graph Intelligence
- **Member 1 (Frontend):** Build dependency graph visualization and supplier risk heatmaps.
- **Member 2 (Backend):** Develop Neo4j-integrated APIs (`/suppliers`, `/risk`, `/dependencies`).
- **Member 3 (AI/ML):** Build supply chain risk scoring engine (supplier concentration, price spikes).
- **Member 4 (Infrastructure):** Build Neo4j nodes and Cypher relationship pathways.

### Day 8-10 — Carbon & Fleet Electrification
- **Member 1 (Frontend):** Build CO₂ savings dashboards and electrification readiness scorecards.
- **Member 2 (Backend):** Develop calculation endpoints for carbon and EV savings.
- **Member 3 (AI/ML):** Implement Scope-1 and Scope-3 emission estimators.
- **Member 4 (Infrastructure):** Integrate OpenStreetMap / Open Charge Map geospatial layers.

### Day 11-14 — Polish, Test & Deploy
- UI polishing, animation refinement.
- End-to-end performance and latency testing.
- Deploy frontend (Vercel), backend (Railway/Render), database cluster.
- Final pitch preparation (architecture diagrams, demo videos).

---

## ⚡ Quick Start

### 1. Pre-requisites
- Docker & Docker Compose
- Node.js (v18+)
- Python (v3.10+)

### 2. Infrastructure Setup
Spin up the data stack (PostgreSQL, TimescaleDB, Neo4j, MQTT, Kafka):
```bash
docker compose up -d
```

### 3. Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 4. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### 5. Running the Simulator
```bash
cd ml
pip install -r requirements.txt
python simulator/simulator.py
```
