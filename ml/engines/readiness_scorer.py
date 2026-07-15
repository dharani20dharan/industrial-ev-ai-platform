"""
Fleet Electrification Readiness Scorer
=======================================
Scores how ready each route/vehicle in a fleet is to transition 
from diesel to electric, based on:
- Route distance vs EV range
- Charging infrastructure availability
- Payload impact on range
- Dwell time at depots (charging opportunity)
- Duty cycle intensity
"""

import numpy as np
import json
import os
from datetime import datetime
from typing import Dict, List, Optional


# EV specifications for different vehicle types
EV_SPECS = {
    'heavy_truck': {
        'battery_kwh': 300,
        'range_km': 300,
        'charge_rate_kw': 150,  # DC fast
        'range_reduction_per_ton': 5,  # km lost per ton payload
        'min_soc_threshold': 15,  # Don't go below 15%
    },
    'medium_truck': {
        'battery_kwh': 150,
        'range_km': 250,
        'charge_rate_kw': 100,
        'range_reduction_per_ton': 8,
        'min_soc_threshold': 15,
    },
    'delivery_van': {
        'battery_kwh': 75,
        'range_km': 200,
        'charge_rate_kw': 50,
        'range_reduction_per_ton': 15,
        'min_soc_threshold': 10,
    },
    'bus': {
        'battery_kwh': 200,
        'range_km': 250,
        'charge_rate_kw': 120,
        'range_reduction_per_ton': 6,
        'min_soc_threshold': 15,
    }
}


class FleetReadinessScorer:
    """
    Scores fleet electrification readiness using multiple factors.
    
    Score 0-100:
    - 80-100: Immediately ready for electrification
    - 60-79:  Ready with minor infrastructure additions
    - 40-59:  Feasible with planning and investment
    - 20-39:  Challenging, requires significant changes
    - 0-19:   Not currently feasible
    """
    
    # Factor weights
    WEIGHTS = {
        'range_feasibility': 0.25,
        'charging_availability': 0.25,
        'payload_impact': 0.20,
        'dwell_time': 0.15,
        'duty_cycle': 0.15,
    }
    
    def __init__(self):
        self.assessments = []
    
    def score_route(self, route: Dict) -> Dict:
        """
        Score electrification readiness for a single route.
        
        Args:
            route: Dict with:
                - route_id: str
                - route_name: str (optional)
                - total_distance_km: float
                - vehicle_type: str
                - avg_payload_tons: float
                - max_payload_tons: float
                - charging_stations_along_route: int
                - has_depot_charging: bool
                - depot_dwell_hours: float (time spent at depot)
                - stops_count: int
                - avg_stop_duration_hours: float
                - daily_trips: int
                - terrain: str ('flat', 'hilly', 'mountainous')
                - temperature_extreme: bool (hot/cold climate)
        """
        route_id = route.get('route_id', 'unknown')
        distance = route.get('total_distance_km', 100)
        vehicle_type = route.get('vehicle_type', 'medium_truck')
        payload = route.get('avg_payload_tons', 5)
        max_payload = route.get('max_payload_tons', 10)
        charging_stations = route.get('charging_stations_along_route', 0)
        has_depot_charging = route.get('has_depot_charging', False)
        dwell_hours = route.get('depot_dwell_hours', 8)
        stops = route.get('stops_count', 3)
        avg_stop_hours = route.get('avg_stop_duration_hours', 0.5)
        daily_trips = route.get('daily_trips', 1)
        terrain = route.get('terrain', 'flat')
        temp_extreme = route.get('temperature_extreme', False)
        
        specs = EV_SPECS.get(vehicle_type, EV_SPECS['medium_truck'])
        
        # ===== Factor 1: Range Feasibility (0-100) =====
        # Can the EV complete the route on a single charge?
        effective_range = specs['range_km']
        
        # Payload reduces range
        effective_range -= payload * specs['range_reduction_per_ton']
        
        # Terrain impact
        terrain_factor = {'flat': 1.0, 'hilly': 0.85, 'mountainous': 0.70}.get(terrain, 1.0)
        effective_range *= terrain_factor
        
        # Temperature impact
        if temp_extreme:
            effective_range *= 0.85  # HVAC load reduces range
        
        # Usable range (accounting for min SoC)
        usable_range = effective_range * (1 - specs['min_soc_threshold'] / 100)
        
        daily_distance = distance * daily_trips
        
        if usable_range >= daily_distance:
            range_score = 100  # Can do full day on single charge
        elif usable_range >= distance:
            # Can do one trip, might need mid-day charge for multiple trips
            range_score = max(40, 100 - (daily_distance - usable_range) / usable_range * 60)
        else:
            # Can't even complete one trip
            range_score = max(0, usable_range / distance * 40)
        
        # ===== Factor 2: Charging Availability (0-100) =====
        charge_score = 0
        
        if has_depot_charging:
            charge_score += 50  # Depot charging is most important
        
        # En-route charging
        if distance > usable_range * 0.7:
            # Need en-route charging
            needed_stations = max(1, int(distance / usable_range))
            if charging_stations >= needed_stations:
                charge_score += 50
            elif charging_stations > 0:
                charge_score += 25 * (charging_stations / needed_stations)
        else:
            # Short route, depot charging is sufficient
            charge_score += 40
        
        charge_score = min(100, charge_score)
        
        # ===== Factor 3: Payload Impact (0-100) =====
        # How much does payload reduce EV viability?
        range_with_max_payload = specs['range_km'] - max_payload * specs['range_reduction_per_ton']
        range_with_max_payload *= terrain_factor
        
        if range_with_max_payload >= distance:
            payload_score = 100  # Even max payload works
        elif range_with_max_payload >= distance * 0.7:
            payload_score = 70  # Works most days
        elif range_with_max_payload >= distance * 0.5:
            payload_score = 40  # Marginal
        else:
            payload_score = max(0, range_with_max_payload / distance * 40)
        
        # ===== Factor 4: Dwell Time / Charging Opportunity (0-100) =====
        # Is there enough dwell time at depots/stops to charge?
        charge_time_needed = specs['battery_kwh'] * 0.8 / specs['charge_rate_kw']  # Hours for 80% charge
        
        total_available_charge_time = dwell_hours  # Depot time
        total_available_charge_time += stops * avg_stop_hours * 0.5  # Partial use of stop time
        
        if total_available_charge_time >= charge_time_needed:
            dwell_score = 100
        elif total_available_charge_time >= charge_time_needed * 0.5:
            dwell_score = 60
        else:
            dwell_score = max(10, total_available_charge_time / charge_time_needed * 60)
        
        # ===== Factor 5: Duty Cycle Intensity (0-100) =====
        # How intense is the driving pattern?
        intensity = daily_distance / specs['range_km']  # >1 means multi-charge needed
        
        if intensity <= 0.5:
            duty_score = 100  # Light duty, easy EV
        elif intensity <= 0.8:
            duty_score = 80
        elif intensity <= 1.0:
            duty_score = 60
        elif intensity <= 1.5:
            duty_score = 35  # Heavy, but possible with charging
        else:
            duty_score = max(5, 100 - intensity * 40)
        
        # ===== Weighted Overall Score =====
        overall_score = (
            range_score * self.WEIGHTS['range_feasibility'] +
            charge_score * self.WEIGHTS['charging_availability'] +
            payload_score * self.WEIGHTS['payload_impact'] +
            dwell_score * self.WEIGHTS['dwell_time'] +
            duty_score * self.WEIGHTS['duty_cycle']
        )
        
        # Readiness level
        if overall_score >= 80:
            level = 'excellent'
            recommendation = 'Immediately suitable for electrification'
            color = 'green'
        elif overall_score >= 60:
            level = 'good'
            recommendation = 'Ready with minor infrastructure additions'
            color = 'blue'
        elif overall_score >= 40:
            level = 'moderate'
            recommendation = 'Feasible with planning and investment in charging'
            color = 'yellow'
        elif overall_score >= 20:
            level = 'challenging'
            recommendation = 'Requires significant infrastructure and operational changes'
            color = 'orange'
        else:
            level = 'not_ready'
            recommendation = 'Not currently feasible. Consider hybrid or wait for better range.'
            color = 'red'
        
        # Limiting factor
        factor_scores = {
            'range_feasibility': range_score,
            'charging_availability': charge_score,
            'payload_impact': payload_score,
            'dwell_time': dwell_score,
            'duty_cycle': duty_score
        }
        limiting_factor = min(factor_scores, key=factor_scores.get)
        
        # Estimated ROI
        annual_km = daily_distance * 260  # Working days
        diesel_cost_per_km = 0.15  # USD (fuel + maintenance)
        ev_cost_per_km = 0.06  # USD (electricity + maintenance)
        savings_per_year = annual_km * (diesel_cost_per_km - ev_cost_per_km)
        ev_premium = {'heavy_truck': 80000, 'medium_truck': 40000, 
                      'delivery_van': 15000, 'bus': 60000}.get(vehicle_type, 40000)
        roi_years = ev_premium / max(savings_per_year, 1)
        
        # Improvements needed
        improvements = []
        if range_score < 50:
            improvements.append("Consider extended-range battery option or route splitting")
        if charge_score < 50:
            improvements.append("Install depot charging infrastructure")
            if charging_stations < 2 and distance > 100:
                improvements.append("Add en-route fast charging stations")
        if payload_score < 50:
            improvements.append("Consider lighter payload distribution or multiple trips")
        if dwell_score < 50:
            improvements.append("Adjust schedules to allow more charging time at depots")
        if duty_score < 50:
            improvements.append("Consider route optimization to reduce daily distance")
        
        result = {
            'route_id': route_id,
            'route_name': route.get('route_name', f'Route {route_id}'),
            'readiness_score': round(overall_score, 1),
            'readiness_level': level,
            'readiness_color': color,
            'recommendation': recommendation,
            'limiting_factor': limiting_factor.replace('_', ' ').title(),
            'factor_scores': {k: round(v, 1) for k, v in factor_scores.items()},
            'vehicle_type': vehicle_type,
            'route_details': {
                'total_distance_km': distance,
                'daily_distance_km': daily_distance,
                'effective_ev_range_km': round(usable_range, 1),
                'terrain': terrain,
            },
            'financial': {
                'estimated_roi_years': round(roi_years, 1),
                'annual_fuel_savings_usd': round(savings_per_year, 0),
                'ev_premium_usd': ev_premium,
            },
            'improvements_needed': improvements,
            'assessed_at': datetime.now().isoformat()
        }
        
        self.assessments.append(result)
        return result
    
    def assess_fleet(self, routes: List[Dict]) -> Dict:
        """Assess all routes in a fleet for electrification readiness."""
        results = []
        for route in routes:
            result = self.score_route(route)
            results.append(result)
        
        # Sort by readiness score
        results.sort(key=lambda r: r['readiness_score'], reverse=True)
        
        scores = [r['readiness_score'] for r in results]
        
        summary = {
            'total_routes': len(routes),
            'assessment_date': datetime.now().isoformat(),
            'overall_readiness_score': round(np.mean(scores), 1),
            'readiness_distribution': {
                'excellent': sum(1 for s in scores if s >= 80),
                'good': sum(1 for s in scores if 60 <= s < 80),
                'moderate': sum(1 for s in scores if 40 <= s < 60),
                'challenging': sum(1 for s in scores if 20 <= s < 40),
                'not_ready': sum(1 for s in scores if s < 20),
            },
            'total_annual_savings_usd': sum(r['financial']['annual_fuel_savings_usd'] for r in results),
            'avg_roi_years': round(np.mean([r['financial']['estimated_roi_years'] for r in results]), 1),
            'recommended_for_immediate_ev': [
                r['route_id'] for r in results if r['readiness_score'] >= 70
            ],
            'route_assessments': results,
        }
        
        return summary
    
    def generate_sample_routes(self, num_routes: int = 30) -> List[Dict]:
        """Generate sample routes for testing."""
        routes = []
        vehicle_types = ['heavy_truck', 'medium_truck', 'delivery_van', 'bus']
        terrains = ['flat', 'hilly', 'mountainous']
        
        for i in range(num_routes):
            vtype = np.random.choice(vehicle_types, p=[0.2, 0.35, 0.35, 0.1])
            distance = np.random.uniform(30, 350)
            
            route = {
                'route_id': f'R-{i+1:03d}',
                'route_name': f'Route {chr(65 + i % 26)}{i // 26 + 1}',
                'total_distance_km': round(distance, 1),
                'vehicle_type': vtype,
                'avg_payload_tons': round(np.random.uniform(1, 15), 1),
                'max_payload_tons': round(np.random.uniform(5, 20), 1),
                'charging_stations_along_route': np.random.randint(0, 5),
                'has_depot_charging': np.random.choice([True, False], p=[0.6, 0.4]),
                'depot_dwell_hours': round(np.random.uniform(4, 12), 1),
                'stops_count': np.random.randint(1, 8),
                'avg_stop_duration_hours': round(np.random.uniform(0.25, 2.0), 2),
                'daily_trips': np.random.randint(1, 4),
                'terrain': np.random.choice(terrains, p=[0.5, 0.35, 0.15]),
                'temperature_extreme': np.random.choice([True, False], p=[0.2, 0.8]),
            }
            routes.append(route)
        
        return routes
    
    def save_assessment(self, output_dir: str, routes: Optional[List[Dict]] = None):
        """Run full assessment and save results."""
        os.makedirs(output_dir, exist_ok=True)
        
        if routes is None:
            routes = self.generate_sample_routes(30)
        
        print("\n" + "=" * 60)
        print("Fleet Electrification Readiness Assessment")
        print("=" * 60)
        
        summary = self.assess_fleet(routes)
        
        print(f"\n  Total Routes: {summary['total_routes']}")
        print(f"  Overall Readiness: {summary['overall_readiness_score']}/100")
        print(f"\n  Readiness Distribution:")
        for level, count in summary['readiness_distribution'].items():
            bar = '#' * count
            print(f"    {level:12s}: {count:3d} {bar}")
        
        print(f"\n  Recommended for immediate EV: {len(summary['recommended_for_immediate_ev'])} routes")
        print(f"  Annual fuel savings potential: ${summary['total_annual_savings_usd']:,.0f}")
        print(f"  Average ROI: {summary['avg_roi_years']:.1f} years")
        
        # Top ready routes
        print(f"\n  Top 5 Readiest Routes:")
        for r in summary['route_assessments'][:5]:
            print(f"    {r['route_id']} ({r['route_name']}): {r['readiness_score']:.0f}/100 [{r['readiness_level']}]")
        
        # Save
        with open(os.path.join(output_dir, 'fleet_readiness_assessment.json'), 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print(f"\n[SAVE] Results saved to {output_dir}")
        return summary


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'data', 'processed')
    
    scorer = FleetReadinessScorer()
    scorer.save_assessment(output_dir)
