import React from 'react';
import { Share2, AlertOctagon, TrendingUp, ShieldAlert, Cpu } from 'lucide-react';

export default function SupplyChain() {
  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-extrabold tracking-tight">Graph-Based Supply Chain Intelligence</h1>
        <p className="text-muted-foreground mt-1">Multi-tier battery material dependencies, supplier risk assessments, and vulnerability tracking.</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Neo4j dependency traversal layout */}
        <div className="glass p-6 rounded-xl lg:col-span-2 flex flex-col justify-between">
          <div>
            <div className="flex justify-between items-center">
              <h2 className="font-semibold text-lg">Multi-Tier Dependency Graph Explorer</h2>
              <Share2 className="h-5 w-5 text-blue-500" />
            </div>
            <p className="text-xs text-muted-foreground mt-1">Neo4j graph representation traversing Mine ➔ Refiner ➔ Battery Plant ➔ Fleet Assembly.</p>
          </div>

          <div className="my-6 h-64 bg-muted/20 border border-border/50 rounded-lg relative overflow-hidden flex items-center justify-center">
            {/* Interactive Graph Node mockups */}
            <div className="absolute top-10 left-10 p-3 glass rounded-lg text-xs flex flex-col items-center">
              <span className="font-bold text-blue-400">Mine</span>
              <span className="text-[10px] text-muted-foreground">Salar de Atacama</span>
            </div>
            <div className="absolute top-36 left-40 p-3 glass rounded-lg text-xs flex flex-col items-center">
              <span className="font-bold text-purple-400">Refinery</span>
              <span className="text-[10px] text-muted-foreground">Tianqi Lithium</span>
            </div>
            <div className="absolute top-12 right-28 p-3 glass rounded-lg text-xs flex flex-col items-center border-amber-500/50">
              <span className="font-bold text-amber-400">Cell Plant</span>
              <span className="text-[10px] text-muted-foreground">CATL Yibin</span>
            </div>
            <div className="absolute top-44 right-10 p-3 glass rounded-lg text-xs flex flex-col items-center">
              <span className="font-bold text-emerald-400">EV Fleet</span>
              <span className="text-[10px] text-muted-foreground">Denver Hub</span>
            </div>

            {/* Connecting SVG lines */}
            <svg className="absolute inset-0 h-full w-full pointer-events-none" xmlns="http://www.w3.org/2000/svg">
              <path d="M 120 70 L 190 145" stroke="rgba(255,255,255,0.15)" strokeWidth="2" strokeDasharray="4" />
              <path d="M 230 160 L 320 80" stroke="rgba(255,255,255,0.15)" strokeWidth="2" strokeDasharray="4" />
              <path d="M 370 80 L 420 170" stroke="rgba(255,255,255,0.15)" strokeWidth="2" strokeDasharray="4" />
            </svg>

            <span className="text-xs text-muted-foreground z-10 bg-background/80 px-2 py-1 rounded">Interactive Cypher queries mapping...</span>
          </div>

          <div className="flex gap-4 text-xs">
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-blue-500" /> Mines</span>
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-purple-500" /> Refiners</span>
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-amber-500" /> Cell Plants</span>
            <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-emerald-500" /> Fleets</span>
          </div>
        </div>

        {/* Risk Scores Engine */}
        <div className="glass p-6 rounded-xl flex flex-col justify-between">
          <div>
            <h2 className="font-semibold text-lg">Supply Chain Risk Scoring</h2>
            <p className="text-xs text-muted-foreground mt-1">Calculated from supplier concentration, shipping bottle-necks, and geopolitics.</p>
          </div>

          <div className="space-y-4 my-6">
            <div className="space-y-1">
              <div className="flex justify-between text-xs font-semibold">
                <span>Concentration Index</span>
                <span className="text-red-400">High Risk (86/100)</span>
              </div>
              <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
                <div className="bg-red-500 h-full w-[86%]" />
              </div>
            </div>

            <div className="space-y-1">
              <div className="flex justify-between text-xs font-semibold">
                <span>Geopolitical Instability</span>
                <span className="text-yellow-400">Medium Risk (54/100)</span>
              </div>
              <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
                <div className="bg-yellow-500 h-full w-[54%]" />
              </div>
            </div>

            <div className="space-y-1">
              <div className="flex justify-between text-xs font-semibold">
                <span>Shipping Botlenecks</span>
                <span className="text-emerald-400">Low Risk (28/100)</span>
              </div>
              <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
                <div className="bg-emerald-500 h-full w-[28%]" />
              </div>
            </div>
          </div>

          <div className="bg-red-500/5 border border-red-500/20 p-3 rounded-lg flex items-start gap-2.5">
            <AlertOctagon className="h-4.5 w-4.5 text-red-400 shrink-0 mt-0.5" />
            <p className="text-[11px] text-red-300">
              <strong>Dependency Alert:</strong> 85% of Active Cells originate from single-tier refiner. Interruption propagates to Denver Hub assembly within 12 days.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
