# from typing import Dict, Any, Optional
# from pydantic import BaseModel, Field

# class TelemetryPayload(BaseModel):
#     """Core kinematic data from the vehicle's engine and operational control units."""
#     speed_kph: float = Field(..., ge=0, le=200)
#     odometer_km: float = Field(..., ge=0)
#     motor_temperature_c: float = Field(..., ge=-40, le=150)
#     torque_nm: float = Field(...)
#     inverter_efficiency: float = Field(..., ge=0, le=1)


# class BatteryPayload(BaseModel):
#     """Real-time electro-chemical battery state statistics."""
#     state_of_charge_pct: float = Field(..., ge=0, le=100)
#     state_of_health_pct: float = Field(..., ge=0, le=100)
#     voltage: float = Field(..., ge=0, le=1000)
#     current_amps: float = Field(...)
#     cell_temperature_max_c: float = Field(..., ge=-40, le=100)
#     internal_resistance_ohm: float = Field(..., ge=0)


# class LocationPayload(BaseModel):
#     """High-precision positional telemetry coordinate data."""
#     latitude: float = Field(..., ge=-90, le=90)
#     longitude: float = Field(..., ge=-180, le=180)
#     altitude_m: float = Field(..., ge=-500, le=9000)
#     heading_deg: float = Field(..., ge=0, le=360)
#     gps_fix_quality: int = Field(..., description="0=Invalid, 1=GPS, 2=DGPS")


# class ChargingPayload(BaseModel):
#     """State management metrics during an active battery charging session."""
#     charger_id: str = Field(...)
#     charging_rate_kw: float = Field(..., ge=0)
#     time_to_full_mins: float = Field(..., ge=0)
#     connector_type: str = Field(..., description="CCS2, Megawatt, etc.")


# class StatusPayload(BaseModel):
#     """High-level operating mode state flags."""
#     operational_status: str = Field(..., description="READY, OPERATIONAL, FAULT, OFFLINE")
#     active_error_codes: list[str] = Field(default_factory=list)
#     driver_id: Optional[str] = Field(default=None)


# class AlertsPayload(BaseModel):
#     """Immediate hardware or safety critical notifications."""
#     alert_code: str = Field(...)
#     severity: str = Field(..., description="INFO, WARNING, CRITICAL")
#     component: str = Field(..., description="BATTERY, MOTOR, BRAKES, POWERTRAIN")
#     description: str = Field(...)


# class HeartbeatPayload(BaseModel):
#     """Lightweight diagnostics asserting infrastructure network health."""
#     uptime_seconds: int = Field(..., ge=0)
#     firmware_version: str = Field(...)
#     signal_strength_dbm: int = Field(..., le=0)



from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field, field_validator

class TelemetryPayload(BaseModel):
    """Kinematic data mapping simulator inputs to system targets with safe defaults."""
    speed_kph: float = Field(default=0.0, validation_alias="speed", ge=0, le=200)
    odometer_km: float = Field(default=0.0, validation_alias="odometer", ge=0)
    motor_temperature_c: float = Field(default=65.0, validation_alias="ambient_temperature", ge=-40, le=150)
    # Simulator doesn't provide torque or efficiency yet; generate clean platform mock defaults
    torque_nm: float = Field(default=210.5, description="Fallback tracking default")
    inverter_efficiency: float = Field(default=0.94, ge=0, le=1)


class BatteryPayload(BaseModel):
    """Electro-chemical stats providing field transformations for native simulator outputs."""
    state_of_charge_pct: float = Field(..., validation_alias="soc", ge=0, le=100)
    state_of_health_pct: float = Field(..., validation_alias="soh", ge=0, le=100)
    voltage: float = Field(..., ge=0, le=1000)
    current_amps: float = Field(..., validation_alias="current")
    cell_temperature_max_c: float = Field(..., validation_alias="cell_temperature", ge=-40, le=100)
    internal_resistance_ohm: float = Field(..., validation_alias="internal_resistance", ge=0)


class LocationPayload(BaseModel):
    """Positional mapping supporting clean initialization blocks for empty topics."""
    latitude: float = Field(default=39.7392, ge=-90, le=90)
    longitude: float = Field(default=-104.9903, ge=-180, le=180)
    altitude_m: float = Field(default=1609.0, ge=-500, le=9000)
    heading_deg: float = Field(default=0.0, ge=0, le=360)
    gps_fix_quality: int = Field(default=1)


class ChargingPayload(BaseModel):
    """Fallback charging structures for silent initialization loops."""
    charger_id: str = Field(default="CHG-STATION-MOCK")
    charging_rate_kw: float = Field(default=0.0, ge=0)
    time_to_full_mins: float = Field(default=0.0, ge=0)
    connector_type: str = Field(default="CCS2")


class StatusPayload(BaseModel):
    operational_status: str = Field(default="OPERATIONAL")
    active_error_codes: List[str] = Field(default_factory=list)
    driver_id: Optional[str] = Field(default="SYSTEM_AUTO")


class AlertsPayload(BaseModel):
    alert_code: str = Field(default="CLR_00")
    severity: str = Field(default="INFO")
    component: str = Field(default="SYSTEM")
    description: str = Field(default="Healthy baseline initialization status.")


class HeartbeatPayload(BaseModel):
    uptime_seconds: int = Field(default=0, ge=0)
    firmware_version: str = Field(default="v1.0.0-mock")
    signal_strength_dbm: int = Field(default=-50, le=0)