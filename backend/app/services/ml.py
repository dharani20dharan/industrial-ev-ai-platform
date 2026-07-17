import os
import sys
import logging
from typing import Dict, Any, List, Optional
import numpy as np

# Resolve paths
# Current file: backend/app/services/ml.py
# Root directory: industrial-ev-ai-platform
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
ML_DIR = os.path.join(ROOT_DIR, "ml")
MODELS_DIR = os.path.join(ML_DIR, "models")

# Add ml folder to sys.path
if ML_DIR not in sys.path:
    sys.path.append(ML_DIR)

logger = logging.getLogger(__name__)

# Lazy initialization placeholders
_anomaly_detector = None
_battery_predictor = None

def get_anomaly_detector():
    """Lazily load and return the pre-trained AnomalyDetector."""
    global _anomaly_detector
    if _anomaly_detector is None:
        try:
            from engines.anomaly_detector import AnomalyDetector
            _anomaly_detector = AnomalyDetector()
            _anomaly_detector.load(MODELS_DIR)
            logger.info("AnomalyDetector engine successfully loaded from models directory.")
        except Exception as e:
            logger.error(f"Critical error loading pre-trained AnomalyDetector: {e}")
            # Fallback mock detector if loading fails
            class FallbackAnomalyDetector:
                def __init__(self):
                    self.is_trained = False
                def predict(self, data: dict):
                    temp = data.get('temperature', 35.0)
                    voltage = data.get('voltage', 380.0)
                    is_anomaly = temp > 45.0 or voltage < 320.0
                    return {
                        'is_anomaly': is_anomaly,
                        'anomaly_score': 0.89 if is_anomaly else 0.05,
                        'anomaly_types': ['thermal_warning' if temp > 45.0 else 'under_voltage'] if is_anomaly else [],
                        'severity': 'high' if is_anomaly else 'normal',
                        'alerts': [f"Fallback: Temp {temp}C exceeds threshold"] if is_anomaly else [],
                        'recommendations': ["Cool battery"] if is_anomaly else []
                    }
            _anomaly_detector = FallbackAnomalyDetector()
    return _anomaly_detector

def get_battery_predictor():
    """Lazily load and return the pre-trained BatteryHealthPredictor."""
    global _battery_predictor
    if _battery_predictor is None:
        try:
            from engines.battery_predictor import BatteryHealthPredictor
            _battery_predictor = BatteryHealthPredictor()
            _battery_predictor.load(MODELS_DIR)
            logger.info("BatteryHealthPredictor engine successfully loaded from models directory.")
        except Exception as e:
            logger.error(f"Critical error loading pre-trained BatteryHealthPredictor: {e}")
            # Fallback mock predictor if loading fails
            class FallbackBatteryPredictor:
                def __init__(self):
                    self.soh_trained = False
                    self.rul_trained = False
                def predict_soh(self, data: dict):
                    capacity = data.get('capacity_ah', 114.0)
                    soh = (capacity / 120.0) * 100.0
                    return {
                        'soh_percent': round(soh, 2),
                        'health_status': 'good' if soh >= 85 else 'fair',
                        'recommendation': 'Fallback prediction: Battery is healthy.',
                        'confidence': 90.0
                    }
                def predict_rul(self, data: dict):
                    cycle = data.get('cycle', 100)
                    rul = max(0, 1500 - cycle)
                    return {
                        'rul_cycles': rul,
                        'estimated_days': round(rul / 2),
                        'urgency': 'low' if rul > 200 else 'medium',
                        'action': 'Fallback prediction: No actions required.',
                        'confidence': 90.0
                    }
                def predict_full(self, data: dict):
                    return {
                        'soh': self.predict_soh(data),
                        'rul': self.predict_rul(data)
                    }
            _battery_predictor = FallbackBatteryPredictor()
    return _battery_predictor

def prepare_features_from_records(records: List[Any], current_payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Constructs a complete ML feature dictionary mapping the 26 statistical/rolling features 
    expected by the pre-trained models from database records and/or active payload.
    """
    # Default/Baseline feature values
    data = {
        'cycle': 100,
        'capacity_ah': 114.0,
        'avg_voltage_v': 380.0,
        'voltage_charged_v': 400.0,
        'voltage_discharged_v': 350.0,
        'charge_current_a': 0.0,
        'discharge_current_a': 10.0,
        'avg_temperature_c': 35.0,
        'max_temperature_c': 38.0,
        'internal_resistance_ohm': 0.04,
        'charge_transfer_resistance_ohm': 0.05,
        'discharge_time_s': 3600.0,
        'charge_efficiency_percent': 95.0,
        'discharge_slope_v_per_s': -0.001,
        'capacity_degradation_rate': -0.005,
        'cumulative_capacity_loss': 6.0,
        'resistance_growth_rate': 0.0001,
        'temp_rolling_mean': 35.0,
        'temp_rolling_std': 1.0,
        'thermal_variance': 1.0,
        'voltage_spread': 50.0,
        'capacity_rolling_std': 0.5,
        'efficiency_drop': 0.0,
        'discharge_rate': 114.0,
        'impedance_ratio': 1.25,
        'cycle_age_normalized': 0.1
    }
    
    if current_payload:
        data['cycle'] = current_payload.get('cycle_count', current_payload.get('cycle', data['cycle']))
        data['avg_voltage_v'] = current_payload.get('voltage', data['avg_voltage_v'])
        data['avg_temperature_c'] = current_payload.get('temperature', data['avg_temperature_c'])
        data['internal_resistance_ohm'] = current_payload.get('internal_resistance', data['internal_resistance_ohm'])
        
        soh_val = current_payload.get('soh', current_payload.get('state_of_health', current_payload.get('state_of_health_pct', 95.0)))
        data['capacity_ah'] = (soh_val / 100.0) * 120.0
        
        current_val = current_payload.get('current', current_payload.get('current_amps', 0.0))
        if current_val > 0:
            data['charge_current_a'] = current_val
            data['discharge_current_a'] = 0.0
        else:
            data['charge_current_a'] = 0.0
            data['discharge_current_a'] = abs(current_val)
            
    if not records:
        return data

    # Extract historical fields from timeseries BatteryRecords
    voltages = [r.voltage for r in records]
    temps = [r.cell_temperature_max_c for r in records]
    currents = [r.current_amps for r in records]
    resistances = [r.internal_resistance_ohm for r in records]
    sohs = [r.state_of_health_pct for r in records]
    cycles = [getattr(r, 'cycle_count', 100) for r in records]
    
    # Calculate rolling features
    data['cycle'] = cycles[0]
    data['capacity_ah'] = (sohs[0] / 100.0) * 120.0
    data['avg_voltage_v'] = sum(voltages) / len(voltages)
    data['voltage_charged_v'] = max(voltages)
    data['voltage_discharged_v'] = min(voltages)
    
    pos_currents = [c for c in currents if c > 0]
    neg_currents = [c for c in currents if c < 0]
    data['charge_current_a'] = max(pos_currents) if pos_currents else 0.0
    data['discharge_current_a'] = abs(min(neg_currents)) if neg_currents else 10.0
    
    data['avg_temperature_c'] = sum(temps) / len(temps)
    data['max_temperature_c'] = max(temps)
    data['internal_resistance_ohm'] = resistances[0]
    data['charge_transfer_resistance_ohm'] = resistances[0] * 1.2
    
    if len(temps) > 1:
        data['temp_rolling_mean'] = sum(temps) / len(temps)
        data['temp_rolling_std'] = float(np.std(temps))
        data['thermal_variance'] = float(np.var(temps))
    
    data['voltage_spread'] = max(voltages) - min(voltages)
    
    if len(sohs) > 1:
        capacities = [(s / 100.0) * 120.0 for s in sohs]
        data['capacity_rolling_std'] = float(np.std(capacities))
        
        cycle_diff = max(1, cycles[0] - cycles[-1])
        data['capacity_degradation_rate'] = (capacities[0] - capacities[-1]) / cycle_diff
        data['cumulative_capacity_loss'] = 120.0 - capacities[0]
        data['resistance_growth_rate'] = (resistances[0] - resistances[-1]) / cycle_diff
        
    data['discharge_rate'] = data['capacity_ah'] / (data['discharge_time_s'] / 3600.0)
    data['impedance_ratio'] = data['charge_transfer_resistance_ohm'] / max(0.001, data['internal_resistance_ohm'])
    data['cycle_age_normalized'] = min(1.0, data['cycle'] / 1000.0)
    
    return data
