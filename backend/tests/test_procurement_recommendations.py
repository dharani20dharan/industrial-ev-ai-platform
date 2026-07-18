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

async def test_get_procurement_recommendations_global():
    async with get_client() as client:
        res = await client.get(f"{BASE_URL}/recommendations")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        assert "recommendations" in data
        assert "summary" in data
        assert isinstance(data["recommendations"], list)
        
        if len(data["recommendations"]) > 0:
            rec = data["recommendations"][0]
            assert "material" in rec
            assert "recommended_suppliers" in rec
            assert "alternative_suppliers" in rec
            assert "diversification_suggestions" in rec
            assert "reason_for_recommendation" in rec
            assert "current_supplier_risk" in rec
            assert "suggested_supplier_risk" in rec
            assert rec["current_supplier_risk"] >= rec["suggested_supplier_risk"]
        print("PASS: test_get_procurement_recommendations_global")

async def test_get_procurement_recommendations_filtered():
    async with get_client() as client:
        res = await client.get(f"{BASE_URL}/recommendations?material_id=MAT-001")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        assert "recommendations" in data
        
        if len(data["recommendations"]) > 0:
            for rec in data["recommendations"]:
                assert "lithium" in rec["material"].lower() or "mat-001" in rec["material"].lower()
        print("PASS: test_get_procurement_recommendations_filtered")

async def main():
    print("Executing Phase 8 Procurement Recommendations API Tests...")
    try:
        await neo4j_client.connect()
        await test_get_procurement_recommendations_global()
        await test_get_procurement_recommendations_filtered()
        print("ALL PHASE 8 TESTS PASSED SUCCESSFULLY!")
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
