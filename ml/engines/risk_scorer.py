"""
Supply Chain Risk Scoring Engine
================================
Scores supply chain risk for EV battery suppliers based on:
- Political stability of source countries
- Commodity price volatility
- Supplier concentration
- Logistics performance
- Historical disruption patterns

Also implements cascading failure detection through the supply chain graph.
"""

import numpy as np
import pandas as pd
import os
import json
from datetime import datetime
from typing import Dict, List, Optional


# ============================================================
# Simulated Reference Data (replace with real data from datasets)
# ============================================================

# Country risk data (based on World Governance Indicators patterns)
COUNTRY_RISK_DATA = {
    'DRC': {'name': 'DR Congo', 'political_stability': 0.15, 'logistics_score': 2.1,
            'minerals': ['cobalt', 'lithium'], 'region': 'Africa'},
    'AUS': {'name': 'Australia', 'political_stability': 0.90, 'logistics_score': 3.8,
            'minerals': ['lithium', 'nickel'], 'region': 'Oceania'},
    'CHL': {'name': 'Chile', 'political_stability': 0.72, 'logistics_score': 3.3,
            'minerals': ['lithium', 'copper'], 'region': 'South America'},
    'CHN': {'name': 'China', 'political_stability': 0.55, 'logistics_score': 3.6,
            'minerals': ['graphite', 'rare_earths', 'lithium'], 'region': 'Asia'},
    'IDN': {'name': 'Indonesia', 'political_stability': 0.45, 'logistics_score': 3.0,
            'minerals': ['nickel'], 'region': 'Asia'},
    'ARG': {'name': 'Argentina', 'political_stability': 0.50, 'logistics_score': 2.8,
            'minerals': ['lithium'], 'region': 'South America'},
    'PHL': {'name': 'Philippines', 'political_stability': 0.40, 'logistics_score': 2.7,
            'minerals': ['nickel'], 'region': 'Asia'},
    'RUS': {'name': 'Russia', 'political_stability': 0.25, 'logistics_score': 2.5,
            'minerals': ['nickel', 'cobalt'], 'region': 'Europe'},
    'CAN': {'name': 'Canada', 'political_stability': 0.92, 'logistics_score': 3.7,
            'minerals': ['nickel', 'cobalt', 'lithium'], 'region': 'North America'},
    'BRA': {'name': 'Brazil', 'political_stability': 0.48, 'logistics_score': 2.9,
            'minerals': ['graphite', 'nickel'], 'region': 'South America'},
    'IND': {'name': 'India', 'political_stability': 0.45, 'logistics_score': 3.2,
            'minerals': ['graphite'], 'region': 'Asia'},
    'USA': {'name': 'United States', 'political_stability': 0.85, 'logistics_score': 3.9,
            'minerals': ['lithium'], 'region': 'North America'},
}

# Commodity price volatility (based on World Bank data patterns)
COMMODITY_VOLATILITY = {
    'lithium': {'price_usd_ton': 25000, 'volatility_30d': 0.35, 'volatility_90d': 0.52,
                'trend': 'declining', 'supply_risk': 0.6},
    'cobalt': {'price_usd_ton': 35000, 'volatility_30d': 0.28, 'volatility_90d': 0.45,
               'trend': 'stable', 'supply_risk': 0.8},
    'nickel': {'price_usd_ton': 18000, 'volatility_30d': 0.22, 'volatility_90d': 0.38,
               'trend': 'rising', 'supply_risk': 0.5},
    'graphite': {'price_usd_ton': 1200, 'volatility_30d': 0.15, 'volatility_90d': 0.25,
                 'trend': 'stable', 'supply_risk': 0.4},
    'copper': {'price_usd_ton': 8500, 'volatility_30d': 0.18, 'volatility_90d': 0.30,
               'trend': 'rising', 'supply_risk': 0.3},
    'manganese': {'price_usd_ton': 4500, 'volatility_30d': 0.12, 'volatility_90d': 0.22,
                  'trend': 'stable', 'supply_risk': 0.35},
    'rare_earths': {'price_usd_ton': 45000, 'volatility_30d': 0.40, 'volatility_90d': 0.55,
                    'trend': 'rising', 'supply_risk': 0.85},
}

# Sample supply chain graph
SAMPLE_SUPPLY_CHAIN = [
    # Mines → Refineries → Battery Plants → Battery Packs → Fleet Vehicles
    {
        'supplier_id': 'S001', 'name': 'CobaltCo DRC', 'type': 'mine',
        'country': 'DRC', 'mineral': 'cobalt', 'capacity_tons_year': 5000,
        'downstream': ['R001'], 'failure_rate': 0.15
    },
    {
        'supplier_id': 'S002', 'name': 'LithiumEx Chile', 'type': 'mine',
        'country': 'CHL', 'mineral': 'lithium', 'capacity_tons_year': 8000,
        'downstream': ['R001', 'R002'], 'failure_rate': 0.05
    },
    {
        'supplier_id': 'S003', 'name': 'NickelPro Indonesia', 'type': 'mine',
        'country': 'IDN', 'mineral': 'nickel', 'capacity_tons_year': 12000,
        'downstream': ['R002'], 'failure_rate': 0.10
    },
    {
        'supplier_id': 'S004', 'name': 'GraphiteCorp China', 'type': 'mine',
        'country': 'CHN', 'mineral': 'graphite', 'capacity_tons_year': 15000,
        'downstream': ['R001', 'R002'], 'failure_rate': 0.08
    },
    {
        'supplier_id': 'S005', 'name': 'LithiumOz Australia', 'type': 'mine',
        'country': 'AUS', 'mineral': 'lithium', 'capacity_tons_year': 10000,
        'downstream': ['R002'], 'failure_rate': 0.03
    },
    {
        'supplier_id': 'R001', 'name': 'CathodeRefine Shanghai', 'type': 'refinery',
        'country': 'CHN', 'mineral': 'cathode_materials', 'capacity_tons_year': 20000,
        'downstream': ['P001'], 'failure_rate': 0.06
    },
    {
        'supplier_id': 'R002', 'name': 'BattMat Korea', 'type': 'refinery',
        'country': 'KOR', 'mineral': 'cathode_materials', 'capacity_tons_year': 18000,
        'downstream': ['P001', 'P002'], 'failure_rate': 0.04
    },
    {
        'supplier_id': 'P001', 'name': 'GigaCell Shenzhen', 'type': 'battery_plant',
        'country': 'CHN', 'mineral': 'battery_cells', 'capacity_tons_year': 50000,
        'downstream': ['F001', 'F002'], 'failure_rate': 0.05
    },
    {
        'supplier_id': 'P002', 'name': 'BatteryWorks USA', 'type': 'battery_plant',
        'country': 'USA', 'mineral': 'battery_cells', 'capacity_tons_year': 30000,
        'downstream': ['F002', 'F003'], 'failure_rate': 0.03
    },
    {
        'supplier_id': 'F001', 'name': 'Fleet Alpha', 'type': 'fleet',
        'country': 'IND', 'mineral': None, 'capacity_tons_year': None,
        'downstream': [], 'failure_rate': 0
    },
    {
        'supplier_id': 'F002', 'name': 'Fleet Beta', 'type': 'fleet',
        'country': 'IND', 'mineral': None, 'capacity_tons_year': None,
        'downstream': [], 'failure_rate': 0
    },
    {
        'supplier_id': 'F003', 'name': 'Fleet Gamma', 'type': 'fleet',
        'country': 'USA', 'mineral': None, 'capacity_tons_year': None,
        'downstream': [], 'failure_rate': 0
    },
]


class SupplyChainRiskScorer:
    """
    Scores supply chain risk using multiple weighted factors.
    
    Risk Score = weighted combination of:
    - Political stability of source country
    - Supplier concentration (single source = high risk)
    - Commodity price volatility
    - Logistics performance
    - Shipping disruption probability
    - Historical failure rate
    """
    
    # Risk factor weights
    WEIGHTS = {
        'political_risk': 0.25,
        'concentration_risk': 0.20,
        'price_volatility_risk': 0.20,
        'logistics_risk': 0.15,
        'shipping_risk': 0.10,
        'historical_risk': 0.10,
    }
    
    def __init__(self):
        self.supply_chain = SAMPLE_SUPPLY_CHAIN
        self.country_data = COUNTRY_RISK_DATA
        self.commodity_data = COMMODITY_VOLATILITY
        self.risk_cache = {}
    
    def score_supplier(self, supplier: Dict) -> Dict:
        """
        Calculate comprehensive risk score for a single supplier.
        
        Returns dict with overall score, breakdown, and recommendations.
        """
        country_code = supplier.get('country', 'UNK')
        mineral = supplier.get('mineral')
        country_info = self.country_data.get(country_code, {})
        
        # 1. Political Risk (0-1, higher = more risky)
        political_stability = country_info.get('political_stability', 0.5)
        political_risk = 1 - political_stability
        
        # 2. Concentration Risk
        # How many alternative suppliers exist for this mineral?
        if mineral and mineral not in ['cathode_materials', 'battery_cells']:
            alternatives = sum(1 for s in self.supply_chain 
                             if s.get('mineral') == mineral and s['supplier_id'] != supplier['supplier_id'])
            concentration_risk = max(0, 1 - (alternatives / 3))  # 3+ alternatives = low risk
        else:
            concentration_risk = 0.3  # Default for non-mineral suppliers
        
        # 3. Price Volatility Risk
        commodity_info = self.commodity_data.get(mineral, {})
        price_volatility_risk = commodity_info.get('volatility_90d', 0.3)
        
        # 4. Logistics Risk
        logistics_score = country_info.get('logistics_score', 3.0)
        logistics_risk = max(0, 1 - (logistics_score / 5))  # 5 = perfect logistics
        
        # 5. Shipping Disruption Risk
        # Higher for distant/conflict regions
        shipping_risk_map = {
            'Africa': 0.6, 'Asia': 0.4, 'South America': 0.5,
            'Europe': 0.3, 'North America': 0.2, 'Oceania': 0.3
        }
        shipping_risk = shipping_risk_map.get(country_info.get('region', ''), 0.4)
        
        # 6. Historical Failure Rate
        historical_risk = supplier.get('failure_rate', 0.05) * 5  # Scale to 0-1
        historical_risk = min(1, historical_risk)
        
        # Weighted overall score (0-100)
        overall_score = (
            political_risk * self.WEIGHTS['political_risk'] +
            concentration_risk * self.WEIGHTS['concentration_risk'] +
            price_volatility_risk * self.WEIGHTS['price_volatility_risk'] +
            logistics_risk * self.WEIGHTS['logistics_risk'] +
            shipping_risk * self.WEIGHTS['shipping_risk'] +
            historical_risk * self.WEIGHTS['historical_risk']
        ) * 100
        
        # Risk level
        if overall_score <= 25:
            level = 'low'
            color = 'green'
            action = 'Monitor quarterly'
        elif overall_score <= 50:
            level = 'medium'
            color = 'yellow'
            action = 'Monitor monthly, identify alternatives'
        elif overall_score <= 75:
            level = 'high'
            color = 'orange'
            action = 'Actively source alternatives, build inventory buffer'
        else:
            level = 'critical'
            color = 'red'
            action = 'Immediate diversification required'
        
        # Recommendations
        recommendations = []
        if political_risk > 0.6:
            recommendations.append(f"HIGH political risk in {country_info.get('name', country_code)}. Diversify sourcing.")
        if concentration_risk > 0.7:
            recommendations.append(f"Single-source dependency for {mineral}. Add alternative suppliers.")
        if price_volatility_risk > 0.4:
            recommendations.append(f"High price volatility for {mineral}. Consider long-term contracts.")
        if logistics_risk > 0.5:
            recommendations.append(f"Weak logistics infrastructure in {country_info.get('name', country_code)}.")
        
        result = {
            'supplier_id': supplier['supplier_id'],
            'supplier_name': supplier['name'],
            'type': supplier['type'],
            'country': country_code,
            'country_name': country_info.get('name', country_code),
            'mineral': mineral,
            'risk_score': round(overall_score, 2),
            'risk_level': level,
            'risk_color': color,
            'action': action,
            'breakdown': {
                'political_risk': round(political_risk * 100, 1),
                'concentration_risk': round(concentration_risk * 100, 1),
                'price_volatility_risk': round(price_volatility_risk * 100, 1),
                'logistics_risk': round(logistics_risk * 100, 1),
                'shipping_risk': round(shipping_risk * 100, 1),
                'historical_risk': round(historical_risk * 100, 1),
            },
            'recommendations': recommendations
        }
        
        self.risk_cache[supplier['supplier_id']] = result
        return result
    
    def score_all_suppliers(self) -> List[Dict]:
        """Score all suppliers in the supply chain."""
        print("\n" + "=" * 60)
        print("Supply Chain Risk Assessment")
        print("=" * 60)
        
        results = []
        for supplier in self.supply_chain:
            result = self.score_supplier(supplier)
            results.append(result)
            
            print(f"\n  {result['supplier_name']} ({result['supplier_id']})")
            print(f"  Type: {result['type']} | Country: {result['country_name']}")
            print(f"  Risk Score: {result['risk_score']:.1f}/100 [{result['risk_level'].upper()}]")
            if result['recommendations']:
                for rec in result['recommendations']:
                    print(f"    -> {rec}")
        
        # Summary
        scores = [r['risk_score'] for r in results]
        print(f"\n{'='*60}")
        print(f"Supply Chain Risk Summary")
        print(f"{'='*60}")
        print(f"  Total suppliers: {len(results)}")
        print(f"  Average risk: {np.mean(scores):.1f}/100")
        print(f"  Highest risk: {max(scores):.1f}/100")
        print(f"  Critical: {sum(1 for r in results if r['risk_level'] == 'critical')}")
        print(f"  High: {sum(1 for r in results if r['risk_level'] == 'high')}")
        print(f"  Medium: {sum(1 for r in results if r['risk_level'] == 'medium')}")
        print(f"  Low: {sum(1 for r in results if r['risk_level'] == 'low')}")
        
        return results
    
    def detect_cascading_failures(self, failed_supplier_id: str) -> Dict:
        """
        Detect cascading failure impact when a supplier fails.
        
        Traces the supply chain graph downstream to find all affected entities.
        
        Example: If a cobalt mine in DRC fails ->
          -> Refinery loses input ->
            -> Battery plant can't produce ->
              -> Fleet vehicles affected
        """
        print(f"\n{'='*60}")
        print(f"Cascading Failure Analysis: {failed_supplier_id}")
        print(f"{'='*60}")
        
        # Find the failed supplier
        failed = None
        supplier_map = {s['supplier_id']: s for s in self.supply_chain}
        failed = supplier_map.get(failed_supplier_id)
        
        if not failed:
            return {'error': f'Supplier {failed_supplier_id} not found'}
        
        print(f"\n  FAILURE ORIGIN: {failed['name']} ({failed['type']})")
        print(f"  Country: {failed.get('country', 'N/A')}")
        print(f"  Material: {failed.get('mineral', 'N/A')}")
        
        # BFS to find all downstream affected entities
        affected = []
        queue = [failed_supplier_id]
        visited = set()
        level = 0
        levels = {}
        
        while queue:
            next_queue = []
            for sid in queue:
                if sid in visited:
                    continue
                visited.add(sid)
                supplier = supplier_map.get(sid)
                if supplier:
                    levels[sid] = level
                    if sid != failed_supplier_id:
                        affected.append({
                            'supplier_id': sid,
                            'name': supplier['name'],
                            'type': supplier['type'],
                            'impact_level': level,
                            'risk_amplification': round(1.5 ** level, 2)
                        })
                    for downstream_id in supplier.get('downstream', []):
                        if downstream_id not in visited:
                            next_queue.append(downstream_id)
            queue = next_queue
            level += 1
        
        # Impact assessment
        affected_fleets = [a for a in affected if supplier_map.get(a['supplier_id'], {}).get('type') == 'fleet']
        affected_plants = [a for a in affected if supplier_map.get(a['supplier_id'], {}).get('type') == 'battery_plant']
        
        result = {
            'failed_supplier': {
                'id': failed_supplier_id,
                'name': failed['name'],
                'type': failed['type'],
                'mineral': failed.get('mineral'),
                'country': failed.get('country')
            },
            'total_affected': len(affected),
            'affected_entities': affected,
            'impact_summary': {
                'refineries_affected': sum(1 for a in affected if supplier_map.get(a['supplier_id'], {}).get('type') == 'refinery'),
                'plants_affected': len(affected_plants),
                'fleets_affected': len(affected_fleets),
                'max_cascade_depth': max(levels.values()) if levels else 0
            },
            'severity': 'critical' if len(affected_fleets) > 1 else 'high' if len(affected_fleets) == 1 else 'medium',
            'mitigation': []
        }
        
        # Mitigation recommendations
        if failed['type'] == 'mine':
            alt_suppliers = [s for s in self.supply_chain 
                           if s.get('mineral') == failed.get('mineral') 
                           and s['supplier_id'] != failed_supplier_id]
            if alt_suppliers:
                result['mitigation'].append(
                    f"Redirect to alternative supplier(s): {', '.join(s['name'] for s in alt_suppliers)}")
            else:
                result['mitigation'].append("CRITICAL: No alternative suppliers for this mineral!")
        
        result['mitigation'].append(f"Activate strategic reserve for {failed.get('mineral', 'materials')}")
        result['mitigation'].append("Notify downstream partners of potential delays")
        
        # Print cascading failure chain
        print(f"\n  IMPACT CHAIN:")
        for a in sorted(affected, key=lambda x: x['impact_level']):
            indent = "  " * (a['impact_level'] + 1)
            print(f"  {indent}-> {a['name']} (Level {a['impact_level']}, amplification: {a['risk_amplification']}x)")
        
        print(f"\n  TOTAL IMPACT: {result['total_affected']} entities affected")
        print(f"  FLEETS AT RISK: {len(affected_fleets)}")
        print(f"  SEVERITY: {result['severity'].upper()}")
        
        return result
    
    def get_supply_chain_graph(self) -> Dict:
        """Return the supply chain as a graph structure for visualization."""
        nodes = []
        edges = []
        
        for supplier in self.supply_chain:
            risk = self.risk_cache.get(supplier['supplier_id'], {})
            nodes.append({
                'id': supplier['supplier_id'],
                'label': supplier['name'],
                'type': supplier['type'],
                'country': supplier.get('country'),
                'risk_score': risk.get('risk_score', 0),
                'risk_level': risk.get('risk_level', 'unknown')
            })
            
            for downstream_id in supplier.get('downstream', []):
                edges.append({
                    'source': supplier['supplier_id'],
                    'target': downstream_id,
                    'material': supplier.get('mineral', 'components')
                })
        
        return {'nodes': nodes, 'edges': edges}
    
    def save_results(self, output_dir: str):
        """Save risk assessment results."""
        os.makedirs(output_dir, exist_ok=True)
        
        results = self.score_all_suppliers()
        
        # Save as JSON
        with open(os.path.join(output_dir, 'supply_chain_risk_scores.json'), 'w') as f:
            json.dump(results, f, indent=2)
        
        # Save as CSV
        df = pd.DataFrame(results)
        df.to_csv(os.path.join(output_dir, 'supply_chain_risk_scores.csv'), index=False)
        
        # Save graph
        graph = self.get_supply_chain_graph()
        with open(os.path.join(output_dir, 'supply_chain_graph.json'), 'w') as f:
            json.dump(graph, f, indent=2)
        
        # Run cascading failure analysis for highest-risk supplier
        highest_risk = max(results, key=lambda x: x['risk_score'])
        cascade = self.detect_cascading_failures(highest_risk['supplier_id'])
        with open(os.path.join(output_dir, 'cascading_failure_analysis.json'), 'w') as f:
            json.dump(cascade, f, indent=2)
        
        print(f"\n[SAVE] Results saved to {output_dir}")


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'data', 'processed')
    
    scorer = SupplyChainRiskScorer()
    scorer.save_results(output_dir)
