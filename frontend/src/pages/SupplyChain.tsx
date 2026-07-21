import React, { useEffect, useState } from 'react';
import NetworkGraph from '../components/supply-chain/NetworkGraph';
import RiskDashboard from '../components/supply-chain/RiskDashboard';
import ProcurementRecommendations from '../components/supply-chain/ProcurementRecommendations';
import { Search } from 'lucide-react';
import { coreApi } from '../services/coreApi';

export default function SupplyChain() {
  const [overview, setOverview] = useState<any>(null);
  const [traceSearch, setTraceSearch] = useState('');
  const [traceResult, setTraceResult] = useState<any>(null);

  useEffect(() => {
    const fetchOverview = async () => {
      try {
        const response = await fetch('/api/v1/supply-chain/dashboard/overview');
        if (response.ok) {
          const data = await response.json();
          setOverview(data);
        }
      } catch (error) {
        console.error('Error fetching dashboard overview:', error);
      }
    };
    fetchOverview();
  }, []);

  const handleTrace = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!traceSearch) return;
    try {
      const data = await coreApi.getTraceability(traceSearch);
      setTraceResult(data);
    } catch (err) {
      console.error("Traceability lookup failed", err);
    }
  };

  return (
    <div className="space-y-6 animate-fade-in">
      <div className="flex justify-between items-start">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight">Graph-Based Supply Chain Intelligence</h1>
          <p className="text-muted-foreground mt-1">Multi-tier battery material dependencies, supplier risk assessments, and vulnerability tracking.</p>

          {overview && (
            <div className="flex gap-4 mt-4 text-sm bg-background/50 p-3 rounded-lg border border-border inline-flex">
              <div><span className="font-semibold">Total Nodes:</span> {overview.total_nodes}</div>
              <div className="border-l border-border pl-4"><span className="font-semibold">Total Relationships:</span> {overview.total_relationships}</div>
            </div>
          )}
        </div>

        {/* NEW: Traceability Deep Lookup Form */}
        <form onSubmit={handleTrace} className="flex gap-2">
          <div className="relative">
            <Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" />
            <input
              type="text"
              placeholder="Deep Trace Entity ID..."
              value={traceSearch}
              onChange={(e) => setTraceSearch(e.target.value)}
              className="pl-9 pr-4 py-2 bg-muted/40 border border-border rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-blue-500"
            />
          </div>
          <button type="submit" className="px-4 py-2 bg-blue-500/20 text-blue-400 hover:bg-blue-500/30 rounded-lg text-sm font-semibold transition-colors">
            Trace
          </button>
        </form>
      </div>

      {/* Traceability Result Overlay */}
      {traceResult && (
        <div className="glass p-4 rounded-xl border border-blue-500/30">
          <div className="flex justify-between items-center mb-2">
            <h3 className="text-sm font-bold text-blue-400">Trace Lineage for: {traceResult.target_id}</h3>
            <button onClick={() => setTraceResult(null)} className="text-xs text-muted-foreground hover:text-slate-200">Clear</button>
          </div>
          <div className="text-xs text-muted-foreground flex gap-4">
            <span>Upstream Hops: {traceResult.upstream_lineage?.length || 0}</span>
            <span>Downstream Targets: {traceResult.downstream_usage?.length || 0}</span>
            <span>Complete Chain Stages: {traceResult.complete_manufacturing_chain?.length || 0}</span>
          </div>
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 flex flex-col gap-6">
          <div className="h-[550px]">
            <NetworkGraph />
          </div>
          <div>
            <ProcurementRecommendations />
          </div>
        </div>

        <div className="flex flex-col gap-6">
          <RiskDashboard />
        </div>
      </div>
    </div>
  );
}
