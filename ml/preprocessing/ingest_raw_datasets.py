"""
Raw NASA Dataset Ingestion Script
=================================
Converts downloaded raw NASA datasets (MATLAB .mat files for Battery PCoE,
and space-separated text files for C-MAPSS) into the CSV formats expected by the pipeline.

Ensure you have downloaded:
1. NASA Battery Dataset: https://ti.arc.nasa.gov/c/5/ (e.g. B0005.mat, B0006.mat, etc.)
2. NASA C-MAPSS Dataset: https://ti.arc.nasa.gov/c/6/ (e.g. train_FD001.txt)

Usage:
  python preprocessing/ingest_raw_datasets.py --battery_dir /path/to/mat_files --cmapss_file /path/to/train_FD001.txt
"""

import os
import argparse
import pandas as pd
import numpy as np
import scipy.io
from datetime import datetime

def parse_battery_mat(mat_path):
    """
    Parses a single NASA battery .mat file (e.g., B0005.mat) and extracts cycle-by-cycle summary features.
    """
    mat_dict = scipy.io.loadmat(mat_path)
    # The filename (without extension) is the key to the nested struct
    battery_id = os.path.basename(mat_path).split('.')[0]
    
    # Extract structural contents
    # Structure path: mat_dict[battery_id][0, 0]['cycle'][0]
    cycle_structs = mat_dict[battery_id][0, 0]['cycle'][0]
    
    cycles_data = []
    
    # Track the last seen values to link charge, discharge, and impedance cycles
    current_capacity = None
    current_impedance_re = None
    current_impedance_rct = None
    
    discharge_cycle_counter = 1
    
    # Temporary lists to align charge/discharge characteristics per cycle
    temp_charge_data = {}
    
    for i, cyc in enumerate(cycle_structs):
        cycle_type = cyc['type'][0]
        
        # Datetime conversion (handles formatting variations in .mat files)
        try:
            dt_tuple = cyc['time'][0]
            dt = datetime(
                year=int(dt_tuple[0]),
                month=int(dt_tuple[1]),
                day=int(dt_tuple[2]),
                hour=int(dt_tuple[3]),
                minute=int(dt_tuple[4]),
                second=int(round(dt_tuple[5]))
            )
        except Exception:
            dt = None
            
        data = cyc['data'][0, 0]
        
        if cycle_type == 'charge':
            try:
                # Voltage measured during charge
                v_meas = data['Voltage_measured'][0]
                # Current measured during charge
                c_meas = data['Current_measured'][0]
                # Temp measured during charge
                t_meas = data['Temperature_measured'][0]
                # Charge time
                time_arr = data['Time'][0]
                
                # Compute charge statistics
                temp_charge_data = {
                    'voltage_charged_v': float(np.max(v_meas)),
                    'charge_current_a': float(np.mean(c_meas)),
                    'charge_time_s': float(time_arr[-1] if len(time_arr) > 0 else 0)
                }
            except (KeyError, IndexError, ValueError):
                pass
                
        elif cycle_type == 'impedance':
            try:
                # Extract impedance measurements if present
                r_est = data['Estimated_electrolyte_resistance'][0, 0]
                r_ct = data['Estimated_charge_transfer_resistance'][0, 0]
                current_impedance_re = float(r_est)
                current_impedance_rct = float(r_ct)
            except (KeyError, IndexError, ValueError):
                pass
                
        elif cycle_type == 'discharge':
            try:
                # Capacity is the key performance target in Ampere-hours
                capacity = float(data['Capacity'][0, 0])
                current_capacity = capacity
                
                v_meas = data['Voltage_measured'][0]
                c_meas = data['Current_measured'][0]
                t_meas = data['Temperature_measured'][0]
                time_arr = data['Time'][0]
                
                # Calculate metrics for discharge
                voltage_charged = float(np.max(v_meas))
                voltage_discharged = float(np.min(v_meas))
                avg_voltage = float(np.mean(v_meas))
                avg_temp = float(np.mean(t_meas))
                max_temp = float(np.max(t_meas))
                discharge_current = float(np.mean(c_meas))
                discharge_time = float(time_arr[-1] if len(time_arr) > 0 else 0)
                
                # Compute voltage slope
                if len(time_arr) > 1 and len(v_meas) > 1:
                    slope = (v_meas[-1] - v_meas[0]) / (time_arr[-1] - time_arr[0])
                else:
                    slope = 0.0
                    
                # Recover charge features if they were stored in the previous step
                charge_current = temp_charge_data.get('charge_current_a', 1.5)
                voltage_chg = temp_charge_data.get('voltage_charged_v', 4.2)
                charge_time = temp_charge_data.get('charge_time_s', 3600)
                
                # Calculate charge efficiency
                # Ah discharged / Ah charged
                charge_efficiency = 100.0
                if charge_time > 0 and discharge_time > 0:
                    ah_charged = abs(charge_current) * (charge_time / 3600)
                    ah_discharged = abs(discharge_current) * (discharge_time / 3600)
                    if ah_charged > 0:
                        charge_efficiency = min(100.0, (ah_discharged / ah_charged) * 100)
                
                # SOH calculation: capacity relative to nominal capacity (2.0 Ah)
                soh = (capacity / 2.0) * 100
                
                # Set default resistances if impedance cycle was missing
                re_ohm = current_impedance_re if current_impedance_re is not None else 0.05
                rct_ohm = current_impedance_rct if current_impedance_rct is not None else 0.08
                
                cycles_data.append({
                    'battery_id': battery_id,
                    'cycle': discharge_cycle_counter,
                    'datetime': dt.isoformat() if dt else '',
                    'type': 'summary',
                    'capacity_ah': round(capacity, 4),
                    'soh_percent': round(soh, 2),
                    'voltage_charged_v': round(voltage_chg, 4),
                    'voltage_discharged_v': round(voltage_discharged, 4),
                    'avg_voltage_v': round(avg_voltage, 4),
                    'charge_current_a': round(charge_current, 4),
                    'discharge_current_a': round(discharge_current, 4),
                    'avg_temperature_c': round(avg_temp, 2),
                    'max_temperature_c': round(max_temp, 2),
                    'internal_resistance_ohm': round(re_ohm, 5),
                    'charge_transfer_resistance_ohm': round(rct_ohm, 5),
                    'discharge_time_s': round(discharge_time, 1),
                    'charge_efficiency_percent': round(charge_efficiency, 2),
                    'discharge_slope_v_per_s': round(slope, 6)
                })
                
                discharge_cycle_counter += 1
            except (KeyError, IndexError, ValueError) as e:
                print(f"  [WARN] Skipping a discharge cycle due to read error: {e}")
                
    # Compute Remaining Useful Life (RUL) in cycles back-propagated
    total_cycles = len(cycles_data)
    for idx, item in enumerate(cycles_data):
        item['rul_cycles'] = total_cycles - item['cycle']
        
    return pd.DataFrame(cycles_data)


def ingest_battery_datasets(battery_dir, output_file):
    """
    Ingests all battery .mat files in a directory and consolidates them into a single CSV.
    """
    print(f"\nScanning directory '{battery_dir}' for battery .mat files...")
    
    mat_files = [f for f in os.listdir(battery_dir) if f.lower().endswith('.mat')]
    if not mat_files:
        print("  [ERROR] No .mat files found in the directory!")
        return False
        
    print(f"Found {len(mat_files)} files: {mat_files}")
    all_dfs = []
    
    for f in mat_files:
        path = os.path.join(battery_dir, f)
        print(f"Processing '{f}'...")
        try:
            df = parse_battery_mat(path)
            if not df.empty:
                all_dfs.append(df)
                print(f"  [OK] Extracted {len(df)} cycles for battery {df['battery_id'].iloc[0]}")
            else:
                print(f"  [WARN] Battery file '{f}' returned no cycles.")
        except Exception as e:
            print(f"  [ERROR] Failed to parse '{f}': {e}")
            
    if not all_dfs:
        print("  [ERROR] No battery data could be extracted.")
        return False
        
    combined_df = pd.concat(all_dfs, ignore_index=True)
    
    # Save output CSV
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    combined_df.to_csv(output_file, index=False)
    print(f"\n[SUCCESS] Consolidate battery CSV saved to: {output_file}")
    print(f"Total records: {len(combined_df)}")
    return True


def ingest_cmapss_dataset(txt_file, output_file):
    """
    Ingests the raw space-separated train_FD001.txt C-MAPSS file and converts it to a standard CSV.
    """
    print(f"\nIngesting C-MAPSS dataset from '{txt_file}'...")
    
    if not os.path.exists(txt_file):
        print(f"  [ERROR] File '{txt_file}' does not exist!")
        return False
        
    # Columns definition matching the NASA standard
    columns = ['unit_id', 'cycle', 'op_setting_1', 'op_setting_2', 'op_setting_3']
    for s_idx in range(1, 22):
        columns.append(f's{s_idx}')
        
    try:
        # Read whitespace-delimited file
        df = pd.read_csv(txt_file, sep=r'\s+', header=None)
        
        # The file might have extra trailing empty columns due to trailing spaces, slice first 26 columns
        df = df.iloc[:, :26]
        df.columns = columns
        
        # Add RUL column based on maximum cycles for each unit
        # Real engines in CMAPSS run to failure, so RUL = max_cycles_of_unit - current_cycle
        rul_dict = {}
        for unit_id, group in df.groupby('unit_id'):
            rul_dict[unit_id] = group['cycle'].max()
            
        df['rul'] = df.apply(lambda row: int(rul_dict[row['unit_id']] - row['cycle']), axis=1)
        
        # Save output CSV
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df.to_csv(output_file, index=False)
        print(f"[SUCCESS] Converted C-MAPSS CSV saved to: {output_file}")
        print(f"Total records: {len(df)} engines: {df['unit_id'].nunique()}")
        return True
    except Exception as e:
        print(f"  [ERROR] Failed to ingest C-MAPSS data: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Ingest NASA raw datasets into EV Platform standard formats.")
    parser.add_argument('--battery_dir', type=str, help="Directory containing B0005.mat, B0006.mat, etc.")
    parser.add_argument('--cmapss_file', type=str, help="Path to raw train_FD001.txt file")
    args = parser.parse_args()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    if args.battery_dir:
        output_battery_csv = os.path.join(base_dir, 'data', 'raw', 'battery', 'nasa_battery_data.csv')
        ingest_battery_datasets(args.battery_dir, output_battery_csv)
        
    if args.cmapss_file:
        output_cmapss_csv = os.path.join(base_dir, 'data', 'raw', 'cmapss', 'cmapss_fd001.csv')
        ingest_cmapss_dataset(args.cmapss_file, output_cmapss_csv)
        
    if not args.battery_dir and not args.cmapss_file:
        print("\n[INFO] No arguments provided. To ingest files, specify options.")
        print("Example:")
        print("  python preprocessing/ingest_raw_datasets.py --battery_dir /path/to/extracted/matfiles --cmapss_file /path/to/train_FD001.txt")


if __name__ == '__main__':
    main()
