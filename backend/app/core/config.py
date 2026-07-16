from typing import List, Optional
from pydantic import Field
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


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__", extra="ignore")
    database_url: str = "postgresql+asyncpg://ev_admin:ev_password@localhost:5432/ev_platform"
    environment: str = Field(default="development")
    debug: bool = Field(default=False)
    mqtt: MqttSettings = MqttSettings()
    kafka: KafkaSettings = KafkaSettings()


settings = AppSettings()