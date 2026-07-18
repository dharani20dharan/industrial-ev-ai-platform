import React, { useEffect, useState } from 'react';
import NetworkGraph from '../components/supply-chain/NetworkGraph';
import RiskDashboard from '../components/supply-chain/RiskDashboard';
import ProcurementRecommendations from '../components/supply-chain/ProcurementRecommendations';

export default function SupplyChain() {
  const [overview, setOverview] = useState<any>(null);

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

  return (
    <div className="space-y-6 animate-fade-in">
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
