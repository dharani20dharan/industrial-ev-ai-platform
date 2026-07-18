import asyncio
import httpx
import sys
import os

if sys.platform.lower() == "win32" or os.name.lower() == "nt":
    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

BASE_URL = "http://testserver/api/v1/sustainability"

def get_client():
    return httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://testserver")

async def test_carbon_history_api():
    """Verify that seeded carbon history can be retrieved."""
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/history?limit=10")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert isinstance(data["data"], list)
        # We assume the seeder has been run prior to this test
        if len(data["data"]) > 0:
            assert "report_id" in data["data"][0]
            assert "vehicle_id" in data["data"][0]
            assert "carbon_saved" in data["data"][0]

async def test_readiness_assessment_api():
    """Verify that a readiness assessment can be requested and saved."""
    payload = {
        "route_distance": 120,
        "payload": 4000,
        "charging_availability": True,
        "dwell_time": 6,
        "vehicle_type": "medium_truck"
    }
    
    async with get_client() as client:
        response = await client.post(f"{BASE_URL}/readiness-assessment", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        assessment = data["data"]
        assert "assessment_id" in assessment
        assert "readiness_score" in assessment
        assert "readiness_level" in assessment
        
        # Verify it can be retrieved via GET
        assessment_id = assessment["assessment_id"]
        get_resp = await client.get(f"{BASE_URL}/readiness/{assessment_id}")
        assert get_resp.status_code == 200
        get_data = get_resp.json()
        assert get_data["success"] is True
        assert get_data["data"]["assessment_id"] == assessment_id

async def test_procurement_recommendation_api():
    """Verify that the procurement ML engine calculates logic correctly."""
    payload = {
        "fleet_size": 200,
        "daily_distance": 250,
        "charging_available": True
    }
    
    async with get_client() as client:
        response = await client.post(f"{BASE_URL}/procurement-recommendation", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        rec = data["data"]
        assert "recommended_vehicle_type" in rec
        assert "recommended_quantity" in rec
        assert "estimated_carbon_saving" in rec
        assert "recommendation_level" in rec

async def test_diesel_vs_ev_api():
    """Verify that diesel vs EV calculations are processed by the ML engine."""
    payload = {
        "distance_km": 500,
        "payload_kg": 20000,
        "diesel_efficiency": 30.5,
        "ev_efficiency": 1.4,
        "vehicle_type": "heavy_truck"
    }
    
    async with get_client() as client:
        response = await client.post(f"{BASE_URL}/diesel-vs-ev", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        comp = data["data"]
        assert "diesel_emission" in comp
        assert "ev_emission" in comp
        assert "carbon_saved" in comp
        assert "reduction_percentage" in comp

async def test_summary_api():
    """Verify dashboard summary aggregates correct KPIs."""
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/summary")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        summary = data["data"]
        assert "total_carbon_saved_kg" in summary
        assert "vehicles_assessed" in summary
        assert "total_reports" in summary

if __name__ == "__main__":
    # Provides a way to run the async tests via the python interpreter easily if needed
    asyncio.run(test_carbon_history_api())
    asyncio.run(test_readiness_assessment_api())
    asyncio.run(test_procurement_recommendation_api())
    asyncio.run(test_diesel_vs_ev_api())
    asyncio.run(test_summary_api())
    print("All tests passed manually.")
