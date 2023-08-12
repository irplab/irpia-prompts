"""
Main application module
"""
import uvicorn
from fastapi import FastAPI
from app.config import get_app_settings
from app.api.routes.api import router as api_router


def get_application() -> FastAPI:
    """
    Application factory

    :return: FastAPI application
    """
    settings = get_app_settings()

    application = FastAPI()

    application.include_router(api_router, prefix=f"{settings.api_prefix}/{settings.api_version}")

    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
