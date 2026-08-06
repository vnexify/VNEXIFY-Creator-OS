from fastapi import APIRouter
from .v1.router import v1_router
from .v1.health import get_health, get_status

router = APIRouter()

# Include versioned API routes under /v1
router.include_router(v1_router, prefix="/v1")

# Expose unversioned health routes under /api for backwards compatibility
router.add_api_route("/health", get_health, methods=["GET"], tags=["Health"])
router.add_api_route("/status", get_status, methods=["GET"], tags=["Health"])
