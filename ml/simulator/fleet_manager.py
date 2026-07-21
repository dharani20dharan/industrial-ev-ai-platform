"""
Fleet & Vehicle Spawn Manager for EV Telemetry Simulator
=========================================================
Manages dynamic spawning of individual vehicles and whole fleets during runtime.
Supports cumulative scaling (e.g. 10 -> 100 -> 500 active vehicles) without resetting.
"""

import numpy as np
from typing import Dict, List, Optional, Any
import threading

from .vehicle_physics import VehiclePhysics
from .gps_engine import GPSTrajectoryEngine
from .profiles import get_profile_config


class SimulatedVehicleAsset:
    """Combines Physics and GPS Trajectory into a single manageable simulated vehicle entity."""

    def __init__(
        self,
        vehicle_id: str,
        fleet_id: str = "FLT-ALPHA-01",
        profile_name: str = "DELIVERY",
        initial_soc: Optional[float] = None
    ):
        self.vehicle_id = vehicle_id
        self.fleet_id = fleet_id
        self.profile_name = profile_name
        self.profile_cfg = get_profile_config(profile_name)

        # Physics model
        self.physics = VehiclePhysics(
            vehicle_id=vehicle_id,
            fleet_id=fleet_id,
            vehicle_type=self.profile_cfg["vehicle_type"],
            battery_capacity_kwh=self.profile_cfg["battery_capacity_kwh"],
            initial_soc=initial_soc
        )

        # GPS Trajectory model
        self.gps_engine = GPSTrajectoryEngine(
            region_key=self.profile_cfg["region"]
        )

        if self.profile_name == "CHARGING":
            self.physics.is_charging = True
            self.physics.charging_rate_kw = 100.0
            self.physics.charger_id = f"CHG-{self.vehicle_id.split('-')[-1]}"
            self.physics.driving_state = "CHARGING"
        elif self.profile_name == "IDLE":
            self.physics.is_charging = False
            self.physics.driving_state = "IDLE"

        self.current_target_speed = 0.0

    def tick(
        self,
        dt_seconds: float,
        speed_multiplier: float = 1.0,
        enable_charging: bool = True,
        enable_regen: bool = True,
        enable_events: bool = True
    ) -> Dict[str, Any]:
        """Advances both physics and GPS movement by one tick."""
        adjusted_dt = dt_seconds * speed_multiplier

        # Update target speed according to profile
        if self.physics.is_charging or self.profile_name in ["IDLE", "CHARGING"]:
            self.current_target_speed = 0.0
        else:
            if np.random.random() < self.profile_cfg["stop_probability"]:
                self.current_target_speed = 0.0
            elif abs(self.physics.speed_kph - self.current_target_speed) < 3.0 or self.current_target_speed < 0.1 or np.random.random() < 0.15:
                self.current_target_speed = float(np.random.uniform(
                    self.profile_cfg["target_speed_min_kph"],
                    self.profile_cfg["target_speed_max_kph"]
                ))

        # Advance physics
        telemetry_frame = self.physics.update_physics(
            dt_seconds=adjusted_dt,
            target_speed_kph=self.current_target_speed,
            charging_threshold_soc=self.profile_cfg.get("charging_threshold_soc", 20.0),
            enable_charging=enable_charging,
            enable_regen=enable_regen,
            enable_events=enable_events
        )

        # Advance continuous GPS position
        location_data = self.gps_engine.update_position(
            speed_kph=self.physics.speed_kph,
            dt_seconds=adjusted_dt
        )

        # Merge location and profile top-level fields into telemetry frame
        telemetry_frame["profile_name"] = self.profile_name
        telemetry_frame["vehicle_type"] = self.profile_cfg["vehicle_type"]
        telemetry_frame["latitude"] = location_data["latitude"]
        telemetry_frame["longitude"] = location_data["longitude"]
        telemetry_frame["heading"] = location_data["heading_deg"]
        telemetry_frame["heading_deg"] = location_data["heading_deg"]

        telemetry_frame["location"] = {
            "vehicle_id": self.vehicle_id,
            "timestamp": telemetry_frame["timestamp"],
            **location_data
        }

        return telemetry_frame


class FleetManager:
    """Manages active vehicle pool, fleet assignments, dynamic spawning and despawning."""

    def __init__(self):
        self.vehicles: Dict[str, SimulatedVehicleAsset] = {}
        self.fleets: Dict[str, List[str]] = {}
        self.lock = threading.Lock()
        self._vehicle_counter = 0

    def spawn_vehicles(
        self,
        count: int = 10,
        profile_name: str = "DELIVERY",
        fleet_id: str = "FLT-ALPHA-01",
        initial_soc: Optional[float] = None
    ) -> List[str]:
        """Spawns specified count of vehicles and appends to existing active simulation."""
        new_ids = []
        with self.lock:
            if fleet_id not in self.fleets:
                self.fleets[fleet_id] = []

            for _ in range(count):
                self._vehicle_counter += 1
                prefix = "EV-HD" if "HEAVY" in profile_name or "HIGHWAY" in profile_name else "EV"
                vid = f"{prefix}-{self._vehicle_counter:03d}"

                vehicle = SimulatedVehicleAsset(
                    vehicle_id=vid,
                    fleet_id=fleet_id,
                    profile_name=profile_name,
                    initial_soc=initial_soc
                )
                self.vehicles[vid] = vehicle
                self.fleets[fleet_id].append(vid)
                new_ids.append(vid)

        return new_ids

    def spawn_fleet(
        self,
        fleet_name: str,
        fleet_type: str,
        count: int,
        profile_name: str
    ) -> str:
        """Spawns an entire fleet entity with assigned vehicles."""
        fleet_id = f"FLT-{fleet_name.upper().replace(' ', '-')}"
        self.spawn_vehicles(count=count, profile_name=profile_name, fleet_id=fleet_id)
        return fleet_id

    def despawn_vehicles(self, vehicle_ids: List[str]) -> int:
        """Removes specified vehicles from active simulation."""
        removed_count = 0
        with self.lock:
            for vid in vehicle_ids:
                if vid in self.vehicles:
                    veh = self.vehicles.pop(vid)
                    if veh.fleet_id in self.fleets and vid in self.fleets[veh.fleet_id]:
                        self.fleets[veh.fleet_id].remove(vid)
                    removed_count += 1
        return removed_count

    def clear(self):
        """Clears all active vehicles and fleets."""
        with self.lock:
            self.vehicles.clear()
            self.fleets.clear()
            self._vehicle_counter = 0

    def get_all_vehicles(self) -> List[SimulatedVehicleAsset]:
        with self.lock:
            return list(self.vehicles.values())

    def get_summary(self) -> Dict[str, Any]:
        with self.lock:
            all_vehs = list(self.vehicles.values())
            total_active = len(all_vehs)
            
            if total_active == 0:
                return {
                    "total_vehicles": 0,
                    "total_fleets": 0,
                    "charging_count": 0,
                    "moving_count": 0,
                    "idle_count": 0,
                    "fault_count": 0,
                    "avg_soc": 0.0,
                    "avg_temp": 0.0,
                    "avg_speed": 0.0,
                    "fleets": {}
                }

            charging = sum(1 for v in all_vehs if v.physics.is_charging)
            moving = sum(1 for v in all_vehs if v.physics.is_moving)
            faults = sum(1 for v in all_vehs if v.physics.active_anomaly is not None)
            idle = total_active - charging - moving

            socs = [v.physics.soc for v in all_vehs]
            temps = [v.physics.cell_temperature for v in all_vehs]
            speeds = [v.physics.speed_kph for v in all_vehs]

            fleet_breakdown = {
                fid: len(vlist) for fid, vlist in self.fleets.items()
            }

            return {
                "total_vehicles": total_active,
                "total_fleets": len(self.fleets),
                "charging_count": charging,
                "moving_count": moving,
                "idle_count": idle,
                "fault_count": faults,
                "avg_soc": float(round(np.mean(socs), 1)),
                "min_soc": float(round(min(socs), 1)),
                "max_soc": float(round(max(socs), 1)),
                "avg_temp": float(round(np.mean(temps), 1)),
                "avg_speed": float(round(np.mean(speeds), 1)),
                "fleets": fleet_breakdown
            }
