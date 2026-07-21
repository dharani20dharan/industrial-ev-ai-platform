"""
Simulator Controller API & Runtime Engine Server
================================================
Provides a REST and WebSocket control panel server for runtime simulator operations:
- Dynamic vehicle/fleet spawning and despawning
- Pause / Resume / Stop / Reset simulation
- Speed multiplier (1x, 2x, 5x, 10x) & telemetry publish rate adjustments
- Preset scenario applications (Small, Medium, Large, Enterprise, Rush Hour, Depot Charging)
- Live streaming analytics, vehicle inspector details, and event log WebSocket
"""

import asyncio
import json
import time
import threading
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

from .fleet_manager import FleetManager
from .profiles import DRIVING_PROFILES

logger = logging.getLogger("simulator_controller")


class SimulatorControllerEngine:
    """Singleton simulation manager executing background telemetry generation and MQTT publishing."""

    def __init__(self):
        self.fleet_manager = FleetManager()
        self.running = False
        self.paused = False
        
        # Runtime settings
        self.publish_interval = 2.0  # seconds
        self.speed_multiplier = 1.0  # 1x, 2x, 5x, 10x
        self.enable_events = True
        self.enable_charging = True
        self.enable_regen = True
        self.output_mode = "mqtt"
        
        # MQTT Client setup
        self.mqtt_host = "localhost"
        self.mqtt_port = 1883
        self.mqtt_client = None
        self._loop_thread = None
        
        # Metrics tracking
        self.start_time = None
        self.messages_sent = 0
        self.messages_per_second = 0.0
        self.event_logs: List[Dict[str, Any]] = []
        self._last_metrics_calc = time.time()
        self._msg_counter_interval = 0
        
        # WebSockets listeners
        self.ws_clients = set()

        # Latest telemetry frame buffer per vehicle
        self.latest_telemetry: Dict[str, Dict[str, Any]] = {}

        # Seed initial fleet (10 vehicles)
        self.fleet_manager.spawn_vehicles(count=10, profile_name="DELIVERY", fleet_id="FLT-ALPHA-01")
        self.add_event_log("SYSTEM", "Initialized default simulator with 10 active vehicles.")

    def add_event_log(self, event_type: str, message: str, vehicle_id: Optional[str] = None):
        """Pushes event log to internal buffer and broadcasts over WebSocket."""
        event_obj = {
            "id": f"evt-{len(self.event_logs) + 1}",
            "timestamp": datetime.utcnow().strftime("%H:%M:%S"),
            "event_type": event_type,
            "message": message,
            "vehicle_id": vehicle_id
        }
        self.event_logs.append(event_obj)
        if len(self.event_logs) > 200:
            self.event_logs.pop(0)

    def setup_mqtt(self, host: str = "localhost", port: int = 1883) -> bool:
        self.mqtt_host = host
        self.mqtt_port = port
        try:
            self.mqtt_client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
            self.mqtt_client.connect(self.mqtt_host, self.mqtt_port, 60)
            self.mqtt_client.loop_start()
            logger.info(f"Connected to MQTT broker at {host}:{port}")
            self.add_event_log("MQTT", f"Connected to MQTT Broker at {host}:{port}")
            return True
        except Exception as e:
            logger.warning(f"Failed to connect to MQTT broker ({e}). Falling back to console logging.")
            self.output_mode = "console"
            self.add_event_log("MQTT_WARN", f"MQTT connection failed ({e}). Operating in standalone mode.")
            return False

    def start(self):
        """Starts the background telemetry loop."""
        if not self.running:
            self.running = True
            self.paused = False
            self.start_time = time.time()
            if self.mqtt_client is None and self.output_mode == "mqtt":
                self.setup_mqtt(self.mqtt_host, self.mqtt_port)
            self._loop_thread = threading.Thread(target=self._run_loop, daemon=True)
            self._loop_thread.start()
            self.add_event_log("SIMULATOR_START", "Simulation loop started.")

    def pause(self):
        self.paused = True
        self.add_event_log("SIMULATOR_PAUSE", "Simulation paused.")

    def resume(self):
        self.paused = False
        self.add_event_log("SIMULATOR_RESUME", "Simulation resumed.")

    def stop(self):
        self.running = False
        self.paused = False
        self.add_event_log("SIMULATOR_STOP", "Simulation stopped.")

    def reset(self):
        self.stop()
        self.fleet_manager.clear()
        self.latest_telemetry.clear()
        self.messages_sent = 0
        self.event_logs.clear()
        self.fleet_manager.spawn_vehicles(count=10, profile_name="DELIVERY", fleet_id="FLT-ALPHA-01")
        self.add_event_log("SIMULATOR_RESET", "Simulation reset to default 10 vehicles.")
        self.start()

    def update_config(self, config_dict: Dict[str, Any]):
        """Updates simulation parameters live at runtime."""
        if "publish_interval" in config_dict:
            self.publish_interval = max(0.2, float(config_dict["publish_interval"]))
        if "speed_multiplier" in config_dict:
            self.speed_multiplier = max(0.5, float(config_dict["speed_multiplier"]))
        if "enable_events" in config_dict:
            self.enable_events = bool(config_dict["enable_events"])
        if "enable_charging" in config_dict:
            self.enable_charging = bool(config_dict["enable_charging"])
        if "enable_regen" in config_dict:
            self.enable_regen = bool(config_dict["enable_regen"])
        
        self.add_event_log("CONFIG_CHANGE", f"Updated runtime settings: {config_dict}")

    def apply_scenario(self, scenario_name: str):
        """Applies predefined demonstration scenarios."""
        name = scenario_name.upper().strip()
        self.fleet_manager.clear()
        self.latest_telemetry.clear()

        if name == "SMALL":
            self.fleet_manager.spawn_vehicles(count=10, profile_name="DELIVERY", fleet_id="FLT-SMALL-ALPHA")
            self.speed_multiplier = 1.0
            
        elif name == "MEDIUM":
            self.fleet_manager.spawn_vehicles(count=30, profile_name="URBAN", fleet_id="FLT-URBAN-FLEET")
            self.fleet_manager.spawn_vehicles(count=20, profile_name="DELIVERY", fleet_id="FLT-DELIVERY-FLEET")
            self.speed_multiplier = 1.0

        elif name == "LARGE":
            self.fleet_manager.spawn_vehicles(count=40, profile_name="URBAN", fleet_id="FLT-URBAN-NORTH")
            self.fleet_manager.spawn_vehicles(count=40, profile_name="HIGHWAY", fleet_id="FLT-HIGHWAY-CORRIDOR")
            self.fleet_manager.spawn_vehicles(count=20, profile_name="CHARGING", fleet_id="FLT-DEPOT-CHARGING")
            self.speed_multiplier = 2.0

        elif name == "ENTERPRISE":
            self.fleet_manager.spawn_vehicles(count=200, profile_name="URBAN", fleet_id="FLT-URBAN-METRO")
            self.fleet_manager.spawn_vehicles(count=150, profile_name="DELIVERY", fleet_id="FLT-LOGISTICS-HUB")
            self.fleet_manager.spawn_vehicles(count=100, profile_name="HIGHWAY", fleet_id="FLT-INTERSTATE-CARGO")
            self.fleet_manager.spawn_vehicles(count=50, profile_name="INDUSTRIAL", fleet_id="FLT-PORT-YARD")
            self.speed_multiplier = 5.0

        elif name == "RUSH_HOUR":
            self.fleet_manager.spawn_vehicles(count=40, profile_name="URBAN", fleet_id="FLT-URBAN-PEAK")
            self.fleet_manager.spawn_vehicles(count=30, profile_name="DELIVERY", fleet_id="FLT-EXPRESS-DELIVERY")
            self.speed_multiplier = 2.0

        elif name == "DEPOT_CHARGING":
            self.fleet_manager.spawn_vehicles(count=30, profile_name="CHARGING", fleet_id="FLT-FAST-CHARGERS")
            self.fleet_manager.spawn_vehicles(count=10, profile_name="IDLE", fleet_id="FLT-DEPOT-QUEUE")
            self.speed_multiplier = 1.0

        elif name == "HEAVY_INDUSTRIAL":
            self.fleet_manager.spawn_vehicles(count=50, profile_name="INDUSTRIAL", fleet_id="FLT-PORT-CONTAINER")
            self.speed_multiplier = 1.0

        if not self.running:
            self.start()

        self.add_event_log("SCENARIO_APPLIED", f"Applied scenario '{scenario_name}' with {len(self.fleet_manager.vehicles)} active vehicles.")

    def _publish_telemetry_frame(self, frame: Dict[str, Any]):
        """Publishes individual telemetry frame across MQTT topics."""
        vehicle_id = frame["vehicle_id"]

        if self.mqtt_client and self.output_mode == "mqtt":
            # 1. Battery payload
            self.mqtt_client.publish(f"ev/battery/{vehicle_id}", json.dumps(frame["battery"]))
            # 2. Telemetry payload
            self.mqtt_client.publish(f"ev/telemetry/{vehicle_id}", json.dumps(frame["telemetry"]))
            # 3. Location payload
            self.mqtt_client.publish(f"ev/location/{vehicle_id}", json.dumps(frame["location"]))
            # 4. Charging payload
            self.mqtt_client.publish(f"ev/charging/{vehicle_id}", json.dumps(frame["charging"]))
            # 5. Status payload
            status_payload = frame.get("status_details") or {"operational_status": frame.get("status", "IDLE")}
            self.mqtt_client.publish(f"ev/status/{vehicle_id}", json.dumps(status_payload))

            if frame["anomaly"]["detected"]:
                alert_payload = {
                    "vehicle_id": vehicle_id,
                    "timestamp": frame["timestamp"],
                    "alert_code": frame["anomaly"]["type"],
                    "severity": "CRITICAL" if frame["anomaly"]["severity"] > 0.8 else "WARNING",
                    "component": "BATTERY_MANAGEMENT",
                    "description": f"Automated anomaly detection triggered for {vehicle_id}"
                }
                self.mqtt_client.publish(f"ev/alerts/{vehicle_id}", json.dumps(alert_payload))
                self.add_event_log("ANOMALY", f"Vehicle {vehicle_id} fault: {frame['anomaly']['type']}", vehicle_id)

            self.messages_sent += 5
            self._msg_counter_interval += 5

    def _run_loop(self):
        """Background execution loop producing continuous telemetry frames."""
        while self.running:
            try:
                if not self.paused:
                    vehicles = self.fleet_manager.get_all_vehicles()
                    
                    for veh in vehicles:
                        try:
                            frame = veh.tick(
                                dt_seconds=self.publish_interval,
                                speed_multiplier=self.speed_multiplier,
                                enable_charging=self.enable_charging,
                                enable_regen=self.enable_regen,
                                enable_events=self.enable_events
                            )
                            self.latest_telemetry[veh.vehicle_id] = frame
                            self._publish_telemetry_frame(frame)
                        except Exception as ve:
                            logger.error(f"Error ticking vehicle {veh.vehicle_id}: {ve}")

                    # Update message rate metrics
                    now = time.time()
                    elapsed = now - self._last_metrics_calc
                    if elapsed >= 1.0:
                        self.messages_per_second = round(self._msg_counter_interval / elapsed, 1)
                        self._msg_counter_interval = 0
                        self._last_metrics_calc = now

            except Exception as e:
                logger.error(f"Simulation loop error: {e}")

            sleep_dur = max(0.2, self.publish_interval / max(1.0, self.speed_multiplier))
            time.sleep(sleep_dur)

    def get_full_status(self) -> Dict[str, Any]:
        """Returns full metrics and breakdown for Simulation Controller Dashboard."""
        summary = self.fleet_manager.get_summary()
        uptime = int(time.time() - self.start_time) if self.start_time and self.running else 0

        return {
            "status": "RUNNING" if (self.running and not self.paused) else ("PAUSED" if self.paused else "STOPPED"),
            "uptime_seconds": uptime,
            "publish_interval": self.publish_interval,
            "speed_multiplier": self.speed_multiplier,
            "enable_events": self.enable_events,
            "enable_charging": self.enable_charging,
            "enable_regen": self.enable_regen,
            "messages_sent": self.messages_sent,
            "messages_per_second": self.messages_per_second,
            "active_vehicles": summary["total_vehicles"],
            "active_fleets": summary["total_fleets"],
            "charging_count": summary["charging_count"],
            "moving_count": summary["moving_count"],
            "idle_count": summary["idle_count"],
            "fault_count": summary["fault_count"],
            "avg_soc": summary["avg_soc"],
            "avg_temp": summary["avg_temp"],
            "avg_speed": summary["avg_speed"],
            "fleet_breakdown": summary["fleets"],
            "recent_events": self.event_logs[-15:]
        }


# Global singleton controller instance
simulator_engine = SimulatorControllerEngine()
