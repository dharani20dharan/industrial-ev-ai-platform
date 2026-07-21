import React from "react";
import { Truck, BatteryCharging, Gauge, Activity, Clock, ShieldAlert, Cpu, Radio } from "lucide-react";

interface LiveSimulationAnalyticsProps {
  activeVehicles: number;
  activeFleets: number;
  chargingCount: number;
  movingCount: number;
  idleCount: number;
  faultCount: number;
  avgSoc: number;
  avgTemp: number;
  avgSpeed: number;
  messagesSent: number;
  messagesPerSecond: number;
  uptimeSeconds: number;
}

export default function LiveSimulationAnalytics({
  activeVehicles,
  activeFleets,
  chargingCount,
  movingCount,
  idleCount,
  faultCount,
  avgSoc,
  avgTemp,
  avgSpeed,
  messagesSent,
  messagesPerSecond,
  uptimeSeconds,
}: LiveSimulationAnalyticsProps) {
  const formatUptime = (secs: number) => {
    const mins = Math.floor(secs / 60);
    const remainingSecs = secs % 60;
    return `${mins}m ${remainingSecs}s`;
  };

  const statCards = [
    {
      title: "Active Vehicles",
      value: activeVehicles,
      subtitle: `${activeFleets} Fleets Running`,
      icon: Truck,
      color: "border-blue-500/30 text-blue-400 bg-blue-500/10",
    },
    {
      title: "Vehicle States",
      value: `${movingCount} Driving`,
      subtitle: `${chargingCount} Charging | ${idleCount} Idle`,
      icon: Activity,
      color: "border-emerald-500/30 text-emerald-400 bg-emerald-500/10",
    },
    {
      title: "Avg Battery SoC",
      value: `${avgSoc}%`,
      subtitle: `Temp: ${avgTemp}°C | Speed: ${avgSpeed} km/h`,
      icon: BatteryCharging,
      color: "border-cyan-500/30 text-cyan-400 bg-cyan-500/10",
    },
    {
      title: "Publish Rate",
      value: `${messagesPerSecond} msg/s`,
      subtitle: `${messagesSent.toLocaleString()} total messages`,
      icon: Radio,
      color: "border-purple-500/30 text-purple-400 bg-purple-500/10",
    },
    {
      title: "System Faults",
      value: faultCount,
      subtitle: faultCount > 0 ? "Active Anomaly Detected" : "Nominal Operations",
      icon: ShieldAlert,
      color: faultCount > 0 ? "border-rose-500/50 text-rose-400 bg-rose-500/15 animate-pulse" : "border-slate-500/30 text-slate-400 bg-slate-500/10",
    },
    {
      title: "Engine Uptime",
      value: formatUptime(uptimeSeconds),
      subtitle: "Continuous Telemetry",
      icon: Clock,
      color: "border-amber-500/30 text-amber-400 bg-amber-500/10",
    },
  ];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-3">
      {statCards.map((card, idx) => {
        const Icon = card.icon;
        return (
          <div
            key={idx}
            className={`bg-card border rounded-xl p-4 shadow-md flex flex-col justify-between ${card.color}`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-muted-foreground">{card.title}</span>
              <Icon className="h-4 w-4 shrink-0" />
            </div>
            <div className="mt-2">
              <div className="text-xl font-black text-foreground tracking-tight">{card.value}</div>
              <div className="text-[11px] text-muted-foreground mt-0.5 font-medium">{card.subtitle}</div>
            </div>
          </div>
        );
      })}
    </div>
  );
}
