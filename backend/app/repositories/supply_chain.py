import logging
import time
from typing import Any, Dict, List, Optional
from neo4j import AsyncSession, AsyncTransaction

logger = logging.getLogger(__name__)

class SupplyChainRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _log_summary(self, query: str, summary: Any, exec_time: float):
        logger.info(
            f"Cypher Query Executed - "
            f"Time: {exec_time:.2f}ms | "
            f"Nodes Created: {summary.counters.nodes_created} | "
            f"Nodes Deleted: {summary.counters.nodes_deleted} | "
            f"Rels Created: {summary.counters.relationships_created} | "
            f"Rels Deleted: {summary.counters.relationships_deleted} | "
            f"Query: {query[:100]}..."
        )

    async def execute_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Executes a generic Cypher query in auto-commit mode."""
        parameters = parameters or {}
        start_time = time.time()
        try:
            result = await self.session.run(query, parameters)
            records = [dict(record) async for record in result]
            summary = await result.consume()
            exec_time = (time.time() - start_time) * 1000
            self._log_summary(query, summary, exec_time)
            return records
        except Exception as e:
            logger.error(f"Cypher execute_query failed: {e}")
            raise e

    async def run_read_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Executes a read-only Cypher query within a read transaction."""
        parameters = parameters or {}
        
        async def _read_tx(tx: AsyncTransaction):
            start_time = time.time()
            result = await tx.run(query, parameters)
            records = [dict(record) async for record in result]
            summary = await result.consume()
            exec_time = (time.time() - start_time) * 1000
            self._log_summary(query, summary, exec_time)
            return records

        try:
            return await self.session.execute_read(_read_tx)
        except Exception as e:
            logger.error(f"Cypher run_read_query failed: {e}")
            raise e

    async def run_write_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Executes a write Cypher query within a write transaction."""
        parameters = parameters or {}
        
        async def _write_tx(tx: AsyncTransaction):
            start_time = time.time()
            result = await tx.run(query, parameters)
            records = [dict(record) async for record in result]
            summary = await result.consume()
            exec_time = (time.time() - start_time) * 1000
            self._log_summary(query, summary, exec_time)
            return records

        try:
            return await self.session.execute_write(_write_tx)
        except Exception as e:
            logger.error(f"Cypher run_write_query failed: {e}")
            raise e

    async def get_vehicle_supply_chain(self, vehicle_id: str) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (v:Vehicle {vehicle_id: $vehicle_id})
        OPTIONAL MATCH path = (n)-[*]->(v)
        WITH v, collect(path) as paths
        RETURN v as root_node,
               [p IN paths | nodes(p)] as path_nodes,
               [p IN paths | relationships(p)] as path_rels
        """
        records = await self.run_read_query(query, {"vehicle_id": vehicle_id})
        return records[0] if records else None

    async def get_supplier_dependencies(self, supplier_id: str) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (s:Supplier {supplier_id: $supplier_id})
        OPTIONAL MATCH path = (s)-[*]->(n)
        WITH s, collect(path) as paths
        RETURN s as root_node,
               [p IN paths | nodes(p)] as path_nodes,
               [p IN paths | relationships(p)] as path_rels
        """
        records = await self.run_read_query(query, {"supplier_id": supplier_id})
        return records[0] if records else None

    async def get_material_trace(self, material_id: str) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (m:Material {material_id: $material_id})
        OPTIONAL MATCH up_path = (n)-[*]->(m)
        OPTIONAL MATCH down_path = (m)-[*]->(o)
        WITH m, collect(up_path) + collect(down_path) as paths
        RETURN m as root_node,
               [p IN paths WHERE p IS NOT NULL | nodes(p)] as path_nodes,
               [p IN paths WHERE p IS NOT NULL | relationships(p)] as path_rels
        """
        records = await self.run_read_query(query, {"material_id": material_id})
        return records[0] if records else None

    async def get_fleet_supply_chain(self, fleet_id: str) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (f:Fleet {fleet_id: $fleet_id})
        OPTIONAL MATCH path = (s:Supplier)-[*]->(f)
        WITH f, collect(path) as paths
        RETURN f as root_node,
               [p IN paths | nodes(p)] as path_nodes,
               [p IN paths | relationships(p)] as path_rels
        """
        records = await self.run_read_query(query, {"fleet_id": fleet_id})
        return records[0] if records else None

    async def get_downstream_impact(self, id_val: str) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (n) WHERE n.supplier_id = $id OR n.material_id = $id OR n.vehicle_id = $id OR n.fleet_id = $id OR n.mine_id = $id OR n.refinery_id = $id OR n.plant_id = $id OR n.cell_id = $id
        OPTIONAL MATCH path = (n)-[*]->(m)
        WITH n, collect(path) as paths
        RETURN n as root_node,
               [p IN paths WHERE p IS NOT NULL | nodes(p)] as path_nodes,
               [p IN paths WHERE p IS NOT NULL | relationships(p)] as path_rels
        """
        records = await self.run_read_query(query, {"id": id_val})
        return records[0] if records else None

    async def get_upstream_dependencies(self, id_val: str) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (n) WHERE n.supplier_id = $id OR n.material_id = $id OR n.vehicle_id = $id OR n.fleet_id = $id OR n.mine_id = $id OR n.refinery_id = $id OR n.plant_id = $id OR n.cell_id = $id
        OPTIONAL MATCH path = (m)-[*]->(n)
        WITH n, collect(path) as paths
        RETURN n as root_node,
               [p IN paths WHERE p IS NOT NULL | nodes(p)] as path_nodes,
               [p IN paths WHERE p IS NOT NULL | relationships(p)] as path_rels
        """
        records = await self.run_read_query(query, {"id": id_val})
        return records[0] if records else None

    async def get_alternative_suppliers_for_material(self, material_id: str) -> List[Dict[str, Any]]:
        query = """
        MATCH (s:Supplier)-[:SUPPLIES]->(mat:Material {material_id: $material_id})
        RETURN s as supplier, mat as material
        """
        return await self.run_read_query(query, {"material_id": material_id})

    async def get_alternative_suppliers_for_supplier(self, supplier_id: str) -> List[Dict[str, Any]]:
        query = """
        MATCH (s:Supplier {supplier_id: $supplier_id})-[:SUPPLIES]->(mat:Material)
        WITH mat
        MATCH (alt:Supplier)-[:SUPPLIES]->(mat)
        WHERE alt.supplier_id <> $supplier_id
        RETURN DISTINCT mat as material, alt as alternative_supplier
        """
        return await self.run_read_query(query, {"supplier_id": supplier_id})

    async def get_graph_statistics(self) -> Dict[str, Any]:
        query = """
        MATCH (n)
        WITH count(n) as node_count
        OPTIONAL MATCH ()-[r]->()
        WITH node_count, count(r) as relationship_count
        MATCH (n)
        RETURN node_count, relationship_count, labels(n)[0] as label, count(n) as count
        """
        records = await self.run_read_query(query)
        if not records:
            return {"node_count": 0, "relationship_count": 0, "entities_by_type": {}}
        
        stats = {
            "node_count": records[0]["node_count"],
            "relationship_count": records[0]["relationship_count"],
            "entities_by_type": {}
        }
        for r in records:
            if r["label"]:
                stats["entities_by_type"][r["label"]] = r["count"]
        return stats

    async def get_full_graph(self) -> Dict[str, Any]:
        query = """
        MATCH (n)
        OPTIONAL MATCH (n)-[r]->(m)
        RETURN [collect(DISTINCT n) + collect(DISTINCT m)] as path_nodes, 
               [collect(DISTINCT r)] as path_rels
        """
        records = await self.run_read_query(query)
        if not records:
            return {"path_nodes": [], "path_rels": []}
        return records[0]

    # --- PHASE 5 GRAPH MANAGEMENT CRUD OPERATIONS ---

    # Supplier Repository Operations
    async def get_supplier_by_id(self, supplier_id: str) -> Optional[Dict[str, Any]]:
        query = "MATCH (s:Supplier {supplier_id: $supplier_id}) RETURN s"
        records = await self.run_read_query(query, {"supplier_id": supplier_id})
        return dict(records[0]["s"]) if records and "s" in records[0] else None

    async def get_all_suppliers(self) -> List[Dict[str, Any]]:
        query = "MATCH (s:Supplier) RETURN s"
        records = await self.run_read_query(query)
        return [dict(r["s"]) for r in records if "s" in r]

    async def create_supplier(self, data: Dict[str, Any]) -> Dict[str, Any]:
        query = """
        CREATE (s:Supplier {
            supplier_id: $supplier_id,
            name: $name,
            country: $country,
            risk_score: $risk_score,
            status: $status
        })
        RETURN s
        """
        records = await self.run_write_query(query, data)
        return dict(records[0]["s"])

    async def update_supplier(self, supplier_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (s:Supplier {supplier_id: $supplier_id})
        SET s += $properties
        RETURN s
        """
        records = await self.run_write_query(query, {"supplier_id": supplier_id, "properties": data})
        return dict(records[0]["s"]) if records and "s" in records[0] else None

    async def delete_supplier(self, supplier_id: str) -> bool:
        query = """
        MATCH (s:Supplier {supplier_id: $supplier_id})
        DETACH DELETE s
        """
        await self.run_write_query(query, {"supplier_id": supplier_id})
        return True

    # Material Repository Operations
    async def get_material_by_id(self, material_id: str) -> Optional[Dict[str, Any]]:
        query = "MATCH (m:Material {material_id: $material_id}) RETURN m"
        records = await self.run_read_query(query, {"material_id": material_id})
        return dict(records[0]["m"]) if records and "m" in records[0] else None

    async def get_all_materials(self) -> List[Dict[str, Any]]:
        query = "MATCH (m:Material) RETURN m"
        records = await self.run_read_query(query)
        return [dict(r["m"]) for r in records if "m" in r]

    async def create_material(self, data: Dict[str, Any]) -> Dict[str, Any]:
        query = """
        CREATE (m:Material {
            material_id: $material_id,
            name: $name,
            type: $type
        })
        RETURN m
        """
        records = await self.run_write_query(query, data)
        return dict(records[0]["m"])

    async def update_material(self, material_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (m:Material {material_id: $material_id})
        SET m += $properties
        RETURN m
        """
        records = await self.run_write_query(query, {"material_id": material_id, "properties": data})
        return dict(records[0]["m"]) if records and "m" in records[0] else None

    async def delete_material(self, material_id: str) -> bool:
        query = """
        MATCH (m:Material {material_id: $material_id})
        DETACH DELETE m
        """
        await self.run_write_query(query, {"material_id": material_id})
        return True

    # Processing Plant Repository Operations
    async def get_processing_plant_by_id(self, plant_id: str) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (p) WHERE (p:ProcessingPlant OR p:Refinery OR p:BatteryPlant) AND (p.plant_id = $plant_id OR p.refinery_id = $plant_id)
        RETURN p
        """
        records = await self.run_read_query(query, {"plant_id": plant_id})
        if not records or "p" not in records[0]:
            return None
        res = dict(records[0]["p"])
        if "plant_id" not in res and "refinery_id" in res:
            res["plant_id"] = res["refinery_id"]
        if "name" not in res:
            res["name"] = f"Plant {res.get('plant_id')}"
        if "plant_type" not in res:
            res["plant_type"] = "Refinery"
        return res

    async def get_all_processing_plants(self) -> List[Dict[str, Any]]:
        query = "MATCH (p) WHERE p:ProcessingPlant OR p:Refinery OR p:BatteryPlant RETURN p"
        records = await self.run_read_query(query)
        result = []
        for r in records:
            if "p" in r:
                res = dict(r["p"])
                if "plant_id" not in res and "refinery_id" in res:
                    res["plant_id"] = res["refinery_id"]
                if "name" not in res:
                    res["name"] = f"Plant {res.get('plant_id')}"
                if "plant_type" not in res:
                    res["plant_type"] = "Refinery"
                result.append(res)
        return result

    async def create_processing_plant(self, data: Dict[str, Any]) -> Dict[str, Any]:
        query = """
        CREATE (p:ProcessingPlant {
            plant_id: $plant_id,
            name: $name,
            country: $country,
            plant_type: $plant_type
        })
        RETURN p
        """
        records = await self.run_write_query(query, data)
        return dict(records[0]["p"])

    async def update_processing_plant(self, plant_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (p) WHERE (p:ProcessingPlant OR p:Refinery OR p:BatteryPlant) AND (p.plant_id = $plant_id OR p.refinery_id = $plant_id)
        SET p += $properties
        RETURN p
        """
        records = await self.run_write_query(query, {"plant_id": plant_id, "properties": data})
        if not records or "p" not in records[0]:
            return None
        res = dict(records[0]["p"])
        if "plant_id" not in res and "refinery_id" in res:
            res["plant_id"] = res["refinery_id"]
        if "name" not in res:
            res["name"] = f"Plant {res.get('plant_id')}"
        if "plant_type" not in res:
            res["plant_type"] = "Refinery"
        return res

    async def delete_processing_plant(self, plant_id: str) -> bool:
        query = """
        MATCH (p) WHERE (p:ProcessingPlant OR p:Refinery OR p:BatteryPlant) AND (p.plant_id = $plant_id OR p.refinery_id = $plant_id)
        DETACH DELETE p
        """
        await self.run_write_query(query, {"plant_id": plant_id})
        return True

    # Mine Repository Operations (Optional)
    async def get_mine_by_id(self, mine_id: str) -> Optional[Dict[str, Any]]:
        query = "MATCH (m:Mine {mine_id: $mine_id}) RETURN m"
        records = await self.run_read_query(query, {"mine_id": mine_id})
        return dict(records[0]["m"]) if records and "m" in records[0] else None

    async def get_all_mines(self) -> List[Dict[str, Any]]:
        query = "MATCH (m:Mine) RETURN m"
        records = await self.run_read_query(query)
        return [dict(r["m"]) for r in records if "m" in r]

    async def create_mine(self, data: Dict[str, Any]) -> Dict[str, Any]:
        query = """
        CREATE (m:Mine {
            mine_id: $mine_id,
            name: $name,
            country: $country,
            material: $material
        })
        RETURN m
        """
        records = await self.run_write_query(query, data)
        return dict(records[0]["m"])

    async def update_mine(self, mine_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (m:Mine {mine_id: $mine_id})
        SET m += $properties
        RETURN m
        """
        records = await self.run_write_query(query, {"mine_id": mine_id, "properties": data})
        return dict(records[0]["m"]) if records and "m" in records[0] else None

    async def delete_mine(self, mine_id: str) -> bool:
        query = """
        MATCH (m:Mine {mine_id: $mine_id})
        DETACH DELETE m
        """
        await self.run_write_query(query, {"mine_id": mine_id})
        return True

    # --- PHASE 6 MATERIAL FLOW & TRACEABILITY CYPHER OPERATIONS ---

    async def get_material_flow_graph(self, material_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        query = """
        MATCH (m:Material)
        WHERE $material_id IS NULL OR m.material_id = $material_id
        OPTIONAL MATCH path = (n)-[*1..4]-(m)
        WITH m, collect(path) as paths
        RETURN m as root_node,
               [p IN paths WHERE p IS NOT NULL | nodes(p)] as path_nodes,
               [p IN paths WHERE p IS NOT NULL | relationships(p)] as path_rels
        """
        records = await self.run_read_query(query, {"material_id": material_id})
        if not records:
            return {"path_nodes": [], "path_rels": []}
        
        # Merge all path_nodes and path_rels across records
        all_nodes = []
        all_rels = []
        for r in records:
            if "root_node" in r and r["root_node"]:
                all_nodes.append([r["root_node"]])
            for pn in r.get("path_nodes", []):
                if pn: all_nodes.append(pn)
            for pr in r.get("path_rels", []):
                if pr: all_rels.append(pr)
                
        return {"path_nodes": all_nodes, "path_rels": all_rels}

    async def get_full_traceability_graph(self, entity_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        if entity_id:
            query = """
            MATCH (n)
            WHERE n.supplier_id = $id OR n.material_id = $id OR n.vehicle_id = $id OR n.fleet_id = $id OR n.mine_id = $id OR n.refinery_id = $id OR n.plant_id = $id OR n.cell_id = $id
            OPTIONAL MATCH up_path = (src)-[*1..6]->(n)
            OPTIONAL MATCH down_path = (n)-[*1..6]->(dst)
            WITH n, collect(up_path) + collect(down_path) as paths
            RETURN n as root_node,
                   [p IN paths WHERE p IS NOT NULL | nodes(p)] as path_nodes,
                   [p IN paths WHERE p IS NOT NULL | relationships(p)] as path_rels
            """
            records = await self.run_read_query(query, {"id": entity_id})
            return records[0] if records else None
        else:
            query = """
            MATCH (n)
            OPTIONAL MATCH (n)-[r]->(m)
            RETURN [collect(DISTINCT n) + collect(DISTINCT m)] as path_nodes, 
                   [collect(DISTINCT r)] as path_rels
            """
            records = await self.run_read_query(query)
            return records[0] if records else {"path_nodes": [], "path_rels": []}


