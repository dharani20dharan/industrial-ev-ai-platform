import asyncio
from app.core.config import settings
from neo4j import AsyncGraphDatabase
from app.services.supply_chain import SupplyChainService

async def test():
    driver = AsyncGraphDatabase.driver(settings.neo4j.uri, auth=(settings.neo4j.username, settings.neo4j.password))
    async with driver.session(database=settings.neo4j.database) as session:
        result = await session.run('''
        MATCH (v:Vehicle {vehicle_id: 'VEH-001'})
        OPTIONAL MATCH path = (n)-[*]->(v)
        WITH v, collect(path) as paths
        RETURN v as root_node,
               [p IN paths | nodes(p)] as path_nodes,
               [p IN paths | relationships(p)] as path_rels
        ''')
        records = [dict(r) async for r in result]
        
        service = SupplyChainService(session)
        graph = service._format_graph_response(records[0])
        print(f"Nodes: {len(graph['nodes'])}")
        print(f"Edges: {len(graph['edges'])}")
        record = records[0]
        edges_list = []
        for path_rels in record.get("path_rels", []):
            if not path_rels: continue
            for rel in path_rels:
                src_id = str(getattr(rel.start_node, "element_id", getattr(rel.start_node, "id", "")))
                dst_id = str(getattr(rel.end_node, "element_id", getattr(rel.end_node, "id", "")))
                try:
                    props = dict(rel)
                    edges_list.append({
                        "source": src_id,
                        "target": dst_id,
                        "type": rel.type,
                        "properties": props
                    })
                except Exception as e:
                    print(f"EXCEPTION IN dict(rel): {e}")
                    
        print("Total edges parsed:", len(edges_list))
                    
    await driver.close()

asyncio.run(test())
