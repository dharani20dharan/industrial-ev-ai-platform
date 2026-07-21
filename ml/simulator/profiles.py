"""
Vehicle Driving Behaviour Profiles for EV Simulator
===================================================
Defines distinct operational profiles that naturally dictate vehicle speeds,
stop frequency, acceleration patterns, battery energy depletion rates, and routes.
"""

from typing import Dict, Any

DRIVING_PROFILES: Dict[str, Dict[str, Any]] = {
    "URBAN": {
        "profile_name": "Urban Traffic",
        "description": "Stop-and-go city transit with frequent stops and low-to-medium speeds.",
        "target_speed_min_kph": 15.0,
        "target_speed_max_kph": 50.0,
        "stop_probability": 0.12,
        "region": "DELHI_NCR",
        "battery_capacity_kwh": 75.0,
        "vehicle_type": "LIGHT_COMMERCIAL",
        "charging_threshold_soc": 25.0
    },
    "HIGHWAY": {
        "profile_name": "Highway Transit",
        "description": "High continuous speeds with minimal stops and heavy power draw.",
        "target_speed_min_kph": 70.0,
        "target_speed_max_kph": 110.0,
        "stop_probability": 0.01,
        "region": "HIGHWAY_CORRIDOR",
        "battery_capacity_kwh": 120.0,
        "vehicle_type": "HEAVY_TRUCK",
        "charging_threshold_soc": 18.0
    },
    "LONG_HAUL": {
        "profile_name": "Long-haul Intercity",
        "description": "Extended interstate cargo transport with periodic depot charging.",
        "target_speed_min_kph": 60.0,
        "target_speed_max_kph": 95.0,
        "stop_probability": 0.03,
        "region": "HIGHWAY_CORRIDOR",
        "battery_capacity_kwh": 200.0,
        "vehicle_type": "HEAVY_HAULER",
        "charging_threshold_soc": 20.0
    },
    "INDUSTRIAL": {
        "profile_name": "Heavy Industrial Depot",
        "description": "Heavy machinery and port yard transport with high torque and frequent pauses.",
        "target_speed_min_kph": 10.0,
        "target_speed_max_kph": 35.0,
        "stop_probability": 0.15,
        "region": "INDUSTRIAL_PORT",
        "battery_capacity_kwh": 150.0,
        "vehicle_type": "PORT_TRACTOR",
        "charging_threshold_soc": 30.0
    },
    "DELIVERY": {
        "profile_name": "Last-mile Delivery",
        "description": "Frequent parcel delivery stops with rapid acceleration/deceleration cycles.",
        "target_speed_min_kph": 20.0,
        "target_speed_max_kph": 60.0,
        "stop_probability": 0.18,
        "region": "DELHI_NCR",
        "battery_capacity_kwh": 85.0,
        "vehicle_type": "DELIVERY_VAN",
        "charging_threshold_soc": 22.0
    },
    "IDLE": {
        "profile_name": "Parked Depot Fleet",
        "description": "Stationary fleet parked at depot maintaining HVAC and telemetry heartbeat.",
        "target_speed_min_kph": 0.0,
        "target_speed_max_kph": 0.0,
        "stop_probability": 1.0,
        "region": "DELHI_NCR",
        "battery_capacity_kwh": 85.0,
        "vehicle_type": "DELIVERY_VAN",
        "charging_threshold_soc": 10.0
    },
    "CHARGING": {
        "profile_name": "Depot Fast-Charging",
        "description": "Vehicles docked at fast chargers rapidly increasing State of Charge.",
        "target_speed_min_kph": 0.0,
        "target_speed_max_kph": 0.0,
        "stop_probability": 1.0,
        "region": "INDUSTRIAL_PORT",
        "battery_capacity_kwh": 100.0,
        "vehicle_type": "DELIVERY_VAN",
        "charging_threshold_soc": 95.0
    }
}

def get_profile_config(profile_name: str) -> Dict[str, Any]:
    """Returns profile configuration by key or defaults to DELIVERY."""
    key = profile_name.upper().strip()
    return DRIVING_PROFILES.get(key, DRIVING_PROFILES["DELIVERY"])
