import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class TelemetryPreprocessor:
    def __init__(self):
        self.scaler = MinMaxScaler()
        
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handles null values in timeseries telemetry columns via forward/backward fill."""
        fill_cols = ["voltage", "current", "temperature", "soc"]
        df[fill_cols] = df[fill_cols].ffill().bfill()
        return df

    def filter_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Removes physical impossibilities or noise outliers from sensor readings."""
        # E.g., voltage must be positive, temperatures below extreme limits
        df = df[(df["voltage"] > 0) & (df["voltage"] < 1000)]
        df = df[(df["temperature"] > -40) & (df["temperature"] < 150)]
        return df

    def engineer_battery_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Engineers critical battery health predictors:
        - Capacity degradation
        - Thermal variance (rolling cell temp delta)
        - Average discharge slope (dV/dt)
        - Charging efficiency (energy absorbed per cycle)
        """
        # Ensure chronological ordering
        df = df.sort_values("timestamp")
        
        # 1. Thermal Variance
        df["temp_rolling_var"] = df["temperature"].rolling(window=10, min_periods=1).var()
        
        # 2. Discharge Slope (dV/dt)
        df["time_diff_sec"] = df["timestamp"].diff().dt.total_seconds()
        df["voltage_diff"] = df["voltage"].diff()
        
        # Calculate dV/dt, replacing division-by-zero with zero
        df["discharge_slope"] = np.where(
            df["time_diff_sec"] > 0, 
            df["voltage_diff"] / df["time_diff_sec"], 
            0.0
        )
        
        # 3. Capacity Fade approximation (Ah depletion integration)
        # Ah = current * time_hours
        df["current_hours"] = (df["current"] * (df["time_diff_sec"] / 3600.0)).abs()
        df["capacity_fade"] = df["current_hours"].cumsum()
        
        return df

    def scale_features(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """Scales numeric telemetry features for deep learning/regression models."""
        df[columns] = self.scaler.fit_transform(df[columns])
        return df
