"""
Anomaly Detection Engine
========================
Uses Isolation Forest to detect anomalous battery behavior in real-time.
Detects: thermal spikes, voltage anomalies, current surges, SoC inconsistencies.
"""

import numpy as np
import pandas as pd
import os
import json
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class AnomalyDetector:
    """
    Isolation Forest-based anomaly detection for EV battery telemetry.
    
    How Isolation Forest works:
    - Builds random trees by randomly selecting features and split values
    - Anomalies are isolated in fewer splits (shorter path length)
    - Normal points need more splits to be isolated (longer path length)
    - Score: -1 = anomaly, 1 = normal (or continuous score)
    """
    
    def __init__(self, contamination: float = 0.05):
        """
        Args:
            contamination: Expected proportion of anomalies (0.01-0.1)
        """
        self.model = IsolationForest(
            n_estimators=200,
            contamination=contamination,
            max_features=0.8,
            bootstrap=True,
            random_state=42,
            n_jobs=-1
        )
        self.scaler = StandardScaler()
        self.is_trained = False
        self.feature_columns = []
        self.thresholds = {}
        
        # Physical limit thresholds for rule-based detection
        self.physical_limits = {
            'temperature_max': 55.0,       # Celsius - critical thermal
            'temperature_warning': 45.0,    # Celsius - warning
            'voltage_min': 300.0,           # Volts - pack level
            'voltage_max': 420.0,           # Volts - pack level
            'current_max': 250.0,           # Amps - max discharge
            'soc_drop_max': 15.0,           # % per reading - impossible drop
            'soc_min': 3.0,                 # % - deep discharge danger
        }
    
    def _get_training_features(self, df: pd.DataFrame) -> List[str]:
        """Get feature columns for anomaly detection."""
        candidate_features = [
            'capacity_ah', 'avg_voltage_v', 'voltage_charged_v', 'voltage_discharged_v',
            'avg_temperature_c', 'max_temperature_c', 'internal_resistance_ohm',
            'charge_transfer_resistance_ohm', 'discharge_time_s',
            'charge_efficiency_percent', 'discharge_slope_v_per_s',
            'capacity_degradation_rate', 'thermal_variance', 'voltage_spread',
            'resistance_growth_rate', 'temp_rolling_std'
        ]
        return [c for c in candidate_features if c in df.columns]
    
    def train(self, df: pd.DataFrame) -> dict:
        """
        Train the Isolation Forest on battery telemetry data.
        
        Args:
            df: DataFrame with battery features (from preprocessing pipeline)
        
        Returns:
            Training summary with metrics
        """
        print("\n" + "=" * 50)
        print("Training Anomaly Detection Model")
        print("=" * 50)
        
        self.feature_columns = self._get_training_features(df)
        X = df[self.feature_columns].values
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        print(f"[TRAIN] Features: {len(self.feature_columns)}")
        print(f"[TRAIN] Samples: {len(X_scaled)}")
        
        # Train Isolation Forest
        self.model.fit(X_scaled)
        self.is_trained = True
        
        # Get anomaly scores for training data
        scores = self.model.decision_function(X_scaled)
        predictions = self.model.predict(X_scaled)
        
        num_anomalies = (predictions == -1).sum()
        anomaly_rate = num_anomalies / len(predictions) * 100
        
        # Compute threshold statistics
        self.thresholds = {
            'score_mean': float(np.mean(scores)),
            'score_std': float(np.std(scores)),
            'score_min': float(np.min(scores)),
            'score_max': float(np.max(scores)),
            'anomaly_threshold': float(np.percentile(scores, 5)),  # Bottom 5%
            'warning_threshold': float(np.percentile(scores, 10)),  # Bottom 10%
        }
        
        summary = {
            'total_samples': len(X_scaled),
            'anomalies_detected': int(num_anomalies),
            'anomaly_rate_percent': round(anomaly_rate, 2),
            'features_used': self.feature_columns,
            'thresholds': self.thresholds,
            'trained_at': datetime.now().isoformat()
        }
        
        print(f"[TRAIN] Anomalies detected: {num_anomalies} ({anomaly_rate:.1f}%)")
        print(f"[TRAIN] Score range: [{scores.min():.3f}, {scores.max():.3f}]")
        print(f"[TRAIN] Anomaly threshold: {self.thresholds['anomaly_threshold']:.3f}")
        
        return summary
    
    def predict(self, data: Dict) -> Dict:
        """
        Predict anomaly for a single telemetry reading.
        
        Combines:
        1. Isolation Forest ML score
        2. Rule-based physical limit checks
        
        Args:
            data: Dict with battery telemetry values
        
        Returns:
            Dict with anomaly score, type, severity, and recommendations
        """
        result = {
            'is_anomaly': False,
            'anomaly_score': 0.0,
            'anomaly_types': [],
            'severity': 'normal',
            'severity_score': 0.0,
            'alerts': [],
            'recommendations': []
        }
        
        # --- Rule-based detection (always active) ---
        self._check_physical_limits(data, result)
        
        # --- ML-based detection (if trained) ---
        if self.is_trained:
            ml_result = self._ml_predict(data)
            result['ml_anomaly_score'] = ml_result['score']
            result['ml_is_anomaly'] = ml_result['is_anomaly']
            
            if ml_result['is_anomaly']:
                result['is_anomaly'] = True
                result['anomaly_types'].append('ml_detected')
                result['alerts'].append(f"ML anomaly score: {ml_result['score']:.3f}")
        
        # --- Combine scores ---
        rule_severity = result['severity_score']
        ml_severity = (1 - result.get('ml_anomaly_score', 0.5)) if self.is_trained else 0
        result['anomaly_score'] = max(rule_severity, ml_severity)
        
        # Determine overall severity
        score = result['anomaly_score']
        if score >= 0.8:
            result['severity'] = 'critical'
        elif score >= 0.5:
            result['severity'] = 'high'
        elif score >= 0.3:
            result['severity'] = 'medium'
        elif score > 0:
            result['severity'] = 'low'
        else:
            result['severity'] = 'normal'
        
        return result
    
    def _check_physical_limits(self, data: Dict, result: Dict):
        """Check against physical limits and thresholds."""
        temp = data.get('temperature', data.get('avg_temperature_c', 0))
        voltage = data.get('voltage', data.get('avg_voltage_v', 0))
        current = data.get('current', 0)
        soc = data.get('soc', data.get('soc_percent', 50))
        
        # Temperature checks
        if temp > self.physical_limits['temperature_max']:
            result['is_anomaly'] = True
            result['anomaly_types'].append('critical_thermal')
            result['severity_score'] = max(result['severity_score'], 0.95)
            result['alerts'].append(f"CRITICAL: Temperature {temp:.1f}C exceeds {self.physical_limits['temperature_max']}C")
            result['recommendations'].append("IMMEDIATE: Shut down vehicle and cool battery")
        elif temp > self.physical_limits['temperature_warning']:
            result['is_anomaly'] = True
            result['anomaly_types'].append('thermal_warning')
            result['severity_score'] = max(result['severity_score'], 0.6)
            result['alerts'].append(f"WARNING: Temperature {temp:.1f}C approaching critical")
            result['recommendations'].append("Reduce load and monitor temperature closely")
        
        # Voltage checks (pack level)
        if voltage > 0:  # Only check if voltage data exists
            if voltage < self.physical_limits['voltage_min']:
                result['is_anomaly'] = True
                result['anomaly_types'].append('under_voltage')
                result['severity_score'] = max(result['severity_score'], 0.7)
                result['alerts'].append(f"Under-voltage: {voltage:.1f}V")
                result['recommendations'].append("Stop discharging immediately")
            elif voltage > self.physical_limits['voltage_max']:
                result['is_anomaly'] = True
                result['anomaly_types'].append('over_voltage')
                result['severity_score'] = max(result['severity_score'], 0.8)
                result['alerts'].append(f"Over-voltage: {voltage:.1f}V")
                result['recommendations'].append("Disconnect charger immediately")
        
        # Current checks
        if abs(current) > self.physical_limits['current_max']:
            result['is_anomaly'] = True
            result['anomaly_types'].append('current_surge')
            result['severity_score'] = max(result['severity_score'], 0.75)
            result['alerts'].append(f"Current surge: {current:.1f}A")
            result['recommendations'].append("Check for short circuit or load issues")
        
        # SoC checks
        if soc < self.physical_limits['soc_min']:
            result['is_anomaly'] = True
            result['anomaly_types'].append('deep_discharge')
            result['severity_score'] = max(result['severity_score'], 0.6)
            result['alerts'].append(f"Deep discharge: SoC at {soc:.1f}%")
            result['recommendations'].append("Charge immediately to prevent damage")
    
    def _ml_predict(self, data: Dict) -> Dict:
        """Run Isolation Forest prediction on a single sample."""
        # Map input data to feature columns
        feature_values = []
        for col in self.feature_columns:
            # Handle both raw telemetry and preprocessed data formats
            key_mapping = {
                'avg_temperature_c': data.get('temperature', data.get('avg_temperature_c', 30)),
                'max_temperature_c': data.get('max_temperature', data.get('max_temperature_c', 35)),
                'avg_voltage_v': data.get('voltage', data.get('avg_voltage_v', 3.5)),
                'capacity_ah': data.get('capacity', data.get('capacity_ah', 1.8)),
                'internal_resistance_ohm': data.get('internal_resistance', data.get('internal_resistance_ohm', 0.04)),
            }
            value = key_mapping.get(col, data.get(col, 0))
            feature_values.append(value)
        
        X = np.array(feature_values).reshape(1, -1)
        X_scaled = self.scaler.transform(X)
        
        score = self.model.decision_function(X_scaled)[0]
        prediction = self.model.predict(X_scaled)[0]
        
        return {
            'score': float(score),
            'is_anomaly': prediction == -1
        }
    
    def predict_batch(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Run anomaly detection on a batch of data.
        
        Returns DataFrame with anomaly scores and labels.
        """
        if not self.is_trained:
            raise RuntimeError("Model not trained. Call train() first.")
        
        X = df[self.feature_columns].values
        X_scaled = self.scaler.transform(X)
        
        scores = self.model.decision_function(X_scaled)
        predictions = self.model.predict(X_scaled)
        
        df = df.copy()
        df['anomaly_score'] = scores
        df['is_anomaly'] = predictions == -1
        df['anomaly_severity'] = df['anomaly_score'].apply(
            lambda s: 'critical' if s < self.thresholds.get('anomaly_threshold', -0.1) else
                      'warning' if s < self.thresholds.get('warning_threshold', 0) else 'normal'
        )
        
        return df
    
    def save(self, model_dir: str):
        """Save the trained model and scaler."""
        os.makedirs(model_dir, exist_ok=True)
        
        joblib.dump(self.model, os.path.join(model_dir, 'anomaly_detector.joblib'))
        joblib.dump(self.scaler, os.path.join(model_dir, 'anomaly_scaler.joblib'))
        
        metadata = {
            'feature_columns': self.feature_columns,
            'thresholds': self.thresholds,
            'physical_limits': self.physical_limits,
            'saved_at': datetime.now().isoformat()
        }
        with open(os.path.join(model_dir, 'anomaly_metadata.json'), 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"[SAVE] Anomaly detector saved to {model_dir}")
    
    def load(self, model_dir: str):
        """Load a trained model."""
        self.model = joblib.load(os.path.join(model_dir, 'anomaly_detector.joblib'))
        self.scaler = joblib.load(os.path.join(model_dir, 'anomaly_scaler.joblib'))
        
        with open(os.path.join(model_dir, 'anomaly_metadata.json'), 'r') as f:
            metadata = json.load(f)
        
        self.feature_columns = metadata['feature_columns']
        self.thresholds = metadata['thresholds']
        self.physical_limits = metadata['physical_limits']
        self.is_trained = True
        
        print(f"[LOAD] Anomaly detector loaded from {model_dir}")


def train_and_save(data_path: str, model_dir: str):
    """Convenience function to train and save the anomaly detector."""
    df = pd.read_csv(data_path)
    
    detector = AnomalyDetector(contamination=0.05)
    summary = detector.train(df)
    
    # Run batch prediction on training data
    df_scored = detector.predict_batch(df)
    anomalies = df_scored[df_scored['is_anomaly']]
    
    print(f"\n[RESULT] Found {len(anomalies)} anomalous readings in training data")
    if len(anomalies) > 0:
        print(f"[RESULT] Anomaly distribution by battery:")
        for bid, group in anomalies.groupby('battery_id'):
            print(f"  {bid}: {len(group)} anomalies")
    
    detector.save(model_dir)
    
    # Save scored data
    scored_path = os.path.join(os.path.dirname(data_path), 'battery_anomaly_scores.csv')
    df_scored.to_csv(scored_path, index=False)
    print(f"[SAVE] Scored data: {scored_path}")
    
    return detector, summary


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'processed', 'battery_features_unscaled.csv')
    model_dir = os.path.join(base_dir, 'models')
    
    if os.path.exists(data_path):
        train_and_save(data_path, model_dir)
    else:
        print(f"[ERROR] Data not found: {data_path}")
        print("Run preprocessing/pipeline.py first!")
