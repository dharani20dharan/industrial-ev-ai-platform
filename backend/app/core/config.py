from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MqttSettings(BaseSettings):
    host: str = Field(default="localhost")
    port: int = Field(default=1883)
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    keepalive: int = Field(default=60)
    client_id: str = Field(default="industrial_ev_streaming_layer")


class KafkaSettings(BaseSettings):
    bootstrap_servers: List[str] = Field(default=["localhost:9092"])
    group_id: str = Field(default="ev_streaming_group")
    auto_offset_reset: str = Field(default="earliest")


class Neo4jSettings(BaseModel):
    uri: str = Field(default="bolt://localhost:7687")
    username: str = Field(default="neo4j")
    password: str = Field(default="ev_password")
    database: str = Field(default="neo4j")


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__", extra="ignore")
    database_url: str = "postgresql+asyncpg://ev_admin:ev_password@localhost:5433/ev_platform"
    redis_url: str = Field(default="redis://localhost:6379")
    environment: str = Field(default="development")
    debug: bool = Field(default=False)
    mqtt: MqttSettings = MqttSettings()
    kafka: KafkaSettings = KafkaSettings()
    neo4j: Neo4jSettings = Neo4jSettings()


settings = AppSettings()