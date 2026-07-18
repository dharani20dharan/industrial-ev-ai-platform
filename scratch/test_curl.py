import httpx
import asyncio

async def test():
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            resp = await client.get("http://localhost:8000/api/v1/supply-chain/vehicle/VEH-001")
            print(resp.status_code, resp.text)
    except Exception as e:
        print("ERROR:", type(e), e.args)

asyncio.run(test())
