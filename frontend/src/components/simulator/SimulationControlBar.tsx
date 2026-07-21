import React from "react";
import { Play, Pause, Square, RotateCcw, Sliders, Zap, ShieldAlert, BatteryCharging, RefreshCw } from "lucide-react";

interface SimulationControlBarProps {
  status: string;
  publishInterval: number;
  speedMultiplier: number;
  enableEvents: boolean;
  enableCharging: boolean;
  enableRegen: boolean;
  onStart: () => void;
  onPause: () => void;
  onResume: () => void;
  onStop: () => void;
  onReset: () => void;
  onUpdateConfig: (config: Record<string, any>) => void;
}

export default function SimulationControlBar({
  status,
  publishInterval,
  speedMultiplier,
  enableEvents,
  enableCharging,
  enableRegen,
  onStart,
  onPause,
  onResume,
  onStop,
  onReset,
  onUpdateConfig,
}: SimulationControlBarProps) {
  const isRunning = status === "RUNNING";
  const isPaused = status === "PAUSED";

  return (
    <div className="bg-card border border-border rounded-xl p-5 shadow-lg space-y-4">
      <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        {/* Left: Action Control Buttons */}
        <div className="flex items-center gap-2.5 flex-wrap">
          {!isRunning && !isPaused && (
            <button
              onClick={onStart}
              className="flex items-center gap-2 px-5 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm rounded-lg shadow border border-emerald-500 transition-all hover:scale-[1.02]"
            >
              <Play className="h-4 w-4 fill-white" />
              <span>Start Simulation</span>
            </button>
          )}

          {isRunning && (
            <button
              onClick={onPause}
              className="flex items-center gap-2 px-5 py-2.5 bg-amber-600 hover:bg-amber-500 text-white font-bold text-sm rounded-lg shadow border border-amber-500 transition-all hover:scale-[1.02]"
            >
              <Pause className="h-4 w-4 fill-white" />
              <span>Pause</span>
            </button>
          )}

          {isPaused && (
            <button
              onClick={onResume}
              className="flex items-center gap-2 px-5 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm rounded-lg shadow border border-emerald-500 transition-all hover:scale-[1.02]"
            >
              <Play className="h-4 w-4 fill-white" />
              <span>Resume</span>
            </button>
          )}

          {(isRunning || isPaused) && (
            <button
              onClick={onStop}
              className="flex items-center gap-2 px-4 py-2.5 bg-rose-600/20 hover:bg-rose-600 text-rose-300 hover:text-white border border-rose-500/40 font-semibold text-sm rounded-lg transition-all"
            >
              <Square className="h-4 w-4 fill-current" />
              <span>Stop</span>
            </button>
          )}

          <button
            onClick={onReset}
            className="flex items-center gap-2 px-4 py-2.5 bg-muted/50 hover:bg-muted text-muted-foreground hover:text-foreground border border-border font-semibold text-sm rounded-lg transition-all"
          >
            <RotateCcw className="h-4 w-4" />
            <span>Reset</span>
          </button>
        </div>

        {/* Status Indicator */}
        <div className="flex items-center gap-3 bg-muted/40 px-3.5 py-1.5 rounded-lg border border-border text-xs font-semibold">
          <span className="text-muted-foreground">Engine Status:</span>
          <span
            className={`flex items-center gap-1.5 font-bold uppercase tracking-wider ${
              isRunning ? "text-emerald-400" : isPaused ? "text-amber-400" : "text-rose-400"
            }`}
          >
            <span
              className={`h-2 w-2 rounded-full ${
                isRunning ? "bg-emerald-500 animate-ping" : isPaused ? "bg-amber-500" : "bg-rose-500"
              }`}
            />
            {status}
          </span>
        </div>
      </div>

      {/* Speed Multiplier & Fine Parameters Controls */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-3 border-t border-border/60">
        {/* Speed Multiplier */}
        <div className="space-y-1.5">
          <label className="text-xs font-semibold text-muted-foreground flex items-center gap-1.5">
            <Zap className="h-3.5 w-3.5 text-amber-400" />
            <span>Speed Multiplier</span>
          </label>
          <div className="flex items-center gap-1 bg-muted/30 p-1 rounded-lg border border-border">
            {[1, 2, 5, 10].map((mult) => (
              <button
                key={mult}
                onClick={() => onUpdateConfig({ speed_multiplier: mult })}
                className={`flex-1 py-1 text-xs font-bold rounded transition-all ${
                  speedMultiplier === mult
                    ? "bg-blue-600 text-white shadow"
                    : "text-muted-foreground hover:text-foreground hover:bg-muted/50"
                }`}
              >
                {mult}x
              </button>
            ))}
          </div>
        </div>

        {/* Telemetry Publish Rate */}
        <div className="space-y-1.5">
          <div className="flex items-center justify-between">
            <label className="text-xs font-semibold text-muted-foreground flex items-center gap-1.5">
              <RefreshCw className="h-3.5 w-3.5 text-blue-400" />
              <span>Publish Interval</span>
            </label>
            <span className="text-xs font-mono font-bold text-foreground">{publishInterval}s</span>
          </div>
          <input
            type="range"
            min="0.5"
            max="5.0"
            step="0.5"
            value={publishInterval}
            onChange={(e) => onUpdateConfig({ publish_interval: parseFloat(e.target.value) })}
            className="w-full h-2 bg-muted rounded-lg appearance-none cursor-pointer accent-blue-500"
          />
        </div>

        {/* Feature Toggles */}
        <div className="sm:col-span-2 grid grid-cols-3 gap-2">
          <button
            onClick={() => onUpdateConfig({ enable_events: !enableEvents })}
            className={`flex items-center justify-center gap-1.5 py-2 px-3 rounded-lg border text-xs font-semibold transition-all ${
              enableEvents
                ? "bg-purple-500/10 border-purple-500/30 text-purple-300"
                : "bg-muted/30 border-border text-muted-foreground opacity-60"
            }`}
          >
            <ShieldAlert className="h-3.5 w-3.5" />
            <span>Random Faults</span>
          </button>

          <button
            onClick={() => onUpdateConfig({ enable_charging: !enableCharging })}
            className={`flex items-center justify-center gap-1.5 py-2 px-3 rounded-lg border text-xs font-semibold transition-all ${
              enableCharging
                ? "bg-cyan-500/10 border-cyan-500/30 text-cyan-300"
                : "bg-muted/30 border-border text-muted-foreground opacity-60"
            }`}
          >
            <BatteryCharging className="h-3.5 w-3.5" />
            <span>Auto-Charging</span>
          </button>

          <button
            onClick={() => onUpdateConfig({ enable_regen: !enableRegen })}
            className={`flex items-center justify-center gap-1.5 py-2 px-3 rounded-lg border text-xs font-semibold transition-all ${
              enableRegen
                ? "bg-emerald-500/10 border-emerald-500/30 text-emerald-300"
                : "bg-muted/30 border-border text-muted-foreground opacity-60"
            }`}
          >
            <Zap className="h-3.5 w-3.5" />
            <span>Regen Braking</span>
          </button>
        </div>
      </div>
    </div>
  );
}
