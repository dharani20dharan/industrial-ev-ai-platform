from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, date
from typing import Optional, List, Dict, Any, Generic, TypeVar
from enum import Enum
from uuid import UUID

T = TypeVar('T')

class ReportPeriod(str, Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"
    CUSTOM = "CUSTOM"

class ReadinessLevel(str, Enum):
    NOT_READY = "NOT_READY"
    PARTIALLY_READY = "PARTIALLY_READY"
    READY = "READY"
    HIGHLY_READY = "HIGHLY_READY"

class RecommendationLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

# Standard JSON response envelope
class APIResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str
    data: Optional[T] = None

# Requests
class CarbonCalculationRequest(BaseModel):
    vehicle_id: str
    start_date: date
    end_date: date
    grid_region: Optional[str] = "india"

class DieselVsEVRequest(BaseModel):
    distance_km: float
    payload_kg: float
    diesel_efficiency: float  # fuel consumption in L/100km
    ev_efficiency: float  # energy consumption in kWh/km
    vehicle_type: Optional[str] = "medium_truck"

class ReadinessAssessmentRequest(BaseModel):
    route_distance: float
    payload: float  # in kg (scorer works in tons, so we'll divide by 1000)
    charging_availability: bool
    dwell_time: float  # in hours
    vehicle_type: Optional[str] = "medium_truck"
    vehicle_id: Optional[str] = None

class ProcurementRecommendationRequest(BaseModel):
    fleet_size: int
    daily_distance: float
    charging_available: bool
    vehicle_type: Optional[str] = "medium_truck"

# Responses
class CarbonReportResponse(BaseModel):
    report_id: UUID
    vehicle_id: str
    distance_travelled: float
    energy_consumed_kwh: float
    diesel_emission: float
    ev_emission: float
    scope1_emission: float
    scope3_emission: float
    carbon_saved: float
    grid_region: str
    generated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DieselVsEVResponse(BaseModel):
    diesel_emission: float
    ev_emission: float
    carbon_saved: float
    reduction_percentage: float
    equivalent_trees: float
    equivalent_gallons_gasoline: float

class ReadinessAssessmentResponse(BaseModel):
    assessment_id: UUID
    readiness_score: float
    readiness_level: str
    recommendation: str
    factor_scores: Dict[str, float]
    financial: Dict[str, Any]
    improvements_needed: List[str]
    generated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ProcurementRecommendationResponse(BaseModel):
    recommended_vehicle_type: str
    recommended_quantity: int
    estimated_carbon_saving: float
    recommendation_level: RecommendationLevel
    reasoning: str

class SustainabilitySummaryResponse(BaseModel):
    total_carbon_saved_kg: float
    scope1_emission_kg: float
    scope3_emission_kg: float
    vehicles_assessed: int
    average_readiness_score: float
    total_reports: int
    grid_region: str
