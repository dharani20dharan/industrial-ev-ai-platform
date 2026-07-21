import { useMemo, useState } from 'react';
import { Truck, Battery, AlertTriangle, Activity, Navigation, Zap, PauseCircle } from 'lucide-react';
import { useFleetData } from '../hooks/useFleetData';
import FleetMap, { FleetMapVehicle } from '../components/maps/FleetMap';
import VehicleInspector from '../components/simulator/VehicleInspector';

function extractStatusString(v: any): string {
  if (!v) return 'IDLE';
  if (typeof v.status === 'string') return v.status.toUpperCase();
  if (v.status && typeof v.status.operational_status === 'string') return v.status.operational_status.toUpperCase();
  if (typeof v.driving_state === 'string') return v.driving_state.toUpperCase();
  if (v.is_charging) return 'CHARGING';
  if (v.is_moving) return 'DRIVING';
  return 'IDLE';
}

export default function FleetOverview() {
  const { fleet, alerts, msgPerSec } = useFleetData();
  const [selectedVehicleId, setSelectedVehicleId] = useState<string | undefined>();

  // Memoize active vehicles list
  const activeAssets = useMemo(() => Object.values(fleet), [fleet]);

  const criticalCount = useMemo(() =>
    alerts.filter(a => a.type === 'Critical').length,
    [alerts]
  );

  // Dynamic Metrics Calculation
  const metrics = useMemo(() => {
    let totalSoC = 0;
    let totalSpeed = 0;
    let drivingCount = 0;
    let chargingCount = 0;
    let idleCount = 0;
    let faultCount = 0;

    activeAssets.forEach(v => {
      totalSoC += (v.soc || 0);
      totalSpeed += (v.speed_kph || 0);
      const status = extractStatusString(v);
      if (status === 'CHARGING' || v.is_charging) chargingCount++;
      else if (status === 'FAULT' || status === 'CRITICAL' || v.active_anomaly) faultCount++;
      else if (status === 'IDLE' || (!v.is_moving && !v.is_charging)) idleCount++;
      else drivingCount++;
    });

    const count = activeAssets.length || 1;
    return {
      avgSoc: (totalSoC / count).toFixed(1),
      avgSpeed: (totalSpeed / count).toFixed(1),
      drivingCount,
      chargingCount,
      idleCount,
      faultCount
    };
  }, [activeAssets]);

  // Format fleet data into standardized FleetMapVehicle array
  const mapVehicles = useMemo<FleetMapVehicle[]>(() =>
    activeAssets.map(liveData => ({
      vehicle_id: liveData.vehicle_id,
      fleet_id: liveData.fleet_id || "FLT-ALPHA-01",
      profile_name: liveData.profile_name || "DELIVERY",
      vehicle_type: liveData.vehicle_type || "DELIVERY_VAN",
      latitude: liveData.latitude,
      longitude: liveData.longitude,
      status: extractStatusString(liveData),
      speed_kph: liveData.speed_kph,
      heading: liveData.heading || liveData.heading_deg,
      motor_temperature_c: liveData.motor_temperature_c || liveData.temperature,
      cell_temp: liveData.cell_temp,
      soc: liveData.soc,
      soh: liveData.soh,
      voltage: liveData.voltage,
      current_amps: liveData.current_amps,
      power_kw: liveData.power_kw,
      is_charging: liveData.is_charging,
      is_moving: liveData.is_moving,
      driving_state: liveData.driving_state,
      active_anomaly: liveData.active_anomaly,
      last_updated: liveData.timestamp
    })),
    [activeAssets]
  );

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header View Row */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight">Fleet Asset Operations</h1>
          <p className="text-muted-foreground mt-1">Single source of truth live telemetry monitoring, asset health, and geospatial operations.</p>
        </div>
        <div className="flex items-center gap-2 bg-muted/50 px-3 py-1.5 rounded-lg text-xs font-medium border border-border">
          <Activity className="h-4.5 w-4.5 text-blue-500 animate-pulse" />
          <span>Ingesting: {msgPerSec || 0} Telemetry msg/sec</span>
        </div>
      </div>

      {/* Metric Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
        <div className="glass p-5 rounded-xl glow-blue">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Active Fleet Assets</span>
            <div className="p-2 bg-blue-500/10 rounded-lg text-blue-500"><Truck className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">{activeAssets.length}</span>
            <span className="text-xs text-emerald-500 font-medium">Online</span>
          </div>
          <div className="mt-3 grid grid-cols-4 gap-1 text-[10px] font-medium text-center">
             <div className="bg-blue-500/10 text-blue-400 rounded py-1">{metrics.drivingCount} Driving</div>
             <div className="bg-emerald-500/10 text-emerald-400 rounded py-1">{metrics.chargingCount} Charging</div>
             <div className="bg-amber-500/10 text-amber-400 rounded py-1">{metrics.idleCount} Idle</div>
             <div className="bg-red-500/10 text-red-400 rounded py-1">{metrics.faultCount} Fault</div>
          </div>
        </div>

        <div className="glass p-5 rounded-xl">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Average Fleet SoC</span>
            <div className="p-2 bg-emerald-500/10 rounded-lg text-emerald-500"><Battery className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">{activeAssets.length > 0 ? metrics.avgSoc : '--'}%</span>
            <span className="text-xs text-muted-foreground">Active Fleet Avg</span>
          </div>
        </div>
        
        <div className="glass p-5 rounded-xl">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Average Fleet Speed</span>
            <div className="p-2 bg-cyan-500/10 rounded-lg text-cyan-500"><Navigation className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">{activeAssets.length > 0 ? metrics.avgSpeed : '--'}</span>
            <span className="text-xs text-muted-foreground">km/h</span>
          </div>
        </div>

        <div className="glass p-5 rounded-xl">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Predictive Maintenance Alerts</span>
            <div className="p-2 bg-red-500/10 rounded-lg text-red-500"><AlertTriangle className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">{criticalCount}</span>
            <span className="text-xs text-red-500 font-semibold">Active Critical Anomalies</span>
          </div>
        </div>
      </div>

      {/* Main Map & Vehicle Inspector Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className={`glass rounded-xl overflow-hidden p-5 ${selectedVehicleId ? 'lg:col-span-2' : 'lg:col-span-3'}`}>
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2">
              <Navigation className="h-5 w-5 text-blue-400" />
              <h2 className="text-lg font-semibold">Live Geospatial Telemetry Map</h2>
            </div>
            {selectedVehicleId && (
              <button 
                onClick={() => setSelectedVehicleId(undefined)}
                className="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 px-3 py-1 rounded transition-colors"
              >
                Clear Selection
              </button>
            )}
          </div>

          <FleetMap
            vehicles={mapVehicles}
            selectedVehicleId={selectedVehicleId}
            onSelectVehicle={setSelectedVehicleId}
            height="h-[460px]"
            defaultCenter={[28.6139, 77.2090]}
            defaultZoom={12}
          />
        </div>

        {/* Vehicle Inspector Drawer when a vehicle is selected */}
        {selectedVehicleId && (
          <div className="lg:col-span-1">
            <VehicleInspector 
              vehicleId={selectedVehicleId} 
              onClose={() => setSelectedVehicleId(undefined)} 
            />
          </div>
        )}
      </div>

      {/* Detailed Live Fleet Operations Table */}
      <div className="glass rounded-xl overflow-hidden">
        <div className="px-6 py-5 border-b border-border flex justify-between items-center">
          <div>
            <h2 className="text-lg font-semibold">Live Fleet Operations Table</h2>
            <p className="text-xs text-muted-foreground mt-0.5">Select any row to focus map marker and view full electro-chemical diagnostics</p>
          </div>
          <span className="text-xs font-semibold text-muted-foreground bg-muted/60 px-3 py-1.5 rounded-lg border border-border">
            Total Active Assets: {activeAssets.length}
          </span>
        </div>
        <div className="overflow-x-auto max-h-[500px] overflow-y-auto">
          <table className="w-full text-left border-collapse relative">
            <thead className="sticky top-0 z-20 glass">
              <tr className="border-b border-border bg-slate-900/90 text-xs uppercase tracking-wider text-slate-400">
                <th className="px-6 py-4">Asset ID</th>
                <th className="px-6 py-4">Fleet</th>
                <th className="px-6 py-4">Profile</th>
                <th className="px-6 py-4">State</th>
                <th className="px-6 py-4">Speed</th>
                <th className="px-6 py-4">Battery SoC</th>
                <th className="px-6 py-4">Motor Temp</th>
                <th className="px-6 py-4">Live Location</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border text-sm">
              {activeAssets.length === 0 ? (
                <tr>
                  <td colSpan={8} className="px-6 py-12 text-center text-muted-foreground">
                    <div className="flex flex-col items-center justify-center">
                      <Truck className="h-10 w-10 text-slate-700 mb-3" />
                      <p>No active vehicles detected in simulation runtime.</p>
                      <p className="text-xs mt-1 text-slate-500">Go to Simulation Controller to spawn fleets or scenarios.</p>
                    </div>
                  </td>
                </tr>
              ) : (
                activeAssets.map((liveData) => {
                  const speedDisplay = liveData.speed_kph !== undefined ? `${liveData.speed_kph.toFixed(1)} km/h` : '0.0 km/h';
                  const tempDisplay = liveData.motor_temperature_c !== undefined ? `${liveData.motor_temperature_c.toFixed(1)}°C` : 'N/A';
                  const socDisplay = liveData.soc !== undefined ? `${liveData.soc.toFixed(1)}%` : 'N/A';
                  
                  const locationDisplay = liveData.latitude && liveData.longitude
                    ? `${liveData.latitude.toFixed(4)}, ${liveData.longitude.toFixed(4)}`
                    : `Unknown`;

                  const currentStatus = extractStatusString(liveData);
                  const isCritical = currentStatus === 'CRITICAL' || currentStatus === 'FAULT' || !!liveData.active_anomaly;
                  const isWarning = currentStatus === 'WARNING';
                  const isCharging = currentStatus === 'CHARGING' || liveData.is_charging;
                  const isSelected = selectedVehicleId === liveData.vehicle_id;

                  return (
                    <tr 
                      key={liveData.vehicle_id} 
                      onClick={() => setSelectedVehicleId(liveData.vehicle_id)}
                      className={`transition-colors cursor-pointer border-l-2 ${
                        isSelected 
                          ? 'bg-blue-500/15 border-blue-500 font-semibold' 
                          : 'border-transparent hover:bg-slate-800/50'
                      }`}
                    >
                      <td className="px-6 py-3.5 font-mono font-bold text-slate-200">
                        {liveData.vehicle_id}
                      </td>
                      <td className="px-6 py-3.5 text-xs text-slate-300">
                        {liveData.fleet_id || "FLT-ALPHA-01"}
                      </td>
                      <td className="px-6 py-3.5 text-xs font-semibold text-slate-400">
                        {liveData.profile_name || "DELIVERY"}
                      </td>
                      <td className="px-6 py-3.5">
                        <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[10px] font-bold tracking-wider ${
                          isCritical ? 'bg-rose-500/20 text-rose-400 border border-rose-500/40 animate-pulse' :
                          isWarning ? 'bg-amber-500/20 text-amber-400 border border-amber-500/40' :
                          isCharging ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' :
                          currentStatus === 'IDLE' ? 'bg-slate-500/20 text-slate-400 border border-slate-500/40' :
                          'bg-blue-500/20 text-blue-400 border border-blue-500/40'
                        }`}>
                          {isCharging && <Zap className="w-3 h-3" />}
                          {currentStatus === 'IDLE' && <PauseCircle className="w-3 h-3" />}
                          {currentStatus === 'DRIVING' && <Navigation className="w-3 h-3" />}
                          {currentStatus}
                        </span>
                      </td>
                      <td className="px-6 py-3.5 font-mono text-slate-300">{speedDisplay}</td>
                      <td className="px-6 py-3.5 font-mono text-cyan-400">{socDisplay}</td>
                      <td className={`px-6 py-3.5 font-mono ${isCritical ? 'text-rose-400 font-bold animate-pulse' : 'text-slate-300'}`}>
                        {tempDisplay}
                      </td>
                      <td className="px-6 py-3.5 font-mono text-xs text-blue-400/90 font-semibold">
                        {locationDisplay}
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
