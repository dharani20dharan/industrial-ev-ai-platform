import os
import sys
from neo4j import GraphDatabase

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4jpassword")

def load_cypher_file(file_path):
    """Loads and splits Cypher queries from the file, stripping comments."""
    if not os.path.exists(file_path):
        print(f"Error: Cypher file not found at {file_path}")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    queries = []
    current_query = []
    
    for line in content.split("\n"):
        stripped = line.strip()
        if not stripped:
            if current_query:
                queries.append("\n".join(current_query))
                current_query = []
            continue
        if stripped.startswith("//"):
            continue
        current_query.append(line)
        
    if current_query:
        queries.append("\n".join(current_query))
        
    return [q.strip() for q in queries if q.strip()]

def seed_database():
    print("Starting Neo4j database seeding...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cypher_path = os.path.join(script_dir, "init_graph.cypher")
    
    queries = load_cypher_file(cypher_path)
    if not queries:
        print("No Cypher queries found to execute.")
        return

    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            # Clean existing nodes and relationships first to avoid duplicates
            print("Cleaning existing graph data...")
            session.run("MATCH (n) DETACH DELETE n")
            
            # Execute initialization queries
            print(f"Executing {len(queries)} seeding queries...")
            for i, query in enumerate(queries, 1):
                print(f"Executing query {i}/{len(queries)}...")
                session.run(query)
                
            print("Successfully seeded Neo4j graph database!")
            
        driver.close()
    except Exception as e:
        print(f"Error connecting to or seeding Neo4j database: {e}")
        sys.exit(1)

if __name__ == "__main__":
    seed_database()
