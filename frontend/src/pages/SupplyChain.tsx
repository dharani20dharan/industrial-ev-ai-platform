import React, { useEffect, useState } from 'react';
import NetworkGraph from '../components/supply-chain/NetworkGraph';
import RiskDashboard from '../components/supply-chain/RiskDashboard';
import ProcurementRecommendations from '../components/supply-chain/ProcurementRecommendations';
import { Search, Layers, GitCommit, CheckCircle, Info, X } from 'lucide-react';

export default function SupplyChain() {
  const [overview, setOverview] = useState<any>(null);
  const [traceSearch, setTraceSearch] = useState('');
  const [activeAnalysis, setActiveAnalysis] = useState<any>(null);
  const [loadingAnalysis, setLoadingAnalysis] = useState(false);

  // Fetch live dashboard metrics directly from backend overview endpoint
  useEffect(() => {
    const fetchOverview = async () => {
      try {
        const response = await fetch('/api/v1/supply-chain/dashboard/overview');
        if (response.ok) {
          const json = await response.json();
          // Handle both direct objects and standard APIResponse wrappers
          const data = json.data || json;
          setOverview(data);
        }
      } catch (error) {
        console.error('Error fetching dashboard overview:', error);
      }
    };
    fetchOverview();
  }, []);

  const executeFullEntityAnalysis = async (entityId: string, entityType: string = 'supplier') => {
    if (!entityId) return;
    setLoadingAnalysis(true);

    try {
      const traceRes = await fetch(`/api/v1/supply-chain/traceability?entity_id=${entityId}`);
      const traceData = traceRes.ok ? await traceRes.json() : null;

      let riskEndpoint = `/api/v1/supply-chain/risk/supplier/${entityId}`;
      const t = entityType.toLowerCase();
      if (t.includes('vehicle') || t.includes('fleet')) {
        riskEndpoint = `/api/v1/supply-chain/risk/vehicle/${entityId}`;
      } else if (t.includes('material')) {
        riskEndpoint = `/api/v1/supply-chain/risk/material/${entityId}`;
      }
      const riskRes = await fetch(riskEndpoint);
      const riskData = riskRes.ok ? await riskRes.json() : null;

      let impactEndpoint = `/api/v1/supply-chain/impact/supplier/${entityId}`;
      if (t.includes('material')) {
        impactEndpoint = `/api/v1/supply-chain/impact/material/${entityId}`;
      } else if (t.includes('refin') || t.includes('processing')) {
        impactEndpoint = `/api/v1/supply-chain/impact/refinery/${entityId}`;
      }
      const impactRes = await fetch(impactEndpoint);
      const impactData = impactRes.ok ? await impactRes.json() : null;

      let altEndpoint = `/api/v1/supply-chain/alternatives/supplier/${entityId}`;
      if (t.includes('material')) {
        altEndpoint = `/api/v1/supply-chain/alternatives/material/${entityId}`;
      }
      const altRes = await fetch(altEndpoint);
      const altData = altRes.ok ? await altRes.json() : null;

      setActiveAnalysis({
        target_id: entityId,
        entity_type: entityType,
        trace: traceData,
        risk: riskData,
        impact: impactData,
        alternatives: altData
      });

    } catch (err) {
      console.error("Entity inspection network error:", err);
    } finally {
      setLoadingAnalysis(false);
    }
  };

  const handleTraceSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    executeFullEntityAnalysis(traceSearch, 'supplier');
  };

  const getPlainEnglishSummary = (analysis: any) => {
    const riskScore = analysis.risk?.risk?.score || 0;
    const vehiclesAffected = analysis.impact?.impacted_vehicles || 0;
    const alternativesCount = analysis.alternatives?.alternative_suppliers?.length || 0;

    if (riskScore >= 70) {
      return `Critical Vulnerability: High operational risk (${riskScore}/100) directly threatens ${vehiclesAffected} active fleet vehicles. Immediate transition to alternative vendors is recommended.`;
    } else if (riskScore >= 40) {
      return `Moderate Risk Warning: Operating normally with minor geopolitical exposure. ${vehiclesAffected} downstream assets depend on this node. ${alternativesCount} backup suppliers are available.`;
    }
    return `Nominal Operation: Stable supply chain node with low disruption risk, securely supporting ${vehiclesAffected} active fleet assets.`;
  };

  return (
    <div className="space-y-6 animate-fade-in pb-12">
      {/* Top Header & Live Dynamic Metrics Bar */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 bg-card border border-border p-6 rounded-2xl shadow-xl bg-gradient-to-r from-blue-950/20 via-card to-card">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight">Supply Chain Command Center</h1>
          <p className="text-muted-foreground mt-1 text-sm">Interactive Multi-Tier Dependency Graph & Live Operational Risk Inspector</p>

          <div className="flex flex-wrap gap-4 mt-3 text-xs bg-background/50 p-2.5 rounded-xl border border-border inline-flex font-mono">
            <div><span className="text-muted-foreground">Suppliers:</span> <strong className="text-foreground">{overview?.total_suppliers ?? '...'}</strong></div>
            <div className="border-l border-border pl-3"><span className="text-muted-foreground">Materials:</span> <strong className="text-foreground">{overview?.total_materials ?? '...'}</strong></div>
            <div className="border-l border-border pl-3"><span className="text-muted-foreground">Vehicles:</span> <strong className="text-foreground">{overview?.total_vehicles ?? '...'}</strong></div>
            <div className="border-l border-border pl-3"><span className="text-muted-foreground">Diversity Index:</span> <strong className="text-emerald-400">{overview?.supply_diversity_index ?? 0}%</strong></div>
          </div>
        </div>

        <form onSubmit={handleTraceSubmit} className="flex gap-2">
          <div className="relative">
            <Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" />
            <input
              type="text"
              placeholder="Search Entity ID..."
              value={traceSearch}
              onChange={(e) => setTraceSearch(e.target.value)}
              className="pl-9 pr-4 py-2 bg-muted/40 border border-border rounded-xl text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 font-mono w-56 shadow-inner"
            />
          </div>
          <button type="submit" disabled={loadingAnalysis} className="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-sm font-semibold transition-colors disabled:opacity-50 shadow">
            {loadingAnalysis ? 'Loading...' : 'Inspect'}
          </button>
        </form>
      </div>

      {/* Master-Detail Layout: Wide Graph + Side Inspector Panel */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">

        {/* Left / Main View: Ultra-Wide Interactive Graph */}
        <div className={`transition-all duration-300 ${activeAnalysis ? 'lg:col-span-8' : 'lg:col-span-12'}`}>
          <div className="h-[680px] w-full shadow-2xl">
            <NetworkGraph
              onSelectEntity={(id, type) => {
                setTraceSearch(id);
                executeFullEntityAnalysis(id, type);
              }}
              selectedEntityId={activeAnalysis?.target_id}
            />
          </div>
        </div>

        {/* Right Side: Consolidated Side Inspector Panel */}
        {activeAnalysis && (
          <div className="lg:col-span-4 glass p-6 rounded-2xl border-2 border-cyan-500/50 space-y-5 shadow-2xl bg-slate-950/95 animate-fade-in relative">
            <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-cyan-500 via-blue-500 to-emerald-500" />

            <div className="flex justify-between items-center border-b border-border pb-3">
              <div>
                <span className="text-[10px] font-bold uppercase tracking-widest bg-cyan-500/20 text-cyan-400 px-2 py-0.5 rounded border border-cyan-500/30 font-mono">
                  Live REST Inspector
                </span>
                <h3 className="text-base font-black text-foreground font-mono mt-1 flex items-center gap-1.5 truncate max-w-[220px]">
                  <GitCommit className="h-4 w-4 text-cyan-400 shrink-0" />
                  {activeAnalysis.target_id}
                </h3>
              </div>
              <button
                onClick={() => setActiveAnalysis(null)}
                className="text-muted-foreground hover:text-foreground p-1 rounded-lg hover:bg-muted/50 transition-all"
                title="Close Inspector"
              >
                <X className="h-5 w-5" />
              </button>
            </div>

            {/* Business Takeaway Banner */}
            <div className="bg-blue-500/10 border border-blue-500/30 p-3.5 rounded-xl flex items-start gap-2.5">
              <Info className="h-4 w-4 text-blue-400 shrink-0 mt-0.5" />
              <p className="text-[11px] text-slate-200 leading-relaxed font-medium">
                {getPlainEnglishSummary(activeAnalysis)}
              </p>
            </div>

            {/* Key Metrics Grid */}
            <div className="grid grid-cols-2 gap-3 text-xs">
              <div className="bg-muted/30 p-3 rounded-xl border border-border/50">
                <span className="text-muted-foreground block text-[10px] uppercase font-bold">Risk Score</span>
                <span className="text-lg font-black font-mono text-rose-400 mt-0.5 block">
                  {activeAnalysis.risk?.risk?.score !== undefined ? `${activeAnalysis.risk.risk.score}/100` : 'N/A'}
                </span>
              </div>
              <div className="bg-muted/30 p-3 rounded-xl border border-border/50">
                <span className="text-muted-foreground block text-[10px] uppercase font-bold">Impacted EVs</span>
                <span className="text-lg font-black font-mono text-emerald-400 mt-0.5 block">
                  {activeAnalysis.impact?.impacted_vehicles !== undefined ? `${activeAnalysis.impact.impacted_vehicles} Assets` : '0'}
                </span>
              </div>
            </div>

            {/* Alternative Vendors */}
            {activeAnalysis.alternatives?.alternative_suppliers && activeAnalysis.alternatives.alternative_suppliers.length > 0 && (
              <div className="space-y-2">
                <h4 className="text-[11px] font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1">
                  <CheckCircle className="h-3.5 w-3.5" /> Backup Vendors
                </h4>
                <div className="space-y-1.5 max-h-36 overflow-y-auto pr-1">
                  {activeAnalysis.alternatives.alternative_suppliers.map((alt: any, i: number) => (
                    <div key={i} className="bg-slate-900 p-2 rounded-lg border border-slate-800 text-xs flex justify-between items-center font-mono">
                      <span className="font-bold text-slate-200 truncate">{alt.supplier_name || alt.name || alt.supplier_id}</span>
                      <span className="text-muted-foreground text-[10px]">{alt.country || 'Global'}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Lineage Summary */}
            {activeAnalysis.trace?.complete_manufacturing_chain && (
              <div className="space-y-2 pt-1 border-t border-border">
                <h4 className="text-[11px] font-bold text-muted-foreground uppercase tracking-wider flex items-center gap-1.5">
                  <Layers className="h-3.5 w-3.5 text-cyan-400" /> Lineage Chain Tiers
                </h4>
                <div className="space-y-1.5 max-h-48 overflow-y-auto pr-1">
                  {activeAnalysis.trace.complete_manufacturing_chain.map((stage: any, idx: number) => (
                    <div key={idx} className="bg-slate-900/80 border border-slate-800 p-2 rounded-lg text-xs flex items-center justify-between font-mono">
                      <div>
                        <span className="text-[9px] uppercase font-bold px-1.5 py-0.5 rounded bg-cyan-500/10 text-cyan-400 mr-2">
                          Tier {stage.stage_order || idx + 1}
                        </span>
                        <span className="font-bold text-slate-200">{stage.name}</span>
                      </div>
                      <span className="text-[10px] text-muted-foreground">{stage.location || 'Global'}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Bottom Section: Risk Dashboard & AI Procurement Recommendations */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 pt-4">
        <RiskDashboard />
        <ProcurementRecommendations />
      </div>
    </div>
  );
}
