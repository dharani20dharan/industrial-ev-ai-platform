import { useEffect, useState } from 'react';
import { Leaf, Award, Activity } from 'lucide-react';
import { sustainabilityApi, SustainabilitySummary, CarbonReport } from '../../services/sustainability';

interface SummaryCardsProps {
  latestReport: CarbonReport | null;
}

export function SummaryCards({ latestReport }: SummaryCardsProps) {
  const [summary, setSummary] = useState<SustainabilitySummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchSummary = async () => {
    try {
      setLoading(true);
      setError(null);
      const res = await sustainabilityApi.getSummary();
      if (res.success) {
        setSummary(res.data);
      } else {
        setError(res.message);
      }
    } catch (err: any) {
      setError(err.message || 'Failed to fetch summary');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSummary();
  }, []);

  // When a new report comes in via websocket, we should probably refetch the summary
  useEffect(() => {
    if (latestReport) {
      fetchSummary();
    }
  }, [latestReport]);

  if (loading && !summary) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 animate-pulse">
        {[1, 2, 3].map(i => (
          <div key={i} className="glass p-6 rounded-xl h-32 bg-muted/20"></div>
        ))}
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-4 border border-red-500/50 bg-red-500/10 text-red-400 rounded-xl flex items-center justify-between">
        <span>Error loading summary: {error}</span>
        <button onClick={fetchSummary} className="px-3 py-1 bg-red-500/20 rounded hover:bg-red-500/30 transition-colors">
          Retry
        </button>
      </div>
    );
  }

  if (!summary) return null;

  const totalSaved = Number(summary.total_carbon_saved_kg ?? (summary as any).total_saved ?? 0);
  const scope1 = Number(summary.scope1_emission_kg ?? (summary as any).scope1_emission ?? 0);
  const scope3 = Number(summary.scope3_emission_kg ?? (summary as any).scope3_emission ?? 0);

  const carbonSavedTons = (totalSaved / 1000).toFixed(1);
  const treesPlanted = Math.floor(totalSaved / 22);
  const totalEmissions = scope1 + scope3;
  const reductionPercentage = totalEmissions > 0 
    ? ((totalSaved / (totalSaved + totalEmissions)) * 100).toFixed(1)
    : '0.0';

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div className="glass p-6 rounded-xl relative overflow-hidden transition-all hover:border-emerald-500/50 hover:shadow-[0_0_15px_rgba(16,185,129,0.15)]">
        <div className="flex justify-between items-center">
          <span className="text-sm font-semibold text-muted-foreground">Total CO₂ Saved</span>
          <Leaf className="h-5 w-5 text-emerald-400" />
        </div>
        <div className="mt-4">
          <span className="text-3xl font-bold text-emerald-400">{carbonSavedTons} Tons</span>
          <span className="block text-xs text-muted-foreground mt-1.5">Equivalent to planting {treesPlanted.toLocaleString()} trees</span>
        </div>
      </div>

      <div className="glass p-6 rounded-xl transition-all hover:border-blue-500/50 hover:shadow-[0_0_15px_rgba(59,130,246,0.15)]">
        <div className="flex justify-between items-center">
          <span className="text-sm font-semibold text-muted-foreground">Fleet Carbon Reduction</span>
          <Activity className="h-5 w-5 text-blue-400" />
        </div>
        <div className="mt-4">
          <span className="text-3xl font-bold text-blue-400">{reductionPercentage}%</span>
          <span className="block text-xs text-muted-foreground mt-1.5">vs Diesel Baseline ({summary.total_reports} reports)</span>
        </div>
      </div>

      <div className="glass p-6 rounded-xl transition-all hover:border-amber-500/50 hover:shadow-[0_0_15px_rgba(245,158,11,0.15)]">
        <div className="flex justify-between items-center">
          <span className="text-sm font-semibold text-muted-foreground">Sustainability Score</span>
          <Award className="h-5 w-5 text-amber-400" />
        </div>
        <div className="mt-4">
          <span className="text-3xl font-bold text-amber-400">{summary.average_readiness_score}/100</span>
          <span className="block text-xs text-muted-foreground mt-1.5">Across {summary.vehicles_assessed} assessed vehicles</span>
        </div>
      </div>
    </div>
  );
}
