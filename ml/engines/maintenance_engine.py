"""
Maintenance Recommendation Engine
==================================
Combines anomaly scores, battery degradation trends, and operational data
to generate maintenance recommendations for each vehicle.

Priority levels: CRITICAL > HIGH > MEDIUM > LOW > ROUTINE
"""

import numpy as np
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class MaintenanceRecommendationEngine:
    """
    Generates smart maintenance recommendations by combining:
    1. Anomaly detection scores
    2. Battery SoH and RUL predictions
    3. Temperature trends
    4. Charging efficiency trends
    5. Operational patterns
    """
    
    # Maintenance action catalog
    MAINTENANCE_ACTIONS = {
        'battery_replacement': {
            'description': 'Full battery pack replacement',
            'estimated_hours': 8,
            'estimated_cost_usd': 15000,
            'category': 'battery'
        },
        'battery_inspection': {
            'description': 'Detailed battery pack inspection and diagnostics',
            'estimated_hours': 2,
            'estimated_cost_usd': 500,
            'category': 'battery'
        },
        'thermal_system_check': {
            'description': 'Battery thermal management system inspection',
            'estimated_hours': 3,
            'estimated_cost_usd': 800,
            'category': 'thermal'
        },
        'cooling_system_service': {
            'description': 'Coolant flush, pump check, fan inspection',
            'estimated_hours': 4,
            'estimated_cost_usd': 1200,
            'category': 'thermal'
        },
        'charging_system_diagnostic': {
            'description': 'Onboard charger and charging port diagnostics',
            'estimated_hours': 2,
            'estimated_cost_usd': 400,
            'category': 'charging'
        },
        'bms_recalibration': {
            'description': 'Battery Management System recalibration',
            'estimated_hours': 1,
            'estimated_cost_usd': 200,
            'category': 'software'
        },
        'cell_balancing': {
            'description': 'Cell voltage balancing procedure',
            'estimated_hours': 6,
            'estimated_cost_usd': 600,
            'category': 'battery'
        },
        'contactor_inspection': {
            'description': 'High-voltage contactor and relay inspection',
            'estimated_hours': 2,
            'estimated_cost_usd': 300,
            'category': 'electrical'
        },
        'routine_service': {
            'description': 'Standard scheduled maintenance check',
            'estimated_hours': 3,
            'estimated_cost_usd': 350,
            'category': 'general'
        },
    }
    
    def __init__(self):
        self.recommendation_history = []
    
    def generate_recommendation(self, vehicle_data: Dict) -> Dict:
        """
        Generate maintenance recommendation for a single vehicle.
        
        Args:
            vehicle_data: Dict containing:
                - vehicle_id: str
                - anomaly_score: float (0-1, from anomaly detector)
                - anomaly_types: list of detected anomaly types
                - soh_percent: float (State of Health)
                - rul_cycles: float (Remaining Useful Life)
                - avg_temperature: float (recent average temperature)
                - temperature_trend: str ('rising', 'stable', 'falling')
                - charging_efficiency: float (%)
                - last_maintenance_days: int (days since last service)
                - odometer_km: float
        """
        vehicle_id = vehicle_data.get('vehicle_id', 'unknown')
        anomaly_score = vehicle_data.get('anomaly_score', 0)
        anomaly_types = vehicle_data.get('anomaly_types', [])
        soh = vehicle_data.get('soh_percent', 100)
        rul = vehicle_data.get('rul_cycles', 500)
        avg_temp = vehicle_data.get('avg_temperature', 30)
        temp_trend = vehicle_data.get('temperature_trend', 'stable')
        charge_eff = vehicle_data.get('charging_efficiency', 95)
        days_since_maint = vehicle_data.get('last_maintenance_days', 30)
        odometer = vehicle_data.get('odometer_km', 0)
        
        actions = []
        priority = 'routine'
        urgency_days = 90  # Default: within 90 days
        
        # ===== Rule-based decision logic =====
        
        # Rule 1: Critical battery condition
        if anomaly_score > 0.8 and soh < 70:
            priority = 'critical'
            urgency_days = 0  # Immediate
            actions.append('battery_replacement')
            actions.append('thermal_system_check')
        
        # Rule 2: High anomaly with thermal issue
        elif anomaly_score > 0.5 and (temp_trend == 'rising' or avg_temp > 45):
            priority = 'high'
            urgency_days = 2
            actions.append('thermal_system_check')
            actions.append('cooling_system_service')
            if 'thermal_spike' in anomaly_types or 'critical_thermal' in anomaly_types:
                actions.append('battery_inspection')
        
        # Rule 3: Low RUL
        elif rul < 30:
            priority = 'critical'
            urgency_days = 1
            actions.append('battery_replacement')
            actions.append('battery_inspection')
        
        elif rul < 100:
            priority = 'high'
            urgency_days = 14
            actions.append('battery_inspection')
            actions.append('bms_recalibration')
        
        # Rule 4: Moderate SoH degradation
        elif soh < 75:
            priority = 'high'
            urgency_days = 7
            actions.append('battery_inspection')
            actions.append('cell_balancing')
        
        elif soh < 85:
            priority = 'medium'
            urgency_days = 30
            actions.append('bms_recalibration')
            actions.append('cell_balancing')
        
        # Rule 5: Charging issues
        elif charge_eff < 80:
            priority = 'high'
            urgency_days = 7
            actions.append('charging_system_diagnostic')
            actions.append('bms_recalibration')
        
        elif charge_eff < 90:
            priority = 'medium'
            urgency_days = 14
            actions.append('charging_system_diagnostic')
        
        # Rule 6: Anomaly detected but no specific pattern
        elif anomaly_score > 0.3:
            priority = 'medium'
            urgency_days = 7
            actions.append('battery_inspection')
            
            if 'voltage_anomaly' in anomaly_types or 'under_voltage' in anomaly_types:
                actions.append('contactor_inspection')
            if 'current_surge' in anomaly_types:
                actions.append('contactor_inspection')
        
        # Rule 7: Overdue routine maintenance
        elif days_since_maint > 60:
            priority = 'low'
            urgency_days = 14
            actions.append('routine_service')
        
        # Rule 8: Everything OK
        else:
            priority = 'routine'
            urgency_days = 90
            actions.append('routine_service')
        
        # Deduplicate actions
        actions = list(dict.fromkeys(actions))
        
        # Build recommendation
        scheduled_date = datetime.now() + timedelta(days=urgency_days)
        
        total_hours = sum(self.MAINTENANCE_ACTIONS[a]['estimated_hours'] for a in actions)
        total_cost = sum(self.MAINTENANCE_ACTIONS[a]['estimated_cost_usd'] for a in actions)
        
        recommendation = {
            'vehicle_id': vehicle_id,
            'priority': priority,
            'urgency_days': urgency_days,
            'scheduled_date': scheduled_date.strftime('%Y-%m-%d'),
            'actions': [
                {
                    'action_id': action,
                    **self.MAINTENANCE_ACTIONS[action]
                } for action in actions
            ],
            'estimated_total_hours': total_hours,
            'estimated_total_cost_usd': total_cost,
            'reasoning': self._generate_reasoning(vehicle_data, priority, actions),
            'vehicle_status': {
                'soh_percent': soh,
                'rul_cycles': rul,
                'anomaly_score': anomaly_score,
                'avg_temperature': avg_temp,
                'charging_efficiency': charge_eff,
                'odometer_km': odometer,
            },
            'generated_at': datetime.now().isoformat()
        }
        
        self.recommendation_history.append(recommendation)
        return recommendation
    
    def _generate_reasoning(self, data: Dict, priority: str, actions: list) -> str:
        """Generate human-readable reasoning for the recommendation."""
        reasons = []
        
        soh = data.get('soh_percent', 100)
        rul = data.get('rul_cycles', 500)
        anomaly_score = data.get('anomaly_score', 0)
        avg_temp = data.get('avg_temperature', 30)
        charge_eff = data.get('charging_efficiency', 95)
        
        if soh < 70:
            reasons.append(f"Battery health critically low at {soh:.0f}%")
        elif soh < 85:
            reasons.append(f"Battery health degraded to {soh:.0f}%")
        
        if rul < 30:
            reasons.append(f"Only {rul:.0f} cycles remaining before end of life")
        elif rul < 100:
            reasons.append(f"Battery approaching end of life ({rul:.0f} cycles remaining)")
        
        if anomaly_score > 0.5:
            reasons.append(f"High anomaly score ({anomaly_score:.2f}) detected")
        
        if avg_temp > 45:
            reasons.append(f"Elevated battery temperature ({avg_temp:.1f}C)")
        
        if charge_eff < 85:
            reasons.append(f"Reduced charging efficiency ({charge_eff:.0f}%)")
        
        if not reasons:
            reasons.append("Routine scheduled maintenance")
        
        return ". ".join(reasons) + "."
    
    def analyze_fleet(self, fleet_data: List[Dict]) -> Dict:
        """
        Generate maintenance schedule for entire fleet.
        
        Args:
            fleet_data: List of vehicle data dicts
        
        Returns:
            Fleet maintenance summary with schedule
        """
        recommendations = []
        for vehicle in fleet_data:
            rec = self.generate_recommendation(vehicle)
            recommendations.append(rec)
        
        # Sort by priority
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3, 'routine': 4}
        recommendations.sort(key=lambda r: priority_order.get(r['priority'], 5))
        
        # Summary
        summary = {
            'fleet_size': len(fleet_data),
            'analysis_date': datetime.now().isoformat(),
            'priority_breakdown': {
                'critical': sum(1 for r in recommendations if r['priority'] == 'critical'),
                'high': sum(1 for r in recommendations if r['priority'] == 'high'),
                'medium': sum(1 for r in recommendations if r['priority'] == 'medium'),
                'low': sum(1 for r in recommendations if r['priority'] == 'low'),
                'routine': sum(1 for r in recommendations if r['priority'] == 'routine'),
            },
            'total_estimated_cost_usd': sum(r['estimated_total_cost_usd'] for r in recommendations),
            'total_estimated_hours': sum(r['estimated_total_hours'] for r in recommendations),
            'immediate_attention_required': sum(1 for r in recommendations if r['urgency_days'] <= 1),
            'this_week': sum(1 for r in recommendations if r['urgency_days'] <= 7),
            'this_month': sum(1 for r in recommendations if r['urgency_days'] <= 30),
            'recommendations': recommendations,
        }
        
        return summary
    
    def generate_sample_fleet_data(self, num_vehicles: int = 50) -> List[Dict]:
        """Generate sample vehicle data for testing."""
        fleet = []
        for i in range(num_vehicles):
            # Vary conditions realistically
            soh = np.random.uniform(55, 100)
            rul = max(0, (soh - 60) / 40 * 500 + np.random.normal(0, 50))
            anomaly_score = max(0, min(1, (100 - soh) / 50 + np.random.normal(0, 0.15)))
            
            vehicle = {
                'vehicle_id': f'EV-{i+1:03d}',
                'anomaly_score': round(anomaly_score, 3),
                'anomaly_types': [],
                'soh_percent': round(soh, 1),
                'rul_cycles': round(rul, 0),
                'avg_temperature': round(np.random.uniform(25, 50), 1),
                'temperature_trend': np.random.choice(['rising', 'stable', 'falling'], p=[0.2, 0.6, 0.2]),
                'charging_efficiency': round(max(70, 99 - (100 - soh) * 0.5 + np.random.normal(0, 2)), 1),
                'last_maintenance_days': np.random.randint(5, 90),
                'odometer_km': np.random.randint(10000, 150000),
            }
            
            # Add anomaly types based on score
            if vehicle['anomaly_score'] > 0.5:
                vehicle['anomaly_types'] = np.random.choice(
                    ['thermal_spike', 'voltage_anomaly', 'current_surge', 'soc_inconsistency'],
                    size=np.random.randint(1, 3), replace=False
                ).tolist()
            
            fleet.append(vehicle)
        
        return fleet
    
    def save_analysis(self, output_dir: str, fleet_data: Optional[List[Dict]] = None):
        """Run full fleet analysis and save results."""
        os.makedirs(output_dir, exist_ok=True)
        
        if fleet_data is None:
            fleet_data = self.generate_sample_fleet_data(50)
        
        print("\n" + "=" * 60)
        print("Maintenance Recommendation Analysis")
        print("=" * 60)
        
        summary = self.analyze_fleet(fleet_data)
        
        print(f"\n  Fleet Size: {summary['fleet_size']}")
        print(f"  Priority Breakdown:")
        for level, count in summary['priority_breakdown'].items():
            print(f"    {level.upper():10s}: {count}")
        print(f"\n  Immediate attention: {summary['immediate_attention_required']} vehicles")
        print(f"  This week: {summary['this_week']} vehicles")
        print(f"  This month: {summary['this_month']} vehicles")
        print(f"  Total estimated cost: ${summary['total_estimated_cost_usd']:,.0f}")
        print(f"  Total estimated hours: {summary['total_estimated_hours']}")
        
        # Show top critical/high recommendations
        critical_high = [r for r in summary['recommendations'] 
                        if r['priority'] in ('critical', 'high')][:5]
        if critical_high:
            print(f"\n  Top Priority Vehicles:")
            for r in critical_high:
                print(f"    {r['vehicle_id']}: [{r['priority'].upper()}] - {r['reasoning'][:80]}")
        
        # Save
        with open(os.path.join(output_dir, 'maintenance_recommendations.json'), 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print(f"\n[SAVE] Results saved to {output_dir}")
        return summary


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'data', 'processed')
    
    engine = MaintenanceRecommendationEngine()
    engine.save_analysis(output_dir)
