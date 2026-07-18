import { useState, useEffect } from 'react';
import { sustainabilityApi, ProcurementRecommendationResponse } from '../../services/sustainability';

export function ProcurementCard() {
  const [fleetSize, setFleetSize] = useState<number>(50);
  const [dailyDistance, setDailyDistance] = useState<number>(120);
  const [charging, setCharging] = useState<boolean>(true);
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ProcurementRecommendationResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleRecommend = async () => {
    try {
      setLoading(true);
      setError(null);
      const res = await sustainabilityApi.getProcurementRecommendation({
        fleet_size: fleetSize,
        daily_distance: dailyDistance,
        charging_available: charging
      });
      if (res.success) {
        setResult(res.data);
      } else {
        setError(res.message);
      }
    } catch (err: any) {
      setError(err.message || 'Failed to get recommendation');
    } finally {
      setLoading(false);
    }
  };

  // Run on mount
  useEffect(() => {
    handleRecommend();
  }, []);

  return (
    <div className="glass p-6 rounded-xl space-y-4 flex flex-col h-full max-h-[500px]">
      <div>
        <h2 className="font-semibold text-lg">Procurement Recommendation</h2>
        <p className="text-xs text-muted-foreground mt-1">Get AI-driven EV purchasing suggestions based on operational needs.</p>
      </div>
      
      <div className="grid grid-cols-2 gap-3 text-sm shrink-0">
        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">Fleet Size</label>
          <input 
            type="number" 
            value={fleetSize} 
            onChange={e => setFleetSize(Number(e.target.value))}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-purple-500/50"
          />
        </div>
        
        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">Avg Daily Distance (km)</label>
          <input 
            type="number" 
            value={dailyDistance} 
            onChange={e => setDailyDistance(Number(e.target.value))}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-purple-500/50"
          />
        </div>

        <div className="flex flex-col gap-1 col-span-2">
          <label className="text-xs text-muted-foreground">Depot Charging Infrastructure</label>
          <select 
            value={charging ? "yes" : "no"} 
            onChange={e => setCharging(e.target.value === "yes")}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-purple-500/50"
          >
            <option value="yes">Installed and Operational</option>
            <option value="no">Planned / Not Available</option>
          </select>
        </div>
      </div>
      
      <button 
        onClick={handleRecommend}
        disabled={loading}
        className="w-full py-2 bg-purple-500/20 text-purple-400 hover:bg-purple-500/30 rounded-lg transition-colors font-semibold disabled:opacity-50 shrink-0"
      >
        {loading ? 'Analyzing...' : 'Generate Recommendation'}
      </button>

      {error && (
        <div className="text-xs text-red-400 p-2 bg-red-500/10 rounded border border-red-500/30 shrink-0">
          {error}
        </div>
      )}

      {result && !loading && (
        <div className="mt-4 pt-4 border-t border-border animate-fade-in flex-1 overflow-y-auto custom-scrollbar pr-2 space-y-4">
          <div className="p-4 bg-purple-500/10 rounded-lg border border-purple-500/20 text-center">
            <span className="block text-xs text-purple-400 font-semibold mb-1">Recommended Action</span>
            <span className="text-xl font-bold">Acquire {result.recommended_quantity}x {result.recommended_vehicle_type}</span>
          </div>
          
          <div className="grid grid-cols-2 gap-3">
            <div className="p-3 bg-muted/20 rounded-lg border border-border/50">
              <span className="block text-[10px] uppercase text-muted-foreground font-semibold mb-1">Impact</span>
              <span className="text-sm font-bold text-emerald-400">-{result.estimated_carbon_saving.toFixed(1)} Tons CO₂/yr</span>
            </div>
            <div className="p-3 bg-muted/20 rounded-lg border border-border/50">
              <span className="block text-[10px] uppercase text-muted-foreground font-semibold mb-1">Confidence</span>
              <span className={`text-sm font-bold ${
                result.recommendation_level === 'HIGH' ? 'text-emerald-400' :
                result.recommendation_level === 'MEDIUM' ? 'text-amber-400' : 'text-red-400'
              }`}>{result.recommendation_level}</span>
            </div>
          </div>

          <div className="text-xs text-muted-foreground leading-relaxed bg-muted/10 p-3 rounded-lg">
            {result.reasoning}
          </div>
        </div>
      )}
    </div>
  );
}
