"""
EV Telemetry Simulator
======================
Simulates real-time sensor data from a fleet of electric vehicles.
Generates battery telemetry, vehicle status, charging sessions, and anomalies.

Modes:
  - Console: Prints telemetry to stdout (default, no dependencies)
  - File: Writes to JSON files for batch processing
  - MQTT: Publishes to MQTT broker (requires Mosquitto/Member 4 setup)
"""

import numpy as np
import json
import time
import os
import sys
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import threading

# Try to import MQTT, but don't fail if not available
try:
    import paho.mqtt.client as mqtt
    MQTT_AVAILABLE = True
except ImportError:
    MQTT_AVAILABLE = False


class EVVehicle:
    """Simulates a single EV with realistic battery behavior."""
    
    def __init__(self, vehicle_id: str, battery_age_cycles: int = None):
        self.vehicle_id = vehicle_id
        self.battery_age_cycles = battery_age_cycles or np.random.randint(50, 600)
        
        # Battery characteristics
        self.initial_capacity = 75.0  # kWh (typical industrial EV)
        self.soh = max(65, 100 - (self.battery_age_cycles / 800) * 35 + np.random.normal(0, 2))
        self.soc = np.random.uniform(20, 95)  # Current charge level
        self.voltage_nominal = 400.0  # Volts (pack level)
        self.temperature = np.random.uniform(25, 35)
        
        # Vehicle state
        self.is_charging = False
        self.is_moving = np.random.choice([True, False], p=[0.7, 0.3])
        self.speed = np.random.uniform(30, 80) if self.is_moving else 0
        self.odometer = np.random.randint(10000, 100000)
        self.latitude = 28.6139 + np.random.uniform(-0.5, 0.5)  # Delhi area
        self.longitude = 77.2090 + np.random.uniform(-0.5, 0.5)
        
        # Internal resistance (increases with age)
        self.internal_resistance = 0.04 + (self.battery_age_cycles / 800) * 0.03
        
        # Anomaly probability increases with age
        self.anomaly_base_prob = 0.01 + (self.battery_age_cycles / 800) * 0.05
    
    def update(self, dt_seconds: float = 2.0) -> Dict:
        """Generate next telemetry reading."""
        
        # --- Update vehicle state ---
        # Randomly transition between driving/stopped/charging
        if np.random.random() < 0.02:  # 2% chance of state change
            if self.is_moving:
                self.is_moving = False
                self.speed = 0
                if self.soc < 30 and np.random.random() < 0.7:
                    self.is_charging = True
            elif self.is_charging:
                if self.soc > 85:
                    self.is_charging = False
                    self.is_moving = True
                    self.speed = np.random.uniform(30, 80)
            else:
                self.is_moving = True
                self.speed = np.random.uniform(30, 80)
        
        # --- Battery simulation ---
        # SoC changes
        if self.is_charging:
            # Charging: SoC increases (~50kW charger)
            charge_rate = 50.0 / self.initial_capacity * 100 / 3600 * dt_seconds  # %/second
            self.soc = min(100, self.soc + charge_rate + np.random.normal(0, 0.1))
            current = 125.0 + np.random.normal(0, 5)  # Positive = charging
        elif self.is_moving:
            # Driving: SoC decreases
            consumption = (0.2 + self.speed / 500) * dt_seconds / 3600 * 100  # % per dt
            self.soc = max(5, self.soc - consumption + np.random.normal(0, 0.05))
            current = -(80 + self.speed * 0.5 + np.random.normal(0, 10))  # Negative = discharging
        else:
            # Parked: minimal drain
            self.soc = max(5, self.soc - 0.001 + np.random.normal(0, 0.01))
            current = -0.5 + np.random.normal(0, 0.1)
        
        # Voltage (depends on SoC and load)
        voltage = self.voltage_nominal * (0.85 + 0.15 * (self.soc / 100))
        voltage += np.random.normal(0, 1.5)
        
        # Temperature (affected by current, ambient, and battery health)
        ambient_temp = 30 + np.random.normal(0, 2)
        heat_from_current = abs(current) * self.internal_resistance * 0.01
        self.temperature = 0.95 * self.temperature + 0.05 * (ambient_temp + heat_from_current)
        self.temperature += np.random.normal(0, 0.3)
        
        # Movement
        if self.is_moving:
            self.speed += np.random.normal(0, 2)
            self.speed = max(0, min(120, self.speed))
            distance = self.speed * dt_seconds / 3600  # km
            self.odometer += distance
            # Update position
            self.latitude += np.random.normal(0, 0.001)
            self.longitude += np.random.normal(0, 0.001)
        
        # --- Anomaly injection ---
        anomaly_type = None
        anomaly_severity = 0
        
        if np.random.random() < self.anomaly_base_prob:
            anomaly_choices = ['thermal_spike', 'voltage_anomaly', 'current_surge', 
                             'soc_inconsistency', 'charging_fault']
            anomaly_type = np.random.choice(anomaly_choices)
            
            if anomaly_type == 'thermal_spike':
                self.temperature += np.random.uniform(8, 20)
                anomaly_severity = min(1.0, (self.temperature - 45) / 20)
            elif anomaly_type == 'voltage_anomaly':
                voltage += np.random.choice([-30, 30]) + np.random.normal(0, 5)
                anomaly_severity = 0.6
            elif anomaly_type == 'current_surge':
                current *= np.random.uniform(2.0, 3.0)
                anomaly_severity = 0.8
            elif anomaly_type == 'soc_inconsistency':
                # SoC jumps unrealistically
                self.soc += np.random.choice([-15, -10])
                anomaly_severity = 0.5
            elif anomaly_type == 'charging_fault':
                if self.is_charging:
                    current = np.random.uniform(-5, 5)  # Near zero despite "charging"
                    anomaly_severity = 0.7
        
        # Build telemetry packet
        telemetry = {
            'vehicle_id': self.vehicle_id,
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'battery': {
                'soc': round(self.soc, 2),
                'voltage': round(voltage, 2),
                'current': round(current, 2),
                'temperature': round(self.temperature, 2),
                'soh': round(self.soh, 2),
                'cycle_count': self.battery_age_cycles,
                'internal_resistance': round(self.internal_resistance, 5),
                'capacity_kwh': round(self.initial_capacity * self.soh / 100, 2)
            },
            'vehicle': {
                'speed_kmh': round(self.speed, 1),
                'odometer_km': round(self.odometer, 1),
                'is_moving': bool(self.is_moving),
                'location': {
                    'latitude': round(self.latitude, 6),
                    'longitude': round(self.longitude, 6)
                }
            },
            'charging': {
                'is_charging': bool(self.is_charging),
                'charger_type': 'DC_FAST' if self.is_charging else None,
                'power_kw': round(abs(current) * voltage / 1000, 2) if self.is_charging else 0
            },
            'anomaly': {
                'detected': bool(anomaly_type is not None),
                'type': anomaly_type,
                'severity': round(anomaly_severity, 3)
            }
        }
        
        return telemetry


class EVFleetSimulator:
    """Simulates an entire fleet of EVs generating telemetry."""
    
    def __init__(self, num_vehicles: int = 50, output_mode: str = 'console'):
        """
        Args:
            num_vehicles: Number of EVs to simulate
            output_mode: 'console', 'file', or 'mqtt'
        """
        self.num_vehicles = num_vehicles
        self.output_mode = output_mode
        self.vehicles: List[EVVehicle] = []
        self.mqtt_client = None
        self.running = False
        self.telemetry_log = []
        
        # Create fleet
        for i in range(num_vehicles):
            vid = f"EV-{i+1:03d}"
            self.vehicles.append(EVVehicle(vid))
        
        print(f"[INIT] Fleet simulator: {num_vehicles} vehicles, mode={output_mode}")
    
    def setup_mqtt(self, broker_host: str = 'localhost', broker_port: int = 1883):
        """Connect to MQTT broker (requires Mosquitto from Member 4)."""
        if not MQTT_AVAILABLE:
            print("[WARN] paho-mqtt not installed. Use: pip install paho-mqtt")
            return False
        
        try:
            # Handles paho-mqtt compatibility for both v1 and v2 APIs
            self.mqtt_client = mqtt.Client(
                callback_api_version=mqtt.CallbackAPIVersion.VERSION2 if hasattr(mqtt, 'CallbackAPIVersion') else None
            )
            self.mqtt_client.connect(broker_host, broker_port, 60)
            self.mqtt_client.loop_start()
            print(f"[MQTT] Connected to {broker_host}:{broker_port}")
            return True
        except Exception as e:
            print(f"[MQTT] Connection failed: {e}")
            print("[MQTT] Falling back to console mode")
            self.output_mode = 'console'
            return False
    
    def publish_telemetry(self, telemetry: Dict):
        """Publish telemetry to the configured output."""
        vehicle_id = telemetry['vehicle_id']
        
        if self.output_mode == 'mqtt' and self.mqtt_client:
            # Match the exact flat payload and topic required by the backend developer for Kafka
            payload = {
                "vehicle_id": vehicle_id,
                "timestamp": telemetry['timestamp'],
                "voltage": telemetry['battery']['voltage'],
                "current": telemetry['battery']['current'],
                "temperature": telemetry['battery']['temperature'],
                "soc": telemetry['battery']['soc'],
                "cycle_count": telemetry['battery']['cycle_count']
            }
            self.mqtt_client.publish(f"ev/battery/{vehicle_id}", json.dumps(payload))
        
        elif self.output_mode == 'file':
            self.telemetry_log.append(telemetry)
        
        elif self.output_mode == 'console':
            # Compact console output
            bat = telemetry['battery']
            veh = telemetry['vehicle']
            anomaly = telemetry['anomaly']
            
            status = "CHRG" if telemetry['charging']['is_charging'] else (
                     "MOVE" if veh['is_moving'] else "PARK")
            
            line = (f"  {vehicle_id} | SoC:{bat['soc']:5.1f}% | "
                   f"V:{bat['voltage']:6.1f} | I:{bat['current']:7.1f}A | "
                   f"T:{bat['temperature']:5.1f}C | SoH:{bat['soh']:5.1f}% | "
                   f"{status} {veh['speed_kmh']:5.1f}km/h")
            
            if anomaly['detected']:
                line += f" | !! {anomaly['type']} (sev:{anomaly['severity']:.2f})"
            
            print(line)
    
    def run(self, duration_seconds: int = 30, interval: float = 2.0):
        """Run the simulator for a given duration."""
        self.running = True
        iterations = int(duration_seconds / interval)
        
        print(f"\n{'='*80}")
        print(f"EV Fleet Simulator - {self.num_vehicles} vehicles, {duration_seconds}s duration")
        print(f"{'='*80}\n")
        
        try:
            for i in range(iterations):
                if not self.running:
                    break
                
                timestamp = datetime.utcnow().strftime('%H:%M:%S')
                print(f"\n[{timestamp}] Tick {i+1}/{iterations}")
                
                for vehicle in self.vehicles:
                    telemetry = vehicle.update(interval)
                    self.publish_telemetry(telemetry)
                
                if i < iterations - 1:
                    time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n[STOP] Simulator interrupted")
        
        self.running = False
        
        # Save file output
        if self.output_mode == 'file' and self.telemetry_log:
            output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                      'data', 'processed')
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, 'simulated_telemetry.json')
            with open(output_path, 'w') as f:
                json.dump(self.telemetry_log, f, indent=2)
            print(f"\n[SAVE] {len(self.telemetry_log)} records saved to {output_path}")
        
        # Generate summary
        self._print_summary()
    
    def generate_batch(self, num_ticks: int = 100, interval: float = 2.0) -> list:
        """Generate a batch of telemetry without real-time delays (for training data)."""
        all_telemetry = []
        for tick in range(num_ticks):
            for vehicle in self.vehicles:
                telemetry = vehicle.update(interval)
                all_telemetry.append(telemetry)
        return all_telemetry
    
    def _print_summary(self):
        """Print fleet status summary."""
        print(f"\n{'='*80}")
        print("Fleet Summary")
        print(f"{'='*80}")
        
        socs = [v.soc for v in self.vehicles]
        sohs = [v.soh for v in self.vehicles]
        temps = [v.temperature for v in self.vehicles]
        
        print(f"  SoC   - Min: {min(socs):.1f}% | Avg: {np.mean(socs):.1f}% | Max: {max(socs):.1f}%")
        print(f"  SoH   - Min: {min(sohs):.1f}% | Avg: {np.mean(sohs):.1f}% | Max: {max(sohs):.1f}%")
        print(f"  Temp  - Min: {min(temps):.1f}C | Avg: {np.mean(temps):.1f}C | Max: {max(temps):.1f}C")
        
        moving = sum(1 for v in self.vehicles if v.is_moving)
        charging = sum(1 for v in self.vehicles if v.is_charging)
        parked = self.num_vehicles - moving - charging
        print(f"  Status - Moving: {moving} | Charging: {charging} | Parked: {parked}")


def main():
    """Run the simulator with default settings."""
    import argparse
    
    parser = argparse.ArgumentParser(description='EV Fleet Telemetry Simulator')
    parser.add_argument('--vehicles', type=int, default=10, help='Number of vehicles (default: 10)')
    parser.add_argument('--duration', type=int, default=20, help='Duration in seconds (default: 20)')
    parser.add_argument('--interval', type=float, default=2.0, help='Update interval in seconds')
    parser.add_argument('--mode', choices=['console', 'file', 'mqtt'], default='console',
                       help='Output mode (default: console)')
    parser.add_argument('--mqtt-host', default='localhost', help='MQTT broker host')
    parser.add_argument('--mqtt-port', type=int, default=1883, help='MQTT broker port')
    
    args = parser.parse_args()
    
    sim = EVFleetSimulator(num_vehicles=args.vehicles, output_mode=args.mode)
    
    if args.mode == 'mqtt':
        sim.setup_mqtt(args.mqtt_host, args.mqtt_port)
    
    sim.run(duration_seconds=args.duration, interval=args.interval)


if __name__ == '__main__':
    main()
