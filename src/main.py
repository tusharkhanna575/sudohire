from fastapi import FastAPI

from api.routes.health import router as health_router

app = FastAPI(
    title="SudoHire",
    description="AI-powered resume intelligence platform",
    version="0.1.0",
)

app.include_router(health_router, prefix="/api/v1")