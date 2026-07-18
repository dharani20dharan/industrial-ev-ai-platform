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

-- 10. Supply Chain Intelligence Time-Series Data
CREATE TABLE IF NOT EXISTS supply_chain_history (
    id SERIAL,
    timestamp TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    entity_id VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    risk_score DOUBLE PRECISION NOT NULL,
    dependency_depth DOUBLE PRECISION DEFAULT 0.0,
    downstream_impacts INTEGER DEFAULT 0
);

SELECT create_hypertable('supply_chain_history', 'timestamp', if_not_exists => TRUE);
CREATE INDEX IF NOT EXISTS idx_sch_entity_timestamp ON supply_chain_history (entity_id, timestamp DESC);
