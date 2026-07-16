from datetime import datetime, timezone
from typing import Generic, TypeVar, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ConfigDict

T = TypeVar('T', bound=BaseModel)

class EventEnvelope(BaseModel, Generic[T]):
    """Standardized event envelope wrapping all platform domain payloads."""
    
    event_id: UUID = Field(default_factory=uuid4, description="Unique identifier for this specific event instance")
    event_type: str = Field(..., description="The type of event (e.g., 'telemetry.raw', 'battery.alert')")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="UTC timestamp of event generation")
    source: str = Field(..., description="Originating service or simulator node name")
    vehicle_id: str = Field(..., description="Unique immutable ID of the industrial vehicle")
    fleet_id: str = Field(..., description="Identifier for the tracking fleet operational partition")
    correlation_id: UUID = Field(default_factory=uuid4, description="Tracing ID sustained across asynchronous boundaries")
    
    payload: T = Field(..., description="The concrete domain data model matching the event type")

    # FIX: Updated old custom encoder blocks to Pydantic V2 model_config structure
    model_config = ConfigDict(
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            UUID: lambda v: str(v)
        }
    )