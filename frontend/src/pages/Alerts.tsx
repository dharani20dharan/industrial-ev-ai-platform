import React, { useState, useEffect, useMemo } from 'react';
import { useFleetData } from '../hooks/useFleetData';
import { ShieldAlert, AlertTriangle, Search, Trash2, CheckCircle2, Radio, Filter } from 'lucide-react';

interface SystemAlert {
  id: string;
  asset: string;
  type: 'Warning' | 'Critical' | 'FAULT';
  msg: string;
  timestamp: string;
}

export default function Alerts() {
  const { alerts: incomingAlerts } = useFleetData();
  const [localAlerts, setLocalAlerts] = useState<SystemAlert[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [severityFilter, setSeverityFilter] = useState<string>('ALL'); // ALL, CRITICAL, WARNING

  // Sophisticated deduplication: If the same vehicle reports the exact same fault message,
  // update its timestamp instead of spamming a duplicate card entry.
  useEffect(() => {
    if (incomingAlerts && incomingAlerts.length > 0) {
      setLocalAlerts((prev) => {
        const updated = [...prev];

        incomingAlerts.forEach((incoming) => {
          // Stable fingerprint based on asset + message content
          const fingerprint = `${incoming.asset}-${incoming.msg}`;
          const existingIndex = updated.findIndex(
            (a) => `${a.asset}-${a.msg}` === fingerprint
          );

          if (existingIndex >= 0) {
            // Update timestamp of existing alert without adding duplicate row
            updated[existingIndex] = {
              ...updated[existingIndex],
              timestamp: incoming.timestamp || new Date().toLocaleTimeString(),
            };
          } else {
            // Prepend new unique alert
            updated.unshift({
              ...incoming,
              id: `${fingerprint}-${Date.now()}`,
            });
          }
        });

        return updated.slice(0, 100); // Keep buffer capped
      });
    }
  }, [incomingAlerts]);

  // Filter alerts based on search query and severity filter
  const filteredAlerts = useMemo(() => {
    return localAlerts.filter((alert) => {
      const matchesSearch =
        !searchQuery ||
        alert.asset.toLowerCase().includes(searchQuery.toLowerCase().trim()) ||
        alert.msg.toLowerCase().includes(searchQuery.toLowerCase().trim());

      if (!matchesSearch) return false;

      if (severityFilter === 'ALL') return true;
      if (severityFilter === 'CRITICAL' && (alert.type === 'Critical' || alert.type === 'FAULT')) return true;
      if (severityFilter === 'WARNING' && alert.type === 'Warning') return true;

      return false;
    });
  }, [localAlerts, searchQuery, severityFilter]);

  const clearAlert = (idToRemove: string) => {
    setLocalAlerts((prev) => prev.filter((alert) => alert.id !== idToRemove));
  };

  const clearAllAlerts = () => {
    setLocalAlerts([]);
  };

  return (
    <div className="space-y-6 animate-fade-in pb-12 max-w-7xl mx-auto">
      {/* Header View Row */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 bg-card border border-border p-6 rounded-2xl shadow-xl bg-gradient-to-r from-blue-950/20 via-card to-card">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight flex items-center gap-3">
            System Activity Fault Logs
            <span className="px-2.5 py-0.5 rounded-full bg-rose-500/10 border border-rose-500/30 text-rose-400 text-xs font-mono">
              {localAlerts.length} Active
            </span>
          </h1>
          <p className="text-muted-foreground mt-1 text-sm">Real-time predictive anomaly diagnostics and threshold excursion telemetry.</p>
        </div>

        <div className="flex items-center gap-3 flex-wrap">
          {localAlerts.length > 0 && (
            <button
              onClick={clearAllAlerts}
              className="flex items-center gap-2 px-4 py-2 bg-rose-600/20 hover:bg-rose-600 text-rose-300 hover:text-white border border-rose-500/40 rounded-xl text-xs font-semibold transition-all shadow"
            >
              <Trash2 className="h-4 w-4" />
              <span>Acknowledge All</span>
            </button>
          )}
        </div>
      </div>

      {/* Control Bar: Search & Severity Filters */}
      <div className="flex flex-col sm:flex-row justify-between items-center gap-4 bg-card border border-border p-4 rounded-xl shadow-md">
        <div className="relative w-full sm:w-80">
          <Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" />
          <input
            type="text"
            placeholder="Search by Vehicle ID or fault message..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-4 py-2 bg-background border border-border rounded-lg text-xs font-mono text-foreground focus:outline-none focus:ring-1 focus:ring-blue-500"
          />
        </div>

        <div className="flex items-center gap-1.5 bg-muted/40 p-1 rounded-lg border border-border text-xs font-semibold">
          {['ALL', 'CRITICAL', 'WARNING'].map((filter) => (
            <button
              key={filter}
              onClick={() => setSeverityFilter(filter)}
              className={`px-3 py-1.5 rounded-md transition-all ${
                severityFilter === filter
                  ? 'bg-blue-600 text-white shadow'
                  : 'text-muted-foreground hover:text-foreground'
              }`}
            >
              {filter}
            </button>
          ))}
        </div>
      </div>

      {/* Alert Feed Section */}
      {filteredAlerts.length === 0 ? (
        <div className="glass p-12 rounded-2xl text-center flex flex-col items-center justify-center space-y-3 border border-dashed border-border">
          <CheckCircle2 className="h-10 w-10 text-emerald-500 animate-pulse" />
          <h3 className="text-base font-bold text-foreground">No Faults Detected</h3>
          <p className="text-xs text-muted-foreground max-w-md">
            All active fleet assets are operating strictly within nominal electro-chemical and thermal safety thresholds.
          </p>
        </div>
      ) : (
        <div className="space-y-3">
          {filteredAlerts.map((alert) => {
            const isCritical = alert.type === 'Critical' || alert.type === 'FAULT';

            return (
              <div
                key={alert.id}
                className={`glass p-4.5 rounded-xl border flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 transition-all duration-200 hover:scale-[1.01] ${
                  isCritical ? 'border-rose-500/40 bg-rose-500/5' : 'border-amber-500/40 bg-amber-500/5'
                }`}
              >
                <div className="flex items-start gap-3.5 flex-1">
                  <div className={`p-2.5 rounded-xl border shrink-0 mt-0.5 ${
                    isCritical ? 'bg-rose-500/10 border-rose-500/30 text-rose-400 animate-pulse' : 'bg-amber-500/10 border-amber-500/30 text-amber-400'
                  }`}>
                    {isCritical ? <ShieldAlert className="h-5 w-5" /> : <AlertTriangle className="h-5 w-5" />}
                  </div>

                  <div className="space-y-1 flex-1">
                    <div className="flex items-center gap-2 flex-wrap">
                      <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider border ${
                        isCritical ? 'bg-rose-500/20 text-rose-300 border-rose-500/40' : 'bg-amber-500/20 text-amber-300 border-amber-500/40'
                      }`}>
                        {alert.type}
                      </span>
                      <strong className="text-sm font-mono font-bold text-foreground">{alert.asset}</strong>
                      <span className="text-[11px] text-muted-foreground font-mono ml-auto sm:ml-0">{alert.timestamp}</span>
                    </div>
                    <p className="text-xs text-slate-300 leading-relaxed font-medium">{alert.msg}</p>
                  </div>
                </div>

                <button
                  onClick={() => clearAlert(alert.id)}
                  className="px-3 py-1.5 bg-muted/40 hover:bg-muted text-muted-foreground hover:text-foreground border border-border rounded-lg text-xs font-semibold transition-all shrink-0 self-end sm:self-center"
                  title="Acknowledge and dismiss fault log"
                >
                  Acknowledge
                </button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
