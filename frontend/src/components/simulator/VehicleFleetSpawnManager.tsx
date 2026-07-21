import React, { useState } from "react";
import { Plus, Users, Trash2, Layers, Truck, Shield } from "lucide-react";

interface VehicleFleetSpawnManagerProps {
  activeVehiclesCount: number;
  activeFleetsCount: number;
  fleetBreakdown: Record<string, number>;
  onSpawnVehicles: (count: number, profileName: string, fleetId: string) => void;
  onSpawnFleet: (fleetName: string, fleetType: string, count: number, profileName: string) => void;
  onResetSimulation: () => void;
}

export default function VehicleFleetSpawnManager({
  activeVehiclesCount,
  activeFleetsCount,
  fleetBreakdown,
  onSpawnVehicles,
  onSpawnFleet,
  onResetSimulation,
}: VehicleFleetSpawnManagerProps) {
  const [spawnCount, setSpawnCount] = useState<number>(10);
  const [selectedProfile, setSelectedProfile] = useState<string>("DELIVERY");
  const [fleetId, setFleetId] = useState<string>("FLT-ALPHA-01");
  const [activeTab, setActiveTab] = useState<"VEHICLES" | "FLEETS">("VEHICLES");

  // Custom Fleet Spawn Form
  const [newFleetName, setNewFleetName] = useState<string>("Regional Delivery");
  const [newFleetCount, setNewFleetCount] = useState<number>(25);

  const profiles = [
    { id: "DELIVERY", label: "Delivery Van" },
    { id: "URBAN", label: "Urban Transit" },
    { id: "HIGHWAY", label: "Highway Truck" },
    { id: "LONG_HAUL", label: "Long-haul Cargo" },
    { id: "INDUSTRIAL", label: "Industrial Yard" },
    { id: "IDLE", label: "Parked Depot" },
    { id: "CHARGING", label: "Fast-Charging" },
  ];

  const quickSpawnCounts = [10, 50, 100, 500];

  const handleCustomVehicleSpawn = (e: React.FormEvent) => {
    e.preventDefault();
    if (spawnCount > 0) {
      onSpawnVehicles(spawnCount, selectedProfile, fleetId);
    }
  };

  const handleCustomFleetSpawn = (e: React.FormEvent) => {
    e.preventDefault();
    if (newFleetCount > 0) {
      onSpawnFleet(newFleetName, selectedProfile, newFleetCount, selectedProfile);
    }
  };

  return (
    <div className="bg-card border border-border rounded-xl p-5 shadow-lg space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-base font-bold text-foreground flex items-center gap-2">
            <Layers className="h-5 w-5 text-blue-400" />
            <span>Configurable Vehicle & Fleet Spawn Manager</span>
          </h3>
          <p className="text-xs text-muted-foreground">
            Dynamically scale active simulation assets during runtime without resetting state
          </p>
        </div>

        {/* Mode Toggle Tabs */}
        <div className="flex bg-muted/40 p-1 rounded-lg border border-border text-xs font-semibold">
          <button
            onClick={() => setActiveTab("VEHICLES")}
            className={`px-3 py-1 rounded transition-all ${
              activeTab === "VEHICLES"
                ? "bg-blue-600 text-white shadow"
                : "text-muted-foreground hover:text-foreground"
            }`}
          >
            Spawn Vehicles
          </button>
          <button
            onClick={() => setActiveTab("FLEETS")}
            className={`px-3 py-1 rounded transition-all ${
              activeTab === "FLEETS"
                ? "bg-blue-600 text-white shadow"
                : "text-muted-foreground hover:text-foreground"
            }`}
          >
            Spawn Fleet
          </button>
        </div>
      </div>

      {activeTab === "VEHICLES" ? (
        <form onSubmit={handleCustomVehicleSpawn} className="space-y-4">
          {/* Quick Spawn Preset Buttons */}
          <div>
            <label className="text-xs font-semibold text-muted-foreground block mb-2">
              Quick Add Vehicles (Accumulates into active pool):
            </label>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
              {quickSpawnCounts.map((cnt) => (
                <button
                  key={cnt}
                  type="button"
                  onClick={() => onSpawnVehicles(cnt, selectedProfile, fleetId)}
                  className="flex items-center justify-center gap-1.5 py-2 px-3 bg-blue-500/10 hover:bg-blue-500/20 text-blue-400 border border-blue-500/30 rounded-lg text-xs font-bold transition-all hover:scale-[1.02]"
                >
                  <Plus className="h-3.5 w-3.5" />
                  <span>Spawn +{cnt} Vehicles</span>
                </button>
              ))}
            </div>
          </div>

          {/* Detailed Custom Inputs */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2 border-t border-border/60">
            <div>
              <label className="text-xs font-semibold text-muted-foreground block mb-1">Vehicle Count</label>
              <input
                type="number"
                min="1"
                max="1000"
                value={spawnCount}
                onChange={(e) => setSpawnCount(parseInt(e.target.value) || 1)}
                className="w-full bg-muted/40 border border-border rounded-lg px-3 py-1.5 text-xs text-foreground font-semibold focus:outline-none focus:border-blue-500"
              />
            </div>

            <div>
              <label className="text-xs font-semibold text-muted-foreground block mb-1">Driving Profile</label>
              <select
                value={selectedProfile}
                onChange={(e) => setSelectedProfile(e.target.value)}
                className="w-full bg-muted/40 border border-border rounded-lg px-3 py-1.5 text-xs text-foreground font-semibold focus:outline-none focus:border-blue-500"
              >
                {profiles.map((p) => (
                  <option key={p.id} value={p.id} className="bg-card text-foreground">
                    {p.label}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="text-xs font-semibold text-muted-foreground block mb-1">Target Fleet ID</label>
              <input
                type="text"
                value={fleetId}
                onChange={(e) => setFleetId(e.target.value)}
                className="w-full bg-muted/40 border border-border rounded-lg px-3 py-1.5 text-xs text-foreground font-semibold focus:outline-none focus:border-blue-500"
              />
            </div>
          </div>

          <div className="flex justify-end gap-2 pt-1">
            <button
              type="submit"
              className="flex items-center gap-1.5 px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs rounded-lg shadow transition-all"
            >
              <Plus className="h-3.5 w-3.5" />
              <span>Spawn Custom Vehicles</span>
            </button>
          </div>
        </form>
      ) : (
        <form onSubmit={handleCustomFleetSpawn} className="space-y-3">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div>
              <label className="text-xs font-semibold text-muted-foreground block mb-1">Fleet Name</label>
              <input
                type="text"
                value={newFleetName}
                onChange={(e) => setNewFleetName(e.target.value)}
                className="w-full bg-muted/40 border border-border rounded-lg px-3 py-1.5 text-xs text-foreground font-semibold focus:outline-none focus:border-blue-500"
              />
            </div>

            <div>
              <label className="text-xs font-semibold text-muted-foreground block mb-1">Fleet Size</label>
              <input
                type="number"
                min="1"
                max="500"
                value={newFleetCount}
                onChange={(e) => setNewFleetCount(parseInt(e.target.value) || 10)}
                className="w-full bg-muted/40 border border-border rounded-lg px-3 py-1.5 text-xs text-foreground font-semibold focus:outline-none focus:border-blue-500"
              />
            </div>

            <div>
              <label className="text-xs font-semibold text-muted-foreground block mb-1">Vehicle Profile</label>
              <select
                value={selectedProfile}
                onChange={(e) => setSelectedProfile(e.target.value)}
                className="w-full bg-muted/40 border border-border rounded-lg px-3 py-1.5 text-xs text-foreground font-semibold focus:outline-none focus:border-blue-500"
              >
                {profiles.map((p) => (
                  <option key={p.id} value={p.id} className="bg-card text-foreground">
                    {p.label}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div className="flex justify-end gap-2 pt-1">
            <button
              type="submit"
              className="flex items-center gap-1.5 px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs rounded-lg shadow transition-all"
            >
              <Truck className="h-3.5 w-3.5" />
              <span>Spawn Fleet</span>
            </button>
          </div>
        </form>
      )}

      {/* Active Fleet Distribution Chips */}
      {Object.keys(fleetBreakdown).length > 0 && (
        <div className="pt-3 border-t border-border/60">
          <label className="text-xs font-semibold text-muted-foreground block mb-2">
            Active Fleet Distribution ({activeFleetsCount} Fleets | {activeVehiclesCount} Active Vehicles):
          </label>
          <div className="flex flex-wrap gap-2">
            {Object.entries(fleetBreakdown).map(([fid, count]) => (
              <div
                key={fid}
                className="bg-muted/40 border border-border rounded-lg px-2.5 py-1 flex items-center gap-2 text-xs"
              >
                <span className="font-bold text-blue-400">{fid}:</span>
                <span className="font-mono font-semibold text-foreground">{count} Vehicles</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
