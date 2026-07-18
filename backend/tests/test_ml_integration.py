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

async def test_get_supply_chain_ml_risk():
    async with get_client() as client:
        res = await client.get(f"{BASE_URL}/risk")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        assert "global_risk_index" in data
        assert "risk_level" in data
        assert "confidence" in data
        assert data["confidence"] == 95.0
        assert "total_suppliers_assessed" in data
        assert data["total_suppliers_assessed"] > 0
        assert "critical_vulnerability" in data
        assert "mitigation_plan" in data
        assert "suppliers" in data
        assert len(data["suppliers"]) > 0
        
        first_supplier = data["suppliers"][0]
        assert "supplier_id" in first_supplier
        assert "risk_score" in first_supplier
        assert "risk_level" in first_supplier
        assert "confidence" in first_supplier
        print("PASS: test_get_supply_chain_ml_risk")

async def test_get_critical_suppliers():
    async with get_client() as client:
        res = await client.get(f"{BASE_URL}/critical-suppliers")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        assert "total_critical_count" in data
        assert "critical_suppliers" in data
        assert "recommendations" in data
        assert data["total_critical_count"] == len(data["critical_suppliers"])
        print("PASS: test_get_critical_suppliers")

async def main():
    print("Executing Deliverable 7 ML Integration API Tests...")
    try:
        await neo4j_client.connect()
        await test_get_supply_chain_ml_risk()
        await test_get_critical_suppliers()
        print("ALL DELIVERABLE 7 TESTS PASSED SUCCESSFULLY!")
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
