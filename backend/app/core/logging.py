import sys
import logging
import json
from datetime import datetime, timezone
from app.core.config import settings


class JsonFormatter(logging.Formatter):
    """Formats log records as single-line JSON strings for production parsing."""
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        if hasattr(record, "correlation_id"):
            log_data["correlation_id"] = record.correlation_id
        if hasattr(record, "vehicle_id"):
            log_data["vehicle_id"] = record.vehicle_id
            
        return json.dumps(log_data)


def setup_logging() -> None:
    """Initializes global logging configurations."""
    root_logger = logging.getLogger()
    
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        
    handler = logging.StreamHandler(sys.stdout)
    
    if hasattr(settings, "environment") and settings.environment.lower() == "production":
        handler.setFormatter(JsonFormatter())
        root_logger.setLevel(logging.INFO)
    else:
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        root_logger.setLevel(logging.DEBUG if getattr(settings, "debug", True) else logging.INFO)
        
    root_logger.addHandler(handler)
    
    logging.getLogger("aiokafka").setLevel(logging.WARNING)
    logging.getLogger("aiomqtt").setLevel(logging.WARNING)