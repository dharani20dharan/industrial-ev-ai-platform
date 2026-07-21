"""
EV Telemetry Simulator (Upgraded Engine Entrypoint)
==================================================
Simulates real-time sensor data, vehicle physics, continuous GPS trajectories,
and operational metrics from a fleet of electric vehicles.

Supports CLI, MQTT, File, Console, and background API control panel server integration.
"""

import sys
import os
import argparse
import time
import json

# Ensure simulator package imports work cleanly
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from vehicle_physics import VehiclePhysics
from gps_engine import GPSTrajectoryEngine
from profiles import DRIVING_PROFILES
from fleet_manager import FleetManager
from controller_server import simulator_engine, SimulatorControllerEngine


def main():
    parser = argparse.ArgumentParser(description="Industrial EV AI Platform Telemetry Simulator")
    parser.add_argument("--vehicles", type=int, default=10, help="Initial number of vehicles (default: 10)")
    parser.add_argument("--profile", type=str, default="DELIVERY", choices=list(DRIVING_PROFILES.keys()), help="Driving profile")
    parser.add_argument("--fleet", type=str, default="FLT-ALPHA-01", help="Fleet Identifier")
    parser.add_argument("--mode", choices=["mqtt", "console", "file"], default="console", help="Output destination")
    parser.add_argument("--duration", type=int, default=0, help="Duration in seconds (0 = run indefinitely)")
    parser.add_argument("--interval", type=float, default=2.0, help="Telemetry publishing interval in seconds")
    parser.add_argument("--mqtt-host", default="localhost", help="MQTT broker host")
    parser.add_argument("--mqtt-port", type=int, default=1883, help="MQTT broker port")
    parser.add_argument("--speed-mult", type=float, default=1.0, help="Simulation speed multiplier (1.0 = realtime)")

    args = parser.parse_args()

    print(f"\n{'='*80}")
    print(f"EV Fleet Telemetry Simulator Engine - {args.vehicles} Vehicles [{args.profile} Profile]")
    print(f"Output Mode: {args.mode} | Interval: {args.interval}s | Speed: {args.speed_mult}x")
    print(f"{'='*80}\n")

    # Configure global simulator engine
    simulator_engine.fleet_manager.clear()
    simulator_engine.fleet_manager.spawn_vehicles(
        count=args.vehicles,
        profile_name=args.profile,
        fleet_id=args.fleet
    )

    simulator_engine.publish_interval = args.interval
    simulator_engine.speed_multiplier = args.speed_mult
    simulator_engine.output_mode = args.mode

    if args.mode == "mqtt":
        simulator_engine.setup_mqtt(args.mqtt_host, args.mqtt_port)

    simulator_engine.start()

    try:
        if args.duration > 0:
            time.sleep(args.duration)
            simulator_engine.stop()
            print("[STOP] Completed requested simulation duration.")
        else:
            print("[RUNNING] Simulation active. Press Ctrl+C to terminate.")
            while simulator_engine.running:
                status = simulator_engine.get_full_status()
                print(f"[{datetime.utcnow().strftime('%H:%M:%S')}] Active: {status['active_vehicles']} veh | "
                      f"State: {status['status']} | Rate: {status['messages_per_second']} msg/s | "
                      f"Avg SoC: {status['avg_soc']}% | Avg Temp: {status['avg_temp']}C")
                time.sleep(5.0)

    except KeyboardInterrupt:
        print("\n[INTERRUPT] Stopping simulator gracefully...")
        simulator_engine.stop()


if __name__ == "__main__":
    from datetime import datetime
    main()
