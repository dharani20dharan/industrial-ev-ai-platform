const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const coreApi = {
  // Charging Endpoints
  getChargingHistory: async (vehicleId: string) => {
    const res = await fetch(`${API_BASE_URL}/api/v1/charging/history?vehicle_id=${vehicleId}`);
    if (!res.ok) throw new Error('Failed to fetch charging history');
    return res.json();
  },

  // Traceability Endpoints
  getTraceability: async (entityId: string) => {
    const res = await fetch(`${API_BASE_URL}/api/v1/supply-chain/traceability?entity_id=${entityId}`);
    if (!res.ok) throw new Error('Failed to fetch traceability data');
    return res.json();
  },

  // Telemetry Timeseries Endpoints
  getTelemetryTimeseries: async (vehicleId: string, limit: number = 24) => {
    const res = await fetch(`${API_BASE_URL}/api/v1/telemetry/timeseries?vehicle_id=${vehicleId}&limit=${limit}`);
    if (!res.ok) throw new Error('Failed to fetch telemetry timeseries');
    return res.json();
  }
};
