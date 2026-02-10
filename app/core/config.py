from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Supabase settings
    SUPABASE_URL: str | None = None
    SUPABASE_SECRET_KEY: str | None = None
    SUPABASE_PUBLISHABLE_KEY: str | None = None

    # App settings
    DEBUG: bool = False
    SECRET_KEY: str | None = None
    ALLOWED_ORIGINS: str = "http://localhost:3000"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
