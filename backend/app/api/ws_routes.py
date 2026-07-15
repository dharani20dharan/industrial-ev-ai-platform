# import logging
# from fastapi import APIRouter, WebSocket, WebSocketDisconnect
# from app.streaming.websocket.manager import ws_manager

# logger = logging.getLogger(__name__)
# router = APIRouter()

# @router.websocket("/ws/dashboard")
# async def dashboard_websocket_endpoint(websocket: WebSocket) -> None:
#     """
#     WebSocket endpoint for the React frontend.
#     Expects incoming JSON commands: {"action": "subscribe", "topic": "telemetry.raw"}
#     """
#     await ws_manager.connect(websocket)
    
#     try:
#         while True:
#             # Wait for control commands from the client
#             data = await websocket.receive_json()
#             action = data.get("action")
#             topic = data.get("topic")
            
#             if action == "subscribe" and topic:
#                 await ws_manager.subscribe(websocket, topic)
#             elif action == "unsubscribe" and topic:
#                 await ws_manager.unsubscribe(websocket, topic)
                
#     except WebSocketDisconnect:
#         ws_manager.disconnect(websocket)
#     except Exception as e:
#         logger.error("WebSocket connection error.", exc_info=True)
#         ws_manager.disconnect(websocket)

import logging
import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.streaming.websocket.manager import ws_manager

logger = logging.getLogger(__name__)
router = APIRouter()

@router.websocket("/ws/dashboard")
async def dashboard_websocket_endpoint(websocket: WebSocket) -> None:
    """
    WebSocket endpoint for the React frontend.
    Logs traffic to the terminal for debugging without a UI.
    """
    await ws_manager.connect(websocket)
    logger.info("=== [TESTING] Terminal Client Connected to Dashboard Stream ===")
    
    try:
        while True:
            data = await websocket.receive_json()
            action = data.get("action")
            topic = data.get("topic")
            
            if action == "subscribe" and topic:
                await ws_manager.subscribe(websocket, topic)
                print(f"\n[SUBSCRIPTION] Client listening to Kafka topic: {topic}")
            elif action == "unsubscribe" and topic:
                await ws_manager.unsubscribe(websocket, topic)
                print(f"\n[UNSUBSCRIPTION] Client stopped listening to Kafka topic: {topic}")
                
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
        logger.info("=== [TESTING] Terminal Client Disconnected ===")
    except Exception as e:
        logger.error("WebSocket connection error.", exc_info=True)
        ws_manager.disconnect(websocket)