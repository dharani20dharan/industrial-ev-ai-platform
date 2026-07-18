import { useState } from 'react';
import { sustainabilityApi, DieselVsEVResponse } from '../../services/sustainability';

export function DieselComparison() {
  const [vehicleType, setVehicleType] = useState('medium_truck');
  const [distance, setDistance] = useState<number>(100);
  const [payload, setPayload] = useState<number>(1000);
  const [dieselEfficiency, setDieselEfficiency] = useState<number>(25);
  const [evEfficiency, setEvEfficiency] = useState<number>(0.8);
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<DieselVsEVResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleCompare = async () => {
    try {
      setLoading(true);
      setError(null);
      const res = await sustainabilityApi.compareDieselVsEv({
        distance_km: distance,
        payload_kg: payload,
        diesel_efficiency: dieselEfficiency,
        ev_efficiency: evEfficiency,
        vehicle_type: vehicleType
      });
      if (res.success) {
        setResult(res.data);
      } else {
        setError(res.message);
      }
    } catch (err: any) {
      setError(err.message || 'Failed to compare options');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="glass p-6 rounded-xl space-y-4">
      <h2 className="font-semibold text-lg">Diesel vs EV Scenario Modeler</h2>
      <p className="text-xs text-muted-foreground">Compare emissions based on specific route metrics and payloads.</p>
      
      <div className="grid grid-cols-2 gap-3 text-sm">
        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">Vehicle Type</label>
          <select 
            value={vehicleType} 
            onChange={e => setVehicleType(e.target.value)}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-blue-500/50"
          >
            <option value="delivery_van">Delivery Van</option>
            <option value="medium_truck">Medium Truck</option>
            <option value="heavy_truck">Heavy Truck</option>
            <option value="bus">Bus</option>
          </select>
        </div>
        
        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">Distance (km)</label>
          <input 
            type="number" 
            value={distance} 
            onChange={e => setDistance(Number(e.target.value))}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-blue-500/50"
          />
        </div>

        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">Payload (kg)</label>
          <input 
            type="number" 
            value={payload} 
            onChange={e => setPayload(Number(e.target.value))}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-blue-500/50"
          />
        </div>

        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">Diesel Efficiency (L/100km)</label>
          <input 
            type="number" 
            value={dieselEfficiency} 
            onChange={e => setDieselEfficiency(Number(e.target.value))}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-blue-500/50"
          />
        </div>

        <div className="flex flex-col gap-1">
          <label className="text-xs text-muted-foreground">EV Efficiency (kWh/km)</label>
          <input 
            type="number" 
            value={evEfficiency} 
            onChange={e => setEvEfficiency(Number(e.target.value))}
            className="bg-muted/20 border border-border/50 rounded-md p-2 outline-none focus:border-blue-500/50"
          />
        </div>
      </div>
      
      <button 
        onClick={handleCompare}
        disabled={loading}
        className="w-full py-2 bg-blue-500/20 text-blue-400 hover:bg-blue-500/30 rounded-lg transition-colors font-semibold disabled:opacity-50"
      >
        {loading ? 'Calculating...' : 'Run Comparison'}
      </button>

      {error && (
        <div className="text-xs text-red-400 p-2 bg-red-500/10 rounded border border-red-500/30">
          {error}
        </div>
      )}

      {result && !loading && (
        <div className="mt-4 pt-4 border-t border-border grid grid-cols-2 gap-4 animate-fade-in">
          <div className="p-3 bg-red-500/10 rounded-lg border border-red-500/20">
            <span className="block text-xs text-red-400 font-semibold mb-1">Diesel Emissions</span>
            <span className="text-xl font-bold">{result.diesel_emission.toFixed(1)} kg</span>
          </div>
          <div className="p-3 bg-emerald-500/10 rounded-lg border border-emerald-500/20">
            <span className="block text-xs text-emerald-400 font-semibold mb-1">EV Emissions</span>
            <span className="text-xl font-bold">{result.ev_emission.toFixed(1)} kg</span>
          </div>
          <div className="col-span-2 p-3 bg-blue-500/10 rounded-lg border border-blue-500/20 flex justify-between items-center">
            <div>
              <span className="block text-xs text-blue-400 font-semibold mb-1">Net Savings</span>
              <span className="text-xl font-bold text-blue-400">{result.carbon_saved.toFixed(1)} kg CO₂</span>
            </div>
            <div className="text-right">
              <span className="block text-xs text-blue-400/80 mb-1">Reduction</span>
              <span className="text-xl font-bold text-blue-400">{result.reduction_percentage.toFixed(1)}%</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
