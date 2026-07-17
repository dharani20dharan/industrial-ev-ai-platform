from fastapi import APIRouter
from ....schemas.telemetry import SupplierRiskResponse, GraphDependencyResponse
from typing import List
from datetime import datetime
import sys
import os

# Append ML directory to sys.path
from app.services.ml import ML_DIR
if ML_DIR not in sys.path:
    sys.path.append(ML_DIR)

from engines.risk_scorer import SupplyChainRiskScorer

router = APIRouter()

@router.get("/suppliers", response_model=List[SupplierRiskResponse])
def get_suppliers():
    scorer = SupplyChainRiskScorer()
    scores = scorer.score_all_suppliers()
    
    response = []
    for idx, s in enumerate(scores):
        num_id = idx + 1
        try:
            # Try parsing digits out of S001 etc.
            digits = "".join(filter(str.isdigit, s['supplier_id']))
            if digits:
                num_id = int(digits)
        except Exception:
            pass
            
        response.append({
            "id": num_id,
            "name": s['supplier_name'],
            "location": s['country'],
            "risk_score": s['risk_score'],
            "material_supplied": s['mineral'].capitalize() if s['mineral'] else s['type'].capitalize()
        })
    return response

@router.get("/risk")
def get_supply_chain_risk():
    scorer = SupplyChainRiskScorer()
    scores = scorer.score_all_suppliers()
    
    global_risk = round(sum(s['risk_score'] for s in scores) / len(scores), 1)
    highest = max(scores, key=lambda x: x['risk_score'])
    critical_vuln = f"High risk concentration from supplier {highest['supplier_name']} ({highest['risk_score']}/100) in {highest['country']}."
    mitigation = highest['recommendations'][0] if highest['recommendations'] else "Diversify sourcing contracts."
    
    return {
        "global_risk_index": global_risk,
        "critical_vulnerability": critical_vuln,
        "mitigation_plan": mitigation,
        "last_updated": datetime.now().isoformat()
    }

@router.get("/materials")
def get_materials_flow():
    scorer = SupplyChainRiskScorer()
    materials = []
    for name, info in scorer.commodity_data.items():
        materials.append({
            "name": name.capitalize(),
            "active_flow_tons": int(info['price_usd_ton'] / 100),
            "safety_buffer_days": int((1.0 - info['supply_risk']) * 100)
        })
    return {"materials": materials}

@router.get("/dependencies", response_model=GraphDependencyResponse)
def get_dependencies_graph():
    scorer = SupplyChainRiskScorer()
    graph = scorer.get_supply_chain_graph()
    
    nodes = []
    for n in graph['nodes']:
        nodes.append({
            "id": n['id'],
            "label": n['type'].capitalize(),
            "properties": {
                "name": n['label'],
                "country": n['country'] or "Unknown",
                "risk_score": n['risk_score'],
                "risk_level": n['risk_level']
            }
        })
        
    edges = []
    for e in graph['edges']:
        edges.append({
            "source": e['source'],
            "target": e['target'],
            "type": e['material'].upper().replace(' ', '_')
        })
        
    return {
        "nodes": nodes,
        "edges": edges
    }
