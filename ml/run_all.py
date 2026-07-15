"""
Master Pipeline Runner
======================
Runs the entire AI/ML pipeline end-to-end:
1. Generate datasets
2. Preprocess data
3. Train anomaly detector
4. Train battery predictor (SoH + RUL)
5. Run supply chain risk scoring
6. Run carbon intelligence analysis
7. Run maintenance recommendations
8. Run fleet readiness assessment
9. Run telemetry simulator demo

Usage: python run_all.py
"""

import os
import sys
import time
import json
from datetime import datetime

# Set base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)


def run_step(step_num, title, func):
    """Run a pipeline step with timing."""
    print(f"\n{'#' * 70}")
    print(f"# STEP {step_num}: {title}")
    print(f"{'#' * 70}")
    start = time.time()
    try:
        result = func()
        elapsed = time.time() - start
        print(f"\n[STEP {step_num} COMPLETE] {title} ({elapsed:.1f}s)")
        return result
    except Exception as e:
        elapsed = time.time() - start
        print(f"\n[STEP {step_num} FAILED] {title} ({elapsed:.1f}s)")
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
        return None





def step2_preprocess():
    """Run preprocessing pipeline."""
    from preprocessing.pipeline import BatteryPreprocessor, CMAPSSPreprocessor
    
    raw_dir = os.path.join(BASE_DIR, 'data', 'raw')
    processed_dir = os.path.join(BASE_DIR, 'data', 'processed')
    os.makedirs(processed_dir, exist_ok=True)
    
    # Battery preprocessing
    battery_proc = BatteryPreprocessor()
    battery_path = os.path.join(raw_dir, 'battery', 'nasa_battery_data.csv')
    battery_proc.process(battery_path, processed_dir)
    
    # C-MAPSS preprocessing
    cmapss_path = os.path.join(raw_dir, 'cmapss', 'cmapss_fd001.csv')
    if os.path.exists(cmapss_path):
        cmapss_proc = CMAPSSPreprocessor()
        cmapss_proc.process(cmapss_path, processed_dir)
    else:
        print("\n  [INFO] C-MAPSS dataset (cmapss_fd001.csv) not found in data/raw/cmapss/. Skipping C-MAPSS preprocessing.")


def step3_train_anomaly_detector():
    """Train Isolation Forest anomaly detector."""
    from engines.anomaly_detector import train_and_save
    
    data_path = os.path.join(BASE_DIR, 'data', 'processed', 'battery_features_unscaled.csv')
    model_dir = os.path.join(BASE_DIR, 'models')
    return train_and_save(data_path, model_dir)


def step4_train_battery_predictor():
    """Train XGBoost SoH and RUL models."""
    from engines.battery_predictor import train_and_save
    
    data_path = os.path.join(BASE_DIR, 'data', 'processed', 'battery_features_unscaled.csv')
    model_dir = os.path.join(BASE_DIR, 'models')
    return train_and_save(data_path, model_dir)


def step5_supply_chain_risk():
    """Run supply chain risk scoring."""
    from engines.risk_scorer import SupplyChainRiskScorer
    
    output_dir = os.path.join(BASE_DIR, 'data', 'processed')
    scorer = SupplyChainRiskScorer()
    scorer.save_results(output_dir)


def step6_carbon_intelligence():
    """Run carbon intelligence analysis."""
    from engines.carbon_engine import CarbonIntelligenceEngine
    
    output_dir = os.path.join(BASE_DIR, 'data', 'processed')
    engine = CarbonIntelligenceEngine(grid_region='india')
    engine.save_analysis(output_dir)


def step7_maintenance_recommendations():
    """Run maintenance recommendation engine."""
    from engines.maintenance_engine import MaintenanceRecommendationEngine
    
    output_dir = os.path.join(BASE_DIR, 'data', 'processed')
    engine = MaintenanceRecommendationEngine()
    engine.save_analysis(output_dir)


def step8_fleet_readiness():
    """Run fleet electrification readiness assessment."""
    from engines.readiness_scorer import FleetReadinessScorer
    
    output_dir = os.path.join(BASE_DIR, 'data', 'processed')
    scorer = FleetReadinessScorer()
    scorer.save_assessment(output_dir)


def step9_simulator_demo():
    """Run a short telemetry simulator demo."""
    from simulator.ev_telemetry_simulator import EVFleetSimulator
    
    sim = EVFleetSimulator(num_vehicles=5, output_mode='file')
    sim.run(duration_seconds=6, interval=2.0)


def print_final_summary():
    """Print final summary of all outputs."""
    print(f"\n{'=' * 70}")
    print(f"{'=' * 70}")
    print("   AI/ML PIPELINE COMPLETE - Industrial EV Intelligence Platform")
    print(f"{'=' * 70}")
    print(f"{'=' * 70}")
    
    # List all outputs
    processed_dir = os.path.join(BASE_DIR, 'data', 'processed')
    model_dir = os.path.join(BASE_DIR, 'models')
    
    print(f"\n  PROCESSED DATA ({processed_dir}):")
    if os.path.exists(processed_dir):
        for f in sorted(os.listdir(processed_dir)):
            size = os.path.getsize(os.path.join(processed_dir, f)) / 1024
            print(f"    {f:50s} {size:8.1f} KB")
    
    print(f"\n  TRAINED MODELS ({model_dir}):")
    if os.path.exists(model_dir):
        for f in sorted(os.listdir(model_dir)):
            size = os.path.getsize(os.path.join(model_dir, f)) / 1024
            print(f"    {f:50s} {size:8.1f} KB")
    
    print(f"\n  PIPELINE OUTPUTS:")
    key_outputs = [
        ('Anomaly Scores', 'battery_anomaly_scores.csv'),
        ('Battery Predictions', 'battery_predictions.csv'),
        ('Supply Chain Risk', 'supply_chain_risk_scores.json'),
        ('Cascading Failure', 'cascading_failure_analysis.json'),
        ('Carbon Analysis', 'carbon_analysis.json'),
        ('Maintenance Recs', 'maintenance_recommendations.json'),
        ('Fleet Readiness', 'fleet_readiness_assessment.json'),
        ('Supply Chain Graph', 'supply_chain_graph.json'),
        ('Simulated Telemetry', 'simulated_telemetry.json'),
    ]
    
    for name, filename in key_outputs:
        path = os.path.join(processed_dir, filename)
        status = "OK" if os.path.exists(path) else "MISSING"
        print(f"    [{status:7s}] {name:25s} -> {filename}")
    
    print(f"\n  Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """Run the complete AI/ML pipeline."""
    print("=" * 70)
    print("  Industrial EV AI Platform - Complete AI/ML Pipeline")
    print("  Member 3 Deliverables")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    total_start = time.time()
    
    run_step(1, "Preprocess & Feature Engineering", step2_preprocess)
    run_step(2, "Train Anomaly Detector (Isolation Forest)", step3_train_anomaly_detector)
    run_step(3, "Train Battery Predictor (XGBoost SoH + RUL)", step4_train_battery_predictor)
    run_step(4, "Supply Chain Risk Scoring", step5_supply_chain_risk)
    run_step(5, "Carbon Intelligence Analysis", step6_carbon_intelligence)
    run_step(6, "Maintenance Recommendations", step7_maintenance_recommendations)
    run_step(7, "Fleet Electrification Readiness", step8_fleet_readiness)
    run_step(8, "Telemetry Simulator Demo", step9_simulator_demo)
    
    total_elapsed = time.time() - total_start
    
    print_final_summary()
    print(f"\n  Total pipeline time: {total_elapsed:.1f} seconds")
    print("\n  All Member 3 deliverables complete!")


if __name__ == '__main__':
    main()
