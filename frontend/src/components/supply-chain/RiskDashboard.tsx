import React, { useEffect, useState } from 'react';
import { AlertOctagon, TrendingUp, ShieldAlert, Cpu } from 'lucide-react';

interface RiskBreakdown {
  political_risk?: number;
  concentration_risk?: number;
  price_volatility_risk?: number;
  logistics_risk?: number;
  shipping_risk?: number;
  historical_risk?: number;
}

interface SupplierRisk {
  supplier_id: string;
  supplier_name: string;
  risk_score: number;
  risk_level: string;
  country: string;
  mineral?: string;
  breakdown: RiskBreakdown;
  recommendations: string[];
}

interface MLRiskResponse {
  global_risk_index: number;
  risk_level: string;
  confidence: number;
  critical_vulnerability: string;
  mitigation_plan: string;
  suppliers: SupplierRisk[];
}

export default function RiskDashboard() {
  const [riskData, setRiskData] = useState<MLRiskResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRisk = async () => {
      try {
        const response = await fetch('/api/v1/supply-chain/risk');
        if (response.ok) {
          const data = await response.json();
          setRiskData(data);
        }
      } catch (error) {
        console.error('Error fetching ML risk data:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchRisk();
  }, []);

  if (loading) {
    return <div className="p-6 glass rounded-xl animate-pulse h-64 flex items-center justify-center">Loading Risk Scores...</div>;
  }

  if (!riskData) {
    return <div className="p-6 glass rounded-xl text-red-400">Failed to load risk data.</div>;
  }

  // Aggregate breakdown across all suppliers to get averages for the bars
  const avgBreakdown = {
    concentration: 0,
    geopolitical: 0,
    shipping: 0
  };

  if (riskData.suppliers.length > 0) {
    let conc = 0, geo = 0, ship = 0;
    riskData.suppliers.forEach(s => {
      conc += s.breakdown?.concentration_risk || 0;
      geo += s.breakdown?.political_risk || 0;
      ship += s.breakdown?.shipping_risk || 0;
    });
    const len = riskData.suppliers.length;
    avgBreakdown.concentration = Math.round(conc / len);
    avgBreakdown.geopolitical = Math.round(geo / len);
    avgBreakdown.shipping = Math.round(ship / len);
  }

  const getRiskColor = (score: number) => {
    if (score >= 75) return 'bg-red-500';
    if (score >= 50) return 'bg-amber-500';
    return 'bg-emerald-500';
  };

  const getRiskTextColor = (score: number) => {
    if (score >= 75) return 'text-red-400';
    if (score >= 50) return 'text-amber-400';
    return 'text-emerald-400';
  };

  const getRiskLabel = (score: number) => {
    if (score >= 75) return 'High Risk';
    if (score >= 50) return 'Medium Risk';
    return 'Low Risk';
  };

  return (
    <div className="glass p-6 rounded-xl flex flex-col justify-between h-full">
      <div>
        <h2 className="font-semibold text-lg">Supply Chain Risk Scoring</h2>
        <p className="text-xs text-muted-foreground mt-1">
          Global Risk Index: <span className="font-bold">{riskData.global_risk_index}/100</span> ({riskData.risk_level}) 
          | Confidence: {riskData.confidence}%
        </p>
      </div>

      <div className="space-y-4 my-6">
        <div className="space-y-1">
          <div className="flex justify-between text-xs font-semibold">
            <span>Concentration Index</span>
            <span className={getRiskTextColor(avgBreakdown.concentration)}>{getRiskLabel(avgBreakdown.concentration)} ({avgBreakdown.concentration}/100)</span>
          </div>
          <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
            <div className={`${getRiskColor(avgBreakdown.concentration)} h-full transition-all duration-1000`} style={{ width: `${avgBreakdown.concentration}%` }} />
          </div>
        </div>

        <div className="space-y-1">
          <div className="flex justify-between text-xs font-semibold">
            <span>Geopolitical Instability</span>
            <span className={getRiskTextColor(avgBreakdown.geopolitical)}>{getRiskLabel(avgBreakdown.geopolitical)} ({avgBreakdown.geopolitical}/100)</span>
          </div>
          <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
            <div className={`${getRiskColor(avgBreakdown.geopolitical)} h-full transition-all duration-1000`} style={{ width: `${avgBreakdown.geopolitical}%` }} />
          </div>
        </div>

        <div className="space-y-1">
          <div className="flex justify-between text-xs font-semibold">
            <span>Shipping Bottlenecks</span>
            <span className={getRiskTextColor(avgBreakdown.shipping)}>{getRiskLabel(avgBreakdown.shipping)} ({avgBreakdown.shipping}/100)</span>
          </div>
          <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
            <div className={`${getRiskColor(avgBreakdown.shipping)} h-full transition-all duration-1000`} style={{ width: `${avgBreakdown.shipping}%` }} />
          </div>
        </div>
      </div>

      {riskData.critical_vulnerability && riskData.critical_vulnerability !== "No supply chain vulnerabilities detected." && (
        <div className="bg-red-500/5 border border-red-500/20 p-3 rounded-lg flex items-start gap-2.5">
          <AlertOctagon className="h-4.5 w-4.5 text-red-400 shrink-0 mt-0.5" />
          <p className="text-[11px] text-red-300">
            <strong>Dependency Alert:</strong> {riskData.critical_vulnerability}
            <br/><span className="text-muted-foreground mt-1 block">Mitigation: {riskData.mitigation_plan}</span>
          </p>
        </div>
      )}
      
      {(!riskData.critical_vulnerability || riskData.critical_vulnerability === "No supply chain vulnerabilities detected.") && (
        <div className="bg-emerald-500/5 border border-emerald-500/20 p-3 rounded-lg flex items-start gap-2.5">
          <ShieldAlert className="h-4.5 w-4.5 text-emerald-400 shrink-0 mt-0.5" />
          <p className="text-[11px] text-emerald-300">
            <strong>Status Normal:</strong> {riskData.critical_vulnerability}
          </p>
        </div>
      )}
    </div>
  );
}
