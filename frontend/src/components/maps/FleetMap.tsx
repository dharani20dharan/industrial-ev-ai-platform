import { useMemo, useEffect, useRef, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Polyline, useMap } from 'react-leaflet';
import L from 'leaflet';
import { Search, Filter, RefreshCw } from 'lucide-react';

export interface FleetMapVehicle {
  vehicle_id: string;
  fleet_id?: string;
  profile_name?: string;
  vehicle_type?: string;
  latitude: number;
  longitude: number;
  status?: string;
  speed_kph?: number;
  heading?: number;
  motor_temperature_c?: number;
  cell_temp?: number;
  soc?: number;
  soh?: number;
  voltage?: number;
  current_amps?: number;
  power_kw?: number;
  is_charging?: boolean;
  is_moving?: boolean;
  driving_state?: string;
  active_anomaly?: string;
  last_updated?: string;
  route_history?: Array<[number, number]>;
}

export interface FleetMapProps {
  vehicles: FleetMapVehicle[];
  selectedVehicleId?: string;
  onSelectVehicle?: (vehicleId: string) => void;
  className?: string;
  height?: string;
  showTrajectories?: boolean;
  autoFitBounds?: boolean;
  defaultCenter?: [number, number];
  defaultZoom?: number;
}

// Controller component to smoothly update camera bounds on major fleet changes or selections
function MapUpdater({
  coordinates,
  selectedLocation,
  autoFitBounds,
}: {
  coordinates: [number, number][];
  selectedLocation?: [number, number];
  autoFitBounds?: boolean;
}) {
  const map = useMap();
  const prevCoordsCountRef = useRef<number>(0);

  useEffect(() => {
    if (selectedLocation && selectedLocation[0] && selectedLocation[1]) {
      map.flyTo(selectedLocation, 15, { animate: true, duration: 0.8 });
    }
  }, [selectedLocation, map]);

  useEffect(() => {
    if (!autoFitBounds) return;
    if (coordinates.length > 0 && Math.abs(coordinates.length - prevCoordsCountRef.current) > 0) {
      prevCoordsCountRef.current = coordinates.length;
      try {
        const bounds = L.latLngBounds(coordinates);
        if (bounds.isValid()) {
          map.fitBounds(bounds, { padding: [50, 50], maxZoom: 14 });
        }
      } catch (err) {
        // Fallback swallow invalid bounds
      }
    }
  }, [coordinates, map, autoFitBounds]);

  return null;
}

const getMarkerStatusStr = (v: FleetMapVehicle): string => {
  if (!v) return "IDLE";
  if (typeof v.status === "string") return v.status;
  if (typeof v.driving_state === "string") return v.driving_state;
  if (v.is_charging) return "CHARGING";
  if (v.is_moving) return "DRIVING";
  return "IDLE";
};

// Factory function building lightweight custom markers
const createCustomMarker = (vehicle: FleetMapVehicle, isSelected: boolean) => {
  const status = getMarkerStatusStr(vehicle).toUpperCase();
  const isCharging = vehicle.is_charging || status === "CHARGING";
  const isFault = status === "FAULT" || status === "CRITICAL" || !!vehicle.active_anomaly;
  const isIdle = status === "IDLE" || status === "WARNING" || (!vehicle.is_moving && !isCharging && !isFault);

  let colorClass = "bg-blue-500 ring-blue-500/40";
  if (isFault) colorClass = "bg-rose-500 ring-rose-500/50 animate-pulse";
  else if (isCharging) colorClass = "bg-emerald-400 ring-emerald-500/40 animate-pulse";
  else if (isIdle) colorClass = "bg-amber-400 ring-amber-500/30";

  const selectedRing = isSelected ? "ring-4 ring-cyan-400 scale-125 z-50" : "";

  return L.divIcon({
    className: 'custom-leaflet-marker',
    html: `
      <div class="relative flex items-center justify-center w-6 h-6 transition-all duration-200 ${selectedRing}">
        <div class="absolute w-6 h-6 rounded-full ring-2 opacity-30 ${colorClass}"></div>
        <div class="w-3.5 h-3.5 rounded-full border-2 border-slate-950 shadow-md ${colorClass}"></div>
      </div>
    `,
    iconSize: [24, 24],
    iconAnchor: [12, 12],
    popupAnchor: [0, -12],
  });
};

export default function FleetMap({
  vehicles,
  selectedVehicleId,
  onSelectVehicle,
  className = "",
  height = "h-[450px]",
  showTrajectories = true,
  autoFitBounds = true,
  defaultCenter = [28.6139, 77.2090],
  defaultZoom = 12,
}: FleetMapProps) {
  const [searchQuery, setSearchQuery] = useState("");
  const [statusFilter, setStatusFilter] = useState<string>("ALL"); // ALL, DRIVING, CHARGING, IDLE, FAULT

  // Filter vehicles dynamically based on ID search and status pills
  const filteredVehicles = useMemo(() => {
    return vehicles.filter(v => {
      if (!v.latitude || !v.longitude || isNaN(v.latitude) || isNaN(v.longitude)) return false;

      // Search query filtering
      const matchesSearch = !searchQuery || v.vehicle_id.toLowerCase().includes(searchQuery.toLowerCase().trim());
      if (!matchesSearch) return false;

      // Status pill filtering
      if (statusFilter === "ALL") return true;
      const status = getMarkerStatusStr(v).toUpperCase();
      if (statusFilter === "DRIVING" && (status === "DRIVING" || v.is_moving)) return true;
      if (statusFilter === "CHARGING" && (status === "CHARGING" || v.is_charging)) return true;
      if (statusFilter === "FAULT" && (status === "FAULT" || status === "CRITICAL" || v.active_anomaly)) return true;
      if (statusFilter === "IDLE" && (status === "IDLE" || (!v.is_moving && !v.is_charging && !v.active_anomaly))) return true;

      return false;
    });
  }, [vehicles, searchQuery, statusFilter]);

  const validCoordinates = useMemo<[number, number][]>(() => {
    return filteredVehicles.map(v => [v.latitude, v.longitude]);
  }, [filteredVehicles]);

  const selectedLocation = useMemo<[number, number] | undefined>(() => {
    if (!selectedVehicleId) return undefined;
    const target = vehicles.find(v => v.vehicle_id === selectedVehicleId);
    return target ? [target.latitude, target.longitude] : undefined;
  }, [selectedVehicleId, vehicles]);

  const initialCenter = useMemo<[number, number]>(() => {
    return validCoordinates.length > 0 ? validCoordinates[0] : defaultCenter;
  }, [validCoordinates, defaultCenter]);

  return (
    <div className={`w-full rounded-xl overflow-hidden border border-border bg-slate-950 flex flex-col relative ${className}`}>
      {/* Map Control Toolbar (Search & Filter Pills) */}
      <div className="absolute top-3 right-3 z-[400] flex flex-wrap items-center gap-2 bg-card/90 backdrop-blur-md p-2 rounded-xl border border-border shadow-xl">
        {/* Search Input */}
        <div className="relative">
          <Search className="absolute left-2.5 top-2.5 h-3.5 w-3.5 text-muted-foreground" />
          <input
            type="text"
            placeholder="Search Vehicle ID..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="pl-8 pr-3 py-1.5 bg-background border border-border rounded-lg text-xs font-mono text-foreground focus:outline-none focus:ring-1 focus:ring-blue-500 w-36 sm:w-44"
          />
        </div>

        {/* Status Filter Pills */}
        <div className="flex items-center gap-1 bg-muted/40 p-1 rounded-lg border border-border text-[11px] font-semibold">
          {["ALL", "DRIVING", "CHARGING", "IDLE", "FAULT"].map(filter => (
            <button
              key={filter}
              onClick={() => setStatusFilter(filter)}
              className={`px-2 py-1 rounded transition-all ${
                statusFilter === filter
                  ? "bg-blue-600 text-white shadow"
                  : "text-muted-foreground hover:text-foreground"
              }`}
            >
              {filter}
            </button>
          ))}
        </div>
      </div>

      {/* Leaflet Map Canvas Container */}
      <div className={`w-full ${height} relative z-10`}>
        <MapContainer
          center={initialCenter}
          zoom={defaultZoom}
          className="h-full w-full"
          style={{ background: '#090d16' }}
        >
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
            url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
          />

          {/* Trajectories / Travel History Lines (Only render for filtered or selected assets to save memory) */}
          {showTrajectories &&
            filteredVehicles.map(v => {
              if (!v.route_history || v.route_history.length < 2) return null;
              const isSelected = v.vehicle_id === selectedVehicleId;
              if (searchQuery && !isSelected) return; // Cull non-selected history when actively searching

              const lineColor = isSelected ? '#38bdf8' : v.is_charging ? '#10b981' : v.active_anomaly ? '#ef4444' : '#3b82f6';
              return (
                <Polyline
                  key={`route-${v.vehicle_id}`}
                  positions={v.route_history}
                  pathOptions={{
                    color: lineColor,
                    weight: isSelected ? 3.5 : 1.5,
                    opacity: isSelected ? 0.9 : 0.4,
                  }}
                />
              );
            })}

          {/* Vehicle Markers */}
          {filteredVehicles.map(v => {
            const isSelected = v.vehicle_id === selectedVehicleId;
            const statusStr = getMarkerStatusStr(v);

            return (
              <Marker
                key={`fleet-marker-${v.vehicle_id}`}
                position={[v.latitude, v.longitude]}
                icon={createCustomMarker(v, isSelected)}
                eventHandlers={{
                  click: () => {
                    if (onSelectVehicle) onSelectVehicle(v.vehicle_id);
                  },
                }}
              >
                <Popup className="custom-map-popup min-w-[220px]">
                  <div className="p-2 font-mono text-xs text-slate-200 space-y-1.5">
                    <div className="flex items-center justify-between border-b border-slate-700/80 pb-1">
                      <strong className="text-blue-400 font-bold text-sm">{v.vehicle_id}</strong>
                      <span className="px-2 py-0.5 rounded text-[9px] font-bold uppercase bg-blue-500/20 text-blue-300">
                        {statusStr}
                      </span>
                    </div>
                    <div className="grid grid-cols-2 gap-1 text-[11px]">
                      <div>Speed: <span className="text-slate-100 font-bold">{v.speed_kph?.toFixed(1) || 0} km/h</span></div>
                      <div>SoC: <span className="text-cyan-400 font-bold">{v.soc?.toFixed(0) || 0}%</span></div>
                      <div>Temp: <span className="text-amber-400 font-bold">{v.motor_temperature_c?.toFixed(1) || 38}°C</span></div>
                      <div>Voltage: <span className="text-slate-100 font-bold">{v.voltage || 400}V</span></div>
                    </div>
                  </div>
                </Popup>
              </Marker>
            );
          })}

          <MapUpdater
            coordinates={validCoordinates}
            selectedLocation={selectedLocation}
            autoFitBounds={autoFitBounds && !searchQuery}
          />
        </MapContainer>
      </div>

      {/* Footer Overlay Count */}
      <div className="absolute bottom-3 left-3 z-[400] bg-card/85 backdrop-blur border border-border px-3 py-1.5 rounded-lg text-xs font-semibold text-muted-foreground shadow-md flex items-center gap-2">
        <span>Showing <strong className="text-foreground">{filteredVehicles.length}</strong> of {vehicles.length} assets</span>
        {searchQuery && (
          <button onClick={() => setSearchQuery("")} className="text-blue-400 hover:underline text-[10px]">Clear Search</button>
        )}
      </div>
    </div>
  );
}
