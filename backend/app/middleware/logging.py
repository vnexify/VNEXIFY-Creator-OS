import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from ..logging.logger import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware for logging HTTP request performance and adding request IDs.
    """
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        start_time = time.time()

        response = await call_next(request)

        process_time_ms = (time.time() - start_time) * 1000
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time-Ms"] = f"{process_time_ms:.2f}"

        logger.info(
            f"[{request.method}] {request.url.path} -> {response.status_code} "
            f"({process_time_ms:.2f}ms) [ReqID: {request_id}]"
        )

        return response
