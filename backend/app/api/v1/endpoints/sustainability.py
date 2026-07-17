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
