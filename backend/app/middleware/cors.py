from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..core.config import settings


def setup_cors_middleware(app: FastAPI) -> None:
    """
    Register CORS middleware with origins configured in settings.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
