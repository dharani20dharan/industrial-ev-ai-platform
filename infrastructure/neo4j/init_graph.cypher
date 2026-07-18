// Constraints
CREATE CONSTRAINT supplier_id_unique IF NOT EXISTS FOR (s:Supplier) REQUIRE s.supplier_id IS UNIQUE;
CREATE CONSTRAINT mine_id_unique IF NOT EXISTS FOR (m:Mine) REQUIRE m.mine_id IS UNIQUE;
CREATE CONSTRAINT material_id_unique IF NOT EXISTS FOR (mat:Material) REQUIRE mat.material_id IS UNIQUE;
CREATE CONSTRAINT refinery_id_unique IF NOT EXISTS FOR (r:Refinery) REQUIRE r.refinery_id IS UNIQUE;
CREATE CONSTRAINT plant_id_unique IF NOT EXISTS FOR (p:BatteryPlant) REQUIRE p.plant_id IS UNIQUE;
CREATE CONSTRAINT cell_id_unique IF NOT EXISTS FOR (c:BatteryCell) REQUIRE c.cell_id IS UNIQUE;
CREATE CONSTRAINT fleet_id_unique IF NOT EXISTS FOR (f:Fleet) REQUIRE f.fleet_id IS UNIQUE;
CREATE CONSTRAINT vehicle_id_unique IF NOT EXISTS FOR (v:Vehicle) REQUIRE v.vehicle_id IS UNIQUE;

// Indexes
CREATE INDEX supplier_id_index IF NOT EXISTS FOR (s:Supplier) ON (s.supplier_id);
CREATE INDEX vehicle_id_index IF NOT EXISTS FOR (v:Vehicle) ON (v.vehicle_id);
CREATE INDEX material_id_index IF NOT EXISTS FOR (m:Material) ON (m.material_id);
CREATE INDEX country_supplier_index IF NOT EXISTS FOR (s:Supplier) ON (s.country);
CREATE INDEX risk_score_index IF NOT EXISTS FOR (s:Supplier) ON (s.risk_score);

// Clear existing data for idempotency
MATCH (n) DETACH DELETE n;

// Nodes - Suppliers
CREATE (s1:Supplier {supplier_id: "SUP-001", name: "Global Minings Corp", country: "Australia", risk_score: 12.5, status: "ACTIVE", mineral: "Lithium"})
CREATE (s2:Supplier {supplier_id: "SUP-002", name: "Euro Refineries Ltd", country: "Germany", risk_score: 8.2, status: "ACTIVE", mineral: "Cobalt"})
CREATE (s3:Supplier {supplier_id: "SUP-003", name: "AmeriCells Inc", country: "USA", risk_score: 15.0, status: "ON_HOLD", mineral: "Lithium"})
CREATE (s4:Supplier {supplier_id: "SUP-004", name: "SinoMaterials", country: "China", risk_score: 85.0, status: "ACTIVE", mineral: "Graphite"})
CREATE (s5:Supplier {supplier_id: "SUP-005", name: "AfriCobalt Ltd", country: "DRC", risk_score: 92.5, status: "ACTIVE", mineral: "Cobalt"})
CREATE (s6:Supplier {supplier_id: "SUP-006", name: "CanMines", country: "Canada", risk_score: 18.4, status: "ACTIVE", mineral: "Nickel"})
CREATE (s7:Supplier {supplier_id: "SUP-007", name: "IndoNickel Corp", country: "Indonesia", risk_score: 76.0, status: "ACTIVE", mineral: "Nickel"})

// Nodes - Mines
CREATE (m1:Mine {mine_id: "MIN-001", name: "Greenbushes", country: "Australia", material: "Lithium"})
CREATE (m2:Mine {mine_id: "MIN-002", name: "Mt Weld", country: "Australia", material: "Cobalt"})
CREATE (m3:Mine {mine_id: "MIN-003", name: "Salar de Atacama", country: "Chile", material: "Lithium"})
CREATE (m4:Mine {mine_id: "MIN-004", name: "Tenke Fungurume", country: "DRC", material: "Cobalt"})
CREATE (m5:Mine {mine_id: "MIN-005", name: "Sudbury Basin", country: "Canada", material: "Nickel"})
CREATE (m6:Mine {mine_id: "MIN-006", name: "Morowali", country: "Indonesia", material: "Nickel"})
CREATE (m7:Mine {mine_id: "MIN-007", name: "Heilongjiang", country: "China", material: "Graphite"})

// Nodes - Materials
CREATE (mat1:Material {material_id: "MAT-001", name: "Lithium Carbonate", type: "Raw"})
CREATE (mat2:Material {material_id: "MAT-002", name: "Cobalt Sulfate", type: "Raw"})
CREATE (mat3:Material {material_id: "MAT-003", name: "Graphite", type: "Raw"})
CREATE (mat4:Material {material_id: "MAT-004", name: "Nickel Sulfate", type: "Raw"})
CREATE (mat5:Material {material_id: "MAT-005", name: "Lithium Hydroxide", type: "Raw"})

// Nodes - Refineries
CREATE (r1:Refinery {refinery_id: "REF-001", country: "Germany"})
CREATE (r2:Refinery {refinery_id: "REF-002", country: "Japan"})
CREATE (r3:Refinery {refinery_id: "REF-003", country: "China"})
CREATE (r4:Refinery {refinery_id: "REF-004", country: "South Korea"})

// Nodes - Battery Plants
CREATE (p1:BatteryPlant {plant_id: "PLT-001", name: "Gigafactory Berlin", country: "Germany"})
CREATE (p2:BatteryPlant {plant_id: "PLT-002", name: "Gigafactory Texas", country: "USA"})
CREATE (p3:BatteryPlant {plant_id: "PLT-003", name: "CATL Ningde", country: "China"})
CREATE (p4:BatteryPlant {plant_id: "PLT-004", name: "LG Chem Ochang", country: "South Korea"})

// Nodes - Battery Cells
CREATE (c1:BatteryCell {cell_id: "CEL-001", chemistry: "LFP", manufacturer: "AmeriCells Inc"})
CREATE (c2:BatteryCell {cell_id: "CEL-002", chemistry: "NMC", manufacturer: "AmeriCells Inc"})
CREATE (c3:BatteryCell {cell_id: "CEL-003", chemistry: "LFP", manufacturer: "Euro Refineries Ltd"})
CREATE (c4:BatteryCell {cell_id: "CEL-004", chemistry: "NMC", manufacturer: "Global Minings Corp"})
CREATE (c5:BatteryCell {cell_id: "CEL-005", chemistry: "LFP", manufacturer: "SinoMaterials"})
CREATE (c6:BatteryCell {cell_id: "CEL-006", chemistry: "NMC811", manufacturer: "SinoMaterials"})

// Nodes - Fleets
CREATE (f1:Fleet {fleet_id: "FLT-001", fleet_name: "Euro Logistics Transport"})
CREATE (f2:Fleet {fleet_id: "FLT-002", fleet_name: "AmeriFreight Lines"})
CREATE (f3:Fleet {fleet_id: "FLT-003", fleet_name: "Asia-Pac Delivery"})

// Nodes - Vehicles
CREATE (v1:Vehicle {vehicle_id: "VEH-001", vin: "VIN00000000000001", model: "HD-Truck"})
CREATE (v2:Vehicle {vehicle_id: "VEH-002", vin: "VIN00000000000002", model: "MD-Truck"})
CREATE (v3:Vehicle {vehicle_id: "VEH-003", vin: "VIN00000000000003", model: "HD-Truck"})
CREATE (v4:Vehicle {vehicle_id: "VEH-004", vin: "VIN00000000000004", model: "LD-Van"})
CREATE (v5:Vehicle {vehicle_id: "VEH-005", vin: "VIN00000000000005", model: "MD-Truck"})
CREATE (v6:Vehicle {vehicle_id: "VEH-006", vin: "VIN00000000000006", model: "HD-Truck"})

// Relationships
// Suppliers -> Mines
CREATE (s1)-[:SUPPLIES]->(m1)
CREATE (s1)-[:SUPPLIES]->(m2)
CREATE (s3)-[:SUPPLIES]->(m3)
CREATE (s5)-[:SUPPLIES]->(m4)
CREATE (s6)-[:SUPPLIES]->(m5)
CREATE (s7)-[:SUPPLIES]->(m6)
CREATE (s4)-[:SUPPLIES]->(m7)

// Mines -> Materials
CREATE (m1)-[:MINES]->(mat1)
CREATE (m2)-[:MINES]->(mat2)
CREATE (m3)-[:MINES]->(mat5)
CREATE (m4)-[:MINES]->(mat2)
CREATE (m5)-[:MINES]->(mat4)
CREATE (m6)-[:MINES]->(mat4)
CREATE (m7)-[:MINES]->(mat3)

// Materials -> Refineries
CREATE (mat1)-[:REFINES]->(r1)
CREATE (mat2)-[:REFINES]->(r2)
CREATE (mat3)-[:REFINES]->(r3)
CREATE (mat4)-[:REFINES]->(r4)
CREATE (mat4)-[:REFINES]->(r3)
CREATE (mat5)-[:REFINES]->(r2)
CREATE (mat2)-[:REFINES]->(r3)

// Refineries -> Plants
CREATE (r1)-[:PROCESSES]->(p1)
CREATE (r2)-[:PROCESSES]->(p2)
CREATE (r3)-[:PROCESSES]->(p3)
CREATE (r4)-[:PROCESSES]->(p4)
CREATE (r3)-[:PROCESSES]->(p1) // Cross-border supply
CREATE (r2)-[:PROCESSES]->(p4)

// Plants -> Cells
CREATE (p1)-[:PRODUCES]->(c1)
CREATE (p1)-[:PRODUCES]->(c3)
CREATE (p2)-[:PRODUCES]->(c2)
CREATE (p2)-[:PRODUCES]->(c4)
CREATE (p3)-[:PRODUCES]->(c5)
CREATE (p3)-[:PRODUCES]->(c6)
CREATE (p4)-[:PRODUCES]->(c4)
CREATE (p4)-[:PRODUCES]->(c2)

// Cells -> Vehicles
CREATE (c1)-[:INSTALLED_IN]->(v1)
CREATE (c2)-[:INSTALLED_IN]->(v2)
CREATE (c3)-[:INSTALLED_IN]->(v3)
CREATE (c4)-[:INSTALLED_IN]->(v4)
CREATE (c5)-[:INSTALLED_IN]->(v5)
CREATE (c6)-[:INSTALLED_IN]->(v6)

// Vehicles -> Fleets
CREATE (v1)-[:BELONGS_TO]->(f1)
CREATE (v2)-[:BELONGS_TO]->(f1)
CREATE (v3)-[:BELONGS_TO]->(f2)
CREATE (v4)-[:BELONGS_TO]->(f2)
CREATE (v5)-[:BELONGS_TO]->(f3)
CREATE (v6)-[:BELONGS_TO]->(f3)

// Partner Relationships
CREATE (s1)-[:PARTNERS_WITH]->(s2)
CREATE (s1)-[:PARTNERS_WITH]->(s3)
CREATE (s6)-[:PARTNERS_WITH]->(s1)
CREATE (s4)-[:PARTNERS_WITH]->(s5)

// Shipping Direct
CREATE (s2)-[:SHIPS_TO]->(p1)
CREATE (s3)-[:SHIPS_TO]->(p2)
CREATE (s4)-[:SHIPS_TO]->(p3)

// Plants -> Fleets Direct Supply Contract
CREATE (p1)-[:SUPPLIES]->(f1)
CREATE (p2)-[:SUPPLIES]->(f2)
CREATE (p3)-[:SUPPLIES]->(f3)
