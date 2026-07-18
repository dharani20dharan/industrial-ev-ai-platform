import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, Boolean, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.models.domain import Base

class CarbonReport(Base):
    __tablename__ = "carbon_report"

    # TimescaleDB requires the time column (generated_at) to be part of the primary key
    report_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    generated_at = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow, index=True)

    vehicle_id = Column(String(50), nullable=False, index=True)
    fleet_id = Column(String(50), nullable=True, index=True)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)
    distance_travelled = Column(Float, nullable=False)
    energy_consumed_kwh = Column(Float, nullable=False)
    diesel_emission = Column(Float, nullable=False)
    ev_emission = Column(Float, nullable=False)
    scope1_emission = Column(Float, nullable=False)
    scope3_emission = Column(Float, nullable=False)
    carbon_saved = Column(Float, nullable=False)
    grid_region = Column(String(50), nullable=False, default="india")

class ReadinessAssessment(Base):
    __tablename__ = "readiness_assessment"

    # TimescaleDB requires the time column (generated_at) to be part of the primary key
    assessment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    generated_at = Column(DateTime(timezone=True), primary_key=True, default=datetime.utcnow, index=True)

    vehicle_id = Column(String(50), nullable=True, index=True)
    fleet_id = Column(String(50), nullable=True, index=True)
    route_distance = Column(Float, nullable=False)
    payload = Column(Float, nullable=False)
    charging_availability = Column(Boolean, nullable=False)
    dwell_time = Column(Float, nullable=False)
    readiness_score = Column(Float, nullable=False)
    readiness_level = Column(String(50), nullable=False)
    recommendation = Column(String(500), nullable=False)
    factor_scores = Column(JSON, nullable=True)
