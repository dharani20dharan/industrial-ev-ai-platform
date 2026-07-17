from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import datetime
import json
import asyncio
import logging

logger = logging.getLogger("app.streaming.processor.telemetry")
router = APIRouter()

MOCK_VEHICLES = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]
MOCK_TELEMETRY = {
    "EV-HD-001": {"vehicle_id": "EV-HD-001", "voltage": 395.2, "current": 12.4, "temperature": 34.5, "soc": 88.0, "id": 1},
    "EV-HD-002": {"vehicle_id": "EV-HD-002", "voltage": 380.1, "current": -45.0, "temperature": 38.2, "soc": 42.0, "id": 2},
    "EV-HD-003": {"vehicle_id": "EV-HD-003", "voltage": 401.5, "current": 10.1, "temperature": 33.1, "soc": 91.0, "id": 3},
    "EV-HD-004": {"vehicle_id": "EV-HD-004", "voltage": 372.4, "current": 115.0, "temperature": 44.8, "soc": 76.0, "id": 4},
}

@router.websocket("/telemetry/live")
async def get_live_telemetry_websocket(websocket: WebSocket):
    await websocket.accept()
    logger.info("Live telemetry matrix stream connection initialized.")
    try:
        while True:
            for vehicle_id in MOCK_VEHICLES:
                # Use a fallback baseline to avoid missing key schema crashes
                raw_telemetry = MOCK_TELEMETRY.get(vehicle_id, {
                    "vehicle_id": vehicle_id, "voltage": 0.0, "current": 0.0, "temperature": 0.0, "soc": 0.0, "id": 0
                }).copy()

                # Format to adhere strictly to your TelemetryResponse schema fields
                payload = {
                    "id": raw_telemetry.get("id"),
                    "vehicle_id": raw_telemetry.get("vehicle_id"),
                    "voltage": float(raw_telemetry.get("voltage")),
                    "current": float(raw_telemetry.get("current")),
                    "temperature": float(raw_telemetry.get("temperature")),
                    "soc": float(raw_telemetry.get("soc")),
                    "timestamp": datetime.datetime.utcnow().isoformat()
                }

                await websocket.send_text(json.dumps(payload))

            # Keep heartbeat frequency high enough to prevent engine drops
            await asyncio.sleep(1.0)

    except WebSocketDisconnect:
        logger.info("Client disconnected cleanly from live telemetry matrix stream.")
    except Exception as e:
        logger.error(f"Stream exception intercepted: {str(e)}")
    finally:
        # Ensure socket state cleanly unmounts even during hard crashes
        try:
            await websocket.close()
        except Exception:
            pass
