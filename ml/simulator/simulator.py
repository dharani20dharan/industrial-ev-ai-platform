import time
import json
import random
import argparse
import logging
import os
from datetime import datetime, timezone

# Configure logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("simulator")

try:
    import paho.mqtt.client as mqtt
except ImportError:
    logger.warning("paho-mqtt not installed. Run 'pip install paho-mqtt'")
    mqtt = None

VEHICLE_IDS = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]

class TelemetrySimulator:
    def __init__(self, broker_address="localhost", broker_port=1883):
        self.broker = broker_address
        self.port = broker_port
        self.client = None

        # Tracking state vectors for physics modeling
        self.states = {
            vid: {
                "soc": random.uniform(50, 95),
                "temperature": random.uniform(28, 35),
                "voltage": 400.0,
                "cycles": random.randint(100, 500),
                # GPS path initial tracking coordinates (Thiruporur region)
                "lat": 12.7040 + random.uniform(-0.01, 0.01),
                "lon": 80.1930 + random.uniform(-0.01, 0.01),
                "odometer": random.uniform(12000.0, 25000.0),
                "uptime": 0
            } for vid in VEHICLE_IDS
        }

    def connect(self):
        if mqtt is None:
            logger.warning("Simulator starting in dry-run mode (MQTT packages missing).")
            return False

        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2 if hasattr(mqtt, 'CallbackAPIVersion') else None)
        try:
            self.client.connect(self.broker, self.port, 60)
            logger.info(f"Connected to Mosquitto MQTT Broker at {self.broker}:{self.port}")
            self.client.loop_start()
            return True
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}. Defaulting to terminal log.")
            self.client = None
            return False

    def simulate_step(self):
        for vid in VEHICLE_IDS:
            state = self.states[vid]
            state["uptime"] += 1
            timestamp_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            
            # --- Simulated Physics Calculation Tier ---
            is_charging = (vid == "EV-HD-002")
            
            if is_charging:
                state["soc"] = min(100.0, state["soc"] + random.uniform(0.1, 0.4))
                current_amps = random.uniform(-60.0, -20.0)  # Negative denotes absorption
                voltage = 380 + (state["soc"] * 0.3)
                state["temperature"] = min(50.0, state["temperature"] + random.uniform(-0.1, 0.3))
                speed_kph = 0.0
                torque_nm = 0.0
                inverter_efficiency = 0.98
            else:
                state["soc"] = max(10.0, state["soc"] - random.uniform(0.05, 0.2))
                current_amps = random.uniform(10.0, 45.0)   # Positive denotes discharge
                voltage = 400 - ((100 - state["soc"]) * 0.3)
                state["temperature"] = max(25.0, state["temperature"] + random.uniform(-0.2, 0.2))
                speed_kph = round(random.uniform(40.0, 90.0), 2)
                torque_nm = round(random.uniform(120.0, 350.0), 1)
                inverter_efficiency = round(random.uniform(0.91, 0.96), 3)
                # Increment continuous spatial tracking attributes
                state["odometer"] += (speed_kph / 3600.0)
                state["lat"] += random.uniform(-0.0001, 0.0001)
                state["lon"] += random.uniform(-0.0001, 0.0001)

            # Simulated Thermal Anomaly Spike Injector
            if vid == "EV-HD-004" and random.random() < 0.10:
                state["temperature"] += random.uniform(5.0, 12.0)
                logger.warning(f"Thermal boundary breakdown simulation on {vid}")

            # 1. Kinematics Stream (`ev/telemetry`)
            telemetry_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "speed_kph": speed_kph,
                "odometer_km": round(state["odometer"], 2),
                "motor_temperature_c": round(state["temperature"] * 1.1, 1),
                "torque_nm": torque_nm,
                "inverter_efficiency": inverter_efficiency
            }

            # 2. Electro-Chemical Stream (`ev/battery`)
            battery_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "state_of_charge_pct": round(float(state["soc"]), 1),
                "state_of_health_pct": round(98.5 - (state["uptime"] * 0.0001), 2),
                "voltage": round(float(voltage), 2),
                "current_amps": round(float(current_amps), 2),
                "cell_temperature_max_c": round(float(state["temperature"]), 2),
                "internal_resistance_ohm": round(0.012 + (state["uptime"] * 0.000001), 6)
            }

            # 3. Geospatial Stream (`ev/location`)
            location_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "latitude": round(state["lat"], 6),
                "longitude": round(state["lon"], 6),
                "altitude_m": 24.5,
                "heading_deg": random.randint(0, 359),
                "gps_fix_quality": "3D_FIX"
            }

            # 4. Energy Grid Coupling Stream (`ev/charging`)
            charging_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "charger_id": "CHG-TPI-99" if is_charging else None,
                "charging_rate_kw": round(abs(voltage * current_amps) / 1000.0, 2) if is_charging else 0.0,
                "time_to_full_mins": int((100.0 - state["soc"]) * 1.5) if is_charging else 0,
                "connector_type": "CCS_TYPE_2" if is_charging else "NONE"
            }

            # 5. Core Operational Status Stream (`ev/status`)
            status_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "operational_status": "CHARGING" if is_charging else "ACTIVE_DRIVE",
                "active_error_codes": ["ERR_CELL_OVERTEMP"] if state["temperature"] > 48.0 else [],
                "driver_id": f"DRV-{vid[-3:]}"
            }

            # 6. High-Priority Alert Engine (`ev/alerts`)
            alert_payload = None
            if state["temperature"] > 48.0:
                alert_payload = {
                    "vehicle_id": vid,
                    "timestamp": timestamp_str,
                    "alert_code": "ALT_THERMAL_CRITICAL",
                    "severity": "CRITICAL",
                    "component": "BATTERY_PACK_A",
                    "description": f"Core cell temperature hit critical boundary limit: {round(state['temperature'], 2)}C"
                }

            # 7. Diagnostic Diagnostics Base (`ev/heartbeat`)
            heartbeat_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "uptime_seconds": state["uptime"],
                "firmware_version": "v2.4.11-prod",
                "signal_strength_dbm": random.randint(-75, -45)
            }

            # --- Unified Non-Blocking Network Pipeline Transmission ---
            if self.client:
                self.client.publish("ev/telemetry", json.dumps(telemetry_payload), qos=1)
                self.client.publish("ev/battery", json.dumps(battery_payload), qos=1)
                self.client.publish("ev/location", json.dumps(location_payload), qos=1)
                self.client.publish("ev/charging", json.dumps(charging_payload), qos=1)
                self.client.publish("ev/status", json.dumps(status_payload), qos=1)
                self.client.publish("ev/heartbeat", json.dumps(heartbeat_payload), qos=1)
                if alert_payload:
                    self.client.publish("ev/alerts", json.dumps(alert_payload), qos=1)
            else:
                logger.debug(f"[DRY-RUN LOG] Emitting 7 contract streams for {vid}")

    def run(self, interval=1.0):
        logger.info("Starting 7-Channel Enterprise EV Telemetry Simulation loop. Press Ctrl+C to terminate.")
        try:
            while True:
                self.simulate_step()
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("Simulation terminated.")
            if self.client:
                self.client.loop_stop()
                self.client.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enterprise EV Telemetry Multi-Stream Simulator")
    parser.add_argument("--host", default="localhost", help="MQTT Broker host")
    parser.add_argument("--port", type=int, default=1883, help="MQTT Broker port")
    parser.add_argument("--interval", type=float, default=1.0, help="Stream tick interval in seconds")
    args = parser.parse_args()

    sim = TelemetrySimulator(args.host, args.port)
    sim.connect()
    sim.run(args.interval)