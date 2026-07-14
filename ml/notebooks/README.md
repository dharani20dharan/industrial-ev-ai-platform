# AI/ML Engineering Notebooks

This folder is designated for exploratory data analysis (EDA), statistical tests, and machine learning model training notebooks (Member 3).

## Recommended Notebook Workflow

### 1. `01_exploratory_data_analysis.ipynb`
- Load and parse datasets: NASA Battery Dataset, Oxford Battery Dataset, NASA C-MAPSS.
- Telemetry profiling: Voltage, Current, Temperature, Capacity Fade, Cycle Count.
- Target derivation: Calculate remaining load cycles before cell capacity hits the 80% degradation threshold.

### 2. `02_model_training_and_evaluation.ipynb`
- Train XGBoost models for Remaining Useful Life (RUL) regression predictions.
- Train Isolation Forest models for real-time anomaly alerts (detecting thermal risks, cell voltage disparities, abnormal charging curves).
- Export trained model weights to production assets (`ml/models/`).
