from fastapi import APIRouter
from .endpoints import health, telemetry, ml_inference, supply_chain, sustainability, simulator

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(telemetry.router, tags=["telemetry"])
api_router.include_router(ml_inference.router, tags=["ml_inference"])
api_router.include_router(supply_chain.router, prefix="/supply-chain", tags=["supply_chain"])
api_router.include_router(sustainability.router, prefix="/sustainability", tags=["sustainability"])
api_router.include_router(simulator.router, tags=["simulator"])


