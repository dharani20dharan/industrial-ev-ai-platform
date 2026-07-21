import React from "react";
import { Terminal, ShieldAlert, Zap, BatteryCharging, Radio, Info } from "lucide-react";

interface EventLog {
  id: string;
  timestamp: string;
  event_type: string;
  message: string;
  vehicle_id?: string;
}

interface SimulatorEventStreamProps {
  events: EventLog[];
}

export default function SimulatorEventStream({ events }: SimulatorEventStreamProps) {
  const getEventBadge = (type: string) => {
    switch (type) {
      case "ANOMALY":
      case "MQTT_WARN":
        return <span className="bg-rose-500/20 text-rose-400 border border-rose-500/30 px-1.5 py-0.5 rounded text-[10px] font-bold">FAULT</span>;
      case "SPAWN":
      case "SPAWN_FLEET":
        return <span className="bg-blue-500/20 text-blue-400 border border-blue-500/30 px-1.5 py-0.5 rounded text-[10px] font-bold">SPAWN</span>;
      case "CHARGING":
        return <span className="bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 px-1.5 py-0.5 rounded text-[10px] font-bold">CHARGING</span>;
      case "SCENARIO_APPLIED":
        return <span className="bg-purple-500/20 text-purple-400 border border-purple-500/30 px-1.5 py-0.5 rounded text-[10px] font-bold">SCENARIO</span>;
      default:
        return <span className="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-1.5 py-0.5 rounded text-[10px] font-bold">SYSTEM</span>;
    }
  };

  return (
    <div className="bg-card border border-border rounded-xl p-5 shadow-lg space-y-3">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-base font-bold text-foreground flex items-center gap-2">
            <Terminal className="h-5 w-5 text-purple-400" />
            <span>Live Event & Anomaly Stream</span>
          </h3>
          <p className="text-xs text-muted-foreground">
            Real-time event-driven log stream broadcasted from simulation engine
          </p>
        </div>
      </div>

      <div className="bg-slate-950 border border-border rounded-xl p-3 h-[240px] overflow-y-auto font-mono text-xs space-y-2">
        {events.length === 0 ? (
          <div className="h-full flex items-center justify-center text-muted-foreground text-xs">
            <span>Awaiting simulation engine event broadcasts...</span>
          </div>
        ) : (
          events.slice().reverse().map((evt) => (
            <div key={evt.id} className="flex items-start gap-2 border-b border-slate-900 pb-1.5 hover:bg-slate-900/40 p-1 rounded transition-colors">
              <span className="text-slate-500 shrink-0">[{evt.timestamp}]</span>
              <div className="shrink-0">{getEventBadge(evt.event_type)}</div>
              <span className="text-slate-200 leading-snug flex-1">{evt.message}</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
