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

async def test_material_flow_global():
    async with get_client() as client:
        res = await client.get(f"{BASE_URL}/material-flow")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        assert "summary" in data
        assert "graph" in data
        assert len(data["summary"]) > 0
        assert len(data["graph"]["nodes"]) > 0
        print("PASS: test_material_flow_global")

async def test_material_flow_filtered():
    async with get_client() as client:
        res = await client.get(f"{BASE_URL}/material-flow?material_id=MAT-001")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        assert "summary" in data
        assert "graph" in data
        mat_ids = [s["material_id"] for s in data["summary"]]
        assert "MAT-001" in mat_ids
        print("PASS: test_material_flow_filtered")

async def test_traceability_global():
    async with get_client() as client:
        res = await client.get(f"{BASE_URL}/traceability")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        assert "upstream_lineage" in data
        assert "downstream_usage" in data
        assert "complete_manufacturing_chain" in data
        assert "graph" in data
        assert len(data["complete_manufacturing_chain"]) > 0
        print("PASS: test_traceability_global")

async def test_traceability_filtered():
    async with get_client() as client:
        res = await client.get(f"{BASE_URL}/traceability?entity_id=SUP-001")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        assert data["target_id"] == "SUP-001"
        assert len(data["complete_manufacturing_chain"]) > 0
        print("PASS: test_traceability_filtered (SUP-001)")

        res_veh = await client.get(f"{BASE_URL}/traceability?entity_id=VEH-001")
        assert res_veh.status_code == 200
        assert res_veh.json()["target_id"] == "VEH-001"
        print("PASS: test_traceability_filtered (VEH-001)")

async def main():
    print("Executing Phase 6 Material Flow & Traceability API Tests...")
    try:
        await neo4j_client.connect()
        await test_material_flow_global()
        await test_material_flow_filtered()
        await test_traceability_global()
        await test_traceability_filtered()
        print("ALL PHASE 6 TESTS PASSED SUCCESSFULLY!")
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
