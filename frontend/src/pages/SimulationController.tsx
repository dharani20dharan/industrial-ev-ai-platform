import { useState, useEffect, useRef, useCallback } from "react";
import ScenarioPresets from "../components/simulator/ScenarioPresets";
import SimulationControlBar from "../components/simulator/SimulationControlBar";
import VehicleFleetSpawnManager from "../components/simulator/VehicleFleetSpawnManager";
import LiveSimulationAnalytics from "../components/simulator/LiveSimulationAnalytics";
import FleetSimulationMap from "../components/simulator/FleetSimulationMap";
import VehicleInspector from "../components/simulator/VehicleInspector";
import SimulatorEventStream from "../components/simulator/SimulatorEventStream";
import { Sliders, RefreshCw } from "lucide-react";

export default function SimulationController() {
  const [statusData, setStatusData] = useState<any>(null);
  const [vehiclesList, setVehiclesList] = useState<any[]>([]);
  const [selectedVehicleId, setSelectedVehicleId] = useState<string | null>(null);

  // Persist active scenario state in localStorage to prevent reset discrepancies on page refresh
  const [activeScenario, setActiveScenario] = useState<string>(() => {
    return localStorage.getItem("ev_sim_active_scenario") || "SMALL";
  });

  const routeHistoryRef = useRef<Record<string, Array<[number, number]>>>({});
  const socketRef = useRef<WebSocket | null>(null);
  const reconnectRef = useRef<NodeJS.Timeout | null>(null);

  const vehiclesBufferRef = useRef<Record<string, any>>({});
  const needsRenderRef = useRef(false);

  const recordHistoryPoint = useCallback((vehicleId: string, lat: number, lng: number) => {
    if (!lat || !lng || isNaN(lat) || isNaN(lng)) return;
    const history = routeHistoryRef.current[vehicleId] || [];
    const lastPoint = history[history.length - 1];

    if (!lastPoint || Math.abs(lastPoint[0] - lat) > 0.00005 || Math.abs(lastPoint[1] - lng) > 0.00005) {
      const updated = [...history, [lat, lng] as [number, number]];
      if (updated.length > 25) updated.shift();
      routeHistoryRef.current[vehicleId] = updated;
    }
  }, []);

  useEffect(() => {
    const renderInterval = setInterval(() => {
      if (needsRenderRef.current) {
        setVehiclesList(Object.values(vehiclesBufferRef.current));
        needsRenderRef.current = false;
      }
    }, 500);
    return () => clearInterval(renderInterval);
  }, []);

  const fetchStatus = async () => {
    try {
      const res = await fetch("http://localhost:8000/api/v1/simulator/status");
      if (res.ok) {
        const data = await res.json();
        setStatusData(data);
      }
    } catch (err) {
      console.warn("Backend API unreachable", err);
    }
  };

  const fetchVehicles = async () => {
    try {
      const res = await fetch("http://localhost:8000/api/v1/simulator/vehicles");
      if (res.ok) {
        const data = await res.json();
        const rawVehicles = data.vehicles || [];

        rawVehicles.forEach((v: any) => {
          recordHistoryPoint(v.vehicle_id, v.latitude, v.longitude);
          vehiclesBufferRef.current[v.vehicle_id] = {
            ...(vehiclesBufferRef.current[v.vehicle_id] || {}),
            ...v,
            route_history: routeHistoryRef.current[v.vehicle_id] || [],
          };
        });
        needsRenderRef.current = true;
      }
    } catch (err) {
      console.warn("Failed to fetch vehicles", err);
    }
  };

  // Sync scenario persistence on load
  useEffect(() => {
    const initializeEngine = async () => {
      await fetchStatus();
      await fetchVehicles();
    };
    initializeEngine();
  }, []);

  useEffect(() => {
    let isMounted = true;

    function connectWs() {
      if (
        socketRef.current &&
        (socketRef.current.readyState === WebSocket.CONNECTING || socketRef.current.readyState === WebSocket.OPEN)
      ) {
        return;
      }

      const socket = new WebSocket('ws://localhost:8000/api/v1/telemetry/live');
      socketRef.current = socket;

      socket.onmessage = (event) => {
        if (!isMounted) return;
        try {
          const data = JSON.parse(event.data);
          const vId = data.vehicle_id;
          if (!vId || data.latitude === undefined || data.longitude === undefined) return;

          recordHistoryPoint(vId, data.latitude, data.longitude);

          vehiclesBufferRef.current[vId] = {
            ...(vehiclesBufferRef.current[vId] || {}),
            ...data,
            route_history: routeHistoryRef.current[vId] || [],
          };
          needsRenderRef.current = true;
        } catch (e) {
          // Ignore parse errors
        }
      };

      socket.onclose = () => {
        if (!isMounted) return;
        socketRef.current = null;
        if (reconnectRef.current) clearTimeout(reconnectRef.current);
        reconnectRef.current = setTimeout(connectWs, 3000);
      };
    }

    connectWs();

    const interval = setInterval(() => {
      fetchStatus();
    }, 2000);

    return () => {
      isMounted = false;
      clearInterval(interval);
      if (reconnectRef.current) clearTimeout(reconnectRef.current);
      if (socketRef.current) {
        socketRef.current.close();
        socketRef.current = null;
      }
    };
  }, [recordHistoryPoint]);

  const handleStart = async () => {
    await fetch("http://localhost:8000/api/v1/simulator/start", { method: "POST" });
    fetchStatus();
  };

  const handlePause = async () => {
    await fetch("http://localhost:8000/api/v1/simulator/pause", { method: "POST" });
    fetchStatus();
  };

  const handleResume = async () => {
    await fetch("http://localhost:8000/api/v1/simulator/resume", { method: "POST" });
    fetchStatus();
  };

  const handleStop = async () => {
    await fetch("http://localhost:8000/api/v1/simulator/stop", { method: "POST" });
    fetchStatus();
  };

  const handleReset = async () => {
    await fetch("http://localhost:8000/api/v1/simulator/reset", { method: "POST" });
    localStorage.removeItem("ev_sim_active_scenario");
    setActiveScenario("SMALL");
    fetchStatus();
    fetchVehicles();
  };

  const handleUpdateConfig = async (config: Record<string, any>) => {
    await fetch("http://localhost:8000/api/v1/simulator/config", {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(config),
    });
    fetchStatus();
  };

  const handleApplyScenario = async (scenarioName: string) => {
    setActiveScenario(scenarioName);
    localStorage.setItem("ev_sim_active_scenario", scenarioName);

    await fetch("http://localhost:8000/api/v1/simulator/scenarios/apply", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ scenario_name: scenarioName }),
    });
    fetchStatus();
    fetchVehicles();
  };

  const handleSpawnVehicles = async (count: number, profileName: string, fleetId: string) => {
    await fetch("http://localhost:8000/api/v1/simulator/vehicles/spawn", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ count, profile_name: profileName, fleet_id: fleetId }),
    });
    fetchStatus();
    fetchVehicles();
  };

  const handleSpawnFleet = async (fleetName: string, fleetType: string, count: number, profileName: string) => {
    await fetch("http://localhost:8000/api/v1/simulator/fleets/spawn", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ fleet_name: fleetName, fleet_type: fleetType, count, profile_name: profileName }),
    });
    fetchStatus();
    fetchVehicles();
  };

  return (
    <div className="space-y-6">
      {/* Top Title Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-card border border-border p-6 rounded-2xl shadow-xl bg-gradient-to-r from-blue-950/20 via-card to-card">
        <div>
          <div className="flex items-center gap-2 text-blue-400 font-bold text-xs uppercase tracking-wider mb-1">
            <Sliders className="h-4 w-4" />
            <span>Industrial Operations Control Panel</span>
          </div>
          <h1 className="text-2xl md:text-3xl font-black text-foreground tracking-tight">
            EV Telemetry Simulation Controller
          </h1>
          <p className="text-sm text-muted-foreground mt-1">
            Real-time continuous fleet telemetry generation, dynamic vehicle spawning, and operational scenario simulation
          </p>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={() => {
              fetchStatus();
              fetchVehicles();
            }}
            className="flex items-center gap-2 px-3 py-2 bg-muted/40 hover:bg-muted text-muted-foreground hover:text-foreground border border-border rounded-lg text-xs font-semibold transition-all"
          >
            <RefreshCw className="h-3.5 w-3.5" />
            <span>Refresh Engine State</span>
          </button>
        </div>
      </div>

      {/* 1. Live Simulation Analytics */}
      <LiveSimulationAnalytics
        activeVehicles={statusData?.active_vehicles || 0}
        activeFleets={statusData?.active_fleets || 0}
        chargingCount={statusData?.charging_count || 0}
        movingCount={statusData?.moving_count || 0}
        idleCount={statusData?.idle_count || 0}
        faultCount={statusData?.fault_count || 0}
        avgSoc={statusData?.avg_soc || 0}
        avgTemp={statusData?.avg_temp || 0}
        avgSpeed={statusData?.avg_speed || 0}
        messagesSent={statusData?.messages_sent || 0}
        messagesPerSecond={statusData?.messages_per_second || 0}
        uptimeSeconds={statusData?.uptime_seconds || 0}
      />

      {/* 2. Demonstration Scenario Presets */}
      <ScenarioPresets onApplyScenario={handleApplyScenario} activeScenario={activeScenario} />

      {/* 3. Runtime Controls & Options */}
      <SimulationControlBar
        status={statusData?.status || "STOPPED"}
        publishInterval={statusData?.publish_interval || 2.0}
        speedMultiplier={statusData?.speed_multiplier || 1.0}
        enableEvents={statusData?.enable_events ?? true}
        enableCharging={statusData?.enable_charging ?? true}
        enableRegen={statusData?.enable_regen ?? true}
        onStart={handleStart}
        onPause={handlePause}
        onResume={handleResume}
        onStop={handleStop}
        onReset={handleReset}
        onUpdateConfig={handleUpdateConfig}
      />

      {/* 4. Vehicle & Fleet Spawn Manager */}
      <VehicleFleetSpawnManager
        activeVehiclesCount={statusData?.active_vehicles || 0}
        activeFleetsCount={statusData?.active_fleets || 0}
        fleetBreakdown={statusData?.fleet_breakdown || {}}
        onSpawnVehicles={handleSpawnVehicles}
        onSpawnFleet={handleSpawnFleet}
        onResetSimulation={handleReset}
      />

      {/* 5. Geospatial Map & Vehicle Inspector */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <FleetSimulationMap
            vehicles={vehiclesList}
            selectedVehicleId={selectedVehicleId || undefined}
            onSelectVehicle={(id) => setSelectedVehicleId(id)}
          />
        </div>

        <div>
          {selectedVehicleId ? (
            <VehicleInspector vehicleId={selectedVehicleId} onClose={() => setSelectedVehicleId(null)} />
          ) : (
            <SimulatorEventStream events={statusData?.recent_events || []} />
          )}
        </div>
      </div>

      {/* Bottom Event Stream (if inspector open) */}
      {selectedVehicleId && <SimulatorEventStream events={statusData?.recent_events || []} />}
    </div>
  );
}
