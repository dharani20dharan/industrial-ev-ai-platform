"""
Preprocessing Pipeline
=====================
Cleans raw NASA battery and C-MAPSS data, engineers features, 
and produces ML-ready datasets.
"""

import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import joblib
import json


class BatteryPreprocessor:
    """Preprocesses NASA Battery PCoE data for ML models."""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.feature_columns = []
    
    def load_data(self, filepath: str) -> pd.DataFrame:
        """Load raw battery CSV data."""
        df = pd.read_csv(filepath)
        print(f"[LOAD] Battery data: {len(df)} records, {df['battery_id'].nunique()} batteries")
        return df
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values, outliers, and data quality issues."""
        original_len = len(df)
        
        # Drop rows with NaN in critical columns
        critical_cols = ['capacity_ah', 'soh_percent', 'avg_voltage_v', 
                        'avg_temperature_c', 'internal_resistance_ohm']
        df = df.dropna(subset=critical_cols)
        
        # Remove physically impossible values
        df = df[df['capacity_ah'] > 0]
        df = df[df['soh_percent'] > 0]
        df = df[df['soh_percent'] <= 110]  # Allow slight over 100 for measurement noise
        df = df[df['avg_temperature_c'] > -20]  # Realistic temp range
        df = df[df['avg_temperature_c'] < 80]
        df = df[df['internal_resistance_ohm'] > 0]
        df = df[df['avg_voltage_v'] > 2.0]
        df = df[df['avg_voltage_v'] < 5.0]
        
        dropped = original_len - len(df)
        if dropped > 0:
            print(f"[CLEAN] Dropped {dropped} invalid rows ({dropped/original_len*100:.1f}%)")
        else:
            print("[CLEAN] No invalid rows found")
        
        return df.reset_index(drop=True)
    
    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create derived features for ML models."""
        print("[FEATURES] Engineering battery features...")
        
        # Per-battery rolling features
        engineered = []
        for battery_id, group in df.groupby('battery_id'):
            group = group.sort_values('cycle').copy()
            
            # 1. Capacity degradation rate (capacity loss per cycle)
            group['capacity_degradation_rate'] = group['capacity_ah'].diff() / group['cycle'].diff()
            
            # 2. Cumulative capacity loss
            initial_capacity = group['capacity_ah'].iloc[0]
            group['cumulative_capacity_loss'] = initial_capacity - group['capacity_ah']
            
            # 3. Resistance growth rate
            group['resistance_growth_rate'] = group['internal_resistance_ohm'].diff() / group['cycle'].diff()
            
            # 4. Rolling temperature statistics (window=10 cycles)
            group['temp_rolling_mean'] = group['avg_temperature_c'].rolling(10, min_periods=1).mean()
            group['temp_rolling_std'] = group['avg_temperature_c'].rolling(10, min_periods=1).std().fillna(0)
            group['thermal_variance'] = group['avg_temperature_c'].rolling(20, min_periods=1).var().fillna(0)
            
            # 5. Voltage spread (charged - discharged)
            group['voltage_spread'] = group['voltage_charged_v'] - group['voltage_discharged_v']
            
            # 6. Rolling capacity statistics
            group['capacity_rolling_std'] = group['capacity_ah'].rolling(10, min_periods=1).std().fillna(0)
            
            # 7. Efficiency trend
            group['efficiency_drop'] = group['charge_efficiency_percent'].iloc[0] - group['charge_efficiency_percent']
            
            # 8. Discharge rate (capacity / time)
            group['discharge_rate'] = group['capacity_ah'] / (group['discharge_time_s'] / 3600)
            
            # 9. Impedance ratio (charge transfer / internal)
            group['impedance_ratio'] = group['charge_transfer_resistance_ohm'] / group['internal_resistance_ohm']
            
            # 10. Cycle age (normalized 0-1)
            max_cycle = group['cycle'].max()
            group['cycle_age_normalized'] = group['cycle'] / max_cycle
            
            engineered.append(group)
        
        result = pd.concat(engineered, ignore_index=True)
        
        # Fill NaN from diff operations
        result = result.fillna(0)
        
        print(f"[FEATURES] Created {len(result.columns) - len(df.columns)} new features")
        return result
    
    def get_ml_features(self) -> list:
        """Return the list of features used for ML training."""
        return [
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
    
    def scale_features(self, df: pd.DataFrame, fit: bool = True) -> pd.DataFrame:
        """Scale features using StandardScaler."""
        feature_cols = self.get_ml_features()
        self.feature_columns = feature_cols
        
        available_cols = [c for c in feature_cols if c in df.columns]
        
        if fit:
            df[available_cols] = self.scaler.fit_transform(df[available_cols])
        else:
            df[available_cols] = self.scaler.transform(df[available_cols])
        
        print(f"[SCALE] Scaled {len(available_cols)} features")
        return df
    
    def process(self, filepath: str, output_dir: str) -> pd.DataFrame:
        """Full preprocessing pipeline."""
        print("\n" + "=" * 50)
        print("Battery Data Preprocessing Pipeline")
        print("=" * 50)
        
        df = self.load_data(filepath)
        df = self.clean(df)
        df = self.engineer_features(df)
        
        # Save unscaled version (for visualization)
        unscaled_path = os.path.join(output_dir, 'battery_features_unscaled.csv')
        df.to_csv(unscaled_path, index=False)
        print(f"[SAVE] Unscaled features: {unscaled_path}")
        
        # Save scaled version (for ML)
        df_scaled = df.copy()
        df_scaled = self.scale_features(df_scaled, fit=True)
        scaled_path = os.path.join(output_dir, 'battery_features_scaled.csv')
        df_scaled.to_csv(scaled_path, index=False)
        print(f"[SAVE] Scaled features: {scaled_path}")
        
        # Save scaler
        scaler_path = os.path.join(output_dir, 'battery_scaler.joblib')
        joblib.dump(self.scaler, scaler_path)
        print(f"[SAVE] Scaler: {scaler_path}")
        
        return df  # Return unscaled


class CMAPSSPreprocessor:
    """Preprocesses NASA C-MAPSS data for RUL prediction."""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.sensor_columns = [f's{i}' for i in range(1, 22)]
        self.op_columns = ['op_setting_1', 'op_setting_2', 'op_setting_3']
    
    def load_data(self, filepath: str) -> pd.DataFrame:
        """Load raw C-MAPSS CSV data."""
        df = pd.read_csv(filepath)
        print(f"[LOAD] C-MAPSS data: {len(df)} records, {df['unit_id'].nunique()} engines")
        return df
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove constant sensors and clean data."""
        # Identify constant or near-constant sensors (std < 0.001)
        constant_sensors = []
        for col in self.sensor_columns:
            if df[col].std() < 0.001:
                constant_sensors.append(col)
        
        if constant_sensors:
            print(f"[CLEAN] Removing {len(constant_sensors)} near-constant sensors: {constant_sensors}")
            self.sensor_columns = [s for s in self.sensor_columns if s not in constant_sensors]
        
        return df
    
    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Engineer features from C-MAPSS sensor data."""
        print("[FEATURES] Engineering C-MAPSS features...")
        
        engineered = []
        for unit_id, group in df.groupby('unit_id'):
            group = group.sort_values('cycle').copy()
            
            # Rolling statistics for each sensor
            for sensor in self.sensor_columns:
                group[f'{sensor}_rolling_mean'] = group[sensor].rolling(5, min_periods=1).mean()
                group[f'{sensor}_rolling_std'] = group[sensor].rolling(5, min_periods=1).std().fillna(0)
            
            # Normalized cycle (0-1 progress through life)
            group['cycle_normalized'] = group['cycle'] / group['cycle'].max()
            
            engineered.append(group)
        
        result = pd.concat(engineered, ignore_index=True).fillna(0)
        new_features = len(result.columns) - len(df.columns)
        print(f"[FEATURES] Created {new_features} new features")
        return result
    
    def process(self, filepath: str, output_dir: str) -> pd.DataFrame:
        """Full C-MAPSS preprocessing pipeline."""
        print("\n" + "=" * 50)
        print("C-MAPSS Data Preprocessing Pipeline")
        print("=" * 50)
        
        df = self.load_data(filepath)
        df = self.clean(df)
        df = self.engineer_features(df)
        
        # Save processed data
        output_path = os.path.join(output_dir, 'cmapss_processed.csv')
        df.to_csv(output_path, index=False)
        print(f"[SAVE] Processed C-MAPSS: {output_path}")
        
        return df


def main():
    """Run all preprocessing pipelines."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(base_dir, 'data', 'raw')
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    os.makedirs(processed_dir, exist_ok=True)
    
    # Process Battery Data
    battery_proc = BatteryPreprocessor()
    battery_path = os.path.join(raw_dir, 'battery', 'nasa_battery_data.csv')
    battery_df = battery_proc.process(battery_path, processed_dir)
    
    # Process C-MAPSS Data
    cmapss_path = os.path.join(raw_dir, 'cmapss', 'cmapss_fd001.csv')
    if os.path.exists(cmapss_path):
        cmapss_proc = CMAPSSPreprocessor()
        cmapss_df = cmapss_proc.process(cmapss_path, processed_dir)
    else:
        print("\n[INFO] C-MAPSS dataset (cmapss_fd001.csv) not found. Skipping CMAPSS preprocessing.")
    
    print("\n" + "=" * 50)
    print("[DONE] All preprocessing complete!")
    print("=" * 50)
    print(f"\nProcessed files in: {processed_dir}")
    for f in os.listdir(processed_dir):
        fpath = os.path.join(processed_dir, f)
        size_kb = os.path.getsize(fpath) / 1024
        print(f"  - {f} ({size_kb:.1f} KB)")


if __name__ == '__main__':
    main()
