import React from 'react';
import { AlertCircle, Ban, BellRing, Settings, Info } from 'lucide-react';

export default function Alerts() {
  return (
    <div className="space-y-6 animate-fade-in">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight">Active System Alerts</h1>
          <p className="text-muted-foreground mt-1">Real-time status updates and telemetry anomalies detected on asset networks.</p>
        </div>
        <button className="flex items-center gap-1.5 bg-muted hover:bg-muted/80 text-xs px-3.5 py-2 rounded-lg font-medium border border-border transition-colors">
          <Settings className="h-4 w-4" />
          <span>Config Rules</span>
        </button>
      </div>

      {/* Quick filters */}
      <div className="flex gap-2 text-xs">
        <button className="px-3.5 py-1.5 rounded-full bg-blue-500 text-white font-medium">All Alerts (18)</button>
        <button className="px-3.5 py-1.5 rounded-full bg-muted text-muted-foreground hover:bg-muted/80 font-medium">Critical (4)</button>
        <button className="px-3.5 py-1.5 rounded-full bg-muted text-muted-foreground hover:bg-muted/80 font-medium">Warnings (8)</button>
        <button className="px-3.5 py-1.5 rounded-full bg-muted text-muted-foreground hover:bg-muted/80 font-medium">Resolved (6)</button>
      </div>

      {/* Alert Feed Container */}
      <div className="space-y-3.5">
        {[
          { id: "A-201", type: "Critical", asset: "EV-HD-004", msg: "Voltage delta exceeds 0.2V limit - potential cell imbalance anomaly.", time: "2 mins ago" },
          { id: "A-202", type: "Warning", asset: "EV-HD-002", msg: "Core cell temperature spiked above 42°C during rapid charge sequence.", time: "12 mins ago" },
          { id: "A-203", type: "Critical", asset: "EV-HD-012", msg: "Remaining Useful Life (RUL) regression predictions fell below 10% threshold limit.", time: "1 hour ago" },
          { id: "A-204", type: "Info", asset: "EV-HD-008", msg: "Scheduled filter maintenance completed. Recalibrating health state metrics.", time: "3 hours ago" }
        ].map((alert, i) => (
          <div key={i} className={`glass p-5 rounded-xl border-l-4 flex justify-between items-start gap-4 ${
            alert.type === 'Critical' ? 'border-l-red-500' :
            alert.type === 'Warning' ? 'border-l-yellow-500' :
            'border-l-blue-500'
          }`}>
            <div className="flex gap-3">
              {alert.type === 'Critical' ? (
                <AlertCircle className="h-5 w-5 text-red-500 shrink-0 mt-0.5" />
              ) : alert.type === 'Warning' ? (
                <BellRing className="h-5 w-5 text-yellow-500 shrink-0 mt-0.5" />
              ) : (
                <Info className="h-5 w-5 text-blue-500 shrink-0 mt-0.5" />
              )}
              <div>
                <div className="flex items-center gap-2">
                  <span className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">Asset: <span className="font-mono text-foreground">{alert.asset}</span></span>
                  <span className="h-1 w-1 rounded-full bg-muted-foreground/50" />
                  <span className="text-[11px] text-muted-foreground">{alert.time}</span>
                </div>
                <p className="text-sm font-semibold mt-1.5">{alert.msg}</p>
              </div>
            </div>
            <button className="text-xs text-muted-foreground hover:text-foreground font-semibold px-2 py-1 rounded bg-muted/30 hover:bg-muted/65 transition-colors">
              Mute
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
