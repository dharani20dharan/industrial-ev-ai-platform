import asyncio
import json
import logging
import os
import sys

# Ensure backend root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from app.core.neo4j import neo4j_client
from app.core.cache import cache_manager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("seed_supply_chain")

async def seed_graph():
    logger.info("Initializing Neo4j Graph Database Seeder for Supply Chain Intelligence...")
    await neo4j_client.connect()
    
    async with neo4j_client.driver.session() as session:
        # Clear existing graph
        logger.info("Clearing old Neo4j graph nodes and relationships...")
        await session.run("MATCH (n) DETACH DELETE n")
        
        # Load ML supply chain graph file if available
        ml_graph_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../ml/data/processed/supply_chain_graph.json"))
        
        nodes_data = []
        edges_data = []
        if os.path.exists(ml_graph_path):
            with open(ml_graph_path, "r") as f:
                graph_json = json.load(f)
                nodes_data = graph_json.get("nodes", [])
                edges_data = graph_json.get("edges", [])
            logger.info(f"Loaded {len(nodes_data)} nodes and {len(edges_data)} edges from ML pipeline output.")
        
        # Create Nodes
        cypher_nodes = """
        // 1. Suppliers / Mines
        CREATE (s1:Supplier:Mine {supplier_id: 'S001', mine_id: 'S001', name: 'CobaltCo DRC', country: 'DRC', risk_score: 72.45, risk_level: 'high', status: 'ACTIVE'})
        CREATE (s2:Supplier:Mine {supplier_id: 'S002', mine_id: 'S002', name: 'LithiumEx Chile', country: 'CHL', risk_score: 43.33, risk_level: 'medium', status: 'ACTIVE'})
        CREATE (s3:Supplier:Mine {supplier_id: 'S003', mine_id: 'S003', name: 'NickelPro Indonesia', country: 'IDN', risk_score: 56.35, risk_level: 'high', status: 'ACTIVE'})
        CREATE (s4:Supplier:Mine {supplier_id: 'S004', mine_id: 'S004', name: 'GraphiteCorp China', country: 'CHN', risk_score: 48.45, risk_level: 'medium', status: 'ACTIVE'})
        CREATE (s5:Supplier:Mine {supplier_id: 'S005', mine_id: 'S005', name: 'LithiumOz Australia', country: 'AUS', risk_score: 34.33, risk_level: 'medium', status: 'ACTIVE'})
        CREATE (s6:Supplier {supplier_id: 'SUP-001', name: 'Global Battery Materials Ltd', country: 'USA', risk_score: 25.0, status: 'ACTIVE'})

        // 2. Refineries / Processing Plants
        CREATE (r1:Refinery:ProcessingPlant {plant_id: 'R001', refinery_id: 'R001', name: 'CathodeRefine Shanghai', country: 'CHN', plant_type: 'Refinery', risk_score: 34.45})
        CREATE (r2:Refinery:ProcessingPlant {plant_id: 'R002', refinery_id: 'R002', name: 'BattMat Korea', country: 'KOR', plant_type: 'Refinery', risk_score: 36.5})

        // 3. Battery Manufacturing Plants
        CREATE (p1:BatteryPlant:ProcessingPlant {plant_id: 'P001', name: 'GigaCell Shenzhen', country: 'CHN', plant_type: 'BatteryPlant', risk_score: 33.95})
        CREATE (p2:BatteryPlant:ProcessingPlant {plant_id: 'P002', name: 'BatteryWorks USA', country: 'USA', plant_type: 'BatteryPlant', risk_score: 22.55})

        // 4. Fleets
        CREATE (f1:Fleet {fleet_id: 'F001', fleet_name: 'Fleet Alpha', name: 'Fleet Alpha', country: 'IND', risk_score: 35.15})
        CREATE (f2:Fleet {fleet_id: 'F002', fleet_name: 'Fleet Beta', name: 'Fleet Beta', country: 'IND', risk_score: 35.15})
        CREATE (f3:Fleet {fleet_id: 'F003', fleet_name: 'Fleet Gamma', name: 'Fleet Gamma', country: 'USA', risk_score: 21.05})
        CREATE (f4:Fleet {fleet_id: 'FLT-001', fleet_name: 'Industrial Heavy Duty Fleet', name: 'Industrial Heavy Duty Fleet', country: 'IND', risk_score: 15.0})

        // 5. Materials
        CREATE (m1:Material {material_id: 'cobalt', name: 'Cobalt', type: 'Raw Material'})
        CREATE (m2:Material {material_id: 'lithium', name: 'Lithium', type: 'Raw Material'})
        CREATE (m3:Material {material_id: 'nickel', name: 'Nickel', type: 'Raw Material'})
        CREATE (m4:Material {material_id: 'graphite', name: 'Graphite', type: 'Raw Material'})
        CREATE (m5:Material {material_id: 'cathode_materials', name: 'Cathode Precursors', type: 'Processed Material'})
        CREATE (m6:Material {material_id: 'battery_cells', name: 'Lithium-Ion Battery Cells', type: 'Component'})
        CREATE (m7:Material {material_id: 'MAT-001', name: 'High-Purity Battery Grade Lithium', type: 'Processed'})

        // 6. Vehicles
        CREATE (v1:Vehicle {vehicle_id: 'EV-HD-001', model: 'Heavy Hauler E1', status: 'ACTIVE'})
        CREATE (v2:Vehicle {vehicle_id: 'EV-HD-002', model: 'Heavy Hauler E1', status: 'ACTIVE'})
        CREATE (v3:Vehicle {vehicle_id: 'EV-HD-003', model: 'Medium Duty Van', status: 'ACTIVE'})
        CREATE (v4:Vehicle {vehicle_id: 'EV-HD-004', model: 'Urban Delivery EV', status: 'ACTIVE'})
        CREATE (v5:Vehicle {vehicle_id: 'VEH-001', model: 'Fleet Truck 001', status: 'ACTIVE'})

        // 7. Battery Cells
        CREATE (c1:BatteryCell {cell_id: 'CELL-NMC-811', chemistry: 'NMC-811', capacity_ah: 100})
        CREATE (c2:BatteryCell {cell_id: 'CELL-LFP-001', chemistry: 'LFP', capacity_ah: 200})

        // --- RELATIONSHIPS ---
        CREATE (s1)-[:SUPPLIES {material: 'cobalt'}]->(m1)
        CREATE (s2)-[:SUPPLIES {material: 'lithium'}]->(m2)
        CREATE (s3)-[:SUPPLIES {material: 'nickel'}]->(m3)
        CREATE (s4)-[:SUPPLIES {material: 'graphite'}]->(m4)
        CREATE (s5)-[:SUPPLIES {material: 'lithium'}]->(m2)
        CREATE (s6)-[:SUPPLIES]->(m7)

        CREATE (m1)-[:PROCESSED_AT]->(r1)
        CREATE (m2)-[:PROCESSED_AT]->(r1)
        CREATE (m2)-[:PROCESSED_AT]->(r2)
        CREATE (m3)-[:PROCESSED_AT]->(r2)
        CREATE (m4)-[:PROCESSED_AT]->(r1)
        CREATE (m4)-[:PROCESSED_AT]->(r2)

        CREATE (r1)-[:SUPPLIES {material: 'cathode_materials'}]->(m5)
        CREATE (r2)-[:SUPPLIES {material: 'cathode_materials'}]->(m5)

        CREATE (m5)-[:USED_IN]->(p1)
        CREATE (m5)-[:USED_IN]->(p2)

        CREATE (p1)-[:PRODUCES]->(c1)
        CREATE (p2)-[:PRODUCES]->(c2)

        CREATE (c1)-[:POWERED_BY]->(m6)
        CREATE (c2)-[:POWERED_BY]->(m6)

        CREATE (m6)-[:INSTALLED_IN]->(f1)
        CREATE (m6)-[:INSTALLED_IN]->(f2)
        CREATE (m6)-[:INSTALLED_IN]->(f3)
        CREATE (m7)-[:INSTALLED_IN]->(f4)

        CREATE (f1)-[:OPERATES]->(v1)
        CREATE (f1)-[:OPERATES]->(v2)
        CREATE (f2)-[:OPERATES]->(v3)
        CREATE (f3)-[:OPERATES]->(v4)
        CREATE (f4)-[:OPERATES]->(v5)

        // Direct paths for quick graph traversals
        CREATE (s1)-[:SUPPLIES {material: 'cobalt'}]->(r1)
        CREATE (s2)-[:SUPPLIES {material: 'lithium'}]->(r1)
        CREATE (s2)-[:SUPPLIES {material: 'lithium'}]->(r2)
        CREATE (s3)-[:SUPPLIES {material: 'nickel'}]->(r2)
        CREATE (s4)-[:SUPPLIES {material: 'graphite'}]->(r1)
        CREATE (s4)-[:SUPPLIES {material: 'graphite'}]->(r2)
        CREATE (s5)-[:SUPPLIES {material: 'lithium'}]->(r2)

        CREATE (r1)-[:DELIVERS {material: 'cathode_materials'}]->(p1)
        CREATE (r2)-[:DELIVERS {material: 'cathode_materials'}]->(p1)
        CREATE (r2)-[:DELIVERS {material: 'cathode_materials'}]->(p2)

        CREATE (p1)-[:DELIVERS {material: 'battery_cells'}]->(f1)
        CREATE (p1)-[:DELIVERS {material: 'battery_cells'}]->(f2)
        CREATE (p2)-[:DELIVERS {material: 'battery_cells'}]->(f2)
        CREATE (p2)-[:DELIVERS {material: 'battery_cells'}]->(f3)
        """
        
        await session.run(cypher_nodes)
        logger.info("Successfully populated Neo4j supply chain graph nodes and relationships!")

    # Invalidate Redis cache key
    logger.info("Flushing Redis cache key 'supply_chain:analytics_dependencies'...")
    try:
        await cache_manager.connect()
        await cache_manager.delete("supply_chain:analytics_dependencies")
        logger.info("Cache invalidated successfully.")
        await cache_manager.close()
    except Exception as e:
        logger.warning(f"Could not clear Redis cache automatically: {e}")

    await neo4j_client.close()
    logger.info("Graph seeding process completed!")

if __name__ == "__main__":
    asyncio.run(seed_graph())
