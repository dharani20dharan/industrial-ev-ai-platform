const API_BASE = '/api/v1/sustainability';

export interface APIResponse<T> {
  success: boolean;
  message: string;
  data: T;
}

export interface SustainabilitySummary {
  total_carbon_saved_kg: number;
  scope1_emission_kg: number;
  scope3_emission_kg: number;
  vehicles_assessed: number;
  average_readiness_score: number;
  total_reports: number;
  grid_region: string;
}

export interface CarbonReport {
  report_id: string;
  vehicle_id: string;
  distance_travelled: number;
  energy_consumed_kwh: number;
  diesel_emission: number;
  ev_emission: number;
  scope1_emission: number;
  scope3_emission: number;
  carbon_saved: number;
  grid_region: string;
  generated_at: string;
}

export interface DieselVsEVRequest {
  distance_km: number;
  payload_kg: number;
  diesel_efficiency: number;
  ev_efficiency: number;
  vehicle_type?: string;
}

export interface DieselVsEVResponse {
  diesel_emission: number;
  ev_emission: number;
  carbon_saved: number;
  reduction_percentage: number;
  equivalent_trees: number;
  equivalent_gallons_gasoline: number;
}

export interface ReadinessAssessmentRequest {
  route_distance: number;
  payload: number;
  charging_availability: boolean;
  dwell_time: number;
  vehicle_type?: string;
  vehicle_id?: string;
}

export interface ReadinessAssessmentResponse {
  assessment_id: string;
  readiness_score: number;
  readiness_level: string;
  recommendation: string;
  factor_scores: Record<string, number>;
  financial: Record<string, any>;
  improvements_needed: string[];
  generated_at: string;
}

export interface ProcurementRecommendationRequest {
  fleet_size: number;
  daily_distance: number;
  charging_available: boolean;
  vehicle_type?: string;
}

export interface ProcurementRecommendationResponse {
  recommended_vehicle_type: string;
  recommended_quantity: number;
  estimated_carbon_saving: number;
  recommendation_level: 'LOW' | 'MEDIUM' | 'HIGH';
  reasoning: string;
}

export const sustainabilityApi = {
  getSummary: async (): Promise<APIResponse<SustainabilitySummary>> => {
    const res = await fetch(`${API_BASE}/summary`);
    if (!res.ok) throw new Error('Failed to fetch sustainability summary');
    return res.json();
  },

  getHistory: async (): Promise<APIResponse<CarbonReport[]>> => {
    const res = await fetch(`${API_BASE}/history?limit=50`);
    if (!res.ok) throw new Error('Failed to fetch sustainability history');
    return res.json();
  },

  compareDieselVsEv: async (payload: DieselVsEVRequest): Promise<APIResponse<DieselVsEVResponse>> => {
    const res = await fetch(`${API_BASE}/diesel-vs-ev`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!res.ok) throw new Error('Failed to compare diesel vs ev');
    return res.json();
  },

  assessReadiness: async (payload: ReadinessAssessmentRequest): Promise<APIResponse<ReadinessAssessmentResponse>> => {
    const res = await fetch(`${API_BASE}/readiness-assessment`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!res.ok) throw new Error('Failed to assess readiness');
    return res.json();
  },

  getReadiness: async (assessmentId: string): Promise<APIResponse<ReadinessAssessmentResponse>> => {
    const res = await fetch(`${API_BASE}/readiness/${assessmentId}`);
    if (!res.ok) throw new Error('Failed to fetch readiness assessment');
    return res.json();
  },

  getProcurementRecommendation: async (payload: ProcurementRecommendationRequest): Promise<APIResponse<ProcurementRecommendationResponse>> => {
    const res = await fetch(`${API_BASE}/procurement-recommendation`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!res.ok) throw new Error('Failed to generate procurement recommendation');
    return res.json();
  },

  getCarbonReport: async (reportId: string): Promise<APIResponse<CarbonReport>> => {
    const res = await fetch(`${API_BASE}/carbon/report/${reportId}`);
    if (!res.ok) throw new Error('Failed to fetch carbon report');
    return res.json();
  }
};
