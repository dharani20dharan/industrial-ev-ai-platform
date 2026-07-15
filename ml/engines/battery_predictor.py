"""
Battery Health Predictor
========================
Uses XGBoost to predict:
1. State of Health (SoH) - Current battery health percentage
2. Remaining Useful Life (RUL) - Cycles remaining before failure

Trained on NASA Battery PCoE format data.
"""

import numpy as np
import pandas as pd
import os
import json
import joblib
from datetime import datetime
from typing import Dict, Tuple, Optional

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler


class BatteryHealthPredictor:
    """
    XGBoost-based battery health prediction engine.
    
    Two models:
    1. SoH Model: Predicts current State of Health (%)
    2. RUL Model: Predicts Remaining Useful Life (cycles)
    """
    
    def __init__(self):
        self.soh_model = XGBRegressor(
            n_estimators=300,
            max_depth=6,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            reg_alpha=0.1,
            reg_lambda=1.0,
            random_state=42,
            n_jobs=-1
        )
        
        self.rul_model = XGBRegressor(
            n_estimators=400,
            max_depth=7,
            learning_rate=0.03,
            subsample=0.8,
            colsample_bytree=0.8,
            reg_alpha=0.5,
            reg_lambda=2.0,
            min_child_weight=3,
            random_state=42,
            n_jobs=-1
        )
        
        self.soh_scaler = StandardScaler()
        self.rul_scaler = StandardScaler()
        self.feature_columns = []
        self.soh_trained = False
        self.rul_trained = False
        self.training_metrics = {}
    
    def _get_features(self, df: pd.DataFrame) -> list:
        """Select features for prediction models."""
        candidate_features = [
            'cycle', 'capacity_ah', 'avg_voltage_v', 'voltage_charged_v',
            'voltage_discharged_v', 'charge_current_a', 'discharge_current_a',
            'avg_temperature_c', 'max_temperature_c', 'internal_resistance_ohm',
            'charge_transfer_resistance_ohm', 'discharge_time_s',
            'charge_efficiency_percent', 'discharge_slope_v_per_s',
            'capacity_degradation_rate', 'cumulative_capacity_loss',
            'resistance_growth_rate', 'temp_rolling_mean', 'temp_rolling_std',
            'thermal_variance', 'voltage_spread', 'capacity_rolling_std',
            'efficiency_drop', 'discharge_rate', 'impedance_ratio',
            'cycle_age_normalized'
        ]
        return [c for c in candidate_features if c in df.columns]
    
    def train_soh(self, df: pd.DataFrame) -> Dict:
        """
        Train SoH prediction model.
        
        Target: soh_percent (0-100)
        """
        print("\n" + "=" * 50)
        print("Training SoH Prediction Model (XGBoost)")
        print("=" * 50)
        
        self.feature_columns = self._get_features(df)
        
        # Exclude SoH-correlated features that would be "cheating"
        soh_features = [f for f in self.feature_columns 
                       if f not in ['soh_percent', 'rul_cycles']]
        
        X = df[soh_features].values
        y = df['soh_percent'].values
        
        # Scale
        X_scaled = self.soh_scaler.fit_transform(X)
        
        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        
        print(f"[TRAIN] Features: {len(soh_features)}")
        print(f"[TRAIN] Train: {len(X_train)} | Test: {len(X_test)}")
        
        # Train
        self.soh_model.fit(
            X_train, y_train,
            eval_set=[(X_test, y_test)],
            verbose=False
        )
        
        # Evaluate
        y_pred = self.soh_model.predict(X_test)
        
        metrics = {
            'rmse': float(np.sqrt(mean_squared_error(y_test, y_pred))),
            'mae': float(mean_absolute_error(y_test, y_pred)),
            'r2': float(r2_score(y_test, y_pred)),
            'features': soh_features,
            'train_size': len(X_train),
            'test_size': len(X_test),
        }
        
        self.soh_trained = True
        self.training_metrics['soh'] = metrics
        self._soh_features = soh_features
        
        print(f"[RESULT] RMSE: {metrics['rmse']:.3f}")
        print(f"[RESULT] MAE:  {metrics['mae']:.3f}")
        print(f"[RESULT] R2:   {metrics['r2']:.4f}")
        
        # Feature importance
        importances = self.soh_model.feature_importances_
        top_features = sorted(zip(soh_features, importances), 
                            key=lambda x: x[1], reverse=True)[:5]
        print("\n[FEATURES] Top 5 most important:")
        for feat, imp in top_features:
            print(f"  {feat}: {imp:.4f}")
        
        return metrics
    
    def train_rul(self, df: pd.DataFrame) -> Dict:
        """
        Train RUL prediction model.
        
        Target: rul_cycles (remaining cycles to failure)
        """
        print("\n" + "=" * 50)
        print("Training RUL Prediction Model (XGBoost)")
        print("=" * 50)
        
        # RUL features - exclude RUL itself and direct SoH
        rul_features = [f for f in self._get_features(df) 
                       if f not in ['rul_cycles', 'soh_percent']]
        
        X = df[rul_features].values
        y = df['rul_cycles'].values
        
        # Clip RUL to reasonable range
        y = np.clip(y, 0, 1000)
        
        # Scale
        X_scaled = self.rul_scaler.fit_transform(X)
        
        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        
        print(f"[TRAIN] Features: {len(rul_features)}")
        print(f"[TRAIN] Train: {len(X_train)} | Test: {len(X_test)}")
        
        # Train
        self.rul_model.fit(
            X_train, y_train,
            eval_set=[(X_test, y_test)],
            verbose=False
        )
        
        # Evaluate
        y_pred = self.rul_model.predict(X_test)
        y_pred = np.maximum(y_pred, 0)  # RUL can't be negative
        
        metrics = {
            'rmse': float(np.sqrt(mean_squared_error(y_test, y_pred))),
            'mae': float(mean_absolute_error(y_test, y_pred)),
            'r2': float(r2_score(y_test, y_pred)),
            'features': rul_features,
            'train_size': len(X_train),
            'test_size': len(X_test),
        }
        
        self.rul_trained = True
        self.training_metrics['rul'] = metrics
        self._rul_features = rul_features
        
        print(f"[RESULT] RMSE: {metrics['rmse']:.3f} cycles")
        print(f"[RESULT] MAE:  {metrics['mae']:.3f} cycles")
        print(f"[RESULT] R2:   {metrics['r2']:.4f}")
        
        # Feature importance
        importances = self.rul_model.feature_importances_
        top_features = sorted(zip(rul_features, importances),
                            key=lambda x: x[1], reverse=True)[:5]
        print("\n[FEATURES] Top 5 most important:")
        for feat, imp in top_features:
            print(f"  {feat}: {imp:.4f}")
        
        return metrics
    
    def predict_soh(self, data: Dict) -> Dict:
        """Predict SoH for a single battery reading."""
        if not self.soh_trained:
            raise RuntimeError("SoH model not trained")
        
        features = []
        for col in self._soh_features:
            features.append(data.get(col, 0))
        
        X = np.array(features).reshape(1, -1)
        X_scaled = self.soh_scaler.transform(X)
        soh = float(self.soh_model.predict(X_scaled)[0])
        soh = max(0, min(100, soh))
        
        # Health category
        if soh >= 85:
            health_status = 'good'
            recommendation = 'Battery in good condition. Continue normal operation.'
        elif soh >= 70:
            health_status = 'fair'
            recommendation = 'Battery showing wear. Monitor closely and plan replacement.'
        elif soh >= 50:
            health_status = 'poor'
            recommendation = 'Battery significantly degraded. Schedule replacement soon.'
        else:
            health_status = 'critical'
            recommendation = 'Battery near end of life. Replace immediately.'
        
        return {
            'soh_percent': round(soh, 2),
            'health_status': health_status,
            'recommendation': recommendation,
            'confidence': round(self.training_metrics['soh']['r2'] * 100, 1)
        }
    
    def predict_rul(self, data: Dict) -> Dict:
        """Predict RUL for a single battery reading."""
        if not self.rul_trained:
            raise RuntimeError("RUL model not trained")
        
        features = []
        for col in self._rul_features:
            features.append(data.get(col, 0))
        
        X = np.array(features).reshape(1, -1)
        X_scaled = self.rul_scaler.transform(X)
        rul = float(self.rul_model.predict(X_scaled)[0])
        rul = max(0, rul)
        
        # Urgency level
        if rul > 200:
            urgency = 'low'
            action = 'No immediate action required.'
        elif rul > 100:
            urgency = 'medium'
            action = 'Begin planning battery replacement.'
        elif rul > 30:
            urgency = 'high'
            action = 'Order replacement battery. Schedule within 2 weeks.'
        else:
            urgency = 'critical'
            action = 'URGENT: Battery replacement needed immediately.'
        
        # Estimate days (assuming ~2 cycles per day for industrial EVs)
        estimated_days = round(rul / 2)
        
        return {
            'rul_cycles': round(rul, 1),
            'estimated_days': estimated_days,
            'urgency': urgency,
            'action': action,
            'confidence': round(self.training_metrics['rul']['r2'] * 100, 1)
        }
    
    def predict_full(self, data: Dict) -> Dict:
        """Get both SoH and RUL predictions."""
        result = {
            'timestamp': datetime.now().isoformat(),
            'battery_id': data.get('battery_id', 'unknown')
        }
        
        if self.soh_trained:
            result['soh'] = self.predict_soh(data)
        
        if self.rul_trained:
            result['rul'] = self.predict_rul(data)
        
        return result
    
    def predict_batch(self, df: pd.DataFrame) -> pd.DataFrame:
        """Run predictions on a batch of data."""
        df = df.copy()
        
        if self.soh_trained:
            X_soh = df[self._soh_features].values
            X_soh_scaled = self.soh_scaler.transform(X_soh)
            df['predicted_soh'] = self.soh_model.predict(X_soh_scaled)
            df['predicted_soh'] = df['predicted_soh'].clip(0, 100)
        
        if self.rul_trained:
            X_rul = df[self._rul_features].values
            X_rul_scaled = self.rul_scaler.transform(X_rul)
            df['predicted_rul'] = self.rul_model.predict(X_rul_scaled)
            df['predicted_rul'] = df['predicted_rul'].clip(0)
        
        return df
    
    def save(self, model_dir: str):
        """Save all models and metadata."""
        os.makedirs(model_dir, exist_ok=True)
        
        if self.soh_trained:
            joblib.dump(self.soh_model, os.path.join(model_dir, 'soh_model.joblib'))
            joblib.dump(self.soh_scaler, os.path.join(model_dir, 'soh_scaler.joblib'))
        
        if self.rul_trained:
            joblib.dump(self.rul_model, os.path.join(model_dir, 'rul_model.joblib'))
            joblib.dump(self.rul_scaler, os.path.join(model_dir, 'rul_scaler.joblib'))
        
        metadata = {
            'soh_features': getattr(self, '_soh_features', []),
            'rul_features': getattr(self, '_rul_features', []),
            'training_metrics': self.training_metrics,
            'soh_trained': self.soh_trained,
            'rul_trained': self.rul_trained,
            'saved_at': datetime.now().isoformat()
        }
        with open(os.path.join(model_dir, 'battery_predictor_metadata.json'), 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"[SAVE] Battery predictor saved to {model_dir}")
    
    def load(self, model_dir: str):
        """Load trained models."""
        with open(os.path.join(model_dir, 'battery_predictor_metadata.json'), 'r') as f:
            metadata = json.load(f)
        
        self._soh_features = metadata['soh_features']
        self._rul_features = metadata['rul_features']
        self.training_metrics = metadata['training_metrics']
        
        if metadata['soh_trained']:
            self.soh_model = joblib.load(os.path.join(model_dir, 'soh_model.joblib'))
            self.soh_scaler = joblib.load(os.path.join(model_dir, 'soh_scaler.joblib'))
            self.soh_trained = True
        
        if metadata['rul_trained']:
            self.rul_model = joblib.load(os.path.join(model_dir, 'rul_model.joblib'))
            self.rul_scaler = joblib.load(os.path.join(model_dir, 'rul_scaler.joblib'))
            self.rul_trained = True
        
        print(f"[LOAD] Battery predictor loaded from {model_dir}")
        print(f"  SoH model: {'loaded' if self.soh_trained else 'not available'}")
        print(f"  RUL model: {'loaded' if self.rul_trained else 'not available'}")


def train_and_save(data_path: str, model_dir: str):
    """Convenience: train both models and save."""
    df = pd.read_csv(data_path)
    
    predictor = BatteryHealthPredictor()
    
    # Train SoH model
    soh_metrics = predictor.train_soh(df)
    
    # Train RUL model
    rul_metrics = predictor.train_rul(df)
    
    # Save
    predictor.save(model_dir)
    
    # Run batch predictions and save
    df_predicted = predictor.predict_batch(df)
    pred_path = os.path.join(os.path.dirname(data_path), 'battery_predictions.csv')
    df_predicted.to_csv(pred_path, index=False)
    print(f"\n[SAVE] Predictions saved: {pred_path}")
    
    # Print example predictions
    print("\n" + "=" * 50)
    print("Example Predictions")
    print("=" * 50)
    sample = df.iloc[0].to_dict()
    full_pred = predictor.predict_full(sample)
    print(json.dumps(full_pred, indent=2))
    
    return predictor


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'processed', 'battery_features_unscaled.csv')
    model_dir = os.path.join(base_dir, 'models')
    
    if os.path.exists(data_path):
        train_and_save(data_path, model_dir)
    else:
        print(f"[ERROR] Data not found: {data_path}")
        print("Run preprocessing/pipeline.py first!")
