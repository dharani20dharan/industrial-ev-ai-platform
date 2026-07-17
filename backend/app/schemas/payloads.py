from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field, ConfigDict

class BasePayload(BaseModel):
    """Base configuration allowing both old aliases and new enterprise keys, while keeping extra data."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    # FIX: Added top-level vehicle string tracking requirement to clean up extraction
    vehicle_id: str = Field(default="VEH-SIM-UNKNOWN")

class TelemetryPayload(BasePayload):
    """Kinematic data mapping simulator inputs to system targets with safe defaults."""
    speed_kph: float = Field(default=0.0, validation_alias="speed", ge=0, le=2000.0)
    odometer_km: float = Field(default=0.0, validation_alias="odometer", ge=0)
    # FIX: Increased upper boundary check to 5000.0 to allow extreme thermal anomalies through
    motor_temperature_c: float = Field(default=25.0, validation_alias="ambient_temperature", ge=-40, le=5000.0)
    torque_nm: float = Field(default=0.0, validation_alias="power_output")
    inverter_efficiency: float = Field(default=0.94, ge=0, le=1)

class BatteryPayload(BasePayload):
    """Electro-chemical stats providing field transformations for native simulator outputs."""
    state_of_charge_pct: float = Field(default=0.0, validation_alias="soc", ge=0, le=100)
    state_of_health_pct: float = Field(default=100.0, validation_alias="soh", ge=0, le=100)
    voltage: float = Field(default=0.0, ge=0, le=1000)
    current_amps: float = Field(default=0.0, validation_alias="current")
    # FIX: Relax constraints further to ensure packets aren't dropped during runtime anomalies
    cell_temperature_max_c: float = Field(default=25.0, validation_alias="cell_temperature", ge=-40, le=5000.0)
    internal_resistance_ohm: float = Field(default=0.01, validation_alias="internal_resistance", ge=0)
    cycle_count: int = Field(default=100, validation_alias="cycle_count", ge=0)

class LocationPayload(BasePayload):
    latitude: float = Field(default=39.7392, ge=-90, le=90)
    longitude: float = Field(default=-104.9903, ge=-180, le=180)
    altitude_m: Optional[float] = Field(default=1609.0, ge=-500, le=9000)
    heading_deg: Optional[float] = Field(default=0.0, ge=0, le=360)
    # FIX: Change to str to cleanly capture status strings like '3D_FIX'
    gps_fix_quality: str = Field(default="UNKNOWN")

class ChargingPayload(BasePayload):
    # FIX: Make Optional to safely handle payloads when the EV is discharging instead of charging
    charger_id: Optional[str] = Field(default="CHG-STATION-MOCK")
    charging_rate_kw: float = Field(default=0.0, ge=-200, le=500) # Accept negative numbers during charge state physics
    time_to_full_mins: float = Field(default=0.0, ge=0)
    connector_type: Optional[str] = Field(default="CCS2")

class StatusPayload(BasePayload):
    operational_status: str = Field(default="OPERATIONAL")
    active_error_codes: List[str] = Field(default_factory=list)
    driver_id: Optional[str] = Field(default="SYSTEM_AUTO")

class AlertsPayload(BasePayload):
    alert_code: str = Field(default="CLR_00")
    severity: str = Field(default="INFO")
    component: str = Field(default="SYSTEM")
    description: str = Field(default="Healthy baseline initialization status.")

class HeartbeatPayload(BasePayload):
    uptime_seconds: int = Field(default=0, ge=0)
    firmware_version: str = Field(default="v1.0.0-mock")
    signal_strength_dbm: int = Field(default=-50, le=0)
