import React, { useEffect, useState } from "react";
import { Gauge, Battery, Thermometer, Navigation, Zap, ShieldAlert, Cpu, X, RefreshCw } from "lucide-react";

interface VehicleInspectorProps {
  vehicleId: string | null;
  onClose: () => void;
}

export default function VehicleInspector({ vehicleId, onClose }: VehicleInspectorProps) {
  const [details, setDetails] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    if (!vehicleId) return;

    const fetchDetails = async () => {
      setLoading(true);
      try {
        const res = await fetch(`http://localhost:8000/api/v1/simulator/vehicles/${vehicleId}`);
        if (res.ok) {
          const data = await res.json();
          setDetails(data);
        }
      } catch (err) {
        console.error("Failed to inspect vehicle", err);
      } finally {
        setLoading(false);
      }
    };

    fetchDetails();
    const interval = setInterval(fetchDetails, 1500);
    return () => clearInterval(interval);
  }, [vehicleId]);

  if (!vehicleId) return null;

  return (
    <div className="bg-card border border-border rounded-xl p-5 shadow-xl space-y-4">
      <div className="flex items-center justify-between border-b border-border pb-3">
        <div className="flex items-center gap-2">
          <div className="h-8 w-8 rounded-lg bg-blue-500/10 border border-blue-500/30 text-blue-400 flex items-center justify-center font-bold text-xs">
            {vehicleId.split("-")[0]}
          </div>
          <div>
            <h4 className="text-sm font-bold text-foreground">{vehicleId}</h4>
            <p className="text-[11px] text-muted-foreground">Fleet Asset Diagnostic & Telemetry Inspector</p>
          </div>
        </div>

        <button
          onClick={onClose}
          className="text-muted-foreground hover:text-foreground p-1 rounded-lg hover:bg-muted/50 transition-all"
        >
          <X className="h-4 w-4" />
        </button>
      </div>

      {loading && !details ? (
        <div className="py-8 flex flex-col items-center justify-center text-muted-foreground text-xs space-y-2">
          <RefreshCw className="h-5 w-5 animate-spin text-blue-500" />
          <span>Polling live vehicle state...</span>
        </div>
      ) : details ? (
        <div className="space-y-4">
          {/* Status Bar */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
            <div className="bg-muted/40 p-2.5 rounded-lg border border-border">
              <span className="text-muted-foreground block text-[10px]">Operational State</span>
              <span className="font-bold text-blue-400 uppercase">{details.driving_state}</span>
            </div>
            <div className="bg-muted/40 p-2.5 rounded-lg border border-border">
              <span className="text-muted-foreground block text-[10px]">Driving Profile</span>
              <span className="font-bold text-foreground">{details.profile_name}</span>
            </div>
            <div className="bg-muted/40 p-2.5 rounded-lg border border-border">
              <span className="text-muted-foreground block text-[10px]">Assigned Fleet</span>
              <span className="font-bold text-foreground">{details.fleet_id}</span>
            </div>
            <div className="bg-muted/40 p-2.5 rounded-lg border border-border">
              <span className="text-muted-foreground block text-[10px]">Active Anomaly</span>
              <span className={`font-bold ${details.active_anomaly ? "text-rose-400" : "text-emerald-400"}`}>
                {details.active_anomaly || "None (Nominal)"}
              </span>
            </div>
          </div>

          {/* Electro-chemical Battery Details */}
          <div className="space-y-2">
            <h5 className="text-xs font-bold text-muted-foreground uppercase tracking-wider flex items-center gap-1.5">
              <Battery className="h-3.5 w-3.5 text-cyan-400" />
              <span>Electro-Chemical Battery Physics</span>
            </h5>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
              <div className="bg-muted/30 p-2 rounded-lg border border-border/60">
                <span className="text-muted-foreground text-[10px] block">State of Charge (SoC)</span>
                <span className="font-mono font-bold text-foreground text-sm">{details.soc}%</span>
              </div>
              <div className="bg-muted/30 p-2 rounded-lg border border-border/60">
                <span className="text-muted-foreground text-[10px] block">State of Health (SoH)</span>
                <span className="font-mono font-bold text-foreground text-sm">{details.soh}%</span>
              </div>
              <div className="bg-muted/30 p-2 rounded-lg border border-border/60">
                <span className="text-muted-foreground text-[10px] block">Cell Temperature</span>
                <span className="font-mono font-bold text-amber-400 text-sm">{details.cell_temperature}°C</span>
              </div>
              <div className="bg-muted/30 p-2 rounded-lg border border-border/60">
                <span className="text-muted-foreground text-[10px] block">Internal Resistance</span>
                <span className="font-mono font-bold text-foreground text-sm">{details.internal_resistance} Ω</span>
              </div>
            </div>
          </div>

          {/* Kinematic & Energy Details */}
          <div className="space-y-2">
            <h5 className="text-xs font-bold text-muted-foreground uppercase tracking-wider flex items-center gap-1.5">
              <Gauge className="h-3.5 w-3.5 text-emerald-400" />
              <span>Kinematics & Energy</span>
            </h5>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
              <div className="bg-muted/30 p-2 rounded-lg border border-border/60">
                <span className="text-muted-foreground text-[10px] block">Speed</span>
                <span className="font-mono font-bold text-foreground text-sm">{details.speed_kph} km/h</span>
              </div>
              <div className="bg-muted/30 p-2 rounded-lg border border-border/60">
                <span className="text-muted-foreground text-[10px] block">Torque</span>
                <span className="font-mono font-bold text-foreground text-sm">{details.torque_nm} Nm</span>
              </div>
              <div className="bg-muted/30 p-2 rounded-lg border border-border/60">
                <span className="text-muted-foreground text-[10px] block">Total Consumed</span>
                <span className="font-mono font-bold text-foreground text-sm">{details.total_energy_consumed_kwh} kWh</span>
              </div>
              <div className="bg-muted/30 p-2 rounded-lg border border-border/60">
                <span className="text-muted-foreground text-[10px] block">Total Regenerated</span>
                <span className="font-mono font-bold text-emerald-400 text-sm">{details.total_energy_regenerated_kwh} kWh</span>
              </div>
            </div>
          </div>

          {/* Position Coordinates */}
          <div className="bg-muted/20 p-2.5 rounded-lg border border-border flex items-center justify-between text-xs">
            <div className="flex items-center gap-2">
              <Navigation className="h-4 w-4 text-blue-400" />
              <span className="text-muted-foreground">Continuous GPS Coordinates:</span>
            </div>
            <span className="font-mono font-bold text-foreground">
              Lat: {details.latitude}, Lon: {details.longitude} | Heading: {details.heading_deg}°
            </span>
          </div>
        </div>
      ) : null}
    </div>
  );
}
