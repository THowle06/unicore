from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import get_settings
from app.core.logging import setup_logging, get_logger

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger = get_logger(__name__)
    logger.info("Starting UniCore API", extra={"env": settings.env})

    yield

    logger.info("Shutting down UniCore API")

app = FastAPI(
    title="UniCore API",
    version="0.1.0",
    lifespan=lifespan,
)

@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    logger = get_logger(__name__)
    logger.debug("Health check requested")

    return {
        "status": "ok",
        "environment": settings.env,
    }