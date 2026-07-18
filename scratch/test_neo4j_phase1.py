import asyncio
import sys
import os
import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

from app.core.neo4j import neo4j_client
from app.repositories.supply_chain import SupplyChainRepository

async def main():
    print("\n--- Test 1: Neo4j Driver Connection & Cypher Tests ---")
    try:
        await neo4j_client.connect()
        driver = neo4j_client.driver
        if not driver:
            print("Failed to initialize driver.")
            return

        async with driver.session() as session:
            repo = SupplyChainRepository(session)
            
            # Query Test
            print("\n>> Query Test: MATCH (n) RETURN COUNT(n)")
            result = await repo.execute_query("MATCH (n) RETURN COUNT(n) as count")
            print(f"PASS - Node count: {result[0]['count']}")
            
            # Node Lookup
            print("\n>> Node Lookup: MATCH (s:Supplier) RETURN s.name as name")
            result = await repo.execute_query("MATCH (s:Supplier) RETURN s.name as name")
            print(f"PASS - Suppliers found: {[r['name'] for r in result]}")
            
            # Traversal
            print("\n>> Relationship Traversal: MATCH (s:Supplier)-[:SUPPLIES]->(m:Mine) RETURN s.name, m.name")
            result = await repo.execute_query("MATCH (s:Supplier)-[:SUPPLIES]->(m:Mine) RETURN s.name as supplier, m.name as mine")
            print("PASS - Relationships found:")
            for r in result:
                print(f"  {r['supplier']} -> {r['mine']}")
                
    except Exception as e:
        print(f"FAIL - {e}")
    finally:
        await neo4j_client.close()


    print("\n--- Test 2: HTTP Health Endpoint ---")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:8000/health/neo4j")
            print(f"HTTP Status: {response.status_code}")
            if response.status_code == 200:
                print(f"PASS - Payload: {response.json()}")
            else:
                print("FAIL - Endpoint returned non-200")
    except Exception as e:
        print(f"FAIL - HTTP request failed (is uvicorn running?): {e}")

if __name__ == "__main__":
    asyncio.run(main())
