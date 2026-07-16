import React from 'react';
import { BatteryCharging, Thermometer, ShieldAlert, Cpu } from 'lucide-react';
import { useFleetData } from '../hooks/useFleetData';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

export default function BatteryAnalytics() {
  const { fleet, alerts } = useFleetData();

  // Focus primarily on EV-HD-004 as our primary telemetry streaming unit
  const targetAssetId = "EV-HD-004";
  const liveData = fleet[targetAssetId];

  // Dynamic values pulled from WebSocket or falling back to static seeds
  const currentTemp = liveData?.motor_temperature_c !== undefined ? liveData.motor_temperature_c : 38.4;
  const tempPercentage = Math.min(100, (currentTemp / 55) * 100);
  const isOverheating = currentTemp > 100;

  // Mocking an XGBoost degradation calculation array based on real-world cell health
  const mockDegradationData = [
    { cycle: 0, nominal: 120, predicted: 120 },
    { cycle: 200, nominal: 120, predicted: 118.5 },
    { cycle: 400, nominal: 120, predicted: 116.8 },
    { cycle: 600, nominal: 120, predicted: 115.2 },
    { cycle: 800, nominal: 120, predicted: 114.2 },
    { cycle: 1000, nominal: 120, predicted: liveData ? 114.2 - (currentTemp * 0.005) : 112.1 },
  ];

  // Dynamic filter looking for high-scoring AI anomalies in the hook's logs
  const targetedCriticalAlerts = alerts.filter(a => a.asset === targetAssetId || a.type === 'Critical');

  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-extrabold tracking-tight">Advanced Battery Intelligence</h1>
        <p className="text-muted-foreground mt-1">Deep analytics on capacity fade, thermal profiles, and degradation predictors.</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Real-time Cell Temp Indicator */}
        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <div className="flex justify-between items-center">
              <h2 className="font-semibold text-lg">Thermal Diagnostics</h2>
              <Thermometer className={`h-5 w-5 ${isOverheating ? 'text-red-500 animate-bounce' : 'text-red-400'}`} />
            </div>
            <p className="text-xs text-muted-foreground mt-1">Real-time status of thermal runaways and core gradients.</p>
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

        {/* Degradation Regression Predictor (Recharts Integration) */}
        <div className="glass p-6 rounded-xl flex flex-col justify-between lg:col-span-2">
          <div>
            <div className="flex justify-between items-center">
              <h2 className="font-semibold text-lg">Capacity Degradation Curve</h2>
              <BatteryCharging className="h-5 w-5 text-emerald-400" />
            </div>
            <p className="text-xs text-muted-foreground mt-1">Calculated capacity fade over consecutive charging/discharging cycles.</p>
          </div>

          <div className="h-48 w-full bg-muted/10 border border-border/40 rounded-lg p-2 mt-4">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={mockDegradationData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#2e2e2e" />
                <XAxis dataKey="cycle" stroke="#888888" fontSize={11} tickLine={false} />
                <YAxis domain={[100, 125]} stroke="#888888" fontSize={11} tickLine={false} />
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

          <div className="grid grid-cols-3 gap-4 text-center mt-4">
            <div className="bg-muted/30 p-2 rounded-lg">
              <span className="block text-xs text-muted-foreground">Nominal Cap</span>
              <span className="text-base font-bold font-mono">120 Ah</span>
            </div>
            <div className="bg-muted/30 p-2 rounded-lg">
              <span className="block text-xs text-muted-foreground">Current Cap</span>
              <span className="text-base font-bold font-mono text-emerald-500">
                {liveData ? (114.2 - (currentTemp * 0.002)).toFixed(1) : '114.2'} Ah
              </span>
            </div>
            <div className="bg-muted/30 p-2 rounded-lg">
              <span className="block text-xs text-muted-foreground">SOH State</span>
              <span className="text-base font-bold font-mono text-blue-500">
                {liveData && isOverheating ? '83.4%' : '95.1%'}
              </span>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Predictive AI Alert Cards */}
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
                    <h4 className="text-sm font-bold text-red-400">Critical Thermal Delta Excursion</h4>
                    <p className="text-xs text-muted-foreground mt-0.5">{alert.msg}</p>
                  </div>
                </div>
              ))
            ) : (
              <>
                <div className="border-l-4 border-red-500 bg-red-500/5 p-4 rounded-r-lg flex items-start gap-3">
                  <ShieldAlert className="h-5 w-5 text-red-500 shrink-0 mt-0.5" />
                  <div>
                    <h4 className="text-sm font-bold text-red-400">Thermal Runaway Baseline (Anomaly Score: 0.98)</h4>
                    <p className="text-xs text-muted-foreground mt-0.5">Asset EV-HD-004 showing abnormal discharge slope & cell delta temperature mismatch.</p>
                  </div>
                </div>
                <div className="border-l-4 border-yellow-500 bg-yellow-500/5 p-4 rounded-r-lg flex items-start gap-3">
                  <ShieldAlert className="h-5 w-5 text-yellow-500 shrink-0 mt-0.5" />
                  <div>
                    <h4 className="text-sm font-bold text-yellow-400">Micro-short Circuit Indicator</h4>
                    <p className="text-xs text-muted-foreground mt-0.5">Asset EV-HD-002 showing slight capacity drop during static charging phase.</p>
                  </div>
                </div>
              </>
            )}
          </div>
        </div>

        {/* SoH Predictor Detail */}
        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <h2 className="font-semibold text-lg">Remaining Useful Life (RUL) Prediction</h2>
            <p className="text-xs text-muted-foreground mt-1">Calculated remaining load cycles before cell capacity dips below 80% (End of Life).</p>
          </div>
          <div className="my-6">
            <div className="text-center">
              <span className="text-4xl font-extrabold text-blue-500 font-mono">
                {liveData && isOverheating ? '430' : '1,120'}
              </span>
              <span className="text-sm text-muted-foreground block mt-1">Estimated Remaining Cycles</span>
            </div>
          </div>
          <div className="border-t border-border pt-4 text-xs text-muted-foreground flex justify-between">
            <span>Regression Confidence: 94.2%</span>
            <span>Next inspection: {liveData && isOverheating ? 'Immediate' : '60 days'}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
