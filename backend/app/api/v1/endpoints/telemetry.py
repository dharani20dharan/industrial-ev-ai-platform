import sys
import os
import datetime
import json
import asyncio
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

try:
    from ml.simulator.controller_server import simulator_engine
except ImportError:
    ML_DIR = os.path.join(PROJECT_ROOT, "ml")
    if ML_DIR not in sys.path:
        sys.path.insert(0, ML_DIR)
    from simulator.controller_server import simulator_engine

logger = logging.getLogger("app.streaming.processor.telemetry")
router = APIRouter()


@router.websocket("/telemetry/live")
async def get_live_telemetry_websocket(websocket: WebSocket):
    await websocket.accept()
    logger.info("Live telemetry matrix stream connection initialized.")
    
    # Auto-start simulator engine if dormant
    if not simulator_engine.running:
        simulator_engine.start()

    try:
        while True:
            vehicles = simulator_engine.fleet_manager.get_all_vehicles()
            if not vehicles:
                await websocket.send_text(json.dumps({"type": "HEARTBEAT", "active_vehicles": 0}))
            else:
                for v in vehicles:
                    frame = simulator_engine.latest_telemetry.get(v.vehicle_id)
                    if not frame:
                        frame = {
                            "vehicle_id": v.vehicle_id,
                            "fleet_id": v.fleet_id,
                            "profile_name": v.profile_name,
                            "vehicle_type": v.physics.vehicle_type,
                            "speed_kph": round(v.physics.speed_kph, 1),
                            "speed": round(v.physics.speed_kph, 1),
                            "soc": round(v.physics.soc, 1),
                            "soh": round(v.physics.soh, 1),
                            "voltage": round(v.physics.nominal_voltage * (0.85 + 0.15 * (v.physics.soc / 100.0)), 1),
                            "current_amps": round(v.physics.torque_nm * 0.1, 1),
                            "motor_temperature_c": round(v.physics.motor_temperature, 1),
                            "cell_temp": round(v.physics.cell_temperature, 1),
                            "status": v.physics.driving_state,
                            "driving_state": v.physics.driving_state,
                            "is_charging": v.physics.is_charging,
                            "is_moving": v.physics.is_moving,
                            "latitude": round(v.gps_engine.latitude, 6),
                            "longitude": round(v.gps_engine.longitude, 6),
                            "heading": round(v.gps_engine.heading_deg, 1),
                            "heading_deg": round(v.gps_engine.heading_deg, 1),
                            "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
                        }
                    await websocket.send_text(json.dumps(frame))

            await asyncio.sleep(1.0)

    except WebSocketDisconnect:
        logger.info("Client disconnected cleanly from live telemetry matrix stream.")
    except Exception as e:
        logger.error(f"Stream exception intercepted: {str(e)}")
    finally:
        try:
            await websocket.close()
        except Exception:
            pass
