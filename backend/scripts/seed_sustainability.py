import os
import sys
import asyncio
from datetime import datetime, date, timedelta
from unittest.mock import patch
import logging

# Ensure the backend directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.session import AsyncSessionLocal
from app.services.sustainability import CarbonService, ReadinessService, ProcurementService
from app.schemas.sustainability import (
    CarbonCalculationRequest,
    ReadinessAssessmentRequest,
    ProcurementRecommendationRequest
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

async def seed_carbon_history(session):
    """Generates 14 days of carbon history across different vehicles."""
    logger.info("Seeding Carbon History...")
    service = CarbonService(session)
    
    vehicles = ["EV-HD-001", "EV-HD-002", "EV-HD-003", "TRK-105", "VAN-302"]
    today = date.today()
    
    reports_generated = 0
    for v_id in vehicles:
        for days_ago in range(14, 0, -1):
            target_date = today - timedelta(days=days_ago)
            target_dt = datetime.combine(target_date, datetime.min.time())
            
            req = CarbonCalculationRequest(
                vehicle_id=v_id,
                start_date=target_date,
                end_date=target_date + timedelta(days=1),
                grid_region="india"
            )
            
            # Patch datetime in the sustainability service so generated_at matches target_date
            # The service imports datetime directly, so we patch app.services.sustainability.datetime
            with patch('app.services.sustainability.datetime') as mock_datetime:
                mock_datetime.utcnow.return_value = target_dt
                mock_datetime.combine.side_effect = datetime.combine
                mock_datetime.min.time = datetime.min.time
                mock_datetime.max.time = datetime.max.time
                
                report = await service.calculate_carbon(req)
            
            reports_generated += 1
            
    logger.info(f"Successfully generated {reports_generated} historical carbon reports.")

async def seed_readiness_assessments(session):
    """Generates diverse readiness assessments."""
    logger.info("Seeding Readiness Assessments...")
    service = ReadinessService(session)
    
    scenarios = [
        # Urban delivery - highly ready
        ReadinessAssessmentRequest(
            vehicle_id="URBAN-RT-1",
            route_distance=80,
            payload=1500,
            dwell_time=12,
            charging_availability=True,
            vehicle_type="delivery_van"
        ),
        # Regional logistics - ready
        ReadinessAssessmentRequest(
            vehicle_id="REG-RT-2",
            route_distance=180,
            payload=5000,
            dwell_time=8,
            charging_availability=True,
            vehicle_type="medium_truck"
        ),
        # Long-haul - not ready
        ReadinessAssessmentRequest(
            vehicle_id="LONG-RT-3",
            route_distance=600,
            payload=20000,
            dwell_time=4,
            charging_availability=False,
            vehicle_type="heavy_truck"
        ),
        # Heavy Payload but short distance - partially ready
        ReadinessAssessmentRequest(
            vehicle_id="IND-RT-4",
            route_distance=50,
            payload=30000,
            dwell_time=6,
            charging_availability=True,
            vehicle_type="heavy_truck"
        )
    ]
    
    for req in scenarios:
        await service.assess_readiness(req)
        
    logger.info(f"Successfully generated {len(scenarios)} readiness assessments.")

async def run_procurement_tests(session):
    """Runs recommendations through the service to verify the ML logic."""
    logger.info("Running Procurement Recommendation ML Logic...")
    service = ProcurementService(session)
    
    scenarios = [
        ProcurementRecommendationRequest(fleet_size=100, daily_distance=80, charging_available=True),
        ProcurementRecommendationRequest(fleet_size=50, daily_distance=150, charging_available=True),
        ProcurementRecommendationRequest(fleet_size=200, daily_distance=400, charging_available=False),
    ]
    
    for req in scenarios:
        res = await service.generate_recommendation(req)
        logger.info(f"Procurement for {req.fleet_size} vehicles at {req.daily_distance}km/day:")
        logger.info(f" -> {res.recommendation_level}: Buy {res.recommended_quantity} {res.recommended_vehicle_type} (Saves {res.estimated_carbon_saving} Tons CO2)")

async def main():
    logger.info("Starting Sustainability Domain Seeder...")
    
    async with AsyncSessionLocal() as session:
        # We append to the DB rather than clearing.
        await seed_carbon_history(session)
        await seed_readiness_assessments(session)
        await run_procurement_tests(session)
        
    logger.info("Sustainability data seeding complete.")

if __name__ == "__main__":
    if sys.platform.lower() == "win32" or os.name.lower() == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
