"""
Vehicle Physics Engine for Industrial EV AI Platform Simulator
===============================================================
Provides realistic, coupled physical simulation for Electric Vehicles:
- State of Charge (SoC), State of Health (SoH), Voltage, Current
- Kinetic acceleration, speed, odometer, torque
- Thermal dynamics for cell temperature and motor temperature
- Regenerative braking energy recovery
- Dynamic charging & discharging states
"""

import numpy as np
from typing import Dict, Any, Optional
from datetime import datetime

class VehiclePhysics:
    """Simulates realistic electro-chemical, kinetic, and thermal dynamics of an EV."""

    def __init__(
        self,
        vehicle_id: str,
        fleet_id: str = "FLT-ALPHA-01",
        vehicle_type: str = "DELIVERY_VAN",
        battery_capacity_kwh: float = 85.0,
        battery_age_cycles: int = None,
        initial_soc: float = None
    ):
        self.vehicle_id = vehicle_id
        self.fleet_id = fleet_id
        self.vehicle_type = vehicle_type
        
        # Battery specs
        self.battery_capacity_kwh = battery_capacity_kwh
        self.battery_age_cycles = battery_age_cycles or np.random.randint(50, 650)
        
        # Electro-chemical health
        self.soh = float(np.clip(100.0 - (self.battery_age_cycles / 900.0) * 30.0 + np.random.normal(0, 1.5), 65.0, 100.0))
        self.soc = float(initial_soc if initial_soc is not None else np.random.uniform(30.0, 95.0))
        self.nominal_voltage = 400.0  # Pack Volts
        self.internal_resistance = float(0.035 + (self.battery_age_cycles / 800.0) * 0.025)
        
        # Dynamic temperatures (deg C)
        self.ambient_temp = float(28.0 + np.random.normal(0, 2.0))
        self.cell_temperature = float(self.ambient_temp + np.random.uniform(2.0, 6.0))
        self.motor_temperature = float(self.ambient_temp + np.random.uniform(5.0, 12.0))
        
        # Kinematics
        self.speed_kph = 0.0
        self.target_speed_kph = 0.0
        self.acceleration_m_s2 = 0.0
        self.odometer_km = float(np.random.randint(5000, 85000))
        self.torque_nm = 0.0
        self.inverter_efficiency = 0.94
        
        # Operational state flags
        self.is_moving = False
        self.is_charging = False
        self.charging_rate_kw = 0.0
        self.charger_id = None
        self.driving_state = "IDLE"  # IDLE, ACCELERATING, CRUISING, BRAKING, CHARGING, FAULT
        
        # Energy metrics
        self.total_energy_consumed_kwh = 0.0
        self.total_energy_regenerated_kwh = 0.0
        
        # Active anomalies
        self.active_anomaly = None
        self.anomaly_severity = 0.0
        self.anomaly_base_prob = float(0.005 + (self.battery_age_cycles / 1000.0) * 0.02)

    def update_physics(
        self,
        dt_seconds: float,
        target_speed_kph: float,
        charging_threshold_soc: float = 20.0,
        enable_charging: bool = True,
        enable_regen: bool = True,
        enable_events: bool = True
    ) -> Dict[str, Any]:
        """Advances vehicle physics state by dt_seconds based on target speed and profile directives."""
        
        # 1. State Decision logic
        if self.is_charging:
            self.target_speed_kph = 0.0
            self.speed_kph = 0.0
            self.is_moving = False
            self.driving_state = "CHARGING"
            if self.soc >= 95.0:
                self.is_charging = False
                self.charging_rate_kw = 0.0
                self.charger_id = None
                self.driving_state = "IDLE"
        else:
            self.target_speed_kph = max(0.0, target_speed_kph)
            if self.target_speed_kph > 0.1:
                self.is_moving = True
                if abs(self.speed_kph - self.target_speed_kph) < 2.0:
                    self.driving_state = "CRUISING"
                elif self.target_speed_kph > self.speed_kph:
                    self.driving_state = "ACCELERATING"
                else:
                    self.driving_state = "BRAKING"
            else:
                if self.speed_kph > 1.0:
                    self.driving_state = "BRAKING"
                else:
                    self.driving_state = "IDLE"
                    self.is_moving = False

            # Auto-charge trigger if battery drops below profile threshold and vehicle is stopped or slowing
            if enable_charging and self.soc <= charging_threshold_soc and self.speed_kph < 2.0 and np.random.random() < 0.40:
                self.is_charging = True
                self.is_moving = False
                self.charging_rate_kw = float(np.random.choice([50.0, 100.0, 150.0]))
                self.charger_id = f"CHG-{self.vehicle_id.split('-')[-1]}"
                self.driving_state = "CHARGING"

        # 2. Kinematic updates
        if self.driving_state == "CHARGING":
            self.speed_kph = 0.0
            self.acceleration_m_s2 = 0.0
            self.torque_nm = 0.0
        else:
            speed_diff = self.target_speed_kph - self.speed_kph
            max_accel = 2.5 if self.vehicle_type == "LIGHT_COMMERCIAL" else 1.8
            max_decel = -3.5
            
            if speed_diff > 0:
                accel = min(max_accel, speed_diff / max(1.0, dt_seconds))
            else:
                accel = max(max_decel, speed_diff / max(1.0, dt_seconds))
                
            self.acceleration_m_s2 = float(round(accel, 2))
            self.speed_kph = max(0.0, min(140.0, float(self.speed_kph + self.acceleration_m_s2 * (dt_seconds * 3.6 / 1.0))))
            
            if self.speed_kph < 0.5 and self.target_speed_kph < 0.5:
                self.speed_kph = 0.0
                self.is_moving = False
                if self.driving_state != "CHARGING":
                    self.driving_state = "IDLE"

            # Odometer evolution
            dist_km = (self.speed_kph / 3600.0) * dt_seconds
            self.odometer_km += dist_km
            
            # Torque estimation (Nm)
            if self.speed_kph > 1.0:
                base_torque = (self.acceleration_m_s2 * 120.0) + (self.speed_kph * 1.5)
                self.torque_nm = max(-150.0, min(450.0, float(round(base_torque + np.random.normal(0, 3.0), 1))))
            else:
                self.torque_nm = 0.0

        # 3. Electrical & Battery Power Dynamics
        if self.is_charging:
            # Charging: Current is positive
            power_kw = self.charging_rate_kw
            current_amps = (power_kw * 1000.0) / self.nominal_voltage
            soc_increment = (power_kw * (dt_seconds / 3600.0) / (self.battery_capacity_kwh * (self.soh / 100.0))) * 100.0
            self.soc = float(min(100.0, self.soc + soc_increment))
            voltage = self.nominal_voltage * (0.85 + 0.15 * (self.soc / 100.0)) + (current_amps * self.internal_resistance)
        
        elif self.driving_state == "BRAKING" and enable_regen and self.speed_kph > 10.0:
            # Regenerative Braking: Recovers energy, current is positive
            regen_power_kw = min(40.0, float(abs(self.acceleration_m_s2) * self.speed_kph * 0.35))
            current_amps = (regen_power_kw * 1000.0) / self.nominal_voltage
            soc_increment = (regen_power_kw * (dt_seconds / 3600.0) / (self.battery_capacity_kwh * (self.soh / 100.0))) * 100.0
            self.soc = float(min(100.0, self.soc + soc_increment))
            self.total_energy_regenerated_kwh += (regen_power_kw * (dt_seconds / 3600.0))
            voltage = self.nominal_voltage * (0.85 + 0.15 * (self.soc / 100.0)) + (current_amps * self.internal_resistance * 0.5)
            
        else:
            # Driving / Idle: Discharging, current is negative
            if self.speed_kph > 0.0:
                base_power_kw = 5.0 + (self.speed_kph * 0.28) + (max(0.0, self.acceleration_m_s2) * 12.0)
            else:
                base_power_kw = 0.8  # HVAC & auxiliary power
                
            power_kw = base_power_kw
            current_amps = -(power_kw * 1000.0) / self.nominal_voltage
            soc_decrement = (power_kw * (dt_seconds / 3600.0) / (self.battery_capacity_kwh * (self.soh / 100.0))) * 100.0
            self.soc = float(max(2.0, self.soc - soc_decrement))
            self.total_energy_consumed_kwh += (power_kw * (dt_seconds / 3600.0))
            voltage = self.nominal_voltage * (0.85 + 0.15 * (self.soc / 100.0)) - (abs(current_amps) * self.internal_resistance)

        # Voltage noise & clipping
        voltage = float(np.clip(voltage + np.random.normal(0, 0.8), 280.0, 450.0))
        current_amps = float(round(current_amps + np.random.normal(0, 1.2), 2))

        # 4. Thermal evolution physics
        ambient_decay = 0.02 * dt_seconds
        heat_gen = (abs(current_amps) ** 2 * self.internal_resistance * 0.00008) * dt_seconds
        
        self.cell_temperature = float(np.clip(
            (1.0 - ambient_decay) * self.cell_temperature + ambient_decay * self.ambient_temp + heat_gen,
            15.0, 95.0
        ))
        
        motor_heat = (self.speed_kph * 0.02 + max(0.0, self.torque_nm) * 0.015) * dt_seconds
        self.motor_temperature = float(np.clip(
            (1.0 - ambient_decay) * self.motor_temperature + ambient_decay * self.ambient_temp + motor_heat,
            20.0, 120.0
        ))

        # 5. Anomaly Injection
        if enable_events and np.random.random() < self.anomaly_base_prob and self.active_anomaly is None:
            anomalies = ['THERMAL_RUNAWAY_WARNING', 'VOLTAGE_SAG', 'CURRENT_SPIKE', 'SOC_DISCREPANCY']
            self.active_anomaly = np.random.choice(anomalies)
            self.anomaly_severity = float(np.random.uniform(0.5, 0.95))
            
        if self.active_anomaly:
            if self.active_anomaly == 'THERMAL_RUNAWAY_WARNING':
                self.cell_temperature += 15.0 * dt_seconds
            elif self.active_anomaly == 'VOLTAGE_SAG':
                voltage -= 45.0
            elif self.active_anomaly == 'CURRENT_SPIKE':
                current_amps *= 2.2
            # Clear anomaly after short period
            if np.random.random() < 0.2:
                self.active_anomaly = None
                self.anomaly_severity = 0.0

        # Output Telemetry Payloads Bundle matching API/Kafka schema format
        timestamp_str = datetime.utcnow().isoformat() + "Z"
        op_status = "FAULT" if self.active_anomaly else ("CHARGING" if self.is_charging else (self.driving_state if self.driving_state != "IDLE" else ("IN_TRANSIT" if self.is_moving else "IDLE")))
        
        return {
            "vehicle_id": self.vehicle_id,
            "fleet_id": self.fleet_id,
            "timestamp": timestamp_str,
            "driving_state": self.driving_state,
            "status": op_status,
            "is_charging": self.is_charging,
            "is_moving": self.is_moving,
            "speed_kph": float(round(self.speed_kph, 1)),
            "speed": float(round(self.speed_kph, 1)),
            "soc": float(round(self.soc, 1)),
            "soh": float(round(self.soh, 1)),
            "voltage": float(round(voltage, 1)),
            "current_amps": float(round(current_amps, 1)),
            "current": float(round(current_amps, 1)),
            "motor_temperature_c": float(round(self.motor_temperature, 1)),
            "temperature": float(round(self.motor_temperature, 1)),
            "cell_temp": float(round(self.cell_temperature, 1)),
            "torque_nm": float(round(self.torque_nm, 1)),
            "odometer_km": float(round(self.odometer_km, 1)),
            "active_anomaly": self.active_anomaly,
            "battery": {
                "vehicle_id": self.vehicle_id,
                "timestamp": timestamp_str,
                "state_of_charge_pct": float(round(self.soc, 2)),
                "soc": float(round(self.soc, 2)),
                "state_of_health_pct": float(round(self.soh, 2)),
                "soh": float(round(self.soh, 2)),
                "voltage": float(round(voltage, 2)),
                "current_amps": float(round(current_amps, 2)),
                "current": float(round(current_amps, 2)),
                "cell_temperature_max_c": float(round(self.cell_temperature, 2)),
                "cell_temperature": float(round(self.cell_temperature, 2)),
                "temperature": float(round(self.cell_temperature, 2)),
                "internal_resistance_ohm": float(round(self.internal_resistance, 5)),
                "internal_resistance": float(round(self.internal_resistance, 5)),
                "cycle_count": int(self.battery_age_cycles)
            },
            "telemetry": {
                "vehicle_id": self.vehicle_id,
                "timestamp": timestamp_str,
                "speed_kph": float(round(self.speed_kph, 1)),
                "speed": float(round(self.speed_kph, 1)),
                "odometer_km": float(round(self.odometer_km, 1)),
                "odometer": float(round(self.odometer_km, 1)),
                "motor_temperature_c": float(round(self.motor_temperature, 1)),
                "ambient_temperature": float(round(self.ambient_temp, 1)),
                "torque_nm": float(round(self.torque_nm, 1)),
                "power_output": float(round(abs(current_amps * voltage) / 1000.0, 2)),
                "inverter_efficiency": self.inverter_efficiency
            },
            "charging": {
                "vehicle_id": self.vehicle_id,
                "timestamp": timestamp_str,
                "is_charging": self.is_charging,
                "charger_id": self.charger_id or f"CHG-NONE",
                "charging_rate_kw": float(round(self.charging_rate_kw if self.is_charging else 0.0, 2)),
                "power_kw": float(round(self.charging_rate_kw if self.is_charging else 0.0, 2)),
                "time_to_full_mins": float(round(((100.0 - self.soc) / 100.0 * self.battery_capacity_kwh / max(1.0, self.charging_rate_kw)) * 60.0, 1)) if self.is_charging else 0.0,
                "connector_type": "CCS2" if self.is_charging else "NONE"
            },
            "status_details": {
                "vehicle_id": self.vehicle_id,
                "timestamp": timestamp_str,
                "operational_status": op_status,
                "active_error_codes": [self.active_anomaly] if self.active_anomaly else [],
                "driver_id": f"DRIVER-{self.vehicle_id}"
            },
            "anomaly": {
                "detected": self.active_anomaly is not None,
                "type": self.active_anomaly,
                "severity": self.anomaly_severity
            }
        }
