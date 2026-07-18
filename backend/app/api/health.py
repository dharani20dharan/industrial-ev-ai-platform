import logging
from fastapi import APIRouter, HTTPException, status
from app.core.container import container

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/health", tags=["Monitoring"])

@router.get("")
async def liveness_check():
    """Basic HTTP liveness probe to verify the API event loop is running."""
    return {"status": "alive", "service": "streaming_layer"}

@router.get("/mqtt")
async def mqtt_readiness_check():
    """Verifies the Mosquitto MQTT broker connection is active."""
    try:
        mqtt = container.mqtt_client
        # Verify the client exists and the background consumption task is actively running
        if mqtt and mqtt._consume_task and not mqtt._consume_task.done():
            return {"status": "connected", "protocol": "mqtt"}
    except RuntimeError:
        # Caught if the DI container hasn't initialized the client yet
        pass
        
    logger.warning("MQTT health check failed.")
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
        detail="MQTT broker connection is not active."
    )

@router.get("/kafka")
async def kafka_readiness_check():
    """Verifies both Kafka Producer and Consumer are active."""
    try:
        producer = container.kafka_producer
        consumer = container.kafka_consumer
        
        is_producer_ok = producer and producer.producer
        is_consumer_ok = consumer and consumer._consume_task and not consumer._consume_task.done()
        
        if is_producer_ok and is_consumer_ok:
            return {"status": "connected", "protocol": "kafka", "components": ["producer", "consumer"]}
            
    except RuntimeError:
        pass
        
    logger.warning("Kafka health check failed.")
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
        detail="Kafka event bus connections are not fully active."
    )

@router.get("/neo4j")
async def neo4j_readiness_check():
    """Verifies the Neo4j Graph Database connection is active."""
    try:
        from app.core.neo4j import get_neo4j_driver
        driver = get_neo4j_driver()
        async with driver.session() as session:
            result = await session.run("MATCH (n) RETURN count(n) as count")
            record = await result.single()
            node_count = record["count"] if record else 0
            
        return {"status": "connected", "protocol": "bolt", "node_count": node_count}
    except Exception as e:
        logger.warning(f"Neo4j health check failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="Neo4j graph database connection is not active."
        )