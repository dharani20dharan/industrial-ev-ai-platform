import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, Integer, JSON, Boolean
from sqlalchemy.orm import declarative_base

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