from datetime import datetime, timezone
from typing import Any, List, Optional
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from ..logging.logger import logger


class AppException(Exception):
    def __init__(
        self,
        code: str = "INTERNAL_SERVER_ERROR",
        message: str = "An unexpected error occurred",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        details: Optional[List[Any]] = None,
    ):
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details or []
        super().__init__(self.message)


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found", details: Optional[List[Any]] = None):
        super().__init__(
            code="RESOURCE_NOT_FOUND",
            message=message,
            status_code=status.HTTP_404_NOT_FOUND,
            details=details,
        )


class ValidationException(AppException):
    def __init__(self, message: str = "Validation failed", details: Optional[List[Any]] = None):
        super().__init__(
            code="VALIDATION_ERROR",
            message=message,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            details=details,
        )


def build_error_response(code: str, message: str, details: List[Any], request: Request) -> JSONResponse:
    request_id = request.headers.get("X-Request-ID", "unknown")
    payload = {
        "success": False,
        "error": {
            "code": code,
            "message": message,
            "details": details,
        },
        "meta": {
            "requestId": request_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    }
    return payload


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        logger.error(f"AppException [{exc.code}]: {exc.message}")
        payload = build_error_response(exc.code, exc.message, exc.details, request)
        return JSONResponse(status_code=exc.status_code, content=payload)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.warning(f"ValidationError on path {request.url.path}: {exc.errors()}")
        details = [{"field": ".".join(str(loc) for loc in err.get("loc", [])), "issue": err.get("msg")} for err in exc.errors()]
        payload = build_error_response("VALIDATION_ERROR", "Request validation failed", details, request)
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=payload)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled Exception: {str(exc)}", exc_info=True)
        payload = build_error_response("INTERNAL_SERVER_ERROR", "An unhandled server exception occurred", [], request)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=payload)
