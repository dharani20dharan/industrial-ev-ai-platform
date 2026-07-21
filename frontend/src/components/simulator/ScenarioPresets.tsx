import React from "react";
import { Zap, ShieldAlert, Truck, Car, Navigation, BatteryCharging, Factory } from "lucide-react";

interface ScenarioPresetsProps {
  onApplyScenario: (scenarioName: string) => void;
  activeScenario?: string;
}

export default function ScenarioPresets({ onApplyScenario, activeScenario }: ScenarioPresetsProps) {
  const scenarios = [
    {
      id: "SMALL",
      name: "Small Fleet (10)",
      desc: "Baseline 10 delivery vans",
      icon: Car,
      color: "from-blue-500/20 to-blue-600/10 text-blue-400 border-blue-500/30",
    },
    {
      id: "MEDIUM",
      name: "Medium Fleet (50)",
      desc: "30 urban + 20 delivery vans",
      icon: Truck,
      color: "from-emerald-500/20 to-emerald-600/10 text-emerald-400 border-emerald-500/30",
    },
    {
      id: "LARGE",
      name: "Large Fleet (100)",
      desc: "40 urban, 40 highway, 20 charging",
      icon: Navigation,
      color: "from-amber-500/20 to-amber-600/10 text-amber-400 border-amber-500/30",
    },
    {
      id: "ENTERPRISE",
      name: "Enterprise Fleet (500)",
      desc: "Full multi-region 500 EV deployment",
      icon: Zap,
      color: "from-purple-500/20 to-purple-600/10 text-purple-400 border-purple-500/30",
    },
    {
      id: "RUSH_HOUR",
      name: "Rush Hour Traffic",
      desc: "High density stop-and-go metro transit",
      icon: ShieldAlert,
      color: "from-rose-500/20 to-rose-600/10 text-rose-400 border-rose-500/30",
    },
    {
      id: "DEPOT_CHARGING",
      name: "Depot Fast-Charging",
      desc: "High DC fast-charging load at hub",
      icon: BatteryCharging,
      color: "from-cyan-500/20 to-cyan-600/10 text-cyan-400 border-cyan-500/30",
    },
    {
      id: "HEAVY_INDUSTRIAL",
      name: "Heavy Industrial Yard",
      desc: "High-torque port yard haulers",
      icon: Factory,
      color: "from-orange-500/20 to-orange-600/10 text-orange-400 border-orange-500/30",
    },
  ];

  return (
    <div className="bg-card border border-border rounded-xl p-5 shadow-lg">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-base font-bold text-foreground flex items-center gap-2">
            <Zap className="h-5 w-5 text-amber-400" />
            <span>Demonstration Scenarios</span>
          </h3>
          <p className="text-xs text-muted-foreground">
            Instantly load operational fleet presets to demonstrate platform capabilities
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-7 gap-3">
        {scenarios.map((sc) => {
          const Icon = sc.icon;
          const isActive = activeScenario === sc.id;

          return (
            <button
              key={sc.id}
              onClick={() => onApplyScenario(sc.id)}
              className={`p-3.5 rounded-lg border text-left transition-all duration-200 bg-gradient-to-br hover:scale-[1.02] flex flex-col justify-between ${sc.color} ${
                isActive ? "ring-2 ring-blue-500 shadow-md scale-[1.02]" : "opacity-90 hover:opacity-100"
              }`}
            >
              <div>
                <div className="flex items-center justify-between mb-1.5">
                  <Icon className="h-5 w-5 shrink-0" />
                  {isActive && (
                    <span className="text-[10px] uppercase font-bold bg-blue-500/30 text-blue-300 px-1.5 py-0.5 rounded">
                      Active
                    </span>
                  )}
                </div>
                <div className="font-bold text-xs leading-snug">{sc.name}</div>
              </div>
              <p className="text-[11px] text-muted-foreground mt-2 line-clamp-2">{sc.desc}</p>
            </button>
          );
        })}
      </div>
    </div>
  );
}
