import { useState, useEffect } from 'react';
import { sustainabilityApi, ReadinessAssessmentResponse } from '../../services/sustainability';

export function ReadinessCard() {
  const [distance, setDistance] = useState<number>(150);
  const [payload, setPayload] = useState<number>(5000);
  const [dwellTime, setDwellTime] = useState<number>(4);
  const [charging, setCharging] = useState<boolean>(true);
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ReadinessAssessmentResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleAssess = async () => {
    try {
      setLoading(true);
      setError(null);
      const res = await sustainabilityApi.assessReadiness({
        route_distance: distance,
        payload: payload,
        dwell_time: dwellTime,
        charging_availability: charging,
        vehicle_type: "medium_truck"
      });
      if (res.success) {
        setResult(res.data);
      } else {
        setError(res.message);
      }
    } catch (err: any) {
      setError(err.message || 'Failed to assess readiness');
    } finally {
      setLoading(false);
    }
  };

  // Run a default assessment on mount
  useEffect(() => {
    handleAssess();
  }, []);

  const getLevelColor = (level: string) => {
    switch (level) {
      case 'HIGHLY_READY': return 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20';
      case 'READY': return 'text-blue-400 bg-blue-500/10 border-blue-500/20';
      case 'PARTIALLY_READY': return 'text-amber-400 bg-amber-500/10 border-amber-500/20';
      case 'NOT_READY': return 'text-red-400 bg-red-500/10 border-red-500/20';
      default: return 'text-gray-400 bg-gray-500/10 border-gray-500/20';
    }
  };

  return (
    <div className="glass p-6 rounded-xl space-y-4">
      <h2 className="font-semibold text-lg">Electrification Readiness Scorecard</h2>
      <p className="text-xs text-muted-foreground">Test a specific route profile for EV feasibility.</p>
      
      <div className="grid grid-cols-2 gap-3 text-sm">
        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">Route Distance (km)</label>
          <input 
            type="number" 
            value={distance} 
            onChange={e => setDistance(Number(e.target.value))}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-amber-500/50"
          />
        </div>
        
        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">Payload (kg)</label>
          <input 
            type="number" 
            value={payload} 
            onChange={e => setPayload(Number(e.target.value))}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-amber-500/50"
          />
        </div>

        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">Depot Dwell Time (hrs)</label>
          <input 
            type="number" 
            value={dwellTime} 
            onChange={e => setDwellTime(Number(e.target.value))}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-amber-500/50"
          />
        </div>

        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">En-Route Charging</label>
          <select 
            value={charging ? "yes" : "no"} 
            onChange={e => setCharging(e.target.value === "yes")}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-amber-500/50"
          >
            <option value="yes">Available</option>
            <option value="no">Not Available</option>
          </select>
        </div>
      </div>
      
      <button 
        onClick={handleAssess}
        disabled={loading}
        className="w-full py-2 bg-amber-500/20 text-amber-400 hover:bg-amber-500/30 rounded-lg transition-colors font-semibold disabled:opacity-50"
      >
        {loading ? 'Assessing...' : 'Score Route'}
      </button>

      {error && (
        <div className="text-xs text-red-400 p-2 bg-red-500/10 rounded border border-red-500/30">
          {error}
        </div>
      )}

      {result && !loading && (
        <div className="mt-4 pt-4 border-t border-border animate-fade-in space-y-4">
          <div className="flex justify-between items-center">
            <div>
              <span className="block text-2xl font-bold">{result.readiness_score.toFixed(0)}/100</span>
              <span className="text-xs text-muted-foreground">Readiness Score</span>
            </div>
            <span className={`text-xs font-bold px-3 py-1.5 rounded-full border ${getLevelColor(result.readiness_level)}`}>
              {result.readiness_level.replace('_', ' ')}
            </span>
          </div>
          
          <div className="text-sm bg-muted/20 p-3 rounded-lg border border-border/50">
            {result.recommendation}
          </div>
          
          {result.improvements_needed && result.improvements_needed.length > 0 && (
            <div>
              <span className="text-xs font-semibold text-muted-foreground mb-2 block">Limiting Factors</span>
              <ul className="text-xs space-y-1 list-disc pl-4 text-red-400/80">
                {result.improvements_needed.map((imp, idx) => (
                  <li key={idx}>{imp}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
