from fastapi import FastAPI

from app.api.routers.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/api")


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Welcome to UniCore API!"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
