from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1.api import api_router
import os

app = FastAPI(
    title="Industrial EV Supply Chain & Asset Intelligence API",
    description="FastAPI backend hosting real-time telemetry pipelines, battery degradation predictors, and Neo4j graph queries.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "*"  # Allow all for development & testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root-level health API redirect/check
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Industrial EV AI Platform API. Access Swagger docs at /docs",
        "status": "online"
    }

# Include API endpoints
app.include_router(api_router, prefix="/api/v1")
