import logging
from datetime import date
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db_session

from app.schemas.sustainability import (
    APIResponse, CarbonCalculationRequest, CarbonReportResponse,
    DieselVsEVRequest, DieselVsEVResponse,
    ReadinessAssessmentRequest, ReadinessAssessmentResponse,
    ProcurementRecommendationRequest, ProcurementRecommendationResponse,
    SustainabilitySummaryResponse
)
from app.services.sustainability import CarbonService, ReadinessService, ProcurementService

logger = logging.getLogger(__name__)
router = APIRouter()

# 1. CARBON EMISSION ENDPOINTS

@router.post("/carbon/calculate", response_model=APIResponse[CarbonReportResponse], status_code=status.HTTP_201_CREATED)
async def calculate_carbon_emissions(
    payload: CarbonCalculationRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Calculates carbon footprint stats for a vehicle or fleet over a query timeframe."""
    try:
        service = CarbonService(session)
        result = await service.calculate_carbon(payload)
        return APIResponse(
            success=True,
            message="Carbon Report Generated",
            data=result
        )
    except Exception as e:
        logger.error(f"Carbon calculation failure: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to run carbon analysis engine."
        )

@router.get("/carbon/report/{report_id}", response_model=APIResponse[CarbonReportResponse])
async def get_carbon_report(
    report_id: str,
    session: AsyncSession = Depends(get_db_session)
):
    """Retrieves a previously generated carbon report record."""
    service = CarbonService(session)
    result = await service.get_carbon_report(report_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Carbon report with ID {report_id} not found."
        )
    return APIResponse(
        success=True,
        message="Carbon Report",
        data=result
    )

@router.post("/diesel-vs-ev", response_model=APIResponse[DieselVsEVResponse])
async def compare_diesel_vs_ev(
    payload: DieselVsEVRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Compares emissions and savings between diesel and electric options."""
    try:
        service = CarbonService(session)
        result = await service.compare_diesel_vs_ev(payload)
        return APIResponse(
            success=True,
            message="Comparison Generated",
            data=result
        )
    except Exception as e:
        logger.error(f"Comparison execution failure: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to perform EV vs Diesel emissions comparison."
        )

# 2. ELECTRIFICATION READINESS ENDPOINTS

@router.post("/readiness-assessment", response_model=APIResponse[ReadinessAssessmentResponse])
async def evaluate_readiness(
    payload: ReadinessAssessmentRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Assesses route electrification feasibility scores."""
    try:
        service = ReadinessService(session)
        result = await service.assess_readiness(payload)
        return APIResponse(
            success=True,
            message="Assessment Completed",
            data=result
        )
    except Exception as e:
        logger.error(f"Readiness assessment failure: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to calculate fleet electrification readiness."
        )

@router.get("/readiness/{assessment_id}", response_model=APIResponse[ReadinessAssessmentResponse])
async def get_readiness_assessment(
    assessment_id: str,
    session: AsyncSession = Depends(get_db_session)
):
    """Retrieves dynamic details for a route readiness assessment."""
    service = ReadinessService(session)
    result = await service.get_readiness_assessment(assessment_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Readiness assessment with ID {assessment_id} not found."
        )
    return APIResponse(
        success=True,
        message="Readiness Assessment",
        data=result
    )

# 3. PROCUREMENT ENDPOINTS

@router.post("/procurement-recommendation", response_model=APIResponse[ProcurementRecommendationResponse])
async def generate_procurement_recommendation(
    payload: ProcurementRecommendationRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Recommends EV vehicle purchases and quantity counts for fleet migration transitions."""
    try:
        service = ProcurementService(session)
        result = await service.generate_recommendation(payload)
        return APIResponse(
            success=True,
            message="Procurement Recommendation",
            data=result
        )
    except Exception as e:
        logger.error(f"Procurement recommender failure: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to formulate EV procurement recommendation."
        )

# 4. KPI & HISTORY ENDPOINTS

@router.get("/summary", response_model=APIResponse[SustainabilitySummaryResponse])
async def get_dashboard_sustainability_summary(
    session: AsyncSession = Depends(get_db_session)
):
    """Calculates overall sustainability KPI summaries for the main dashboard."""
    try:
        service = CarbonService(session)
        result = await service.get_sustainability_summary()
        return APIResponse(
            success=True,
            message="Sustainability Summary",
            data=result
        )
    except Exception as e:
        logger.error(f"Summary fetch failure: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to compile sustainability summary statistics."
        )

@router.get("/history", response_model=APIResponse[List[CarbonReportResponse]])
async def get_sustainability_history(
    vehicle_id: Optional[str] = Query(None, description="Filters reports by vehicle ID"),
    fleet_id: Optional[str] = Query(None, description="Filters reports by fleet ID"),
    start_date: Optional[date] = Query(None, description="Filters reports generated after start date"),
    end_date: Optional[date] = Query(None, description="Filters reports generated before end date"),
    page: int = Query(1, ge=1, description="Page number for pagination"),
    limit: int = Query(20, ge=1, le=100, description="Page size limit"),
    session: AsyncSession = Depends(get_db_session)
):
    """Fetches paginated historical carbon logs."""
    try:
        service = CarbonService(session)
        result = await service.get_history(
            vehicle_id=vehicle_id,
            fleet_id=fleet_id,
            start_date=start_date,
            end_date=end_date,
            page=page,
            limit=limit
        )
        return APIResponse(
            success=True,
            message="Historical Carbon Reports Retrieved",
            data=result
        )
    except Exception as e:
        logger.error(f"History query failure: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to query historical carbon reports."
        )
