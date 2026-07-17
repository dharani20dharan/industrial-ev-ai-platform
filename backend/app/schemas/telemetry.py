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