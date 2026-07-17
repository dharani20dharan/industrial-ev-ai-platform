from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException, Depends
from ....schemas.telemetry import BatteryHealthResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db_session
from app.models.domain import BatteryRecord
from sqlalchemy import select
import asyncio
import random
import json

router = APIRouter()

MOCK_BATTERY_HEALTH = {
    "EV-HD-001": {"vehicle_id": "EV-HD-001", "capacity_fade": 5.8, "cycle_count": 260, "state_of_health": 96.0, "remaining_useful_life": 1240},
    "EV-HD-002": {"vehicle_id": "EV-HD-002", "capacity_fade": 9.2, "cycle_count": 410, "state_of_health": 91.0, "remaining_useful_life": 890},
    "EV-HD-003": {"vehicle_id": "EV-HD-003", "capacity_fade": 2.1, "cycle_count": 95, "state_of_health": 98.0, "remaining_useful_life": 1450},
    "EV-HD-004": {"vehicle_id": "EV-HD-004", "capacity_fade": 17.5, "cycle_count": 780, "state_of_health": 83.0, "remaining_useful_life": 430},
}

@router.get("/battery/status", response_model=BatteryHealthResponse)
async def get_battery_status(
    vehicle_id: str = Query(..., description="ID of the EV vehicle asset"),
    session: AsyncSession = Depends(get_db_session)
):
    from app.services.ml import get_battery_predictor, prepare_features_from_records
    
    # 1. Fetch latest 20 database entries to compile history for rolling features
    stmt = select(BatteryRecord).where(BatteryRecord.vehicle_id == vehicle_id).order_by(BatteryRecord.timestamp.desc()).limit(20)
    result = await session.execute(stmt)
    records = result.scalars().all()
    
    if records:
        features = prepare_features_from_records(records)
        predictor = get_battery_predictor()
        
        soh_res = predictor.predict_soh(features)
        rul_res = predictor.predict_rul(features)
        
        return {
            "vehicle_id": vehicle_id,
            "capacity_fade": round(120.0 - features['capacity_ah'], 2),
            "cycle_count": int(features['cycle']),
            "state_of_health": soh_res['soh_percent'],
            "remaining_useful_life": int(rul_res['rul_cycles'])
        }
        
    # 2. Fallback to mock data if no DB records found
    if vehicle_id in MOCK_BATTERY_HEALTH:
        return MOCK_BATTERY_HEALTH[vehicle_id]
        
    raise HTTPException(status_code=404, detail="Battery status not found for vehicle")

@router.post("/predict/rul")
def predict_rul(payload: dict):
    from app.services.ml import get_battery_predictor, prepare_features_from_records
    features = prepare_features_from_records([], payload)
    predictor = get_battery_predictor()
    res = predictor.predict_rul(features)
    return {
        "predicted_rul_cycles": int(res['rul_cycles']),
        "confidence_interval": [max(0, int(res['rul_cycles']) - 50), int(res['rul_cycles']) + 50],
        "model_version": "xgboost-battery-rul-v1.0",
        "urgency": res['urgency'],
        "action": res['action']
    }

@router.post("/predict/soh")
def predict_soh(payload: dict):
    from app.services.ml import get_battery_predictor, prepare_features_from_records
    features = prepare_features_from_records([], payload)
    predictor = get_battery_predictor()
    res = predictor.predict_soh(features)
    return {
        "state_of_health": res['soh_percent'],
        "capacity_fade_ah": round(120.0 - features['capacity_ah'], 2),
        "health_status": res['health_status'],
        "recommendation": res['recommendation'],
        "model_version": "xgboost-battery-soh-v1.0"
    }

@router.post("/predict/anomaly")
def predict_anomaly(payload: dict):
    from app.services.ml import get_anomaly_detector, prepare_features_from_records
    features = prepare_features_from_records([], payload)
    detector = get_anomaly_detector()
    res = detector.predict(features)
    return {
        "is_anomaly": res['is_anomaly'],
        "anomaly_score": res['anomaly_score'],
        "severity": res['severity'],
        "anomaly_types": res['anomaly_types'],
        "alerts": res['alerts'],
        "recommendations": res['recommendations'],
        "model_version": "isolation-forest-anomaly-v1.0"
    }

@router.websocket("/telemetry/ws/{vehicle_id}")
async def websocket_endpoint(websocket: WebSocket, vehicle_id: str):
    await websocket.accept()
    try:
        while True:
            data = {
                "vehicle_id": vehicle_id,
                "timestamp": str(asyncio.get_event_loop().time()),
                "voltage": round(random.uniform(370, 410), 2),
                "current": round(random.uniform(-50, 50), 2),
                "temperature": round(random.uniform(30, 48), 2),
                "soc": round(random.uniform(20, 99), 1)
              }
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        pass
