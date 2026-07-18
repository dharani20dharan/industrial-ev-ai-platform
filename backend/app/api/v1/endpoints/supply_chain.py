from fastapi import APIRouter, Depends, status
from typing import List, Optional
from datetime import datetime
import sys

from app.services.ml import ML_DIR
if ML_DIR not in sys.path:
    sys.path.append(ML_DIR)

from engines.risk_scorer import SupplyChainRiskScorer
from ....schemas.telemetry import SupplierRiskResponse, GraphDependencyResponse
from app.core.neo4j import get_neo4j_session
from app.services.supply_chain import SupplyChainService
from app.schemas.supply_chain import (
    VehicleTraceResponse, SupplierResponse, MaterialTraceResponse, 
    FleetDependencyResponse, GraphStatisticsResponse,
    RiskAnalysisResponse, ImpactAnalysisResponse, AlternativeSupplierResponse,
    AnalyticsDependenciesResponse,
    SupplierCreate, SupplierUpdate, SupplierNodeResponse,
    MaterialCreate, MaterialUpdate, MaterialNodeResponse,
    ProcessingPlantCreate, ProcessingPlantUpdate, ProcessingPlantNodeResponse,
    MineCreate, MineUpdate, MineNodeResponse,
    MaterialFlowResponse, TraceabilityResponse,
    SupplyChainMLRiskResponse, CriticalSuppliersResponse,
    ProcurementRecommendationResponse
)




router = APIRouter()

async def get_supply_chain_service(session=Depends(get_neo4j_session)):
    return SupplyChainService(session)

# ---------------------------------------------------------
# NEW GRAPH QUERY ENDPOINTS (Phase 3 Intelligence)
# ---------------------------------------------------------

@router.get("/risk/supplier/{supplier_id}", response_model=RiskAnalysisResponse)
async def analyze_supplier_risk(supplier_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.analyze_risk(supplier_id)

@router.get("/risk/material/{material_id}", response_model=RiskAnalysisResponse)
async def analyze_material_risk(material_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.analyze_risk(material_id)

@router.get("/risk/vehicle/{vehicle_id}", response_model=RiskAnalysisResponse)
async def analyze_vehicle_risk(vehicle_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.analyze_risk(vehicle_id)

@router.get("/risk/fleet/{fleet_id}", response_model=RiskAnalysisResponse)
async def analyze_fleet_risk(fleet_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.analyze_risk(fleet_id)

@router.get("/impact/supplier/{supplier_id}", response_model=ImpactAnalysisResponse)
async def analyze_supplier_impact(supplier_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.analyze_impact(supplier_id)

@router.get("/impact/material/{material_id}", response_model=ImpactAnalysisResponse)
async def analyze_material_impact(material_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.analyze_impact(material_id)

@router.get("/impact/refinery/{refinery_id}", response_model=ImpactAnalysisResponse)
async def analyze_refinery_impact(refinery_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.analyze_impact(refinery_id)

@router.get("/analytics/dependencies", response_model=AnalyticsDependenciesResponse)
async def get_analytics_dependencies(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_analytics_dependencies()

@router.get("/alternatives/material/{material_id}", response_model=AlternativeSupplierResponse)
async def find_material_alternatives(material_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_alternatives_for_material(material_id)

@router.get("/alternatives/supplier/{supplier_id}", response_model=AlternativeSupplierResponse)
async def find_supplier_alternatives(supplier_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_alternatives_for_supplier(supplier_id)

# ---------------------------------------------------------
# PHASE 4 DASHBOARD ENDPOINTS
# ---------------------------------------------------------
from app.schemas.supply_chain import (
    DashboardOverviewResponse, 
    NetworkVisualizationResponse, 
    RecommendationResponse
)

@router.get("/dashboard/overview", response_model=DashboardOverviewResponse)
async def get_dashboard_overview(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_dashboard_overview()

@router.get("/dashboard/network", response_model=NetworkVisualizationResponse)
async def get_network_visualization(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_network_visualization()

@router.get("/dashboard/recommendations", response_model=RecommendationResponse)
async def get_dashboard_recommendations(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.generate_recommendations()

# ---------------------------------------------------------
# GRAPH QUERY ENDPOINTS (Phase 2 Traversal)
# ---------------------------------------------------------
# ---------------------------------------------------------

@router.get("/vehicle/{vehicle_id}", response_model=VehicleTraceResponse)
async def trace_vehicle(vehicle_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.trace_vehicle(vehicle_id)

@router.get("/supplier/{supplier_id}", response_model=SupplierResponse)
async def trace_supplier(supplier_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.trace_supplier(supplier_id)

@router.get("/material/{material_id}", response_model=MaterialTraceResponse)
async def trace_material(material_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.trace_material(material_id)

@router.get("/fleet/{fleet_id}", response_model=FleetDependencyResponse)
async def trace_fleet(fleet_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.trace_fleet(fleet_id)

@router.get("/stats", response_model=GraphStatisticsResponse)
async def get_stats(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_stats()

# ---------------------------------------------------------
# PHASE 5 GRAPH MANAGEMENT ENDPOINTS (CRUD)
# ---------------------------------------------------------

# --- Supplier Endpoints ---

@router.post("/suppliers", response_model=SupplierNodeResponse, status_code=status.HTTP_217_CREATED if False else status.HTTP_201_CREATED)
async def create_supplier(payload: SupplierCreate, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.create_supplier(payload)

@router.get("/suppliers", response_model=List[SupplierNodeResponse])
async def list_suppliers(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.list_suppliers()

@router.get("/suppliers/{supplier_id}", response_model=SupplierNodeResponse)
async def get_supplier(supplier_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_supplier(supplier_id)

@router.patch("/suppliers/{supplier_id}", response_model=SupplierNodeResponse)
async def update_supplier(supplier_id: str, payload: SupplierUpdate, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.update_supplier(supplier_id, payload)

@router.delete("/suppliers/{supplier_id}")
async def delete_supplier(supplier_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.delete_supplier(supplier_id)

# --- Material Endpoints ---

@router.post("/materials", response_model=MaterialNodeResponse, status_code=status.HTTP_201_CREATED)
async def create_material(payload: MaterialCreate, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.create_material(payload)

@router.get("/materials", response_model=List[MaterialNodeResponse])
async def list_materials(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.list_materials()

@router.get("/materials/{material_id}", response_model=MaterialNodeResponse)
async def get_material(material_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_material(material_id)

@router.patch("/materials/{material_id}", response_model=MaterialNodeResponse)
async def update_material(material_id: str, payload: MaterialUpdate, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.update_material(material_id, payload)

@router.delete("/materials/{material_id}")
async def delete_material(material_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.delete_material(material_id)

# --- Processing Plant Endpoints ---

@router.post("/processing-plants", response_model=ProcessingPlantNodeResponse, status_code=status.HTTP_201_CREATED)
async def create_processing_plant(payload: ProcessingPlantCreate, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.create_processing_plant(payload)

@router.get("/processing-plants", response_model=List[ProcessingPlantNodeResponse])
async def list_processing_plants(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.list_processing_plants()

@router.get("/processing-plants/{plant_id}", response_model=ProcessingPlantNodeResponse)
async def get_processing_plant(plant_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_processing_plant(plant_id)

@router.patch("/processing-plants/{plant_id}", response_model=ProcessingPlantNodeResponse)
async def update_processing_plant(plant_id: str, payload: ProcessingPlantUpdate, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.update_processing_plant(plant_id, payload)

@router.delete("/processing-plants/{plant_id}")
async def delete_processing_plant(plant_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.delete_processing_plant(plant_id)

# --- Mine Endpoints (Optional) ---

@router.post("/mines", response_model=MineNodeResponse, status_code=status.HTTP_201_CREATED)
async def create_mine(payload: MineCreate, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.create_mine(payload)

@router.get("/mines", response_model=List[MineNodeResponse])
async def list_mines(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.list_mines()

@router.get("/mines/{mine_id}", response_model=MineNodeResponse)
async def get_mine(mine_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_mine(mine_id)

@router.patch("/mines/{mine_id}", response_model=MineNodeResponse)
async def update_mine(mine_id: str, payload: MineUpdate, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.update_mine(mine_id, payload)

@router.delete("/mines/{mine_id}")
async def delete_mine(mine_id: str, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.delete_mine(mine_id)

# ---------------------------------------------------------
# PHASE 6 MATERIAL FLOW & TRACEABILITY ENDPOINTS
# ---------------------------------------------------------

@router.get("/material-flow", response_model=MaterialFlowResponse)
async def get_material_flow(material_id: Optional[str] = None, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_material_flow(material_id)

@router.get("/traceability", response_model=TraceabilityResponse)
async def get_traceability(entity_id: Optional[str] = None, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_traceability(entity_id)

# ---------------------------------------------------------
# DELIVERABLE 7 ML INTEGRATION ENDPOINTS
# ---------------------------------------------------------

@router.get("/risk", response_model=SupplyChainMLRiskResponse)
async def get_supply_chain_ml_risk(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_ml_supply_chain_risk()

@router.get("/critical-suppliers", response_model=CriticalSuppliersResponse)
async def get_critical_suppliers(service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_ml_critical_suppliers()

# ---------------------------------------------------------
# PHASE 8 PROCUREMENT RECOMMENDATIONS
# ---------------------------------------------------------

@router.get("/recommendations", response_model=ProcurementRecommendationResponse)
async def get_procurement_recommendations(material_id: Optional[str] = None, service: SupplyChainService = Depends(get_supply_chain_service)):
    return await service.get_procurement_recommendations(material_id)
