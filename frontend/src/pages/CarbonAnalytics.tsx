import React from 'react';
import { Leaf, Award, Compass, Zap, Cpu } from 'lucide-react';

export default function CarbonAnalytics() {
  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-extrabold tracking-tight">Sustainability & Carbon Intelligence</h1>
        <p className="text-muted-foreground mt-1">Scope emissions reporting, electrification metrics, and offset tracking calculations.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Core sustainability cards */}
        <div className="glass p-6 rounded-xl relative overflow-hidden">
          <div className="flex justify-between items-center">
            <span className="text-sm font-semibold text-muted-foreground">CO₂ Savings (YTD)</span>
            <Leaf className="h-5 w-5 text-emerald-400" />
          </div>
          <div className="mt-4">
            <span className="text-3xl font-bold text-emerald-400">142.6 Metric Tons</span>
            <span className="block text-xs text-muted-foreground mt-1.5">Equivalent to planting 5,800 trees</span>
          </div>
        </div>

        <div className="glass p-6 rounded-xl">
          <div className="flex justify-between items-center">
            <span className="text-sm font-semibold text-muted-foreground">Electrification Ratio</span>
            <Zap className="h-5 w-5 text-blue-400" />
          </div>
          <div className="mt-4">
            <span className="text-3xl font-bold text-blue-400">42%</span>
            <span className="block text-xs text-muted-foreground mt-1.5">82 of 195 routes fully converted</span>
          </div>
        </div>

        <div className="glass p-6 rounded-xl">
          <div className="flex justify-between items-center">
            <span className="text-sm font-semibold text-muted-foreground">Readiness Score</span>
            <Award className="h-5 w-5 text-amber-400" />
          </div>
          <div className="mt-4">
            <span className="text-3xl font-bold text-amber-400">84/100</span>
            <span className="block text-xs text-muted-foreground mt-1.5">Based on range suitability & chargers</span>
          </div>
        </div>
      </div>

      {/* Scope analysis section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <h2 className="font-semibold text-lg">Scope-1 & Scope-3 Emission Estimation</h2>
            <p className="text-xs text-muted-foreground mt-1">Calculates diesel displacement emissions relative to charging grid dependencies.</p>
          </div>
          <div className="my-8 h-40 bg-muted/20 border border-border/50 rounded-lg flex items-center justify-center text-xs text-muted-foreground">
            {/* Chart Placeholder */}
            <div className="flex flex-col items-center gap-1.5">
              <Cpu className="h-8 w-8 text-emerald-500/80" />
              <span>Scope emissions tracking graphics render here</span>
            </div>
          </div>
          <div className="border-t border-border pt-4 text-xs text-muted-foreground flex justify-between">
            <span>Grid Emission Factor: 0.32 kg CO₂/kWh</span>
            <span>Last calculated: Today</span>
          </div>
        </div>

        {/* Fleet Route Electrification Roadmap */}
        <div className="glass p-6 rounded-xl space-y-4">
          <h2 className="font-semibold text-lg">Electrification Readiness Scorecard</h2>
          <p className="text-xs text-muted-foreground">Top recommended routes for EV conversion based on distance, payload, and dwell time.</p>
          <div className="space-y-3">
            {[
              { route: "Denver - Boulder Corridor", readiness: "94%", reason: "Excellent charging availability & short route profile" },
              { route: "Houston Local Hub Delivery", readiness: "88%", reason: "Optimized route profile with idle times for dwell charging" },
              { route: "Chicago Regional Logistics", readiness: "54%", reason: "Long hauling requires high-capacity batteries & mega chargers" },
            ].map((route, i) => (
              <div key={i} className="p-3 bg-muted/30 border border-border/50 rounded-lg flex justify-between items-center gap-4">
                <div>
                  <h4 className="text-sm font-bold">{route.route}</h4>
                  <p className="text-[11px] text-muted-foreground mt-0.5">{route.reason}</p>
                </div>
                <span className={`text-sm font-extrabold px-2.5 py-1 rounded-lg ${
                  parseInt(route.readiness) >= 80 ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' :
                  'bg-yellow-500/10 text-yellow-400 border border-yellow-500/20'
                }`}>
                  {route.readiness}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
