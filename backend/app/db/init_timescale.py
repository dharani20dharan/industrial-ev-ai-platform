import asyncio
import logging
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from app.core.config import settings
from app.models.domain import Base

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

DATABASE_URL = settings.database_url 

async def init_db():
    engine = create_async_engine(DATABASE_URL, echo=False)

    async with engine.begin() as conn:
        # Step 1: Initialize standardized base schemas
        await conn.run_sync(Base.metadata.create_all)
        
        # Step 2: Convert structural physical logs to partitioned hypertables
        hypertable_queries = [
            "SELECT create_hypertable('telemetry', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('battery_records', 'timestamp', if_not_exists => TRUE);",
            "SELECT create_hypertable('location_history', 'timestamp', if_not_exists => TRUE);"
        ]

        for query in hypertable_queries:
            try:
                await conn.execute(text(query))
            except Exception:
                pass

    await engine.dispose()
    print(">>> TimescaleDB Initialization Matrix Complete <<<")

if __name__ == "__main__":
    asyncio.run(init_db())