from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

# 1. Create the Async Engine
engine = create_async_engine(
    settings.database_url,
    echo=False,  # Set to True for debugging SQL queries
    pool_size=20, # Connection pool optimized for high-throughput streaming
    max_overflow=10
)

# 2. Create the Async Session Maker
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False # Prevents SQLAlchemy from issuing extra SELECTs after commit
)

# 3. Dependency function for FastAPI routes and Kafka processors
async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session