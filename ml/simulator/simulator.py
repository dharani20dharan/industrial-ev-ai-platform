import time
import json
import random
import argparse
from datetime import datetime
import numpy as np

try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("Warning: paho-mqtt not installed. Run 'pip install paho-mqtt'")
    mqtt = None

VEHICLE_IDS = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "EV-HD-004"]

class TelemetrySimulator:
    def __init__(self, broker_address="localhost", broker_port=1883):
        self.broker = broker_address
        self.port = broker_port
        self.client = None
        
        # State profiles for vehicles: nominal capacity, current soc, temperature, cycle counts
        self.states = {
            vid: {
                "soc": random.uniform(50, 95),
                "temperature": random.uniform(28, 35),
                "voltage": 400.0,
                "cycles": random.randint(100, 500),
                "degradation_factor": random.uniform(0.01, 0.05)
            } for vid in VEHICLE_IDS
        }

    def connect(self):
        if mqtt is None:
            print("Simulator starting in dry-run mode (MQTT packages missing).")
            return False
            
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2 if hasattr(mqtt, 'CallbackAPIVersion') else None)
        try:
            self.client.connect(self.broker, self.port, 60)
            print(f"Connected to Mosquitto MQTT Broker at {self.broker}:{self.port}")
            self.client.loop_start()
            return True
        except Exception as e:
            print(f"Failed to connect to MQTT broker: {e}. Defaulting to terminal log.")
            self.client = None
            return False

    def simulate_step(self):
        for vid in VEHICLE_IDS:
            state = self.states[vid]
            
            # Simulate SOC dropping or raising based on current charging logic
            # Let's say vehicles are active (discharging)
            is_charging = vid == "EV-HD-002"
            
            if is_charging:
                state["soc"] = min(100.0, state["soc"] + random.uniform(0.1, 0.4))
                current = random.uniform(-60.0, -20.0)  # negative current represents charge
                voltage = 380 + (state["soc"] * 0.3)
                state["temperature"] = min(50.0, state["temperature"] + random.uniform(-0.1, 0.3))
            else:
                state["soc"] = max(10.0, state["soc"] - random.uniform(0.05, 0.2))
                current = random.uniform(10.0, 45.0)  # positive represents discharge
                voltage = 400 - ((100 - state["soc"]) * 0.3)
                state["temperature"] = max(25.0, state["temperature"] + random.uniform(-0.2, 0.2))

            # Simulate thermal anomaly on EV-HD-004
            if vid == "EV-HD-004" and random.random() < 0.15:
                state["temperature"] += random.uniform(2.0, 5.0)  # Thermal spike!
                print(f"[ANOMALY WARNING] Simulated thermal runaway surge on {vid}")

            # Battery degradation progression
            state["cycles"] += int(random.random() < 0.01) # incremental cycle increase
            
            payload = {
                "vehicle_id": vid,
                "timestamp": datetime.utcnow().isoformat(),
                "voltage": round(float(voltage), 2),
                "current": round(float(current), 2),
                "temperature": round(float(state["temperature"]), 2),
                "soc": round(float(state["soc"]), 1),
                "cycle_count": state["cycles"]
            }

            topic = f"ev/battery/{vid}"
            if self.client:
                self.client.publish(topic, json.dumps(payload))
            else:
                print(f"[SIMULATED STREAM] TOPIC: {topic} | DATA: {payload}")

    def run(self, interval=1.0):
        print("Starting EV Telemetry Simulation loop. Press Ctrl+C to terminate.")
        try:
            while True:
                self.simulate_step()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Simulation terminated.")
            if self.client:
                self.client.loop_stop()
                self.client.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EV Battery Telemetry Simulator")
    parser.add_argument("--host", default="localhost", help="MQTT Broker host")
    parser.add_argument("--port", type=int, default=1883, help="MQTT Broker port")
    parser.add_argument("--interval", type=float, default=1.0, help="Stream tick interval in seconds")
    args = parser.parse_args()

    sim = TelemetrySimulator(args.host, args.port)
    sim.connect()
    sim.run(args.interval)
