from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class TelemetryPayload(BaseModel):
    """Core kinematic data from the vehicle's engine and operational control units."""
    speed_kph: float = Field(..., ge=0, le=200)
    odometer_km: float = Field(..., ge=0)
    motor_temperature_c: float = Field(..., ge=-40, le=150)
    torque_nm: float = Field(...)
    inverter_efficiency: float = Field(..., ge=0, le=1)


class BatteryPayload(BaseModel):
    """Real-time electro-chemical battery state statistics."""
    state_of_charge_pct: float = Field(..., ge=0, le=100)
    state_of_health_pct: float = Field(..., ge=0, le=100)
    voltage: float = Field(..., ge=0, le=1000)
    current_amps: float = Field(...)
    cell_temperature_max_c: float = Field(..., ge=-40, le=100)
    internal_resistance_ohm: float = Field(..., ge=0)


class LocationPayload(BaseModel):
    """High-precision positional telemetry coordinate data."""
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    altitude_m: float = Field(..., ge=-500, le=9000)
    heading_deg: float = Field(..., ge=0, le=360)
    gps_fix_quality: int = Field(..., description="0=Invalid, 1=GPS, 2=DGPS")


class ChargingPayload(BaseModel):
    """State management metrics during an active battery charging session."""
    charger_id: str = Field(...)
    charging_rate_kw: float = Field(..., ge=0)
    time_to_full_mins: float = Field(..., ge=0)
    connector_type: str = Field(..., description="CCS2, Megawatt, etc.")


class StatusPayload(BaseModel):
    """High-level operating mode state flags."""
    operational_status: str = Field(..., description="READY, OPERATIONAL, FAULT, OFFLINE")
    active_error_codes: list[str] = Field(default_factory=list)
    driver_id: Optional[str] = Field(default=None)


class AlertsPayload(BaseModel):
    """Immediate hardware or safety critical notifications."""
    alert_code: str = Field(...)
    severity: str = Field(..., description="INFO, WARNING, CRITICAL")
    component: str = Field(..., description="BATTERY, MOTOR, BRAKES, POWERTRAIN")
    description: str = Field(...)


class HeartbeatPayload(BaseModel):
    """Lightweight diagnostics asserting infrastructure network health."""
    uptime_seconds: int = Field(..., ge=0)
    firmware_version: str = Field(...)
    signal_strength_dbm: int = Field(..., le=0)