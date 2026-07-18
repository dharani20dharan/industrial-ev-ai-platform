import logging
from typing import Dict, Any
from app.streaming.websocket.adapter import kafka_to_ws_broadcaster
from app.core.cache import cache_manager
from app.core.timescale_supply import timescale_supply_repo

logger = logging.getLogger(__name__)

class SupplyChainProcessor:
    """Processes 'ev.supply_chain' streams for event-driven updates."""

    async def process_event(self, topic: str, event_envelope: Dict[str, Any]) -> None:
        payload = event_envelope.get("payload", {})
        event_type = payload.get("event_type", "UNKNOWN")
        entity_id = payload.get("entity_id", "UNKNOWN")
        
        logger.info(f"[PROCESSOR] Intercepted supply chain event: {event_type} for {entity_id}")

        # Invalidate dashboard caches because the graph state has changed
        await cache_manager.delete("supply_chain:analytics_dependencies")

        if event_type == "RISK_UPDATED":
            risk_score = float(payload.get("new_risk_score", 0.0))
            
            # 1. Store the new risk in TimescaleDB for historical trend analytics
            await timescale_supply_repo.insert_snapshot(
                entity_id=entity_id,
                entity_type=payload.get("entity_type", "Supplier"),
                risk_score=risk_score
            )
            
            # 2. Push real-time alert to UI Dashboards
            await kafka_to_ws_broadcaster(
                topic="ev.supply_chain.alerts",
                payload={
                    "alert_type": "SUPPLY_CHAIN_RISK_INCREASE",
                    "entity_id": entity_id,
                    "new_risk_score": risk_score,
                    "message": f"Risk score for {entity_id} was updated to {risk_score}."
                }
            )
            
        elif event_type == "BOTTLENECK_DETECTED":
            # Direct push to dashboard
            await kafka_to_ws_broadcaster(
                topic="ev.supply_chain.alerts",
                payload={
                    "alert_type": "CRITICAL_BOTTLENECK",
                    "entity_id": entity_id,
                    "message": f"Critical bottleneck detected at {entity_id}."
                }
            )

supply_chain_processor = SupplyChainProcessor()
