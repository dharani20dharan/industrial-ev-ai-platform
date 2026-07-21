"""
GPS Continuous Movement Engine for EV Simulator
================================================
Generates realistic, continuous geospatial vehicle trajectories:
- Geodesic position updates: Lat/Lon calculated continuously from previous position
- Smooth bearing/heading angle evolution
- Waypoint-based route loops (Urban Grid, Highway Corridors, Industrial Hubs)
- Stops at intersections/waypoints without random teleportation
"""

import numpy as np
import math
from typing import Dict, Tuple, List, Optional, Any

EARTH_RADIUS_KM = 6371.0

def destination_point(lat: float, lon: float, bearing_deg: float, distance_km: float) -> Tuple[float, float]:
    """Calculates destination latitude and longitude given start point, bearing, and distance."""
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    bearing_rad = math.radians(bearing_deg)

    angular_dist = distance_km / EARTH_RADIUS_KM

    dest_lat_rad = math.asin(
        math.sin(lat_rad) * math.cos(angular_dist) +
        math.cos(lat_rad) * math.sin(angular_dist) * math.cos(bearing_rad)
    )

    dest_lon_rad = lon_rad + math.atan2(
        math.sin(bearing_rad) * math.sin(angular_dist) * math.cos(lat_rad),
        math.cos(angular_dist) - math.sin(lat_rad) * math.sin(dest_lat_rad)
    )

    return math.degrees(dest_lat_rad), math.degrees(dest_lon_rad)


def calculate_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculates bearing angle in degrees from (lat1, lon1) to (lat2, lon2)."""
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)

    dlon = lon2_rad - lon1_rad
    y = math.sin(dlon) * math.cos(lat2_rad)
    x = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(dlon)

    bearing = math.degrees(math.atan2(y, x))
    return (bearing + 360.0) % 360.0


# Pre-defined operational route waypoints for realistic industrial & logistics corridors
REGION_WAYPOINTS = {
    "DELHI_NCR": [
        (28.6139, 77.2090),  # Connaught Place Hub
        (28.5355, 77.3910),  # Noida Logistics Center
        (28.4595, 77.0266),  # Gurgaon Industrial Belt
        (28.7041, 77.1025),  # North Delhi Depot
        (28.5244, 77.1855)   # Airport Freight Terminal
    ],
    "HIGHWAY_CORRIDOR": [
        (28.6139, 77.2090),  # Delhi Hub
        (27.1767, 78.0081),  # Agra Transit Hub
        (26.8467, 80.9462),  # Lucknow Logistics Complex
        (25.3176, 82.9739)   # Varanasi Distribution Hub
    ],
    "INDUSTRIAL_PORT": [
        (19.0760, 72.8777),  # Mumbai Central Terminal
        (18.9500, 72.9500),  # JNPT Container Port
        (19.2183, 72.9781),  # Thane Manufacturing Hub
        (18.5204, 73.8567)   # Pune Automotive Cluster
    ]
}


class GPSTrajectoryEngine:
    """Manages continuous GPS updates and route progression for a single vehicle."""

    def __init__(
        self,
        region_key: str = "DELHI_NCR",
        initial_lat: Optional[float] = None,
        initial_lon: Optional[float] = None
    ):
        self.waypoints = REGION_WAYPOINTS.get(region_key, REGION_WAYPOINTS["DELHI_NCR"])
        self.current_waypoint_idx = np.random.randint(0, len(self.waypoints))
        
        start_wp = self.waypoints[self.current_waypoint_idx]
        if initial_lat is not None and initial_lon is not None:
            self.latitude = initial_lat
            self.longitude = initial_lon
        else:
            # Offset significantly around starting waypoint for wide geographical spread
            self.latitude = start_wp[0] + np.random.uniform(-0.15, 0.15)
            self.longitude = start_wp[1] + np.random.uniform(-0.15, 0.15)
            
        self.heading_deg = np.random.uniform(0, 360)
        self.target_heading_deg = self.heading_deg
        self.altitude_m = float(round(np.random.uniform(180, 250), 1))
        self.gps_fix_quality = "3D_FIX"

        # Advance to next waypoint
        self._select_next_target()

    def _select_next_target(self):
        self.current_waypoint_idx = (self.current_waypoint_idx + 1) % len(self.waypoints)
        target_lat, target_lon = self.waypoints[self.current_waypoint_idx]
        self.target_heading_deg = calculate_bearing(self.latitude, self.longitude, target_lat, target_lon)

    def update_position(self, speed_kph: float, dt_seconds: float) -> Dict[str, Any]:
        """Derives new lat/lon derived from previous location and current speed."""
        if speed_kph > 0.1:
            # Smooth heading transition (turn rate ~ 30 deg/sec)
            angle_diff = (self.target_heading_deg - self.heading_deg + 180.0) % 360.0 - 180.0
            turn_step = np.clip(angle_diff, -30.0 * dt_seconds, 30.0 * dt_seconds)
            self.heading_deg = (self.heading_deg + turn_step + 360.0) % 360.0

            # Calculate displacement distance
            distance_km = (speed_kph / 3600.0) * dt_seconds
            
            # Update lat/lon using geodesic formula
            self.latitude, self.longitude = destination_point(
                self.latitude, self.longitude, self.heading_deg, distance_km
            )

            # Check distance to current target waypoint
            target_lat, target_lon = self.waypoints[self.current_waypoint_idx]
            dist_to_target = math.sqrt((self.latitude - target_lat)**2 + (self.longitude - target_lon)**2) * 111.0  # Approx km
            
            if dist_to_target < 0.5:
                self._select_next_target()

            # Subtle altitude fluctuation
            self.altitude_m += np.random.uniform(-0.2, 0.2)

        return {
            "latitude": float(round(self.latitude, 6)),
            "longitude": float(round(self.longitude, 6)),
            "altitude_m": float(round(self.altitude_m, 1)),
            "heading_deg": float(round(self.heading_deg, 1)),
            "gps_fix_quality": self.gps_fix_quality
        }
