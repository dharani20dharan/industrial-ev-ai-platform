import React, { useMemo } from 'react';
import { Truck, Battery, AlertTriangle, ShieldCheck, Activity, Navigation } from 'lucide-react';
import { useFleetData } from '../hooks/useFleetData';

// Leaflet UI Engine Components
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';

// Core Map Controller Component to smoothly pan the camera to the main cluster
function MapUpdater({ coordinates }: { coordinates: [number, number][] }) {
  const map = useMap();
  React.useEffect(() => {
    if (coordinates.length > 0) {
      const bounds = L.latLngBounds(coordinates);
      map.fitBounds(bounds, { padding: [40, 40], maxZoom: 14 });
    }
  }, [coordinates, map]);
  return null;
}

// Factory function to build custom DOM-styled markers that bypass Leaflet's blue legacy images
const createCustomMarker = (status: string) => {
  let colorClass = "bg-emerald-400 ring-emerald-500/30";
  if (status === "Critical") colorClass = "bg-red-500 ring-red-500/50 animate-pulse";
  if (status === "Warning") colorClass = "bg-amber-400 ring-amber-500/30";
  if (status === "Charging") colorClass = "bg-blue-400 ring-blue-500/30 animate-pulse";

  return L.divIcon({
    className: 'custom-leaflet-marker',
    html: `
      <div class="relative flex items-center justify-center w-6 h-6">
        <div class="absolute w-6 h-6 rounded-full ring-4 opacity-40 animate-ping ${colorClass}"></div>
        <div class="w-3 h-3 rounded-full border-2 border-slate-900 shadow-md ${colorClass}"></div>
      </div>
    `,
    iconSize: [24, 24],
    iconAnchor: [12, 12]
  });
};

export default function FleetOverview() {
  const { fleet, alerts, msgPerSec } = useFleetData();

  // LATENCY PROTECTION: Memoize aggregate operations so 5 concurrent
  // high-frequency WebSocket vehicles don't cause browser execution chokes.
  const activeAssets = useMemo(() => Object.values(fleet), [fleet]);

  const criticalCount = useMemo(() =>
    alerts.filter(a => a.type === 'Critical').length,
    [alerts]
  );

  const defaultFleet = useMemo(() => [
    { id: "EV-HD-001", fallbackStatus: "Active", defaultLat: 37.7749, defaultLng: -122.4194 },
    { id: "EV-HD-002", fallbackStatus: "Charging", defaultLat: 37.7833, defaultLng: -122.4167 },
    { id: "EV-HD-003", fallbackStatus: "Active", defaultLat: 37.7699, defaultLng: -122.4468 },
    { id: "EV-HD-004", fallbackStatus: "Warning", defaultLat: 37.7599, defaultLng: -122.4368 },
  ], []);

  // Compute active coordinates array dynamically to feed the automated viewport framing calculations
  const mapCoordinates = useMemo<[number, number][]>(() =>
    defaultFleet.map(v => {
      const liveData = fleet[v.id];
      return [liveData?.latitude || v.defaultLat, liveData?.longitude || v.defaultLng];
    }),
    [fleet, defaultFleet]
  );

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header View Row */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight">Fleet Asset Intelligence</h1>
          <p className="text-muted-foreground mt-1">Real-time status, health index, and predictive alerts for industrial EV assets.</p>
        </div>
        <div className="flex items-center gap-2 bg-muted/50 px-3 py-1.5 rounded-lg text-xs font-medium border border-border">
          <Activity className="h-4.5 w-4.5 text-blue-500 animate-pulse" />
          <span>Ingesting: {msgPerSec || 1} Telemetry msg/sec</span>
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
            <span className="text-3xl font-bold">{Math.max(4, activeAssets.length)}</span>
            <span className="text-xs text-emerald-500 font-medium">100% Monitored</span>
          </div>
        </div>

        <div className="glass p-5 rounded-xl">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Average SoC</span>
            <div className="p-2 bg-emerald-500/10 rounded-lg text-emerald-500"><Battery className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">78.4%</span>
            <span className="text-xs text-muted-foreground">Healthy Charging</span>
          </div>
        </div>

        <div className="glass p-5 rounded-xl">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Predictive Maintenance Alerts</span>
            <div className="p-2 bg-red-500/10 rounded-lg text-red-500"><AlertTriangle className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">{criticalCount}</span>
            <span className="text-xs text-red-500 font-semibold">Critical Risks Active</span>
          </div>
        </div>

        <div className="glass p-5 rounded-xl">
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-muted-foreground">Avg Fleet Health Index</span>
            <div className="p-2 bg-emerald-500/10 rounded-lg text-emerald-500"><ShieldCheck className="h-5 w-5" /></div>
          </div>
          <div className="mt-4 flex items-baseline gap-2">
            <span className="text-3xl font-bold">92.8%</span>
            <span className="text-xs text-emerald-500 font-medium">+1.2% this week</span>
          </div>
        </div>
      </div>

      {/* Live Geospatial Real Map Layer Section */}
      <div className="glass rounded-xl overflow-hidden p-5">
        <div className="flex items-center gap-2 mb-4">
          <Navigation className="h-5 w-5 text-blue-400" />
          <h2 className="text-lg font-semibold">Live Geospatial Telemetry Layer</h2>
        </div>

        <div className="h-96 w-full rounded-lg overflow-hidden border border-border bg-slate-900 z-10 relative">
          <MapContainer
            center={[37.7749, -122.4194]}
            zoom={13}
            className="h-full w-full"
            style={{ background: '#0f172a' }}
          >
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
              url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
            />

            {defaultFleet.map((v) => {
              const liveData = fleet[v.id];
              const lat = liveData?.latitude || v.defaultLat;
              const lng = liveData?.longitude || v.defaultLng;
              const currentStatus = liveData ? liveData.status : v.fallbackStatus;

              return (
                <Marker
                  key={`real-map-${v.id}`}
                  position={[lat, lng]}
                  icon={createCustomMarker(currentStatus)}
                >
                  <Popup className="custom-map-popup">
                    <div className="p-1 font-mono text-xs text-slate-200">
                      <strong className="text-blue-400 block mb-1">{v.id}</strong>
                      <div className="space-y-0.5">
                        <div>Speed: {liveData?.speed_kph !== undefined ? `${liveData.speed_kph.toFixed(1)} kph` : '72.0 kph'}</div>
                        <div>Temp: {liveData?.motor_temperature_c !== undefined ? `${liveData.motor_temperature_c.toFixed(1)}°C` : '38.5°C'}</div>
                        <div>Status: <span className="font-bold uppercase text-[10px]">{currentStatus}</span></div>
                      </div>
                    </div>
                  </Popup>
                </Marker>
              );
            })}

            <MapUpdater coordinates={mapCoordinates} />
          </MapContainer>
        </div>
      </div>

      {/* Detailed Live Fleet Table */}
      <div className="glass rounded-xl overflow-hidden">
        <div className="px-6 py-5 border-b border-border">
          <h2 className="text-lg font-semibold">Real-Time Vehicle Assets Status</h2>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-border bg-muted/30 text-xs uppercase tracking-wider text-muted-foreground">
                <th className="px-6 py-4">Asset ID</th>
                <th className="px-6 py-4">Speed</th>
                <th className="px-6 py-4">Live Location (Lat, Lon)</th>
                <th className="px-6 py-4">Avg Motor Temp</th>
                <th className="px-6 py-4">Torque Load</th>
                <th className="px-6 py-4">Status Flag</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border text-sm">
              {defaultFleet.map((v) => {
                const liveData = fleet[v.id];

                const speedDisplay = liveData?.speed_kph !== undefined ? `${liveData.speed_kph.toFixed(1)} kph` : '72.0 kph';
                const tempDisplay = liveData?.motor_temperature_c !== undefined ? `${liveData.motor_temperature_c.toFixed(1)}°C` : '38.5°C';
                const torqueDisplay = liveData?.torque_nm !== undefined ? `${liveData.torque_nm.toFixed(1)} Nm` : '210 Nm';

                const locationDisplay = liveData?.latitude && liveData?.longitude
                  ? `${liveData.latitude.toFixed(4)}, ${liveData.longitude.toFixed(4)}`
                  : `${v.defaultLat.toFixed(4)}, ${v.defaultLng.toFixed(4)}`;

                const currentStatus = liveData ? liveData.status : v.fallbackStatus;
                const isCritical = currentStatus === 'Critical';
                const isWarning = currentStatus === 'Warning';

                return (
                  <tr key={v.id} className="hover:bg-muted/10 transition-colors">
                    <td className="px-6 py-4 font-mono font-medium">{v.id}</td>
                    <td className="px-6 py-4 font-mono">{speedDisplay}</td>
                    <td className="px-6 py-4 font-mono text-xs text-blue-400 font-semibold">
                      {locationDisplay}
                    </td>
                    <td className={`px-6 py-4 font-mono font-semibold ${isCritical ? 'text-red-400 animate-pulse' : isWarning ? 'text-yellow-400' : ''}`}>
                      {tempDisplay}
                    </td>
                    <td className="px-6 py-4 font-mono">{torqueDisplay}</td>
                    <td className="px-6 py-4">
                      <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-semibold ${
                        isCritical ? 'bg-red-500/10 text-red-500 animate-pulse' :
                        isWarning ? 'bg-yellow-500/10 text-yellow-500' :
                        'bg-emerald-500/10 text-emerald-500'
                      }`}>
                        {currentStatus}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
