"""
Carbon Intelligence Engine
===========================
Calculates CO2 emissions, diesel vs EV comparisons,
Scope-1/Scope-3 estimation, and fleet sustainability metrics.

Based on EPA GHG emission factors and OWID CO2 datasets.
"""

import numpy as np
import pandas as pd
import os
import json
from datetime import datetime
from typing import Dict, List, Optional


# ============================================================
# EPA/Standard Emission Factors
# ============================================================

# Source: EPA GHG Emission Factors Hub 2025
EMISSION_FACTORS = {
    # Fuel emission factors (kg CO2 per unit)
    'diesel_kg_co2_per_liter': 2.68,       # EPA: 2.68 kg CO2/liter diesel
    'gasoline_kg_co2_per_liter': 2.31,     # EPA: 2.31 kg CO2/liter gasoline
    'cng_kg_co2_per_kg': 2.75,             # Compressed natural gas
    
    # Electricity grid emission factors (kg CO2 per kWh)
    # Varies by region - using common values
    'grid_india_kg_co2_per_kwh': 0.708,     # India grid average
    'grid_us_avg_kg_co2_per_kwh': 0.386,    # US national average
    'grid_eu_avg_kg_co2_per_kwh': 0.276,    # EU average
    'grid_china_kg_co2_per_kwh': 0.555,     # China grid average
    'grid_renewable_kg_co2_per_kwh': 0.020, # Renewable/solar
    
    # Vehicle consumption defaults
    'diesel_truck_l_per_100km': 32.0,       # Medium/heavy duty diesel truck
    'diesel_van_l_per_100km': 12.0,         # Delivery van
    'ev_truck_kwh_per_km': 1.2,             # EV truck consumption
    'ev_van_kwh_per_km': 0.25,              # EV van consumption
    'ev_bus_kwh_per_km': 1.5,               # Electric bus
}

# Vehicle categories
VEHICLE_CATEGORIES = {
    'heavy_truck': {
        'diesel_l_per_100km': 35.0,
        'ev_kwh_per_km': 1.4,
        'payload_tons': 20,
        'annual_km': 80000,
    },
    'medium_truck': {
        'diesel_l_per_100km': 25.0,
        'ev_kwh_per_km': 0.8,
        'payload_tons': 10,
        'annual_km': 60000,
    },
    'delivery_van': {
        'diesel_l_per_100km': 12.0,
        'ev_kwh_per_km': 0.25,
        'payload_tons': 2,
        'annual_km': 40000,
    },
    'bus': {
        'diesel_l_per_100km': 30.0,
        'ev_kwh_per_km': 1.3,
        'payload_tons': 8,
        'annual_km': 70000,
    }
}


class CarbonIntelligenceEngine:
    """
    Calculates and compares carbon emissions between diesel and EV fleets.
    
    Provides:
    - Per-vehicle emission calculations
    - Fleet-wide carbon savings
    - Scope-1 and Scope-3 estimates
    - Sustainability metrics and equivalents
    """
    
    def __init__(self, grid_region: str = 'india'):
        """
        Args:
            grid_region: Electricity grid region for emission factors
                         Options: 'india', 'us', 'eu', 'china', 'renewable'
        """
        grid_key = f'grid_{grid_region}_kg_co2_per_kwh'
        if grid_key not in EMISSION_FACTORS:
            grid_key = 'grid_india_kg_co2_per_kwh'
        
        self.grid_emission_factor = EMISSION_FACTORS[grid_key]
        self.grid_region = grid_region
        self.diesel_factor = EMISSION_FACTORS['diesel_kg_co2_per_liter']
    
    def calculate_diesel_emissions(self, 
                                    distance_km: float,
                                    vehicle_type: str = 'medium_truck',
                                    custom_consumption: Optional[float] = None) -> Dict:
        """
        Calculate CO2 emissions for a diesel vehicle.
        
        Args:
            distance_km: Total distance driven
            vehicle_type: Type of vehicle
            custom_consumption: Override fuel consumption (L/100km)
        """
        category = VEHICLE_CATEGORIES.get(vehicle_type, VEHICLE_CATEGORIES['medium_truck'])
        consumption = custom_consumption or category['diesel_l_per_100km']
        
        # Fuel used
        fuel_liters = distance_km * consumption / 100
        
        # CO2 emissions (Scope 1 - direct combustion)
        co2_kg = fuel_liters * self.diesel_factor
        
        # Well-to-tank emissions (Scope 3 upstream) ~20% additional
        scope3_upstream = co2_kg * 0.20
        
        return {
            'distance_km': distance_km,
            'vehicle_type': vehicle_type,
            'fuel_type': 'diesel',
            'fuel_consumed_liters': round(fuel_liters, 2),
            'consumption_l_per_100km': consumption,
            'scope_1_co2_kg': round(co2_kg, 2),
            'scope_3_upstream_co2_kg': round(scope3_upstream, 2),
            'total_co2_kg': round(co2_kg + scope3_upstream, 2),
            'co2_per_km_kg': round((co2_kg + scope3_upstream) / max(distance_km, 1), 4),
        }
    
    def calculate_ev_emissions(self,
                                distance_km: float,
                                vehicle_type: str = 'medium_truck',
                                custom_consumption: Optional[float] = None,
                                renewable_fraction: float = 0.0) -> Dict:
        """
        Calculate CO2 emissions for an EV.
        
        Args:
            distance_km: Total distance driven
            vehicle_type: Type of vehicle
            custom_consumption: Override energy consumption (kWh/km)
            renewable_fraction: Fraction of charging from renewables (0-1)
        """
        category = VEHICLE_CATEGORIES.get(vehicle_type, VEHICLE_CATEGORIES['medium_truck'])
        consumption = custom_consumption or category['ev_kwh_per_km']
        
        # Energy used
        energy_kwh = distance_km * consumption
        
        # Grid emissions (Scope 2)
        grid_energy = energy_kwh * (1 - renewable_fraction)
        renewable_energy = energy_kwh * renewable_fraction
        
        scope2_co2 = grid_energy * self.grid_emission_factor
        scope2_co2 += renewable_energy * EMISSION_FACTORS['grid_renewable_kg_co2_per_kwh']
        
        # Scope 3: Battery manufacturing lifecycle (~30-40 kg CO2/kWh battery capacity)
        # Amortized over battery life (~200,000 km)
        battery_lifecycle_co2_per_km = 0.05  # kg CO2/km (amortized)
        scope3_co2 = distance_km * battery_lifecycle_co2_per_km
        
        return {
            'distance_km': distance_km,
            'vehicle_type': vehicle_type,
            'fuel_type': 'electric',
            'energy_consumed_kwh': round(energy_kwh, 2),
            'consumption_kwh_per_km': consumption,
            'grid_region': self.grid_region,
            'grid_emission_factor': self.grid_emission_factor,
            'renewable_fraction': renewable_fraction,
            'scope_1_co2_kg': 0,  # EVs have zero direct emissions
            'scope_2_co2_kg': round(scope2_co2, 2),
            'scope_3_battery_co2_kg': round(scope3_co2, 2),
            'total_co2_kg': round(scope2_co2 + scope3_co2, 2),
            'co2_per_km_kg': round((scope2_co2 + scope3_co2) / max(distance_km, 1), 4),
        }
    
    def compare_diesel_vs_ev(self,
                              distance_km: float,
                              vehicle_type: str = 'medium_truck',
                              renewable_fraction: float = 0.0) -> Dict:
        """
        Compare emissions between diesel and EV for the same journey.
        """
        diesel = self.calculate_diesel_emissions(distance_km, vehicle_type)
        ev = self.calculate_ev_emissions(distance_km, vehicle_type, 
                                          renewable_fraction=renewable_fraction)
        
        savings_kg = diesel['total_co2_kg'] - ev['total_co2_kg']
        savings_percent = (savings_kg / max(diesel['total_co2_kg'], 0.001)) * 100
        
        return {
            'diesel': diesel,
            'ev': ev,
            'savings': {
                'co2_saved_kg': round(savings_kg, 2),
                'co2_saved_percent': round(savings_percent, 1),
                'equivalent_trees_year': round(savings_kg / 22, 1),  # 1 tree absorbs ~22kg CO2/year
                'equivalent_gallons_gasoline': round(savings_kg / 8.89, 1),
            }
        }
    
    def analyze_fleet(self, fleet: List[Dict]) -> Dict:
        """
        Analyze carbon impact for an entire fleet.
        
        Args:
            fleet: List of vehicle dicts with keys:
                   'vehicle_id', 'vehicle_type', 'annual_km', 
                   'fuel_type' ('diesel' or 'electric'),
                   'renewable_fraction' (optional)
        """
        results = []
        total_diesel_co2 = 0
        total_ev_co2 = 0
        total_savings = 0
        total_distance = 0
        
        for vehicle in fleet:
            vid = vehicle.get('vehicle_id', 'unknown')
            vtype = vehicle.get('vehicle_type', 'medium_truck')
            annual_km = vehicle.get('annual_km', VEHICLE_CATEGORIES.get(vtype, {}).get('annual_km', 50000))
            fuel_type = vehicle.get('fuel_type', 'electric')
            renewable = vehicle.get('renewable_fraction', 0.0)
            
            comparison = self.compare_diesel_vs_ev(annual_km, vtype, renewable)
            
            results.append({
                'vehicle_id': vid,
                'vehicle_type': vtype,
                'annual_km': annual_km,
                'current_fuel': fuel_type,
                'diesel_co2_tons': round(comparison['diesel']['total_co2_kg'] / 1000, 3),
                'ev_co2_tons': round(comparison['ev']['total_co2_kg'] / 1000, 3),
                'savings_tons': round(comparison['savings']['co2_saved_kg'] / 1000, 3),
                'savings_percent': comparison['savings']['co2_saved_percent'],
            })
            
            total_diesel_co2 += comparison['diesel']['total_co2_kg']
            total_ev_co2 += comparison['ev']['total_co2_kg']
            total_savings += comparison['savings']['co2_saved_kg']
            total_distance += annual_km
        
        fleet_summary = {
            'fleet_size': len(fleet),
            'total_annual_km': total_distance,
            'diesel_scenario': {
                'total_co2_tons': round(total_diesel_co2 / 1000, 2),
                'co2_per_km_g': round(total_diesel_co2 / max(total_distance, 1) * 1000, 1),
            },
            'ev_scenario': {
                'total_co2_tons': round(total_ev_co2 / 1000, 2),
                'co2_per_km_g': round(total_ev_co2 / max(total_distance, 1) * 1000, 1),
            },
            'savings': {
                'co2_saved_tons': round(total_savings / 1000, 2),
                'co2_saved_percent': round(total_savings / max(total_diesel_co2, 1) * 100, 1),
                'equivalent_trees': round(total_savings / 22),
                'equivalent_homes_electricity': round(total_savings / 4000),  # ~4 tons CO2/home/year
                'equivalent_flights_nyc_london': round(total_savings / 1000),  # ~1 ton/flight
            },
            'scope_summary': {
                'scope_1_tons': round(total_diesel_co2 / 1000, 2) if any(v.get('fuel_type') == 'diesel' for v in fleet) else 0,
                'scope_2_tons': round(total_ev_co2 * 0.85 / 1000, 2),
                'scope_3_tons': round(total_ev_co2 * 0.15 / 1000, 2),
            },
            'vehicle_details': results,
            'grid_region': self.grid_region,
            'calculated_at': datetime.now().isoformat()
        }
        
        return fleet_summary
    
    def generate_sample_fleet(self, size: int = 50) -> List[Dict]:
        """Generate a sample fleet for analysis."""
        fleet = []
        vehicle_types = ['heavy_truck', 'medium_truck', 'delivery_van', 'bus']
        weights = [0.2, 0.4, 0.3, 0.1]
        
        for i in range(size):
            vtype = np.random.choice(vehicle_types, p=weights)
            category = VEHICLE_CATEGORIES[vtype]
            
            fleet.append({
                'vehicle_id': f'EV-{i+1:03d}',
                'vehicle_type': vtype,
                'annual_km': int(category['annual_km'] * np.random.uniform(0.7, 1.3)),
                'fuel_type': 'electric',
                'renewable_fraction': np.random.uniform(0.0, 0.3)
            })
        
        return fleet
    
    def save_analysis(self, output_dir: str, fleet: Optional[List[Dict]] = None):
        """Run full analysis and save results."""
        os.makedirs(output_dir, exist_ok=True)
        
        if fleet is None:
            fleet = self.generate_sample_fleet(50)
        
        print("\n" + "=" * 60)
        print("Carbon Intelligence Analysis")
        print("=" * 60)
        
        # Fleet analysis
        summary = self.analyze_fleet(fleet)
        
        print(f"\n  Fleet Size: {summary['fleet_size']}")
        print(f"  Total Annual KM: {summary['total_annual_km']:,}")
        print(f"  Grid Region: {summary['grid_region']}")
        print(f"\n  DIESEL SCENARIO: {summary['diesel_scenario']['total_co2_tons']:.1f} tons CO2/year")
        print(f"  EV SCENARIO:     {summary['ev_scenario']['total_co2_tons']:.1f} tons CO2/year")
        print(f"  CO2 SAVED:       {summary['savings']['co2_saved_tons']:.1f} tons/year ({summary['savings']['co2_saved_percent']:.1f}%)")
        print(f"\n  Equivalents:")
        print(f"    Trees planted: {summary['savings']['equivalent_trees']:,}")
        print(f"    Homes powered: {summary['savings']['equivalent_homes_electricity']}")
        print(f"    NYC-London flights: {summary['savings']['equivalent_flights_nyc_london']}")
        
        # Save results
        with open(os.path.join(output_dir, 'carbon_analysis.json'), 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Save vehicle details as CSV
        df = pd.DataFrame(summary['vehicle_details'])
        df.to_csv(os.path.join(output_dir, 'carbon_vehicle_details.csv'), index=False)
        
        # Example comparison
        print(f"\n  Single Vehicle Comparison (medium_truck, 60,000 km/year):")
        comparison = self.compare_diesel_vs_ev(60000, 'medium_truck')
        print(f"    Diesel: {comparison['diesel']['total_co2_kg']:.0f} kg CO2")
        print(f"    EV:     {comparison['ev']['total_co2_kg']:.0f} kg CO2")
        print(f"    Saved:  {comparison['savings']['co2_saved_kg']:.0f} kg CO2 ({comparison['savings']['co2_saved_percent']:.0f}%)")
        
        with open(os.path.join(output_dir, 'carbon_comparison_example.json'), 'w') as f:
            json.dump(comparison, f, indent=2)
        
        print(f"\n[SAVE] Results saved to {output_dir}")
        
        return summary


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'data', 'processed')
    
    engine = CarbonIntelligenceEngine(grid_region='india')
    engine.save_analysis(output_dir)
