from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Application
    env: str = "development"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # Supabase
    supabase_url: str | None = None
    supabase_publishable_key: str | None = None
    supabase_secret_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

@lru_cache
def get_settings() -> Settings:
    """
    Cached settings instance.
    Ensures settings are loaded once per process.
    """
    return Settings()