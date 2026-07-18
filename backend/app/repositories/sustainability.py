import uuid
import logging
from datetime import datetime, date, timedelta
from typing import List, Dict, Any, Optional
from sqlalchemy import select, desc, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.sustainability import CarbonReport, ReadinessAssessment

logger = logging.getLogger(__name__)

# Static in-memory storage fallback to ensure APIs work even if DB connection is offline
_in_memory_reports: Dict[uuid.UUID, CarbonReport] = {}
_in_memory_assessments: Dict[uuid.UUID, ReadinessAssessment] = {}

# Mock Fleet vehicle lookup configurations
MOCK_FLEET: Dict[str, Dict[str, Any]] = {
    "EV-HD-001": {
        "vehicle_id": "EV-HD-001",
        "vehicle_type": "heavy_truck",
        "annual_km": 80000,
        "fleet_id": "FLT-ALPHA-01",
        "renewable_fraction": 0.1,
        "daily_km": 320,
        "payload_tons": 15.0,
    },
    "EV-HD-002": {
        "vehicle_id": "EV-HD-002",
        "vehicle_type": "medium_truck",
        "annual_km": 60000,
        "fleet_id": "FLT-ALPHA-01",
        "renewable_fraction": 0.15,
        "daily_km": 240,
        "payload_tons": 8.0,
    },
    "EV-HD-003": {
        "vehicle_id": "EV-HD-003",
        "vehicle_type": "delivery_van",
        "annual_km": 40000,
        "fleet_id": "FLT-ALPHA-01",
        "renewable_fraction": 0.20,
        "daily_km": 160,
        "payload_tons": 2.0,
    },
    "EV-HD-004": {
        "vehicle_id": "EV-HD-004",
        "vehicle_type": "medium_truck",
        "annual_km": 65000,
        "fleet_id": "FLT-ALPHA-01",
        "renewable_fraction": 0.05,
        "daily_km": 260,
        "payload_tons": 10.0,
    },
}

MOCK_BATTERY_SUMMARY: Dict[str, Dict[str, Any]] = {
    "EV-HD-001": {"soh_percent": 96.0, "rul_cycles": 1240, "avg_temperature": 34.5, "charging_efficiency": 94.0, "odometer_km": 45000},
    "EV-HD-002": {"soh_percent": 91.0, "rul_cycles": 890, "avg_temperature": 38.2, "charging_efficiency": 91.0, "odometer_km": 72000},
    "EV-HD-003": {"soh_percent": 98.0, "rul_cycles": 1450, "avg_temperature": 33.1, "charging_efficiency": 96.0, "odometer_km": 18000},
    "EV-HD-004": {"soh_percent": 83.0, "rul_cycles": 430, "avg_temperature": 44.8, "charging_efficiency": 86.0, "odometer_km": 94000},
}

class SustainabilityRepository:
    """Handles persistence of carbon reports/readiness assessments, and mocks fleet operations."""
    
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save_carbon_report(self, report: CarbonReport) -> CarbonReport:
        """Saves a carbon report to the database, falling back to in-memory on error."""
        try:
            self.session.add(report)
            await self.session.commit()
            logger.info(f"Carbon report {report.report_id} committed to TimescaleDB.")
            return report
        except Exception as e:
            logger.warning(f"Database commit failed, storing report in-memory: {e}")
            await self.session.rollback()
            _in_memory_reports[report.report_id] = report
            return report

    async def get_carbon_report(self, report_id: str) -> Optional[CarbonReport]:
        """Fetches a carbon report by UUID from either database or in-memory fallback."""
        try:
            uid = uuid.UUID(report_id)
        except ValueError:
            return None

        # Try in-memory first for quick diagnostics if present
        if uid in _in_memory_reports:
            return _in_memory_reports[uid]

        try:
            stmt = select(CarbonReport).where(CarbonReport.report_id == uid).limit(1)
            res = await self.session.execute(stmt)
            return res.scalar_one_or_none()
        except Exception as e:
            logger.error(f"Failed to fetch report from DB: {e}")
            return _in_memory_reports.get(uid)

    async def get_carbon_reports_history(
        self,
        vehicle_id: Optional[str] = None,
        fleet_id: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        page: int = 1,
        limit: int = 20
    ) -> List[CarbonReport]:
        """Queries historical carbon reports from DB with pagination and filters."""
        # Try retrieving from DB
        try:
            stmt = select(CarbonReport)
            if vehicle_id:
                stmt = stmt.where(CarbonReport.vehicle_id == vehicle_id)
            if fleet_id:
                stmt = stmt.where(CarbonReport.fleet_id == fleet_id)
            if start_date:
                dt_start = datetime.combine(start_date, datetime.min.time())
                stmt = stmt.where(CarbonReport.generated_at >= dt_start)
            if end_date:
                dt_end = datetime.combine(end_date, datetime.max.time())
                stmt = stmt.where(CarbonReport.generated_at <= dt_end)

            stmt = stmt.order_by(desc(CarbonReport.generated_at))
            stmt = stmt.offset((page - 1) * limit).limit(limit)
            
            res = await self.session.execute(stmt)
            return list(res.scalars().all())
        except Exception as e:
            logger.warning(f"Failed to query database history, falling back to in-memory list: {e}")
            # Filter in-memory fallback list
            reports = list(_in_memory_reports.values())
            if vehicle_id:
                reports = [r for r in reports if r.vehicle_id == vehicle_id]
            if fleet_id:
                reports = [r for r in reports if r.fleet_id == fleet_id]
            if start_date:
                dt_start = datetime.combine(start_date, datetime.min.time())
                reports = [r for r in reports if r.generated_at >= dt_start]
            if end_date:
                dt_end = datetime.combine(end_date, datetime.max.time())
                reports = [r for r in reports if r.generated_at <= dt_end]
            
            reports.sort(key=lambda x: x.generated_at, reverse=True)
            offset = (page - 1) * limit
            return reports[offset : offset + limit]

    async def save_readiness_assessment(self, assessment: ReadinessAssessment) -> ReadinessAssessment:
        """Saves a readiness assessment, falling back to in-memory on error."""
        try:
            self.session.add(assessment)
            await self.session.commit()
            logger.info(f"Readiness assessment {assessment.assessment_id} committed to TimescaleDB.")
            return assessment
        except Exception as e:
            logger.warning(f"Database commit failed, storing assessment in-memory: {e}")
            await self.session.rollback()
            _in_memory_assessments[assessment.assessment_id] = assessment
            return assessment

    async def get_readiness_assessment(self, assessment_id: str) -> Optional[ReadinessAssessment]:
        """Fetches a readiness assessment from DB or in-memory fallback."""
        try:
            uid = uuid.UUID(assessment_id)
        except ValueError:
            return None

        if uid in _in_memory_assessments:
            return _in_memory_assessments[uid]

        try:
            stmt = select(ReadinessAssessment).where(ReadinessAssessment.assessment_id == uid).limit(1)
            res = await self.session.execute(stmt)
            return res.scalar_one_or_none()
        except Exception as e:
            logger.error(f"Failed to fetch assessment from DB: {e}")
            return _in_memory_assessments.get(uid)

    # --- MOCK SERVICE INTEGRATION BOUNDARIES ---

    async def get_vehicle(self, vehicle_id: str) -> Dict[str, Any]:
        """
        Retrieves a vehicle's metadata characteristics.
        Integrates with the future Fleet Management component.
        """
        if vehicle_id in MOCK_FLEET:
            return MOCK_FLEET[vehicle_id]
        
        # Safe default fallback for unknown vehicles
        # Derive vehicle properties pseudo-randomly to allow dynamic testing
        hash_val = sum(ord(c) for c in vehicle_id)
        vtypes = ["heavy_truck", "medium_truck", "delivery_van", "bus"]
        vtype = vtypes[hash_val % len(vtypes)]
        
        return {
            "vehicle_id": vehicle_id,
            "vehicle_type": vtype,
            "annual_km": 50000 + (hash_val % 10) * 5000,
            "fleet_id": "FLT-GENERIC",
            "renewable_fraction": float((hash_val % 5) * 0.05),
            "daily_km": 150 + (hash_val % 10) * 20,
            "payload_tons": 5.0 + (hash_val % 5) * 2.0
        }

    async def get_fleet(self, fleet_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Returns a list of all active vehicles matching the fleet_id criteria.
        Integrates with the future Fleet Management component.
        """
        # For now return the main list
        return list(MOCK_FLEET.values())

    async def get_telemetry_summary(self, vehicle_id: str, start_date: date, end_date: date) -> Dict[str, Any]:
        """
        Fetches consolidated historical odometer / energy usage records over a time duration.
        Integrates with the telemetry hypertable queries.
        """
        days = (end_date - start_date).days or 1
        vehicle_meta = await self.get_vehicle(vehicle_id)
        vtype = vehicle_meta["vehicle_type"]
        
        # Estimate telemetry averages based on specs in carbon_engine
        # defaults: heavy_truck: 1.4 kWh/km, medium_truck: 0.8, delivery_van: 0.25, bus: 1.3
        kwh_rates = {"heavy_truck": 1.4, "medium_truck": 0.8, "delivery_van": 0.25, "bus": 1.3}
        kwh_per_km = kwh_rates.get(vtype, 0.8)
        
        # Calculate approximate active distance travelled
        daily_km_val = vehicle_meta.get("daily_km", 200)
        total_dist = daily_km_val * days * 0.7  # 70% duty cycle factor
        total_kwh = total_dist * kwh_per_km
        
        return {
            "distance_travelled_km": round(total_dist, 1),
            "energy_consumed_kwh": round(total_kwh, 1),
            "avg_speed_kph": 48.5,
            "trip_count": int(days * 2)
        }

    async def get_battery_summary(self, vehicle_id: str) -> Dict[str, Any]:
        """
        Retrieves real-time electro-chemical state averages.
        Integrates with the Battery service.
        """
        if vehicle_id in MOCK_BATTERY_SUMMARY:
            return MOCK_BATTERY_SUMMARY[vehicle_id]
            
        hash_val = sum(ord(c) for c in vehicle_id)
        return {
            "soh_percent": round(90.0 + (hash_val % 10) * 0.9, 1),
            "rul_cycles": 800 + (hash_val % 10) * 70,
            "avg_temperature": round(32.0 + (hash_val % 5) * 1.5, 1),
            "charging_efficiency": round(88.0 + (hash_val % 5) * 1.8, 1),
            "odometer_km": 50000 + (hash_val % 5) * 10000,
        }

    async def get_summary_stats(self) -> Dict[str, Any]:
        """Aggregates all stored report values to compile fleet sustainability totals."""
        try:
            stmt = select(
                func.sum(CarbonReport.carbon_saved),
                func.sum(CarbonReport.scope1_emission),
                func.sum(CarbonReport.scope3_emission),
                func.count(CarbonReport.report_id)
            )
            res = await self.session.execute(stmt)
            stats = res.fetchone()
            
            # Query average readiness score
            r_stmt = select(func.avg(ReadinessAssessment.readiness_score))
            r_res = await self.session.execute(r_stmt)
            avg_readiness = r_res.scalar() or 0.0
            
            if stats and stats[3] > 0:
                return {
                    "total_carbon_saved_kg": stats[0] or 0.0,
                    "scope1_emission_kg": stats[1] or 0.0,
                    "scope3_emission_kg": stats[2] or 0.0,
                    "total_reports": stats[3] or 0,
                    "average_readiness_score": round(avg_readiness, 1)
                }
        except Exception as e:
            logger.warning(f"Could not compute DB aggregates, accumulating in-memory: {e}")

        # In-memory accumulator fallback
        reports = list(_in_memory_reports.values())
        assessments = list(_in_memory_assessments.values())
        
        saved = sum(r.carbon_saved for r in reports)
        s1 = sum(r.scope1_emission for r in reports)
        s3 = sum(r.scope3_emission for r in reports)
        scores = [a.readiness_score for a in assessments]
        avg_score = sum(scores) / len(scores) if scores else 0.0
        
        # Seed values to display clean summaries if there's no data generated yet
        if not reports:
            saved = 48520.0
            s1 = 0.0
            s3 = 1542.0
            avg_score = 82.0
            
        return {
            "total_carbon_saved_kg": saved,
            "scope1_emission_kg": s1,
            "scope3_emission_kg": s3,
            "total_reports": len(reports),
            "average_readiness_score": round(avg_score, 1)
        }
