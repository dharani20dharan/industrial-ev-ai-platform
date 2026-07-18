import asyncio
import httpx
import sys
import os

if sys.platform.lower() == "win32" or os.name.lower() == "nt":
    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app
from app.core.neo4j import neo4j_client

BASE_URL = "http://testserver/api/v1/supply-chain"

def get_client():
    return httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://testserver")

async def test_trace_vehicle_success():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/vehicle/VEH-001")
        assert response.status_code == 200
        data = response.json()
        assert data["vehicle_id"] == "VEH-001"
        assert len(data["nodes"]) > 0
        assert len(data["edges"]) > 0
        print("PASS: test_trace_vehicle_success")

async def test_trace_vehicle_not_found():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/vehicle/VEH-999")
        assert response.status_code == 404
        print("PASS: test_trace_vehicle_not_found")

async def test_trace_supplier_success():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/supplier/SUP-001")
        assert response.status_code == 200
        data = response.json()
        assert data["supplier_id"] == "SUP-001"
        assert len(data["nodes"]) > 0
        print("PASS: test_trace_supplier_success")

async def test_trace_supplier_not_found():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/supplier/SUP-999")
        assert response.status_code == 404
        print("PASS: test_trace_supplier_not_found")

async def test_trace_material_success():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/material/MAT-001")
        assert response.status_code == 200
        data = response.json()
        assert data["material_id"] == "MAT-001"
        assert len(data["nodes"]) > 0
        print("PASS: test_trace_material_success")

async def test_trace_fleet_success():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/fleet/FLT-001")
        assert response.status_code == 200
        data = response.json()
        assert data["fleet_id"] == "FLT-001"
        assert len(data["nodes"]) > 0
        print("PASS: test_trace_fleet_success")

async def test_get_stats():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/stats")
        assert response.status_code == 200
        data = response.json()
        assert data["node_count"] > 0
        assert data["relationship_count"] > 0
        assert "Supplier" in data["entities_by_type"]
        print("PASS: test_get_stats")

async def test_analyze_supplier_risk():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/risk/supplier/SUP-001")
        assert response.status_code == 200
        data = response.json()
        assert "risk" in data
        assert data["risk"]["score"] > 0
        assert data["downstream_impact_count"] > 0
        print("PASS: test_analyze_supplier_risk")

async def test_analyze_supplier_impact():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/impact/supplier/SUP-001")
        assert response.status_code == 200
        data = response.json()
        assert data["total_downstream_entities"] > 0
        assert data["impacted_battery_cells"] >= 0
        print("PASS: test_analyze_supplier_impact")

async def test_find_material_alternatives():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/alternatives/material/MAT-001")
        assert response.status_code == 200
        data = response.json()
        assert data["target_id"] == "MAT-001"
        assert len(data["alternative_suppliers"]) > 0
        print("PASS: test_find_material_alternatives")

async def test_find_supplier_alternatives():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/alternatives/supplier/SUP-001")
        assert response.status_code == 200
        data = response.json()
        assert data["target_id"] == "SUP-001"
        assert len(data["alternative_suppliers"]) >= 0
        print("PASS: test_find_supplier_alternatives")

async def test_analyze_material_impact():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/impact/material/MAT-001")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        data = response.json()
        assert data["entity_type"] == "Material"
        assert data["total_downstream_entities"] >= 0
        print("PASS: test_analyze_material_impact")

async def test_analyze_refinery_impact():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/impact/refinery/REF-001")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        data = response.json()
        assert data["entity_type"] == "Refinery"
        assert data["total_downstream_entities"] >= 0
        print("PASS: test_analyze_refinery_impact")

async def test_get_analytics_dependencies():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/analytics/dependencies")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        data = response.json()
        assert "critical_bottlenecks" in data
        assert "global_dependency_depth" in data
        print("PASS: test_get_analytics_dependencies")

async def test_dashboard_overview():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/dashboard/overview")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        data = response.json()
        assert "total_suppliers" in data
        assert "high_risk_suppliers_count" in data
        print("PASS: test_dashboard_overview")

async def test_dashboard_network():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/dashboard/network")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        data = response.json()
        assert "elements" in data
        assert "nodes" in data["elements"]
        assert "edges" in data["elements"]
        print("PASS: test_dashboard_network")

async def test_dashboard_recommendations():
    async with get_client() as client:
        response = await client.get(f"{BASE_URL}/dashboard/recommendations")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        data = response.json()
        assert "recommendations" in data
        assert isinstance(data["recommendations"], list)
        print("PASS: test_dashboard_recommendations")

async def main():
    print("Running Supply Chain API Tests...")
    try:
        await neo4j_client.connect()
        await test_trace_vehicle_success()
        await test_trace_vehicle_not_found()
        await test_trace_supplier_success()
        await test_trace_supplier_not_found()
        await test_trace_material_success()
        await test_trace_fleet_success()
        await test_get_stats()
        
        # Phase 3 Tests
        await test_analyze_supplier_risk()
        await test_analyze_supplier_impact()
        await test_find_material_alternatives()
        await test_find_supplier_alternatives()
        await test_analyze_material_impact()
        await test_analyze_refinery_impact()
        await test_get_analytics_dependencies()
        
        # Phase 4 Tests
        await test_dashboard_overview()
        await test_dashboard_network()
        await test_dashboard_recommendations()
        
        print("ALL TESTS PASSED!")
    except AssertionError as e:
        import traceback
        traceback.print_exc()
        print(f"TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"ERROR: {e}")
        sys.exit(1)
    finally:
        await neo4j_client.close()

if __name__ == "__main__":
    asyncio.run(main())
