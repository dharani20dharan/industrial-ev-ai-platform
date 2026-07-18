import logging
from typing import Optional
from neo4j import AsyncGraphDatabase, AsyncDriver
from app.core.config import settings

logger = logging.getLogger(__name__)

class Neo4jClient:
    def __init__(self):
        self.driver: Optional[AsyncDriver] = None

    async def connect(self):
        try:
            self.driver = AsyncGraphDatabase.driver(
                settings.neo4j.uri,
                auth=(settings.neo4j.username, settings.neo4j.password),
                max_connection_lifetime=3600,
                max_connection_pool_size=50,
                connection_acquisition_timeout=60.0
            )
            # Verify connectivity
            await self.driver.verify_connectivity()
            logger.info("Successfully connected to Neo4j database.")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j: {e}")
            raise e

    async def close(self):
        if self.driver is not None:
            await self.driver.close()
            logger.info("Neo4j driver connection closed.")

    async def verify_connectivity(self) -> bool:
        if not self.driver:
            return False
        try:
            await self.driver.verify_connectivity()
            return True
        except Exception as e:
            logger.error(f"Neo4j health check failed: {e}")
            return False


neo4j_client = Neo4jClient()


def get_neo4j_driver() -> AsyncDriver:
    if neo4j_client.driver is None:
        raise RuntimeError("Neo4j driver is not initialized. Call connect() first.")
    return neo4j_client.driver


async def get_neo4j_session():
    """Dependency for providing a neo4j session in FastAPI."""
    driver = get_neo4j_driver()
    async with driver.session(database=settings.neo4j.database) as session:
        yield session
