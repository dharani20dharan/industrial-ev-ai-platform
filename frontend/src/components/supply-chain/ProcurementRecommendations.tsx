import React, { useEffect, useState } from 'react';
import { TrendingUp, ShieldAlert, CheckCircle, ArrowRight } from 'lucide-react';

interface SupplierRecommendation {
  supplier_id: string;
  supplier_name: string;
  country: string;
  mineral: string;
}

interface RecommendationItem {
  material: string;
  recommended_suppliers: SupplierRecommendation[];
  alternative_suppliers: SupplierRecommendation[];
  diversification_suggestions: string[];
  reason_for_recommendation: string;
  current_supplier_risk: number;
  suggested_supplier_risk: number;
}

interface RecommendationsResponse {
  recommendations: RecommendationItem[];
  summary: string;
}

export default function ProcurementRecommendations() {
  const [data, setData] = useState<RecommendationsResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        const response = await fetch('/api/v1/supply-chain/recommendations');
        if (response.ok) {
          const json = await response.json();
          setData(json);
        }
      } catch (error) {
        console.error('Error fetching procurement recommendations:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchRecommendations();
  }, []);

  if (loading) {
    return <div className="p-6 glass rounded-xl animate-pulse h-64 flex items-center justify-center">Loading AI Recommendations...</div>;
  }

  if (!data || data.recommendations.length === 0) {
    return <div className="p-6 glass rounded-xl text-muted-foreground">No procurement recommendations available at this time.</div>;
  }

  return (
    <div className="glass p-6 rounded-xl flex flex-col space-y-4">
      <div>
        <h2 className="font-semibold text-lg flex items-center gap-2">
          <TrendingUp className="h-5 w-5 text-blue-400" />
          AI Procurement Recommendations
        </h2>
        <p className="text-xs text-muted-foreground mt-1">{data.summary}</p>
      </div>

      <div className="space-y-4">
        {data.recommendations.map((rec, idx) => (
          <div key={idx} className="bg-background/40 border border-border/50 rounded-lg p-4 space-y-3">
            <div className="flex justify-between items-start">
              <h3 className="font-bold capitalize">{rec.material} Strategy</h3>
              <div className="text-xs flex items-center gap-2">
                <span className="text-red-400 font-semibold">Current Risk: {rec.current_supplier_risk}</span>
                <ArrowRight className="h-3 w-3 text-muted-foreground" />
                <span className="text-emerald-400 font-semibold">Suggested Risk: {rec.suggested_supplier_risk}</span>
              </div>
            </div>

            <p className="text-xs text-muted-foreground">
              {rec.reason_for_recommendation}
            </p>

            {rec.recommended_suppliers.length > 0 && (
              <div className="bg-emerald-500/10 border border-emerald-500/20 rounded p-2 text-xs">
                <span className="font-semibold text-emerald-400 flex items-center gap-1 mb-1">
                  <CheckCircle className="h-3 w-3" /> Recommended Supplier
                </span>
                {rec.recommended_suppliers.map(s => (
                  <div key={s.supplier_id} className="flex justify-between ml-4">
                    <span>{s.supplier_name}</span>
                    <span className="text-muted-foreground">{s.country}</span>
                  </div>
                ))}
              </div>
            )}

            {rec.diversification_suggestions.length > 0 && (
              <div className="bg-blue-500/10 border border-blue-500/20 rounded p-2 text-xs">
                <span className="font-semibold text-blue-400 flex items-center gap-1 mb-1">
                  <ShieldAlert className="h-3 w-3" /> Diversification
                </span>
                <ul className="list-disc list-inside ml-2 text-muted-foreground">
                  {rec.diversification_suggestions.map((sug, i) => (
                    <li key={i}>{sug}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
