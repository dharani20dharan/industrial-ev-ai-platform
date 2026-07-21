import sys
import os
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field

# Ensure ML package is resolvable from backend context
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

try:
    from ml.simulator.controller_server import simulator_engine
except ImportError:
    # Direct import fallback
    ML_DIR = os.path.join(PROJECT_ROOT, "ml")
    if ML_DIR not in sys.path:
        sys.path.insert(0, ML_DIR)
    from simulator.controller_server import simulator_engine

router = APIRouter(prefix="/simulator", tags=["Simulator Control Panel"])


# Pydantic Schemas
class SpawnVehiclesRequest(BaseModel):
    count: int = Field(default=10, ge=1, le=1000)
    profile_name: str = Field(default="DELIVERY")
    fleet_id: str = Field(default="FLT-ALPHA-01")

class SpawnFleetRequest(BaseModel):
    fleet_name: str = Field(default="Delivery Fleet A")
    fleet_type: str = Field(default="DELIVERY")
    count: int = Field(default=20, ge=1, le=1000)
    profile_name: str = Field(default="DELIVERY")

class DespawnVehiclesRequest(BaseModel):
    vehicle_ids: List[str]

class ConfigUpdateRequest(BaseModel):
    publish_interval: Optional[float] = None
    speed_multiplier: Optional[float] = None
    enable_events: Optional[bool] = None
    enable_charging: Optional[bool] = None
    enable_regen: Optional[bool] = None

class ScenarioApplyRequest(BaseModel):
    scenario_name: str = Field(default="MEDIUM")


@router.get("/status")
async def get_simulator_status():
    """Returns real-time status and operational metrics for the simulation engine."""
    return simulator_engine.get_full_status()


@router.post("/start")
async def start_simulator():
    simulator_engine.start()
    return {"status": "SUCCESS", "message": "Simulation started successfully."}


@router.post("/pause")
async def pause_simulator():
    simulator_engine.pause()
    return {"status": "SUCCESS", "message": "Simulation paused."}


@router.post("/resume")
async def resume_simulator():
    simulator_engine.resume()
    return {"status": "SUCCESS", "message": "Simulation resumed."}


@router.post("/stop")
async def stop_simulator():
    simulator_engine.stop()
    return {"status": "SUCCESS", "message": "Simulation stopped."}


@router.post("/reset")
async def reset_simulator():
    simulator_engine.reset()
    return {"status": "SUCCESS", "message": "Simulation reset to default 10 vehicles."}


@router.post("/vehicles/spawn")
async def spawn_vehicles(req: SpawnVehiclesRequest):
    new_ids = simulator_engine.fleet_manager.spawn_vehicles(
        count=req.count,
        profile_name=req.profile_name,
        fleet_id=req.fleet_id
    )
    simulator_engine.add_event_log("SPAWN", f"Spawned {len(new_ids)} vehicles under fleet {req.fleet_id}.")
    return {
        "status": "SUCCESS",
        "spawned_count": len(new_ids),
        "vehicle_ids": new_ids,
        "total_active_vehicles": len(simulator_engine.fleet_manager.vehicles)
    }


@router.post("/fleets/spawn")
async def spawn_fleet(req: SpawnFleetRequest):
    fleet_id = simulator_engine.fleet_manager.spawn_fleet(
        fleet_name=req.fleet_name,
        fleet_type=req.fleet_type,
        count=req.count,
        profile_name=req.profile_name
    )
    simulator_engine.add_event_log("SPAWN_FLEET", f"Spawned new fleet '{req.fleet_name}' ({fleet_id}) with {req.count} vehicles.")
    return {
        "status": "SUCCESS",
        "fleet_id": fleet_id,
        "spawned_count": req.count,
        "total_active_vehicles": len(simulator_engine.fleet_manager.vehicles)
    }


@router.post("/vehicles/despawn")
async def despawn_vehicles(req: DespawnVehiclesRequest):
    removed_count = simulator_engine.fleet_manager.despawn_vehicles(req.vehicle_ids)
    simulator_engine.add_event_log("DESPAWN", f"Despawned {removed_count} vehicles.")
    return {
        "status": "SUCCESS",
        "removed_count": removed_count,
        "total_active_vehicles": len(simulator_engine.fleet_manager.vehicles)
    }


@router.patch("/config")
async def update_simulator_config(req: ConfigUpdateRequest):
    update_data = req.model_dump(exclude_unset=True)
    simulator_engine.update_config(update_data)
    return {"status": "SUCCESS", "updated_config": update_data}


@router.post("/scenarios/apply")
async def apply_scenario(req: ScenarioApplyRequest):
    simulator_engine.apply_scenario(req.scenario_name)
    return {
        "status": "SUCCESS",
        "scenario": req.scenario_name,
        "active_vehicles": len(simulator_engine.fleet_manager.vehicles)
    }


@router.get("/vehicles")
async def list_simulated_vehicles():
    """Lists summary of all currently active simulated vehicles."""
    vehicles = simulator_engine.fleet_manager.get_all_vehicles()
    results = []
    for v in vehicles:
        results.append({
            "vehicle_id": v.vehicle_id,
            "fleet_id": v.fleet_id,
            "profile_name": v.profile_name,
            "speed_kph": round(v.physics.speed_kph, 1),
            "soc": round(v.physics.soc, 1),
            "cell_temp": round(v.physics.cell_temperature, 1),
            "voltage": round(v.physics.nominal_voltage * (0.85 + 0.15 * (v.physics.soc / 100.0)), 1),
            "is_charging": v.physics.is_charging,
            "is_moving": v.physics.is_moving,
            "driving_state": v.physics.driving_state,
            "latitude": round(v.gps_engine.latitude, 6),
            "longitude": round(v.gps_engine.longitude, 6)
        })
    return {"total": len(results), "vehicles": results}


@router.get("/vehicles/{vehicle_id}")
async def inspect_vehicle(vehicle_id: str):
    """Detailed physics and GPS inspection for a single vehicle."""
    with simulator_engine.fleet_manager.lock:
        if vehicle_id not in simulator_engine.fleet_manager.vehicles:
            raise HTTPException(status_code=404, detail="Simulated vehicle not found.")
        v = simulator_engine.fleet_manager.vehicles[vehicle_id]
        
    return {
        "vehicle_id": v.vehicle_id,
        "fleet_id": v.fleet_id,
        "profile_name": v.profile_name,
        "driving_state": v.physics.driving_state,
        "soc": round(v.physics.soc, 2),
        "soh": round(v.physics.soh, 2),
        "speed_kph": round(v.physics.speed_kph, 1),
        "acceleration_m_s2": v.physics.acceleration_m_s2,
        "odometer_km": round(v.physics.odometer_km, 1),
        "torque_nm": v.physics.torque_nm,
        "cell_temperature": round(v.physics.cell_temperature, 1),
        "motor_temperature": round(v.physics.motor_temperature, 1),
        "ambient_temp": round(v.physics.ambient_temp, 1),
        "internal_resistance": v.physics.internal_resistance,
        "battery_age_cycles": v.physics.battery_age_cycles,
        "is_charging": v.physics.is_charging,
        "charging_rate_kw": v.physics.charging_rate_kw,
        "charger_id": v.physics.charger_id,
        "total_energy_consumed_kwh": round(v.physics.total_energy_consumed_kwh, 2),
        "total_energy_regenerated_kwh": round(v.physics.total_energy_regenerated_kwh, 2),
        "latitude": round(v.gps_engine.latitude, 6),
        "longitude": round(v.gps_engine.longitude, 6),
        "altitude_m": v.gps_engine.altitude_m,
        "heading_deg": v.gps_engine.heading_deg,
        "active_anomaly": v.physics.active_anomaly
    }
