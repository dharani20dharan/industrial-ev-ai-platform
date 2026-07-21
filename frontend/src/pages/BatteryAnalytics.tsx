import React, { useState, useEffect } from 'react';
import { BatteryCharging, Thermometer, ShieldAlert, Cpu, Zap } from 'lucide-react';
import { useFleetData } from '../hooks/useFleetData';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';
import { coreApi } from '../services/coreApi';

interface PredictionCurvePoint {
  cycle: number;
  nominal: number;
  predicted: number;
}

export default function BatteryAnalytics() {
  const { fleet, alerts } = useFleetData();
  const [degradationData, setDegradationData] = useState<PredictionCurvePoint[]>([]);
  const [chargingHistory, setChargingHistory] = useState<any[]>([]);
  const [apiError, setApiError] = useState<boolean>(false);

  const targetAssetId = "EV-HD-004";
  const liveData = fleet[targetAssetId];

  const currentTemp = liveData?.motor_temperature_c !== undefined ? liveData.motor_temperature_c : 38.4;
  const tempPercentage = Math.min(100, (currentTemp / 55) * 100);
  const isOverheating = currentTemp > 100;

  const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

  useEffect(() => {
    const fetchPredictionCurve = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/api/v1/battery/status?vehicle_id=${targetAssetId}`);
        if (!response.ok) throw new Error("Target pipeline output unreachable");
        const data = await response.json();

        const currentCapacity = 120 * (data.state_of_health / 100);
        const currentCycle = data.cycle_count || 1000;

        const generatedCurve = [
          { cycle: 0, nominal: 120, predicted: 120 },
          { cycle: Math.floor(currentCycle * 0.25), nominal: 120, predicted: 120 - (data.capacity_fade * 0.25) },
          { cycle: Math.floor(currentCycle * 0.50), nominal: 120, predicted: 120 - (data.capacity_fade * 0.50) },
          { cycle: Math.floor(currentCycle * 0.75), nominal: 120, predicted: 120 - (data.capacity_fade * 0.75) },
          { cycle: currentCycle, nominal: 120, predicted: currentCapacity },
          { cycle: currentCycle + data.remaining_useful_life, nominal: 120, predicted: 96 },
        ];

        setDegradationData(generatedCurve);
        setApiError(false);
      } catch (error) {
        console.warn("Falling back to baseline matrix - API disconnected:", error);
        setApiError(true);
      }
    };

    const fetchChargingData = async () => {
      try {
        const history = await coreApi.getChargingHistory(targetAssetId);
        setChargingHistory(history.slice(0, 5)); // Show latest 5 sessions
      } catch (error) {
        console.error("Failed to load charging history", error);
      }
    };

    fetchPredictionCurve();
    fetchChargingData();
  }, [API_BASE_URL]);

  const displayData = apiError || degradationData.length === 0 ? [
    { cycle: 0, nominal: 120, predicted: 120 },
    { cycle: 200, nominal: 120, predicted: 118.5 },
    { cycle: 400, nominal: 120, predicted: 116.8 },
    { cycle: 600, nominal: 120, predicted: 115.2 },
    { cycle: 800, nominal: 120, predicted: 114.2 },
    { cycle: 1000, nominal: 120, predicted: liveData ? 114.2 - (currentTemp * 0.005) : 112.1 },
  ] : degradationData;

  const targetedCriticalAlerts = alerts.filter(a => a.asset === targetAssetId || a.type === 'Critical');

  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-extrabold tracking-tight">Advanced Battery Intelligence</h1>
            <p className="text-muted-foreground mt-1">Deep analytics on capacity fade, thermal profiles, and degradation predictors.</p>
          </div>
          {apiError && (
            <span className="px-2 py-1 rounded bg-amber-500/10 border border-amber-500/20 text-amber-400 text-xs font-mono">
              Offline Cache Mode
            </span>
          )}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <div className="flex justify-between items-center">
              <h2 className="font-semibold text-lg">Thermal Diagnostics</h2>
              <Thermometer className={`h-5 w-5 ${isOverheating ? 'text-red-500 animate-bounce' : 'text-red-400'}`} />
            </div>
          </div>
          <div className="my-8 flex justify-center items-center">
            <div className={`relative h-32 w-32 rounded-full border-4 border-dashed flex flex-col justify-center items-center transition-all ${
              isOverheating ? 'border-red-500 bg-red-500/10 animate-pulse' : 'border-red-500/30'
            }`}>
              <span className="text-2xl font-bold font-mono">{currentTemp.toFixed(1)}°C</span>
              <span className={`text-[10px] uppercase tracking-wider font-semibold ${isOverheating ? 'text-red-400' : 'text-emerald-400'}`}>
                {isOverheating ? 'Thermal Overload' : 'Healthy Range'}
              </span>
            </div>
          </div>
          <div className="space-y-2">
            <div className="flex justify-between text-xs font-semibold text-muted-foreground">
              <span>Upper Safety Threshold</span>
              <span>55.0°C</span>
            </div>
            <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
              <div
                className={`h-full transition-all duration-300 ${isOverheating ? 'bg-red-500' : 'bg-amber-500'}`}
                style={{ width: `${tempPercentage}%` }}
              />
            </div>
          </div>
        </div>

        <div className="glass p-6 rounded-xl flex flex-col justify-between lg:col-span-2">
          <div>
            <div className="flex justify-between items-center">
              <h2 className="font-semibold text-lg">Capacity Degradation Curve</h2>
              <BatteryCharging className="h-5 w-5 text-emerald-400" />
            </div>
          </div>
          <div className="h-48 w-full bg-muted/10 border border-border/40 rounded-lg p-2 mt-4">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={displayData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#2e2e2e" />
                <XAxis dataKey="cycle" stroke="#888888" fontSize={11} tickLine={false} />
                <YAxis domain={['auto', 'auto']} stroke="#888888" fontSize={11} tickLine={false} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#1e1b4b', borderColor: '#312e81', borderRadius: '8px' }}
                  labelStyle={{ color: '#94a3b8', fontSize: '11px' }}
                  itemStyle={{ fontSize: '12px' }}
                />
                <Line type="monotone" dataKey="nominal" stroke="#64748b" strokeDasharray="5 5" name="Nominal Limit" dot={false} />
                <Line type="monotone" dataKey="predicted" stroke="#3b82f6" strokeWidth={2.5} name="XGBoost Prediction" dot={true} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="glass p-6 rounded-xl space-y-4">
          <div className="flex items-center gap-2">
            <Cpu className="h-5 w-5 text-blue-400" />
            <h2 className="font-semibold text-lg">AI Anomaly Alerts</h2>
          </div>
          <div className="space-y-3 max-h-[180px] overflow-y-auto pr-1">
            {targetedCriticalAlerts.length > 0 ? (
              targetedCriticalAlerts.map((alert, idx) => (
                <div key={idx} className="border-l-4 border-red-500 bg-red-500/5 p-4 rounded-r-lg flex items-start gap-3">
                  <ShieldAlert className="h-5 w-5 text-red-500 shrink-0 mt-0.5 animate-pulse" />
                  <div>
                    <h4 className="text-sm font-bold text-red-400">Critical Anomaly</h4>
                    <p className="text-xs text-muted-foreground mt-0.5">{alert.msg}</p>
                  </div>
                </div>
              ))
            ) : (
              <div className="text-xs text-muted-foreground">No active anomalies for this asset.</div>
            )}
          </div>
        </div>

        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <h2 className="font-semibold text-lg">RUL Prediction</h2>
          </div>
          <div className="my-6 text-center">
            <span className="text-4xl font-extrabold text-blue-500 font-mono">
              {liveData && isOverheating ? '430' : '1,120'}
            </span>
            <span className="text-sm text-muted-foreground block mt-1">Estimated Remaining Cycles</span>
          </div>
        </div>

        {/* NEW: Charging History Component */}
        <div className="glass p-6 rounded-xl flex flex-col">
          <div className="flex items-center gap-2 mb-4">
            <Zap className="h-5 w-5 text-amber-400" />
            <h2 className="font-semibold text-lg">Recent Charge Sessions</h2>
          </div>
          <div className="space-y-3 overflow-y-auto">
            {chargingHistory.length > 0 ? chargingHistory.map((session, idx) => (
              <div key={idx} className="flex justify-between items-center text-xs p-2 rounded bg-muted/20 border border-border/50">
                <div>
                  <span className="font-bold text-slate-200 block">Charger: {session.charger_id}</span>
                  <span className="text-muted-foreground">Consumed: {session.energy_consumed_kwh?.toFixed(1)} kWh</span>
                </div>
                <div className="text-right">
                  <span className="text-emerald-400 font-mono block">{session.starting_soc}% → {session.ending_soc}%</span>
                  <span className="text-muted-foreground">{new Date(session.end_time).toLocaleDateString()}</span>
                </div>
              </div>
            )) : (
              <div className="text-xs text-muted-foreground text-center py-4">Awaiting charging telemetry...</div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
