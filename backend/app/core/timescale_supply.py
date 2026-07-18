import logging
from typing import List
from datetime import datetime
from app.db.session import AsyncSessionLocal
from app.models.domain import SupplyChainHistory
from sqlalchemy.future import select

logger = logging.getLogger(__name__)

class TimescaleSupplyRepository:
    """Manages historical tracking of supply chain analytics in TimescaleDB."""

    async def insert_snapshot(self, entity_id: str, entity_type: str, risk_score: float, depth: float = 0.0, downstream_impacts: int = 0) -> None:
        try:
            record = SupplyChainHistory(
                entity_id=entity_id,
                entity_type=entity_type,
                risk_score=risk_score,
                dependency_depth=depth,
                downstream_impacts=downstream_impacts,
                timestamp=datetime.utcnow()
            )
            async with AsyncSessionLocal() as session:
                session.add(record)
                await session.commit()
                logger.debug(f"Saved historical snapshot for {entity_type} {entity_id}")
        except Exception as e:
            logger.error(f"Failed to save supply chain history for {entity_id}: {e}")

    async def get_historical_trends(self, entity_id: str, limit: int = 30) -> List[SupplyChainHistory]:
        try:
            async with AsyncSessionLocal() as session:
                stmt = select(SupplyChainHistory).where(
                    SupplyChainHistory.entity_id == entity_id
                ).order_by(SupplyChainHistory.timestamp.asc()).limit(limit)
                
                result = await session.execute(stmt)
                return result.scalars().all()
        except Exception as e:
            logger.error(f"Failed to query supply chain history for {entity_id}: {e}")
            return []

timescale_supply_repo = TimescaleSupplyRepository()
