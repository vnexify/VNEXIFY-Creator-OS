from fastapi import APIRouter
from ...core.config import settings

router = APIRouter()


@router.get("/health")
def get_health():
    """
    Health check endpoint for frontend and system diagnostic telemetry.
    Returns status: ok and current backend version.
    """
    return {
        "status": "ok",
        "version": settings.VERSION,
    }


@router.get("/status")
def get_status():
    """
    Detailed system status placeholder endpoint.
    """
    return {
        "status": "ok",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": "development",
    }
