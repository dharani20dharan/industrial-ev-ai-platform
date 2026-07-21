import { useMemo } from "react";
import { Navigation, Radio } from "lucide-react";
import FleetMap, { FleetMapVehicle } from "../maps/FleetMap";

interface VehicleSummary {
  vehicle_id: string;
  fleet_id?: string;
  profile_name?: string;
  vehicle_type?: string;
  speed_kph?: number;
  soc?: number;
  soh?: number;
  cell_temp?: number;
  motor_temperature_c?: number;
  voltage?: number;
  current_amps?: number;
  is_charging?: boolean;
  is_moving?: boolean;
  driving_state?: string;
  active_anomaly?: string;
  latitude: number;
  longitude: number;
  heading?: number;
  last_updated?: string;
  route_history?: Array<[number, number]>;
}

interface FleetSimulationMapProps {
  vehicles: VehicleSummary[];
  selectedVehicleId?: string;
  onSelectVehicle: (vehicleId: string) => void;
}

export default function FleetSimulationMap({
  vehicles,
  selectedVehicleId,
  onSelectVehicle,
}: FleetSimulationMapProps) {
  // Convert vehicle summaries to standardized FleetMapVehicle array
  const mapVehicles = useMemo<FleetMapVehicle[]>(() => {
    return vehicles.map((v) => ({
      vehicle_id: v.vehicle_id,
      fleet_id: v.fleet_id || "Fleet Alpha",
      profile_name: v.profile_name,
      vehicle_type: v.vehicle_type,
      latitude: v.latitude,
      longitude: v.longitude,
      speed_kph: v.speed_kph,
      heading: v.heading,
      soc: v.soc,
      soh: v.soh,
      cell_temp: v.cell_temp,
      motor_temperature_c: v.motor_temperature_c,
      voltage: v.voltage,
      current_amps: v.current_amps,
      is_charging: v.is_charging,
      is_moving: v.is_moving,
      driving_state: v.driving_state,
      active_anomaly: v.active_anomaly,
      last_updated: v.last_updated,
      route_history: v.route_history,
      status: v.driving_state || (v.is_charging ? "Charging" : v.is_moving ? "Driving" : "Idle"),
    }));
  }, [vehicles]);

  return (
    <div className="bg-card border border-border rounded-xl p-5 shadow-lg space-y-3">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
        <div>
          <h3 className="text-base font-bold text-foreground flex items-center gap-2">
            <Navigation className="h-5 w-5 text-blue-400" />
            <span>Live Geospatial Fleet Telemetry Map</span>
          </h3>
          <p className="text-xs text-muted-foreground">
            Continuous real-time position tracking and route progression across operational hubs
          </p>
        </div>

        {/* Legend */}
        <div className="flex items-center gap-3 text-xs font-semibold">
          <div className="flex items-center gap-1">
            <span className="h-2.5 w-2.5 rounded-full bg-blue-500" />
            <span className="text-muted-foreground">Driving</span>
          </div>
          <div className="flex items-center gap-1">
            <span className="h-2.5 w-2.5 rounded-full bg-emerald-400 animate-pulse" />
            <span className="text-muted-foreground">Charging</span>
          </div>
          <div className="flex items-center gap-1">
            <span className="h-2.5 w-2.5 rounded-full bg-amber-400" />
            <span className="text-muted-foreground">Idle</span>
          </div>
          <div className="flex items-center gap-1">
            <span className="h-2.5 w-2.5 rounded-full bg-rose-500 animate-pulse" />
            <span className="text-muted-foreground">Fault</span>
          </div>
        </div>
      </div>

      {/* Interactive Leaflet Map Visualizer Container */}
      <div className="relative w-full rounded-xl overflow-hidden border border-border">
        {vehicles.length === 0 ? (
          <div className="relative w-full h-[380px] bg-slate-950 rounded-xl flex flex-col items-center justify-center text-muted-foreground text-xs space-y-2">
            <Radio className="h-8 w-8 text-blue-500 animate-pulse" />
            <p>No active simulated vehicles. Click "Start Simulation" or "Spawn Vehicles" above.</p>
          </div>
        ) : (
          <FleetMap
            vehicles={mapVehicles}
            selectedVehicleId={selectedVehicleId}
            onSelectVehicle={onSelectVehicle}
            height="h-[380px]"
            showTrajectories={true}
            autoFitBounds={true}
          />
        )}

        {/* Live Active Overlay */}
        <div className="absolute bottom-3 left-3 z-[400] bg-card/85 backdrop-blur border border-border px-3 py-1.5 rounded-lg text-xs font-semibold text-muted-foreground shadow-md">
          Showing <span className="text-foreground font-bold">{vehicles.length}</span> active simulated assets on real map
        </div>
      </div>
    </div>
  );
}

