import { useMemo, useEffect, useRef } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Polyline, useMap } from 'react-leaflet';
import L from 'leaflet';

export interface FleetMapVehicle {
  vehicle_id: string;
  fleet_id?: string;
  profile_name?: string;
  vehicle_type?: string;
  latitude: number;
  longitude: number;
  status?: string; // "Active" | "Driving" | "Charging" | "Idle" | "Fault" | "Critical" | "Warning" | "Offline"
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

// Controller component to smoothly update camera bounds on major fleet changes
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

  // Pan to selected vehicle when selected
  useEffect(() => {
    if (selectedLocation && selectedLocation[0] && selectedLocation[1]) {
      map.panTo(selectedLocation, { animate: true, duration: 0.8 });
    }
  }, [selectedLocation, map]);

  // Fit bounds when fleet coordinate count changes or initially loads
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
  if (v.is_charging) return "Charging";
  if (v.is_moving) return "Driving";
  return "Idle";
};

// Factory function building custom Leaflet markers matching platform theme
const createCustomMarker = (vehicle: FleetMapVehicle, isSelected: boolean) => {
  const rawStatus = getMarkerStatusStr(vehicle);
  const status = rawStatus.toUpperCase();
  const isCharging = vehicle.is_charging || status === "CHARGING";
  const isFault = status === "FAULT" || status === "CRITICAL" || !!vehicle.active_anomaly;
  const isIdle = status === "IDLE" || status === "WARNING" || (!vehicle.is_moving && !isCharging && !isFault);
  const isOffline = status === "OFFLINE";

  let colorClass = "bg-blue-500 ring-blue-500/40"; // Driving / Active
  if (isFault) {
    colorClass = "bg-red-500 ring-red-500/50 animate-pulse";
  } else if (isCharging) {
    colorClass = "bg-emerald-400 ring-emerald-500/40 animate-pulse";
  } else if (isIdle) {
    colorClass = "bg-amber-400 ring-amber-500/30";
  } else if (isOffline) {
    colorClass = "bg-slate-500 ring-slate-500/20";
  }

  const selectedRing = isSelected ? "ring-4 ring-cyan-400 scale-125 z-50" : "";

  return L.divIcon({
    className: 'custom-leaflet-marker',
    html: `
      <div class="relative flex items-center justify-center w-7 h-7 transition-all duration-300 ${selectedRing}">
        <div class="absolute w-7 h-7 rounded-full ring-4 opacity-40 animate-ping ${colorClass}"></div>
        <div class="w-4 h-4 rounded-full border-2 border-slate-950 shadow-lg ${colorClass} flex items-center justify-center text-[8px] font-black text-white">
        </div>
      </div>
    `,
    iconSize: [28, 28],
    iconAnchor: [14, 14],
    popupAnchor: [0, -14],
  });
};

export default function FleetMap({
  vehicles,
  selectedVehicleId,
  onSelectVehicle,
  className = "",
  height = "h-[420px]",
  showTrajectories = true,
  autoFitBounds = true,
  defaultCenter = [28.6139, 77.2090], // Delhi NCR / Central hub fallback
  defaultZoom = 12,
}: FleetMapProps) {
  // Memoize valid coordinates for automated viewport framing
  const validCoordinates = useMemo<[number, number][]>(() => {
    return vehicles
      .filter((v) => typeof v.latitude === "number" && typeof v.longitude === "number" && !isNaN(v.latitude) && !isNaN(v.longitude))
      .map((v) => [v.latitude, v.longitude]);
  }, [vehicles]);

  // Selected vehicle coordinate lookup
  const selectedLocation = useMemo<[number, number] | undefined>(() => {
    if (!selectedVehicleId) return undefined;
    const target = vehicles.find((v) => v.vehicle_id === selectedVehicleId);
    if (target && target.latitude && target.longitude) {
      return [target.latitude, target.longitude];
    }
    return undefined;
  }, [selectedVehicleId, vehicles]);

  // Initial center resolution (first vehicle or default center)
  const initialCenter = useMemo<[number, number]>(() => {
    if (validCoordinates.length > 0) {
      return validCoordinates[0];
    }
    return defaultCenter;
  }, [validCoordinates, defaultCenter]);

  return (
    <div className={`w-full rounded-xl overflow-hidden border border-border bg-slate-950 z-10 relative ${height} ${className}`}>
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

        {/* Trajectories / Travel History Lines */}
        {showTrajectories &&
          vehicles.map((v) => {
            if (!v.route_history || v.route_history.length < 2) return null;
            const isSelected = v.vehicle_id === selectedVehicleId;
            const lineColor = isSelected ? '#38bdf8' : v.is_charging ? '#10b981' : v.driving_state === 'FAULT' ? '#ef4444' : '#3b82f6';
            return (
              <Polyline
                key={`route-${v.vehicle_id}`}
                positions={v.route_history}
                pathOptions={{
                  color: lineColor,
                  weight: isSelected ? 3.5 : 2,
                  opacity: isSelected ? 0.9 : 0.6,
                  dashArray: isSelected ? undefined : '5, 5',
                }}
              />
            );
          })}

        {/* Vehicle Markers Loop */}
        {vehicles.map((v) => {
          if (typeof v.latitude !== "number" || typeof v.longitude !== "number" || isNaN(v.latitude) || isNaN(v.longitude)) {
            return null;
          }

          const isSelected = v.vehicle_id === selectedVehicleId;
          const statusStr = getMarkerStatusStr(v);

          return (
            <Marker
              key={`fleet-marker-${v.vehicle_id}`}
              position={[v.latitude, v.longitude]}
              icon={createCustomMarker(v, isSelected)}
              eventHandlers={{
                click: () => {
                  if (onSelectVehicle) {
                    onSelectVehicle(v.vehicle_id);
                  }
                },
              }}
            >
              <Popup className="custom-map-popup min-w-[240px]">
                <div className="p-2 font-mono text-xs text-slate-200 space-y-2">
                  {/* Header Row */}
                  <div className="flex items-center justify-between border-b border-slate-700/80 pb-1.5">
                    <div>
                      <strong className="text-blue-400 font-bold text-sm block tracking-wide">{v.vehicle_id}</strong>
                      <span className="text-[10px] text-slate-400">
                        Fleet: <span className="text-slate-200 font-semibold">{v.fleet_id || "Fleet Alpha"}</span>
                      </span>
                    </div>
                    <span
                      className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider ${
                        statusStr.toUpperCase() === "CHARGING" || v.is_charging
                          ? "bg-emerald-500/20 text-emerald-400 border border-emerald-500/40"
                          : statusStr.toUpperCase() === "FAULT" || statusStr.toUpperCase() === "CRITICAL"
                          ? "bg-rose-500/20 text-rose-400 border border-rose-500/40 animate-pulse"
                          : statusStr.toUpperCase() === "IDLE"
                          ? "bg-amber-500/20 text-amber-400 border border-amber-500/40"
                          : "bg-blue-500/20 text-blue-400 border border-blue-500/40"
                      }`}
                    >
                      {statusStr}
                    </span>
                  </div>

                  {/* Operational Telemetry Grid */}
                  <div className="grid grid-cols-2 gap-1.5 text-[11px]">
                    <div className="bg-slate-900/80 p-1.5 rounded border border-slate-800">
                      <span className="text-slate-400 block text-[9px]">Speed & Heading</span>
                      <span className="font-bold text-slate-100">
                        {v.speed_kph !== undefined ? `${v.speed_kph.toFixed(1)} km/h` : "0.0 km/h"}
                      </span>
                      {v.heading !== undefined && (
                        <span className="text-[9px] text-slate-400 block">Heading: {v.heading}°</span>
                      )}
                    </div>

                    <div className="bg-slate-900/80 p-1.5 rounded border border-slate-800">
                      <span className="text-slate-400 block text-[9px]">Battery SoC / SoH</span>
                      <span className="font-bold text-cyan-400">
                        {v.soc !== undefined ? `${v.soc.toFixed(0)}%` : "N/A"}
                      </span>
                      <span className="text-[9px] text-slate-400 block">
                        SoH: {v.soh !== undefined ? `${v.soh.toFixed(0)}%` : "100%"}
                      </span>
                    </div>

                    <div className="bg-slate-900/80 p-1.5 rounded border border-slate-800">
                      <span className="text-slate-400 block text-[9px]">Motor / Cell Temp</span>
                      <span className="font-bold text-slate-100">
                        {v.motor_temperature_c !== undefined
                          ? `${v.motor_temperature_c.toFixed(1)}°C`
                          : v.cell_temp !== undefined
                          ? `${v.cell_temp.toFixed(1)}°C`
                          : "38.0°C"}
                      </span>
                    </div>

                    <div className="bg-slate-900/80 p-1.5 rounded border border-slate-800">
                      <span className="text-slate-400 block text-[9px]">Voltage / Current</span>
                      <span className="font-bold text-slate-100">
                        {v.voltage !== undefined ? `${v.voltage.toFixed(0)}V` : "400V"}{" "}
                        {v.current_amps !== undefined ? `${v.current_amps.toFixed(0)}A` : ""}
                      </span>
                    </div>
                  </div>

                  {/* Profile & Location Footer */}
                  <div className="text-[10px] text-slate-400 pt-1 border-t border-slate-800/80 flex items-center justify-between">
                    <div>
                      <span>Profile: </span>
                      <span className="text-slate-200 font-semibold">{v.profile_name || v.vehicle_type || "Delivery Van"}</span>
                    </div>
                    <div className="text-blue-400 font-mono text-[9px]">
                      {v.latitude.toFixed(4)}, {v.longitude.toFixed(4)}
                    </div>
                  </div>

                  {v.last_updated && (
                    <div className="text-[9px] text-slate-500 text-right italic">
                      Updated: {new Date(v.last_updated).toLocaleTimeString()}
                    </div>
                  )}
                </div>
              </Popup>
            </Marker>
          );
        })}

        <MapUpdater
          coordinates={validCoordinates}
          selectedLocation={selectedLocation}
          autoFitBounds={autoFitBounds}
        />
      </MapContainer>
    </div>
  );
}
