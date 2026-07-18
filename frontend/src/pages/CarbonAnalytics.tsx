import { useCarbonWebSocket } from '../hooks/useCarbonWebSocket';
import { SummaryCards } from '../components/carbon/SummaryCards';
import { CarbonHistory } from '../components/carbon/CarbonHistory';
import { DieselComparison } from '../components/carbon/DieselComparison';
import { ReadinessCard } from '../components/carbon/ReadinessCard';
import { ProcurementCard } from '../components/carbon/ProcurementCard';

export default function CarbonAnalytics() {
  const { latestReport, connectionStatus } = useCarbonWebSocket();

  return (
    <div className="space-y-6 animate-fade-in pb-12">
      <div className="flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight">Sustainability & Carbon Intelligence</h1>
          <p className="text-muted-foreground mt-1">Real-time emissions tracking, electrification readiness, and automated fleet procurement.</p>
        </div>
        <div className="flex items-center gap-2 text-xs">
          <span className="text-muted-foreground">Live Stream:</span>
          <span className={`px-2 py-1 rounded-full font-bold ${
            connectionStatus === 'connected' ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' :
            connectionStatus === 'connecting' ? 'bg-amber-500/10 text-amber-400 border border-amber-500/20' :
            'bg-red-500/10 text-red-400 border border-red-500/20'
          }`}>
            {connectionStatus.toUpperCase()}
          </span>
        </div>
      </div>

      {/* Top Summary Cards (Dynamic) */}
      <SummaryCards latestReport={latestReport} />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Left Column */}
        <div className="space-y-6">
          <CarbonHistory latestReport={latestReport} />
          <ReadinessCard />
        </div>

        {/* Right Column */}
        <div className="space-y-6">
          <DieselComparison />
          <ProcurementCard />
        </div>
      </div>
    </div>
  );
}
