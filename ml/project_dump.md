# Project Dump

Project: ml

## Directory Tree

```text
ml
├── notebooks
│   └── README.md
├── project_dump.md
├── requirements.txt
├── simulator
│   └── simulator.py
└── src
    └── preprocessing.py
```

# File Contents

---

## project_dump.md

**[Empty File]**

---

## requirements.txt

```text
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.2.0
xgboost>=1.7.0
paho-mqtt>=1.6.0
faker>=19.0.0
jupyter>=1.0.0
```

---

## notebooks\README.md

```markdown
# AI/ML Engineering Notebooks

This folder is designated for exploratory data analysis (EDA), statistical tests, and machine learning model training notebooks (Member 3).

## Recommended Notebook Workflow

### 1. `01_exploratory_data_analysis.ipynb`
- Load and parse datasets: NASA Battery Dataset, Oxford Battery Dataset, NASA C-MAPSS.
- Telemetry profiling: Voltage, Current, Temperature, Capacity Fade, Cycle Count.
- Target derivation: Calculate remaining load cycles before cell capacity hits the 80% degradation threshold.

### 2. `02_model_training_and_evaluation.ipynb`
- Train XGBoost models for Remaining Useful Life (RUL) regression predictions.
- Train Isolation Forest models for real-time anomaly alerts (detecting thermal risks, cell voltage disparities, abnormal charging curves).
- Export trained model weights to production assets (`ml/models/`).
```

---

## simulator\simulator.py

```python
import time
import json
import random
import argparse
from datetime import datetime,timezone
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

            # --- Simulated Physics Engine Logic ---
            is_charging = vid == "EV-HD-002"

            if is_charging:
                state["soc"] = min(100.0, state["soc"] + random.uniform(0.1, 0.4))
                current = random.uniform(-60.0, -20.0)  # negative represents charge
                voltage = 380 + (state["soc"] * 0.3)
                state["temperature"] = min(50.0, state["temperature"] + random.uniform(-0.1, 0.3))
                speed = 0.0
                motor_rpm = 0
                power_output = round(float(voltage * current / 1000.0), 2)  # negative power during charge
            else:
                state["soc"] = max(10.0, state["soc"] - random.uniform(0.05, 0.2))
                current = random.uniform(10.0, 45.0)  # positive represents discharge
                voltage = 400 - ((100 - state["soc"]) * 0.3)
                state["temperature"] = max(25.0, state["temperature"] + random.uniform(-0.2, 0.2))
                speed = round(random.uniform(40.0, 90.0), 2)
                motor_rpm = int(speed * 50 + random.uniform(-100, 100))
                power_output = round(float(voltage * current / 1000.0), 2)

            if vid == "EV-HD-004" and random.random() < 0.15:
                state["temperature"] += random.uniform(2.0, 5.0)
                print(f"[ANOMALY WARNING] Simulated thermal runaway surge on {vid}")

            state["cycles"] += int(random.random() < 0.01)

            # ISO-8601 UTC timestamp format compliance string
            timestamp_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

            # --- Contract Payload 1: General EV Telemetry (Topic: ev/telemetry) ---
            telemetry_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "speed": speed,
                "odometer": round(15000.0 + (state["cycles"] * 2.5), 2),
                "motor_rpm": motor_rpm,
                "power_output": power_output,
                "ambient_temperature": round(random.uniform(20.0, 30.0), 1)
            }

            # --- Contract Payload 2: Battery Telemetry (Topic: ev/battery) ---
            battery_payload = {
                "vehicle_id": vid,
                "timestamp": timestamp_str,
                "soc": round(float(state["soc"]), 1),
                "soh": round(100.0 - (state["cycles"] * 0.015), 2),  # Degrades gradually over cycles
                "voltage": round(float(voltage), 2),
                "current": round(float(current), 2),
                "capacity": 75.0,  # Nominal capacity in kWh
                "cycle_count": state["cycles"],
                "internal_resistance": round(0.01 + (state["cycles"] * 0.00005), 5),
                "cell_temperature": round(float(state["temperature"]), 2)
            }

            # --- Publishing Engine Block ---
            if self.client:
                # Direct match to specifications using flat base paths
                self.client.publish("ev/telemetry", json.dumps(telemetry_payload), qos=1)
                self.client.publish("ev/battery", json.dumps(battery_payload), qos=1)
            else:
                print(f"[SIMULATED STREAM] TOPIC: ev/telemetry | DATA: {telemetry_payload}")
                print(f"[SIMULATED STREAM] TOPIC: ev/battery | DATA: {battery_payload}")

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
```

---

## src\preprocessing.py

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class TelemetryPreprocessor:
    def __init__(self):
        self.scaler = MinMaxScaler()
        
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handles null values in timeseries telemetry columns via forward/backward fill."""
        fill_cols = ["voltage", "current", "temperature", "soc"]
        df[fill_cols] = df[fill_cols].ffill().bfill()
        return df

    def filter_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Removes physical impossibilities or noise outliers from sensor readings."""
        # E.g., voltage must be positive, temperatures below extreme limits
        df = df[(df["voltage"] > 0) & (df["voltage"] < 1000)]
        df = df[(df["temperature"] > -40) & (df["temperature"] < 150)]
        return df

    def engineer_battery_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Engineers critical battery health predictors:
        - Capacity degradation
        - Thermal variance (rolling cell temp delta)
        - Average discharge slope (dV/dt)
        - Charging efficiency (energy absorbed per cycle)
        """
        # Ensure chronological ordering
        df = df.sort_values("timestamp")
        
        # 1. Thermal Variance
        df["temp_rolling_var"] = df["temperature"].rolling(window=10, min_periods=1).var()
        
        # 2. Discharge Slope (dV/dt)
        df["time_diff_sec"] = df["timestamp"].diff().dt.total_seconds()
        df["voltage_diff"] = df["voltage"].diff()
        
        # Calculate dV/dt, replacing division-by-zero with zero
        df["discharge_slope"] = np.where(
            df["time_diff_sec"] > 0, 
            df["voltage_diff"] / df["time_diff_sec"], 
            0.0
        )
        
        # 3. Capacity Fade approximation (Ah depletion integration)
        # Ah = current * time_hours
        df["current_hours"] = (df["current"] * (df["time_diff_sec"] / 3600.0)).abs()
        df["capacity_fade"] = df["current_hours"].cumsum()
        
        return df

    def scale_features(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """Scales numeric telemetry features for deep learning/regression models."""
        df[columns] = self.scaler.fit_transform(df[columns])
        return df
```
