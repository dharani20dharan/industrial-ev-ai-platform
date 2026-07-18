import logging
from typing import Dict, Any, List, Optional
from fastapi import HTTPException

from app.repositories.supply_chain import SupplyChainRepository
from app.schemas.supply_chain import (
    VehicleTraceResponse, SupplierResponse, MaterialTraceResponse, 
    FleetDependencyResponse, GraphStatisticsResponse,
    RiskAnalysisResponse, ImpactAnalysisResponse, AlternativeSupplierResponse,
    SupplyChainRiskScore, RiskScoreCategory,
    SupplierCreate, SupplierUpdate, SupplierNodeResponse,
    MaterialCreate, MaterialUpdate, MaterialNodeResponse,
    ProcessingPlantCreate, ProcessingPlantUpdate, ProcessingPlantNodeResponse,
    MineCreate, MineUpdate, MineNodeResponse,
    MaterialFlowSummaryItem, MaterialFlowResponse, TraceabilityStage, TraceabilityResponse,
    SupplierMLRiskItem, SupplyChainMLRiskResponse, CriticalSuppliersResponse,
    SupplierRecommendation, ProcurementRecommendationItem, ProcurementRecommendationResponse
)




logger = logging.getLogger(__name__)

class SupplyChainService:
    def __init__(self, session):
        self.repository = SupplyChainRepository(session)

    def _format_graph_response(self, record: Dict[str, Any]) -> Dict[str, Any]:
        nodes_dict = {}
        edges_list = []
        
        if "root_node" in record and record["root_node"]:
            rn = record["root_node"]
            n_id = str(getattr(rn, "element_id", getattr(rn, "id", "")))
            nodes_dict[n_id] = {
                "id": n_id,
                "label": list(rn.labels)[0] if rn.labels else "Unknown",
                "properties": dict(rn)
            }
            
        for path_nodes in record.get("path_nodes", []):
            if path_nodes is None: continue
            for node in path_nodes:
                if node is None: continue
                n_id = str(getattr(node, "element_id", getattr(node, "id", "")))
                if n_id not in nodes_dict:
                    nodes_dict[n_id] = {
                        "id": n_id,
                        "label": list(node.labels)[0] if node.labels else "Unknown",
                        "properties": dict(node)
                    }
                    
        for path_rels in record.get("path_rels", []):
            if path_rels is None: continue
            for rel in path_rels:
                if rel is None: continue
                try:
                    src_id = str(getattr(rel.start_node, "element_id", getattr(rel.start_node, "id", "")))
                    dst_id = str(getattr(rel.end_node, "element_id", getattr(rel.end_node, "id", "")))
                    edges_list.append({
                        "source": src_id,
                        "target": dst_id,
                        "type": rel.type,
                        "properties": dict(rel)
                    })
                except Exception as e:
                    logger.error(f"Error parsing edge: {e}")
                
        unique_edges = []
        seen_edges = set()
        print(f"Edges list size before dedup: {len(edges_list)}")
        for e in edges_list:
            sig = (e["source"], e["target"], e["type"])
            if sig not in seen_edges:
                seen_edges.add(sig)
                unique_edges.append(e)
                
        print(f"Parsed {len(unique_edges)} unique edges")
        return {
            "nodes": list(nodes_dict.values()),
            "edges": unique_edges
        }

    # --- PHASE 2 METHODS ---

    async def trace_vehicle(self, vehicle_id: str) -> VehicleTraceResponse:
        record = await self.repository.get_vehicle_supply_chain(vehicle_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"Vehicle '{vehicle_id}' not found in graph.")
        graph = self._format_graph_response(record)
        return VehicleTraceResponse(vehicle_id=vehicle_id, **graph)

    async def trace_supplier(self, supplier_id: str) -> SupplierResponse:
        record = await self.repository.get_supplier_dependencies(supplier_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"Supplier '{supplier_id}' not found in graph.")
        graph = self._format_graph_response(record)
        return SupplierResponse(supplier_id=supplier_id, **graph)

    async def trace_material(self, material_id: str) -> MaterialTraceResponse:
        record = await self.repository.get_material_trace(material_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"Material '{material_id}' not found in graph.")
        graph = self._format_graph_response(record)
        return MaterialTraceResponse(material_id=material_id, **graph)

    async def trace_fleet(self, fleet_id: str) -> FleetDependencyResponse:
        record = await self.repository.get_fleet_supply_chain(fleet_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"Fleet '{fleet_id}' not found in graph.")
        graph = self._format_graph_response(record)
        return FleetDependencyResponse(fleet_id=fleet_id, **graph)

    async def get_stats(self) -> GraphStatisticsResponse:
        stats = await self.repository.get_graph_statistics()
        return GraphStatisticsResponse(**stats)

    # --- PHASE 3 INTELLIGENCE METHODS ---

    def _calculate_depth(self, edges: List[Dict[str, Any]]) -> int:
        if not edges: return 0
        adj = {}
        in_degree = {}
        for e in edges:
            u, v = e["source"], e["target"]
            if u not in adj: adj[u] = []
            adj[u].append(v)
            if u not in in_degree: in_degree[u] = 0
            if v not in in_degree: in_degree[v] = 0
            in_degree[v] += 1
            
        queue = [n for n, d in in_degree.items() if d == 0]
        if not queue: queue = [list(in_degree.keys())[0]] # fallback for cycles
        depths = {n: 0 for n in queue}
        max_d = 0
        
        while queue:
            curr = queue.pop(0)
            d = depths.get(curr, 0)
            max_d = max(max_d, d)
            for nxt in adj.get(curr, []):
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    depths[nxt] = d + 1
                    queue.append(nxt)
                    
        return max_d

    def _calculate_risk_score(self, properties: dict, down_count: int, up_count: int, label: str, alt_count: int = 0, depth: int = 0) -> SupplyChainRiskScore:
        base_score = float(properties.get("risk_score", 50.0))
        
        score = base_score
        
        if label == "Supplier":
            country = properties.get("country", "")
            if country in ["China", "DRC", "Russia"]:
                score += 25
            if down_count > 10:
                score += 15
            if alt_count == 0:
                score += 10
        else:
            score = 30.0 + (up_count * 2.0) + (down_count * 1.5)
            
        score += depth * 2.0
            
        score = min(max(score, 0.0), 100.0)
        
        if score >= 80: category = RiskScoreCategory.CRITICAL
        elif score >= 60: category = RiskScoreCategory.HIGH
        elif score >= 30: category = RiskScoreCategory.MEDIUM
        else: category = RiskScoreCategory.LOW
            
        return SupplyChainRiskScore(
            score=round(score, 1),
            category=category,
            factors={
                "base_risk": base_score, 
                "downstream_impacts": down_count, 
                "upstream_dependencies": up_count,
                "alternative_suppliers": alt_count,
                "supply_chain_depth": depth
            }
        )

    async def analyze_risk(self, entity_id: str) -> RiskAnalysisResponse:
        down_record = await self.repository.get_downstream_impact(entity_id)
        if not down_record:
            raise HTTPException(status_code=404, detail=f"Entity '{entity_id}' not found in graph.")
            
        up_record = await self.repository.get_upstream_dependencies(entity_id)
        
        down_graph = self._format_graph_response(down_record)
        up_graph = self._format_graph_response(up_record) if up_record else {"nodes": [], "edges": []}
        
        down_count = max(0, len(down_graph["nodes"]) - 1)
        up_count = max(0, len(up_graph["nodes"]) - 1)
        
        rn = down_record.get("root_node")
        label = list(rn.labels)[0] if rn.labels else "Unknown"
        
        # Calculate depth of downstream graph
        depth = self._calculate_depth(down_graph["edges"])
        
        # Calculate alternative suppliers count if it's a supplier
        alt_count = 0
        if label == "Supplier":
            alts = await self.repository.get_alternative_suppliers_for_supplier(entity_id)
            alt_count = len(alts)
        elif label == "Material":
            alts = await self.repository.get_alternative_suppliers_for_material(entity_id)
            alt_count = len(alts)
        
        risk = self._calculate_risk_score(dict(rn), down_count, up_count, label, alt_count=alt_count, depth=depth)
        
        return RiskAnalysisResponse(
            entity_id=entity_id,
            entity_type=label,
            risk=risk,
            downstream_impact_count=down_count,
            upstream_dependency_count=up_count
        )

    async def analyze_impact(self, entity_id: str) -> ImpactAnalysisResponse:
        record = await self.repository.get_downstream_impact(entity_id)
        if not record:
            raise HTTPException(status_code=404, detail=f"Entity '{entity_id}' not found.")
        
        graph = self._format_graph_response(record)
        
        impacted_suppliers = 0
        impacted_vehicles = 0
        impacted_fleets = 0
        impacted_battery_cells = 0
        
        for node in graph["nodes"]:
            label = node.get("label", "")
            if label == "Supplier": impacted_suppliers += 1
            elif label == "Vehicle": impacted_vehicles += 1
            elif label == "Fleet": impacted_fleets += 1
            elif label == "BatteryCell": impacted_battery_cells += 1
            
        rn = record.get("root_node")
        rn_label = list(rn.labels)[0] if rn.labels else ""
        if rn_label == "Supplier": impacted_suppliers -= 1
        elif rn_label == "Vehicle": impacted_vehicles -= 1
        elif rn_label == "Fleet": impacted_fleets -= 1
        elif rn_label == "BatteryCell": impacted_battery_cells -= 1
        
        return ImpactAnalysisResponse(
            entity_id=entity_id,
            entity_type=rn_label,
            impacted_suppliers=max(0, impacted_suppliers),
            impacted_vehicles=max(0, impacted_vehicles),
            impacted_fleets=max(0, impacted_fleets),
            impacted_battery_cells=max(0, impacted_battery_cells),
            dependency_depth=self._calculate_depth(graph["edges"]),
            total_downstream_entities=len(graph["nodes"]) - 1,
            graph=graph
        )

    async def get_alternatives_for_material(self, material_id: str) -> AlternativeSupplierResponse:
        records = await self.repository.get_alternative_suppliers_for_material(material_id)
        suppliers = []
        for r in records:
            s = r["supplier"]
            s_dict = dict(s)
            s_dict["id"] = s_dict.get("supplier_id")
            suppliers.append(s_dict)
            
        return AlternativeSupplierResponse(
            target_id=material_id,
            target_type="Material",
            alternative_suppliers=suppliers
        )
        
    async def get_alternatives_for_supplier(self, supplier_id: str) -> AlternativeSupplierResponse:
        records = await self.repository.get_alternative_suppliers_for_supplier(supplier_id)
        suppliers = []
        for r in records:
            alt = r["alternative_supplier"]
            mat = r["material"]
            s_dict = dict(alt)
            s_dict["id"] = s_dict.get("supplier_id")
            s_dict["supplies_material"] = dict(mat).get("name")
            suppliers.append(s_dict)
            
        return AlternativeSupplierResponse(
            target_id=supplier_id,
            target_type="Supplier",
            original_supplier_id=supplier_id,
            alternative_suppliers=suppliers
        )
        
    def _find_bottlenecks(self, nodes: List[Dict[str, Any]], edges: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # A bottleneck is a node that is the ONLY incoming edge to another node, meaning it's a single point of failure
        in_degree = {}
        incoming_edges_map = {}
        
        for e in edges:
            v = e["target"]
            u = e["source"]
            if v not in in_degree:
                in_degree[v] = 0
                incoming_edges_map[v] = []
            in_degree[v] += 1
            incoming_edges_map[v].append(u)
            
        bottlenecks = []
        bottleneck_ids = set()
        
        # Determine out degrees to find impact
        out_degree = {}
        for e in edges:
            u = e["source"]
            out_degree[u] = out_degree.get(u, 0) + 1
            
        nodes_dict = {n["id"]: n for n in nodes}
        
        for target_id, count in in_degree.items():
            if count == 1:
                source_id = incoming_edges_map[target_id][0]
                if source_id not in bottleneck_ids and source_id in nodes_dict:
                    impact = out_degree.get(source_id, 1)
                    source_node = nodes_dict[source_id]
                    bottleneck_ids.add(source_id)
                    bottlenecks.append({
                        "node_id": source_id,
                        "label": source_node.get("label", "Unknown"),
                        "name": source_node.get("properties", {}).get("name") or source_node.get("properties", {}).get("plant_id", source_id),
                        "bottleneck_type": "SINGLE_SOURCE",
                        "impacted_entities": impact
                    })
                    
        return sorted(bottlenecks, key=lambda x: x["impacted_entities"], reverse=True)

    async def get_analytics_dependencies(self) -> Any:
        from app.core.cache import cache_manager
        
        cache_key = "supply_chain:analytics_dependencies"
        cached = await cache_manager.get(cache_key)
        if cached:
            return cached

        record = await self.repository.get_full_graph()
        graph = self._format_graph_response(record)
        
        depth = self._calculate_depth(graph["edges"])
        bottlenecks = self._find_bottlenecks(graph["nodes"], graph["edges"])
        
        from app.schemas.supply_chain import AnalyticsDependenciesResponse, CriticalNodeResponse
        
        crit_nodes = [CriticalNodeResponse(**b) for b in bottlenecks]
        
        response = AnalyticsDependenciesResponse(
            critical_bottlenecks=crit_nodes,
            global_dependency_depth=depth,
            graph=graph
        )
        
        await cache_manager.set(cache_key, response.model_dump(), expire=600)
        return response

    async def get_dashboard_overview(self) -> Any:
        # Re-uses the cached analytical dependencies
        analytics = await self.get_analytics_dependencies()
        if isinstance(analytics, dict):
            # It came from cache, reconstruct the model to easily access properties
            from app.schemas.supply_chain import AnalyticsDependenciesResponse
            analytics = AnalyticsDependenciesResponse(**analytics)

        graph = analytics.graph
        
        suppliers = sum(1 for n in graph.nodes if n.label == "Supplier")
        materials = sum(1 for n in graph.nodes if n.label == "Material")
        vehicles = sum(1 for n in graph.nodes if n.label == "Vehicle")
        fleets = sum(1 for n in graph.nodes if n.label == "Fleet")
        
        # High risk count (dummy check using properties if risk_score exists)
        high_risk = sum(1 for n in graph.nodes if n.label == "Supplier" and float(n.properties.get("risk_score", 0)) > 60)
        
        from app.schemas.supply_chain import DashboardOverviewResponse
        return DashboardOverviewResponse(
            total_suppliers=suppliers,
            total_materials=materials,
            total_vehicles=vehicles,
            total_fleets=fleets,
            average_supply_chain_depth=analytics.global_dependency_depth,
            high_risk_suppliers_count=high_risk,
            critical_bottlenecks_count=len(analytics.critical_bottlenecks),
            supply_diversity_index=max(0, 100 - (len(analytics.critical_bottlenecks) * 5.0)) # Simple diversity calculation
        )

    async def get_network_visualization(self) -> Any:
        analytics = await self.get_analytics_dependencies()
        if isinstance(analytics, dict):
            from app.schemas.supply_chain import AnalyticsDependenciesResponse
            analytics = AnalyticsDependenciesResponse(**analytics)

        graph = analytics.graph
        
        # Format for Cytoscape.js
        nodes = []
        for n in graph.nodes:
            nodes.append({
                "data": {
                    "id": n.id,
                    "label": n.properties.get("name", n.id),
                    "type": n.label,
                    **n.properties
                },
                "classes": n.label.lower()
            })
            
        edges = []
        for e in graph.edges:
            edges.append({
                "data": {
                    "source": e.source,
                    "target": e.target,
                    "label": e.type
                }
            })
            
        from app.schemas.supply_chain import NetworkVisualizationResponse
        return NetworkVisualizationResponse(
            elements={"nodes": nodes, "edges": edges}
        )

    async def generate_recommendations(self) -> Any:
        analytics = await self.get_analytics_dependencies()
        if isinstance(analytics, dict):
            from app.schemas.supply_chain import AnalyticsDependenciesResponse
            analytics = AnalyticsDependenciesResponse(**analytics)

        from app.schemas.supply_chain import RecommendationAction, RecommendationResponse
        
        recommendations = []
        for bottleneck in analytics.critical_bottlenecks:
            # If the bottleneck is a supplier
            if bottleneck.label == "Supplier":
                recommendations.append(RecommendationAction(
                    action_type="DIVERSIFY_SOURCING",
                    target_entity_id=bottleneck.node_id,
                    target_entity_type="Supplier",
                    reason=f"Supplier {bottleneck.name} is a single source bottleneck impacting {bottleneck.impacted_entities} downstream entities."
                ))
            elif bottleneck.label == "Mine":
                recommendations.append(RecommendationAction(
                    action_type="IDENTIFY_NEW_MINE",
                    target_entity_id=bottleneck.node_id,
                    target_entity_type="Mine",
                    reason=f"Mine {bottleneck.name} is a critical bottleneck impacting {bottleneck.impacted_entities} entities."
                ))
                
        return RecommendationResponse(recommendations=recommendations)

    # --- PHASE 5 GRAPH MANAGEMENT SERVICE METHODS ---

    async def _invalidate_analytics_cache(self):
        try:
            from app.core.cache import cache_manager
            await cache_manager.delete("supply_chain:analytics_dependencies")
        except Exception as e:
            logger.warning(f"Cache invalidation failed: {e}")

    # Supplier Operations
    async def create_supplier(self, payload: SupplierCreate) -> SupplierNodeResponse:
        existing = await self.repository.get_supplier_by_id(payload.supplier_id)
        if existing:
            raise HTTPException(status_code=409, detail=f"Supplier with ID '{payload.supplier_id}' already exists.")
        
        data = payload.model_dump()
        node = await self.repository.create_supplier(data)
        await self._invalidate_analytics_cache()
        return SupplierNodeResponse(**node)

    async def get_supplier(self, supplier_id: str) -> SupplierNodeResponse:
        node = await self.repository.get_supplier_by_id(supplier_id)
        if not node:
            raise HTTPException(status_code=404, detail=f"Supplier '{supplier_id}' not found.")
        return SupplierNodeResponse(**node)

    async def list_suppliers(self) -> List[SupplierNodeResponse]:
        nodes = await self.repository.get_all_suppliers()
        return [SupplierNodeResponse(**n) for n in nodes]

    async def update_supplier(self, supplier_id: str, payload: SupplierUpdate) -> SupplierNodeResponse:
        existing = await self.repository.get_supplier_by_id(supplier_id)
        if not existing:
            raise HTTPException(status_code=404, detail=f"Supplier '{supplier_id}' not found.")
        
        update_data = payload.model_dump(exclude_unset=True)
        if not update_data:
            return SupplierNodeResponse(**existing)
            
        updated = await self.repository.update_supplier(supplier_id, update_data)
        await self._invalidate_analytics_cache()
        return SupplierNodeResponse(**updated)

    async def delete_supplier(self, supplier_id: str) -> Dict[str, str]:
        existing = await self.repository.get_supplier_by_id(supplier_id)
        if not existing:
            raise HTTPException(status_code=404, detail=f"Supplier '{supplier_id}' not found.")
            
        await self.repository.delete_supplier(supplier_id)
        await self._invalidate_analytics_cache()
        return {"message": f"Supplier '{supplier_id}' deleted successfully."}

    # Material Operations
    async def create_material(self, payload: MaterialCreate) -> MaterialNodeResponse:
        existing = await self.repository.get_material_by_id(payload.material_id)
        if existing:
            raise HTTPException(status_code=409, detail=f"Material with ID '{payload.material_id}' already exists.")
            
        data = payload.model_dump()
        node = await self.repository.create_material(data)
        await self._invalidate_analytics_cache()
        return MaterialNodeResponse(**node)

    async def get_material(self, material_id: str) -> MaterialNodeResponse:
        node = await self.repository.get_material_by_id(material_id)
        if not node:
            raise HTTPException(status_code=404, detail=f"Material '{material_id}' not found.")
        return MaterialNodeResponse(**node)

    async def list_materials(self) -> List[MaterialNodeResponse]:
        nodes = await self.repository.get_all_materials()
        return [MaterialNodeResponse(**n) for n in nodes]

    async def update_material(self, material_id: str, payload: MaterialUpdate) -> MaterialNodeResponse:
        existing = await self.repository.get_material_by_id(material_id)
        if not existing:
            raise HTTPException(status_code=404, detail=f"Material '{material_id}' not found.")
            
        update_data = payload.model_dump(exclude_unset=True)
        if not update_data:
            return MaterialNodeResponse(**existing)
            
        updated = await self.repository.update_material(material_id, update_data)
        await self._invalidate_analytics_cache()
        return MaterialNodeResponse(**updated)

    async def delete_material(self, material_id: str) -> Dict[str, str]:
        existing = await self.repository.get_material_by_id(material_id)
        if not existing:
            raise HTTPException(status_code=404, detail=f"Material '{material_id}' not found.")
            
        await self.repository.delete_material(material_id)
        await self._invalidate_analytics_cache()
        return {"message": f"Material '{material_id}' deleted successfully."}

    # Processing Plant Operations
    async def create_processing_plant(self, payload: ProcessingPlantCreate) -> ProcessingPlantNodeResponse:
        existing = await self.repository.get_processing_plant_by_id(payload.plant_id)
        if existing:
            raise HTTPException(status_code=409, detail=f"Processing plant with ID '{payload.plant_id}' already exists.")
            
        data = payload.model_dump()
        node = await self.repository.create_processing_plant(data)
        await self._invalidate_analytics_cache()
        return ProcessingPlantNodeResponse(**node)

    async def get_processing_plant(self, plant_id: str) -> ProcessingPlantNodeResponse:
        node = await self.repository.get_processing_plant_by_id(plant_id)
        if not node:
            raise HTTPException(status_code=404, detail=f"Processing plant '{plant_id}' not found.")
        return ProcessingPlantNodeResponse(**node)

    async def list_processing_plants(self) -> List[ProcessingPlantNodeResponse]:
        nodes = await self.repository.get_all_processing_plants()
        return [ProcessingPlantNodeResponse(**n) for n in nodes]

    async def update_processing_plant(self, plant_id: str, payload: ProcessingPlantUpdate) -> ProcessingPlantNodeResponse:
        existing = await self.repository.get_processing_plant_by_id(plant_id)
        if not existing:
            raise HTTPException(status_code=404, detail=f"Processing plant '{plant_id}' not found.")
            
        update_data = payload.model_dump(exclude_unset=True)
        if not update_data:
            return ProcessingPlantNodeResponse(**existing)
            
        updated = await self.repository.update_processing_plant(plant_id, update_data)
        await self._invalidate_analytics_cache()
        return ProcessingPlantNodeResponse(**updated)

    async def delete_processing_plant(self, plant_id: str) -> Dict[str, str]:
        existing = await self.repository.get_processing_plant_by_id(plant_id)
        if not existing:
            raise HTTPException(status_code=404, detail=f"Processing plant '{plant_id}' not found.")
            
        await self.repository.delete_processing_plant(plant_id)
        await self._invalidate_analytics_cache()
        return {"message": f"Processing plant '{plant_id}' deleted successfully."}

    # Mine Operations (Optional)
    async def create_mine(self, payload: MineCreate) -> MineNodeResponse:
        existing = await self.repository.get_mine_by_id(payload.mine_id)
        if existing:
            raise HTTPException(status_code=409, detail=f"Mine with ID '{payload.mine_id}' already exists.")
            
        data = payload.model_dump()
        node = await self.repository.create_mine(data)
        await self._invalidate_analytics_cache()
        return MineNodeResponse(**node)

    async def get_mine(self, mine_id: str) -> MineNodeResponse:
        node = await self.repository.get_mine_by_id(mine_id)
        if not node:
            raise HTTPException(status_code=404, detail=f"Mine '{mine_id}' not found.")
        return MineNodeResponse(**node)

    async def list_mines(self) -> List[MineNodeResponse]:
        nodes = await self.repository.get_all_mines()
        return [MineNodeResponse(**n) for n in nodes]

    async def update_mine(self, mine_id: str, payload: MineUpdate) -> MineNodeResponse:
        existing = await self.repository.get_mine_by_id(mine_id)
        if not existing:
            raise HTTPException(status_code=404, detail=f"Mine '{mine_id}' not found.")
            
        update_data = payload.model_dump(exclude_unset=True)
        if not update_data:
            return MineNodeResponse(**existing)
            
        updated = await self.repository.update_mine(mine_id, update_data)
        await self._invalidate_analytics_cache()
        return MineNodeResponse(**updated)

    async def delete_mine(self, mine_id: str) -> Dict[str, str]:
        existing = await self.repository.get_mine_by_id(mine_id)
        if not existing:
            raise HTTPException(status_code=404, detail=f"Mine '{mine_id}' not found.")
            
        await self.repository.delete_mine(mine_id)
        await self._invalidate_analytics_cache()
        return {"message": f"Mine '{mine_id}' deleted successfully."}

    # --- PHASE 6 MATERIAL FLOW & TRACEABILITY SERVICE METHODS ---

    async def get_material_flow(self, material_id: Optional[str] = None) -> MaterialFlowResponse:
        record = await self.repository.get_material_flow_graph(material_id)
        graph = self._format_graph_response(record) if record else {"nodes": [], "edges": []}
        
        material_nodes = [n for n in graph["nodes"] if n.get("label") == "Material"]
        if material_id and not material_nodes:
            m_obj = await self.repository.get_material_by_id(material_id)
            if m_obj:
                material_nodes = [{"id": m_obj["material_id"], "label": "Material", "properties": m_obj}]
                
        summary_items = []
        for m in material_nodes:
            props = m.get("properties", {})
            mat_id = props.get("material_id") or m.get("id")
            
            suppliers_count = sum(1 for n in graph["nodes"] if n.get("label") in ["Supplier", "Mine"])
            refineries_count = sum(1 for n in graph["nodes"] if n.get("label") in ["Refinery", "ProcessingPlant"])
            plants_count = sum(1 for n in graph["nodes"] if n.get("label") == "BatteryPlant")
            vehicles_count = sum(1 for n in graph["nodes"] if n.get("label") in ["Vehicle", "BatteryCell"])
            
            summary_items.append(MaterialFlowSummaryItem(
                material_id=mat_id,
                name=props.get("name", mat_id),
                type=props.get("type", "Raw"),
                suppliers_count=suppliers_count,
                refineries_count=refineries_count,
                plants_count=plants_count,
                vehicles_count=vehicles_count
            ))
            
        return MaterialFlowResponse(
            summary=summary_items,
            graph=graph
        )

    async def get_traceability(self, entity_id: Optional[str] = None) -> TraceabilityResponse:
        record = await self.repository.get_full_traceability_graph(entity_id)
        if entity_id and not record:
            raise HTTPException(status_code=404, detail=f"Entity '{entity_id}' not found in supply chain graph.")
            
        graph = self._format_graph_response(record) if record else {"nodes": [], "edges": []}
        
        upstream_nodes = []
        downstream_nodes = []
        
        stage_mapping = {
            "Supplier": (1, "1. Raw Sourcing"),
            "Mine": (2, "2. Mineral Mining"),
            "Material": (3, "3. Raw Material"),
            "Refinery": (4, "4. Material Refining"),
            "ProcessingPlant": (4, "4. Material Refining"),
            "BatteryPlant": (5, "5. Plant Processing"),
            "BatteryCell": (6, "6. Cell Manufacturing"),
            "Vehicle": (7, "7. Vehicle Integration"),
            "Fleet": (8, "8. Fleet Operation")
        }
        
        stages = []
        for node in graph["nodes"]:
            label = node.get("label", "Unknown")
            props = node.get("properties", {})
            node_id = props.get("supplier_id") or props.get("material_id") or props.get("mine_id") or props.get("refinery_id") or props.get("plant_id") or props.get("cell_id") or props.get("vehicle_id") or props.get("fleet_id") or node.get("id")
            
            if label in ["Supplier", "Mine", "Material"]:
                upstream_nodes.append({"id": node_id, "label": label, "name": props.get("name", node_id), "country": props.get("country")})
            else:
                downstream_nodes.append({"id": node_id, "label": label, "name": props.get("name", node_id), "country": props.get("country")})
                
            stage_info = stage_mapping.get(label, (9, f"{label} Stage"))
            stages.append(TraceabilityStage(
                stage_order=stage_info[0],
                stage_name=stage_info[1],
                entity_id=node_id,
                entity_type=label,
                name=props.get("name") or props.get("model") or props.get("fleet_name") or node_id,
                location=props.get("country") or props.get("location"),
                details=props
            ))
            
        stages.sort(key=lambda s: (s.stage_order, s.entity_id))
        
        return TraceabilityResponse(
            target_id=entity_id,
            upstream_lineage=upstream_nodes,
            downstream_usage=downstream_nodes,
            complete_manufacturing_chain=stages,
            graph=graph
        )

    # --- DELIVERABLE 7 ML INTEGRATION SERVICE METHODS ---

    async def get_ml_supply_chain_risk(self) -> SupplyChainMLRiskResponse:
        from app.services.ml import get_supply_chain_risk_scorer
        scorer = get_supply_chain_risk_scorer()
        
        db_suppliers = await self.repository.get_all_suppliers()
        scored_items = []
        
        if db_suppliers:
            for s in db_suppliers:
                supplier_dict = {
                    'supplier_id': s.get('supplier_id'),
                    'name': s.get('name', 'Unknown Supplier'),
                    'country': s.get('country', 'USA'),
                    'mineral': s.get('mineral', 'lithium'),
                    'type': 'mine',
                    'failure_rate': float(s.get('risk_score', 10.0)) / 100.0
                }
                res = scorer.score_supplier(supplier_dict)
                scored_items.append(SupplierMLRiskItem(
                    supplier_id=res['supplier_id'],
                    supplier_name=res['supplier_name'],
                    type=res['type'],
                    country=res['country'],
                    country_name=res.get('country_name'),
                    mineral=res.get('mineral'),
                    risk_score=res['risk_score'],
                    risk_level=res['risk_level'],
                    risk_color=res.get('risk_color'),
                    confidence=95.0,
                    action=res.get('action'),
                    breakdown=res.get('breakdown', {}),
                    recommendations=res.get('recommendations', [])
                ))
        else:
            ml_results = scorer.score_all_suppliers()
            for res in ml_results:
                scored_items.append(SupplierMLRiskItem(
                    supplier_id=res['supplier_id'],
                    supplier_name=res['supplier_name'],
                    type=res['type'],
                    country=res['country'],
                    country_name=res.get('country_name'),
                    mineral=res.get('mineral'),
                    risk_score=res['risk_score'],
                    risk_level=res['risk_level'],
                    risk_color=res.get('risk_color'),
                    confidence=95.0,
                    action=res.get('action'),
                    breakdown=res.get('breakdown', {}),
                    recommendations=res.get('recommendations', [])
                ))
                
        scores = [s.risk_score for s in scored_items]
        avg_score = round(sum(scores) / len(scores), 1) if scores else 0.0
        
        if avg_score >= 75: overall_level = "critical"
        elif avg_score >= 50: overall_level = "high"
        elif avg_score >= 25: overall_level = "medium"
        else: overall_level = "low"
        
        highest = max(scored_items, key=lambda x: x.risk_score) if scored_items else None
        vuln_msg = f"High risk concentration from supplier {highest.supplier_name} ({highest.risk_score}/100) in {highest.country}." if highest else "No supply chain vulnerabilities detected."
        mitigation_msg = highest.recommendations[0] if highest and highest.recommendations else "Diversify sourcing contracts."
        
        from datetime import datetime
        return SupplyChainMLRiskResponse(
            global_risk_index=avg_score,
            risk_level=overall_level,
            confidence=95.0,
            total_suppliers_assessed=len(scored_items),
            critical_vulnerability=vuln_msg,
            mitigation_plan=mitigation_msg,
            suppliers=scored_items,
            last_updated=datetime.now().isoformat()
        )

    async def get_ml_critical_suppliers(self) -> CriticalSuppliersResponse:
        risk_response = await self.get_ml_supply_chain_risk()
        criticals = [s for s in risk_response.suppliers if s.risk_level in ["high", "critical"]]
        
        all_recs = []
        for c in criticals:
            all_recs.extend(c.recommendations)
        unique_recs = list(dict.fromkeys(all_recs))
        
        return CriticalSuppliersResponse(
            total_critical_count=len(criticals),
            critical_suppliers=criticals,
            recommendations=unique_recs
        )

    # --- PHASE 8 PROCUREMENT RECOMMENDATION SERVICE METHODS ---

    async def get_procurement_recommendations(self, material_id: Optional[str] = None) -> ProcurementRecommendationResponse:
        risk_response = await self.get_ml_supply_chain_risk()
        
        # Filter suppliers by material if material_id is provided
        suppliers = risk_response.suppliers
        if material_id:
            # Simple assumption: material_id is closely related to mineral
            # E.g., MAT-001 is lithium, MAT-002 is cobalt
            target_mineral = None
            if "MAT-001" in material_id or "lithium" in material_id.lower():
                target_mineral = "lithium"
            elif "MAT-002" in material_id or "cobalt" in material_id.lower():
                target_mineral = "cobalt"
            
            if target_mineral:
                suppliers = [s for s in suppliers if s.mineral == target_mineral]

        # Group by material
        material_groups = {}
        for s in suppliers:
            mat = s.mineral or "general"
            if mat not in material_groups:
                material_groups[mat] = []
            material_groups[mat].append(s)

        recommendations = []
        for mat, group_suppliers in material_groups.items():
            if not group_suppliers:
                continue
                
            # Find current supplier (the one with highest risk as a candidate for replacement)
            current_supplier = max(group_suppliers, key=lambda x: x.risk_score)
            
            # Find alternatives (lower risk)
            alternatives = [s for s in group_suppliers if s.supplier_id != current_supplier.supplier_id and s.risk_score < current_supplier.risk_score]
            # Sort alternatives by lowest risk
            alternatives.sort(key=lambda x: x.risk_score)
            
            rec_suppliers = []
            if alternatives:
                best_alt = alternatives[0]
                rec_suppliers = [SupplierRecommendation(
                    supplier_id=best_alt.supplier_id,
                    supplier_name=best_alt.supplier_name,
                    country=best_alt.country,
                    mineral=best_alt.mineral or mat
                )]
            
            alt_suppliers_out = []
            for alt in alternatives[1:]:
                alt_suppliers_out.append(SupplierRecommendation(
                    supplier_id=alt.supplier_id,
                    supplier_name=alt.supplier_name,
                    country=alt.country,
                    mineral=alt.mineral or mat
                ))
                
            diversification = []
            countries = {s.country for s in group_suppliers}
            if len(countries) < 3:
                diversification.append(f"Consider sourcing {mat} from additional countries to reduce geopolitical risk.")
            if current_supplier.risk_level in ["high", "critical"]:
                diversification.append(f"Shift 30% of volume from {current_supplier.supplier_name} to lower-risk alternatives.")
                
            reason = f"Current primary supplier {current_supplier.supplier_name} has {current_supplier.risk_level} risk ({current_supplier.risk_score})."
            if rec_suppliers:
                reason += f" Switching to {rec_suppliers[0].supplier_name} reduces risk by {round(current_supplier.risk_score - best_alt.risk_score, 1)} points."

            recommendations.append(ProcurementRecommendationItem(
                material=mat,
                recommended_suppliers=rec_suppliers,
                alternative_suppliers=alt_suppliers_out,
                diversification_suggestions=diversification,
                reason_for_recommendation=reason,
                current_supplier_risk=current_supplier.risk_score,
                suggested_supplier_risk=best_alt.risk_score if alternatives else current_supplier.risk_score
            ))

        return ProcurementRecommendationResponse(
            recommendations=recommendations,
            summary=f"Generated {len(recommendations)} procurement recommendations based on ML risk scores."
        )



