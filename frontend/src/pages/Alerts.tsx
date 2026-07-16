import React, { useState, useEffect } from 'react';
import { useFleetData } from '../hooks/useFleetData';

interface SystemAlert {
  id: string; // Dynamic ID to prevent duplicate key warning
  asset: string;
  type: 'Warning' | 'Critical';
  msg: string;
  timestamp: string;
}

export default function Alerts() {
  // 1. Grab incoming stream alerts from our custom hook
  const { alerts: incomingAlerts } = useFleetData();

  // 2. Maintain a local state so we can actually delete or acknowledge them on screen
  const [localAlerts, setLocalAlerts] = useState<SystemAlert[]>([]);

  // Sync incoming live updates with local state, assigning a bulletproof ID
  useEffect(() => {
    if (incomingAlerts && incomingAlerts.length > 0) {
      setLocalAlerts((prev) => {
        // Create an array of fresh entries with robust keys
        const formattedIncoming = incomingAlerts.map((alert, index) => ({
          ...alert,
          // Generate a truly unique composite key string
          id: `${alert.asset}-${alert.timestamp}-${index}-${alert.msg.substring(0, 5)}`
        }));

        // Deduplicate incoming vs existing to prevent view pop duplicates
        const existingKeys = new Set(prev.map(a => a.id));
        const newUniqueAlerts = formattedIncoming.filter(a => !existingKeys.has(a.id));

        return [...newUniqueAlerts, ...prev].slice(0, 50);
      });
    }
  }, [incomingAlerts]);

  // FIX: This now safely mutates the correct local state array!
  const clearAlert = (idToRemove: string) => {
    setLocalAlerts((prev) => prev.filter((alert) => alert.id !== idToRemove));
  };

  const clearAllAlerts = () => {
    setLocalAlerts([]);
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-800">System Activity Fault Logs</h2>
        {localAlerts.length > 0 && (
          <button
            onClick={clearAllAlerts}
            className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded text-sm transition"
          >
            Clear All Logs
          </button>
        )}
      </div>

      {localAlerts.length === 0 ? (
        <div className="p-8 text-center bg-gray-50 border border-dashed rounded text-gray-500">
          🟢 All vehicle assets running within nominal thresholds. No faults detected.
        </div>
      ) : (
        <div className="space-y-3">
          {localAlerts.map((alert) => (
            // FIX: Explicitly passing down our absolute unique dynamic ID key
            <div
              key={alert.id}
              className={`p-4 rounded border flex justify-between items-start transition ${
                alert.type === 'Critical' ? 'bg-red-50 border-red-200' : 'bg-amber-50 border-amber-200'
              }`}
            >
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <span className={`px-2 py-0.5 rounded text-xs font-semibold ${
                    alert.type === 'Critical' ? 'bg-red-200 text-red-800' : 'bg-amber-200 text-amber-800'
                  }`}>
                    {alert.type}
                  </span>
                  <strong className="text-gray-900">{alert.asset}</strong>
                  <span className="text-xs text-gray-500 font-mono">{alert.timestamp}</span>
                </div>
                <p className="text-sm text-gray-700">{alert.msg}</p>
              </div>

              <button
                onClick={() => clearAlert(alert.id)}
                className="text-gray-400 hover:text-gray-600 ml-4 font-bold text-lg leading-none"
                title="Acknowledge fault"
              >
                &times;
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
