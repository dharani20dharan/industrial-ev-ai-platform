import asyncio
import httpx
import sys
import os

# Set up event loop policy for Windows if running standalone
if sys.platform.lower() == "win32" or os.name.lower() == "nt":
    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app
from app.core.neo4j import neo4j_client

BASE_URL = "http://testserver/api/v1/supply-chain"

async def test_supplier_crud():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://testserver") as client:
        # 1. Create Supplier (201)
        new_supplier = {
            "supplier_id": "SUP-999",
            "name": "Test Supplier Corp",
            "country": "Canada",
            "risk_score": 25.0,
            "status": "ACTIVE"
        }
        res = await client.post("/api/v1/supply-chain/suppliers", json=new_supplier)
        assert res.status_code == 201, f"Expected 201, got {res.status_code}: {res.text}"
        data = res.json()
        assert data["supplier_id"] == "SUP-999"
        assert data["name"] == "Test Supplier Corp"
        print("PASS: Supplier Creation (201)")

        # 2. Duplicate Supplier Creation (409)
        res_dup = await client.post("/api/v1/supply-chain/suppliers", json=new_supplier)
        assert res_dup.status_code == 409, f"Expected 409, got {res_dup.status_code}: {res_dup.text}"
        print("PASS: Supplier Duplicate Validation (409)")

        # 3. Get Supplier (200)
        res_get = await client.get("/api/v1/supply-chain/suppliers/SUP-999")
        assert res_get.status_code == 200, f"Expected 200, got {res_get.status_code}"
        assert res_get.json()["country"] == "Canada"
        print("PASS: Get Supplier (200)")

        # 4. Get Non-existent Supplier (404)
        res_404 = await client.get("/api/v1/supply-chain/suppliers/SUP-000")
        assert res_404.status_code == 404
        print("PASS: Get Non-existent Supplier (404)")

        # 5. List Suppliers (200)
        res_list = await client.get("/api/v1/supply-chain/suppliers")
        assert res_list.status_code == 200
        ids = [s["supplier_id"] for s in res_list.json()]
        assert "SUP-999" in ids
        print("PASS: List Suppliers (200)")

        # 6. Update Supplier (200)
        update_payload = {"risk_score": 45.5, "status": "ON_HOLD"}
        res_patch = await client.patch("/api/v1/supply-chain/suppliers/SUP-999", json=update_payload)
        assert res_patch.status_code == 200
        patched_data = res_patch.json()
        assert patched_data["risk_score"] == 45.5
        assert patched_data["status"] == "ON_HOLD"
        print("PASS: Update Supplier (200)")

        # 7. Delete Supplier (200)
        res_del = await client.delete("/api/v1/supply-chain/suppliers/SUP-999")
        assert res_del.status_code == 200
        print("PASS: Delete Supplier (200)")

        # 8. Delete Non-existent Supplier (404)
        res_del_404 = await client.delete("/api/v1/supply-chain/suppliers/SUP-999")
        assert res_del_404.status_code == 404
        print("PASS: Delete Non-existent Supplier (404)")


async def test_material_crud():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://testserver") as client:
        # 1. Create Material (201)
        new_mat = {
            "material_id": "MAT-999",
            "name": "Synthetic Anode Material",
            "type": "Processed"
        }
        res = await client.post("/api/v1/supply-chain/materials", json=new_mat)
        assert res.status_code == 201, f"Expected 201, got {res.status_code}: {res.text}"
        data = res.json()
        assert data["material_id"] == "MAT-999"
        print("PASS: Material Creation (201)")

        # 2. Duplicate Material (409)
        res_dup = await client.post("/api/v1/supply-chain/materials", json=new_mat)
        assert res_dup.status_code == 409
        print("PASS: Material Duplicate Validation (409)")

        # 3. Get Material (200)
        res_get = await client.get("/api/v1/supply-chain/materials/MAT-999")
        assert res_get.status_code == 200
        assert res_get.json()["name"] == "Synthetic Anode Material"
        print("PASS: Get Material (200)")

        # 4. Patch Material (200)
        res_patch = await client.patch("/api/v1/supply-chain/materials/MAT-999", json={"name": "High Grade Anode"})
        assert res_patch.status_code == 200
        assert res_patch.json()["name"] == "High Grade Anode"
        print("PASS: Update Material (200)")

        # 5. Delete Material (200)
        res_del = await client.delete("/api/v1/supply-chain/materials/MAT-999")
        assert res_del.status_code == 200
        print("PASS: Delete Material (200)")


async def test_processing_plant_crud():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://testserver") as client:
        # 1. Create Processing Plant (201)
        new_plant = {
            "plant_id": "PLT-999",
            "name": "Nordic Battery Refinery",
            "country": "Sweden",
            "plant_type": "Refinery"
        }
        res = await client.post("/api/v1/supply-chain/processing-plants", json=new_plant)
        assert res.status_code == 201, f"Expected 201, got {res.status_code}: {res.text}"
        assert res.json()["plant_id"] == "PLT-999"
        print("PASS: Processing Plant Creation (201)")

        # 2. Get Processing Plant (200)
        res_get = await client.get("/api/v1/supply-chain/processing-plants/PLT-999")
        assert res_get.status_code == 200
        print("PASS: Get Processing Plant (200)")

        # 3. Patch Processing Plant (200)
        res_patch = await client.patch("/api/v1/supply-chain/processing-plants/PLT-999", json={"country": "Norway"})
        assert res_patch.status_code == 200
        assert res_patch.json()["country"] == "Norway"
        print("PASS: Update Processing Plant (200)")

        # 4. Delete Processing Plant (200)
        res_del = await client.delete("/api/v1/supply-chain/processing-plants/PLT-999")
        assert res_del.status_code == 200
        print("PASS: Delete Processing Plant (200)")


async def main():
    print("Executing Phase 5 Graph Management API Tests...")
    try:
        await neo4j_client.connect()
        await test_supplier_crud()
        await test_material_crud()
        await test_processing_plant_crud()
        print("ALL GRAPH MANAGEMENT TESTS PASSED SUCCESSFULLY!")
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
