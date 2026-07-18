from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from enum import Enum

class NodeSchema(BaseModel):
    id: str
    label: str
    properties: Dict[str, Any]

class EdgeSchema(BaseModel):
    source: str
    target: str
    type: str
    properties: Dict[str, Any]

class GraphResponse(BaseModel):
    nodes: List[NodeSchema]
    edges: List[EdgeSchema]

class VehicleTraceResponse(GraphResponse):
    vehicle_id: str

class SupplierResponse(GraphResponse):
    supplier_id: str

class MaterialTraceResponse(GraphResponse):
    material_id: str

class FleetDependencyResponse(GraphResponse):
    fleet_id: str

class GraphStatisticsResponse(BaseModel):
    node_count: int
    relationship_count: int
    entities_by_type: Dict[str, int]

# --- PHASE 3 INTELLIGENCE SCHEMAS ---

class RiskScoreCategory(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class SupplyChainRiskScore(BaseModel):
    score: float = Field(..., description="Normalized risk score from 0 to 100")
    category: RiskScoreCategory
    factors: Dict[str, Any] = Field(default_factory=dict, description="Factors contributing to the risk score")

class RiskAnalysisResponse(BaseModel):
    entity_id: str
    entity_type: str
    risk: SupplyChainRiskScore
    downstream_impact_count: int
    upstream_dependency_count: int

class ImpactAnalysisResponse(BaseModel):
    entity_id: str
    entity_type: str
    impacted_suppliers: int = 0
    impacted_vehicles: int = 0
    impacted_fleets: int = 0
    impacted_battery_cells: int = 0
    dependency_depth: int = 0
    total_downstream_entities: int = 0
    graph: GraphResponse

class DependencyAnalysisResponse(BaseModel):
    entity_id: str
    entity_type: str
    # Supplier Metrics
    downstream_consumers: int = 0
    supplied_materials: int = 0
    dependent_vehicles: int = 0
    # Vehicle Metrics
    suppliers_involved: int = 0
    mines_involved: int = 0
    materials_used: int = 0
    # Fleet Metrics
    supplier_diversity: int = 0
    material_diversity: int = 0
    manufacturing_diversity: int = 0

class CriticalNodeResponse(BaseModel):
    node_id: str
    label: str
    name: str
    bottleneck_type: str
    impacted_entities: int

class AnalyticsDependenciesResponse(BaseModel):
    critical_bottlenecks: List[CriticalNodeResponse]
    global_dependency_depth: int
    graph: GraphResponse

class AlternativeSupplierResponse(BaseModel):
    target_id: str
    target_type: str
    original_supplier_id: Optional[str] = None
    alternative_suppliers: List[Dict[str, Any]]

# --- PHASE 4 DASHBOARD SCHEMAS ---

class DashboardOverviewResponse(BaseModel):
    total_suppliers: int
    total_materials: int
    total_vehicles: int
    total_fleets: int
    average_supply_chain_depth: float
    high_risk_suppliers_count: int
    critical_bottlenecks_count: int
    supply_diversity_index: float

class RiskSummaryResponse(BaseModel):
    high_risk_suppliers: List[Dict[str, Any]]
    critical_bottlenecks: List[CriticalNodeResponse]
    risk_distribution: Dict[str, int]

class NetworkVisualizationNode(BaseModel):
    data: Dict[str, Any]
    classes: Optional[str] = None

class NetworkVisualizationEdge(BaseModel):
    data: Dict[str, Any]

class NetworkVisualizationResponse(BaseModel):
    elements: Dict[str, List[Any]]

class RecommendationAction(BaseModel):
    action_type: str
    target_entity_id: str
    target_entity_type: str
    reason: str
    suggested_alternatives: List[Dict[str, Any]] = []

class RecommendationResponse(BaseModel):
    recommendations: List[RecommendationAction]

class HistoricalTrendResponse(BaseModel):
    timestamps: List[str]
    risk_scores: List[float]
    depths: List[float]

# --- PHASE 5 GRAPH MANAGEMENT SCHEMAS ---

class SupplierCreate(BaseModel):
    supplier_id: str = Field(..., description="Unique supplier identifier (e.g. SUP-004)")
    name: str = Field(..., description="Name of the supplier")
    country: str = Field(..., description="Country location of the supplier")
    risk_score: float = Field(default=0.0, description="Risk score from 0 to 100")
    status: str = Field(default="ACTIVE", description="Status (ACTIVE, ON_HOLD, etc.)")

class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    risk_score: Optional[float] = None
    status: Optional[str] = None

class SupplierNodeResponse(BaseModel):
    supplier_id: str
    name: str
    country: str
    risk_score: float = 0.0
    status: str = "ACTIVE"

class MaterialCreate(BaseModel):
    material_id: str = Field(..., description="Unique material identifier (e.g. MAT-004)")
    name: str = Field(..., description="Material name")
    type: str = Field(..., description="Material type (Raw, Processed, etc.)")

class MaterialUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None

class MaterialNodeResponse(BaseModel):
    material_id: str
    name: str
    type: str

class ProcessingPlantCreate(BaseModel):
    plant_id: str = Field(..., description="Unique processing plant identifier (e.g. PLT-003)")
    name: str = Field(..., description="Plant name")
    country: str = Field(..., description="Country location of the processing plant")
    plant_type: Optional[str] = Field(default="Refinery", description="Type of plant (Refinery, Gigafactory, etc.)")

class ProcessingPlantUpdate(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    plant_type: Optional[str] = None

class ProcessingPlantNodeResponse(BaseModel):
    plant_id: str
    name: str
    country: str
    plant_type: Optional[str] = "Refinery"

class MineCreate(BaseModel):
    mine_id: str = Field(..., description="Unique mine identifier (e.g. MIN-004)")
    name: str = Field(..., description="Mine name")
    country: str = Field(..., description="Country location")
    material: str = Field(..., description="Primary mineral extracted")

class MineUpdate(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    material: Optional[str] = None

class MineNodeResponse(BaseModel):
    mine_id: str
    name: str
    country: str
    material: str

# --- PHASE 6 MATERIAL FLOW & TRACEABILITY SCHEMAS ---

class MaterialFlowSummaryItem(BaseModel):
    material_id: str
    name: str
    type: str
    suppliers_count: int = 0
    refineries_count: int = 0
    plants_count: int = 0
    vehicles_count: int = 0

class MaterialFlowResponse(BaseModel):
    summary: List[MaterialFlowSummaryItem]
    graph: GraphResponse

class TraceabilityStage(BaseModel):
    stage_order: int
    stage_name: str
    entity_id: str
    entity_type: str
    name: str
    location: Optional[str] = None
    details: Dict[str, Any] = Field(default_factory=dict)

class TraceabilityResponse(BaseModel):
    target_id: Optional[str] = None
    upstream_lineage: List[Dict[str, Any]]
    downstream_usage: List[Dict[str, Any]]
    complete_manufacturing_chain: List[TraceabilityStage]
    graph: GraphResponse

# --- DELIVERABLE 7 ML RISK SCHEMAS ---

class SupplierMLRiskItem(BaseModel):
    supplier_id: str
    supplier_name: str
    type: str = "mine"
    country: str
    country_name: Optional[str] = None
    mineral: Optional[str] = None
    risk_score: float
    risk_level: str
    risk_color: Optional[str] = None
    confidence: float = 95.0
    action: Optional[str] = None
    breakdown: Dict[str, float] = Field(default_factory=dict)
    recommendations: List[str] = Field(default_factory=list)

class SupplyChainMLRiskResponse(BaseModel):
    global_risk_index: float
    risk_level: str
    confidence: float = 95.0
    total_suppliers_assessed: int
    critical_vulnerability: str
    mitigation_plan: str
    suppliers: List[SupplierMLRiskItem]
    last_updated: str

class CriticalSuppliersResponse(BaseModel):
    total_critical_count: int
    critical_suppliers: List[SupplierMLRiskItem]
    recommendations: List[str]

# --- PHASE 8 PROCUREMENT RECOMMENDATION SCHEMAS ---

class SupplierRecommendation(BaseModel):
    supplier_id: str
    supplier_name: str
    country: str
    mineral: str

class ProcurementRecommendationItem(BaseModel):
    material: str
    recommended_suppliers: List[SupplierRecommendation]
    alternative_suppliers: List[SupplierRecommendation]
    diversification_suggestions: List[str]
    reason_for_recommendation: str
    current_supplier_risk: float
    suggested_supplier_risk: float

class ProcurementRecommendationResponse(BaseModel):
    recommendations: List[ProcurementRecommendationItem]
    summary: str
