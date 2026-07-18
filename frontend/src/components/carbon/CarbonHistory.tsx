import { useEffect, useState } from 'react';
import { Cpu } from 'lucide-react';
import { sustainabilityApi, CarbonReport } from '../../services/sustainability';

interface CarbonHistoryProps {
  latestReport: CarbonReport | null;
}

export function CarbonHistory({ latestReport }: CarbonHistoryProps) {
  const [history, setHistory] = useState<CarbonReport[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchHistory = async () => {
    try {
      setLoading(true);
      setError(null);
      const res = await sustainabilityApi.getHistory();
      if (res.success && res.data) {
        setHistory(res.data);
      } else {
        setError(res.message);
      }
    } catch (err: any) {
      setError(err.message || 'Failed to fetch history');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  useEffect(() => {
    if (latestReport) {
      // Prepend the new report for an immediate update without full refetch
      setHistory(prev => {
        // Prevent duplicates if websocket fires twice or fetch brings it in
        if (prev.find(r => r.report_id === latestReport.report_id)) return prev;
        return [latestReport, ...prev].slice(0, 50); // Keep max 50
      });
    }
  }, [latestReport]);

  if (loading && history.length === 0) {
    return (
      <div className="glass p-6 rounded-xl flex flex-col justify-between animate-pulse min-h-[300px]">
        <div className="h-6 w-1/2 bg-muted/20 rounded mb-4"></div>
        <div className="flex-1 bg-muted/10 rounded"></div>
      </div>
    );
  }

  if (error && history.length === 0) {
    return (
      <div className="glass p-6 rounded-xl border border-red-500/30 flex flex-col items-center justify-center min-h-[300px] text-red-400">
        <p className="mb-4">Failed to load carbon history</p>
        <button onClick={fetchHistory} className="px-4 py-2 bg-red-500/20 rounded hover:bg-red-500/30 transition-colors">
          Retry
        </button>
      </div>
    );
  }

  if (history.length === 0) {
    return (
      <div className="glass p-6 rounded-xl flex flex-col justify-between min-h-[300px]">
        <div>
          <h2 className="font-semibold text-lg">Scope-1 & Scope-3 Emission History</h2>
          <p className="text-xs text-muted-foreground mt-1">No historical reports available yet.</p>
        </div>
        <div className="my-8 h-40 bg-muted/20 border border-border/50 rounded-lg flex items-center justify-center text-xs text-muted-foreground">
          <div className="flex flex-col items-center gap-1.5">
            <Cpu className="h-8 w-8 text-muted-foreground/50" />
            <span>Telemetry streams will generate data here</span>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="glass p-6 rounded-xl flex flex-col h-full max-h-[500px]">
      <div>
        <h2 className="font-semibold text-lg">Scope-1 & Scope-3 Emission History</h2>
        <p className="text-xs text-muted-foreground mt-1">Historical carbon footprint tracking per vehicle.</p>
      </div>
      
      <div className="mt-4 flex-1 overflow-y-auto space-y-3 pr-2 custom-scrollbar">
        {history.map(report => (
          <div key={report.report_id} className="p-3 bg-muted/20 hover:bg-muted/30 transition-colors border border-border/50 rounded-lg flex flex-col gap-2">
            <div className="flex justify-between items-center">
              <span className="text-sm font-bold">{report.vehicle_id}</span>
              <span className="text-[10px] text-muted-foreground">
                {new Date(report.generated_at).toLocaleString()}
              </span>
            </div>
            
            <div className="grid grid-cols-3 gap-2 text-xs">
              <div>
                <span className="block text-muted-foreground">Distance</span>
                <span className="font-medium">{report.distance_travelled.toFixed(1)} km</span>
              </div>
              <div>
                <span className="block text-muted-foreground">Scope-1 (Diesel)</span>
                <span className="font-medium text-red-400">{report.scope1_emission.toFixed(1)} kg</span>
              </div>
              <div>
                <span className="block text-muted-foreground">Scope-3 (EV)</span>
                <span className="font-medium text-emerald-400">{report.scope3_emission.toFixed(1)} kg</span>
              </div>
            </div>
          </div>
        ))}
      </div>
      
      <div className="border-t border-border pt-3 mt-3 text-xs text-muted-foreground flex justify-between shrink-0">
        <span>Region: {history[0]?.grid_region.toUpperCase() || 'INDIA'}</span>
        <span>Latest Update: {new Date(history[0]?.generated_at).toLocaleDateString()}</span>
      </div>
    </div>
  );
}
