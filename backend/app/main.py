from fastapi import FastAPI
from .core.config import settings
from .logging.logger import logger
from .middleware.cors import setup_cors_middleware
from .middleware.logging import RequestLoggingMiddleware
from .exceptions.handlers import register_exception_handlers
from .api.router import router as api_router
from .api.v1.health import get_health

# Initialize FastAPI application with settings from core/config.py
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
)

# Register CORS Middleware
setup_cors_middleware(app)

# Register Custom Request Logging Middleware
app.add_middleware(RequestLoggingMiddleware)

# Register Global Exception Handlers
register_exception_handlers(app)

# Root level health endpoint (http://127.0.0.1:8000/health)
@app.get("/health", tags=["Health"])
def root_health():
    return get_health()

# Include API Router under /api (exposing /api/v1/... and /api/health)
app.include_router(api_router, prefix="/api")

logger.info(f"Initialized {settings.PROJECT_NAME} v{settings.VERSION} backend foundation.")
