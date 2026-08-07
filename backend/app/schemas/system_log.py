from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class SystemLogCreate(BaseSchema):
    """
    DTO for creating a new SystemLog diagnostic log entry.
    """
    level: str = Field(..., min_length=1, max_length=20, description="Log severity level (INFO, WARNING, ERROR)")
    message: str = Field(..., min_length=1, description="Log message text")
    context: Optional[str] = Field(None, description="Optional diagnostic context or stack trace")
    is_active: bool = Field(True, description="Active status flag")


class SystemLogUpdate(BaseSchema):
    """
    DTO for updating an existing SystemLog diagnostic log entry.
    """
    level: Optional[str] = Field(None, description="Updated severity level")
    message: Optional[str] = Field(None, description="Updated message text")
    context: Optional[str] = Field(None, description="Updated context text")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class SystemLogRead(TimestampSchema):
    """
    DTO for reading SystemLog diagnostic log details.
    """
    level: str = Field(..., description="Log severity level")
    message: str = Field(..., description="Log message text")
    context: Optional[str] = Field(None, description="Diagnostic context")


class SystemLogResponse(SuccessResponse[SystemLogRead]):
    """
    Response envelope DTO for single SystemLog entity payload.
    """
    pass


class SystemLogListResponse(PaginatedResponse[SystemLogRead]):
    """
    Response envelope DTO for paginated SystemLog entities payload.
    """
    pass
