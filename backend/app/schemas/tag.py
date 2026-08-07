from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class TagCreate(BaseSchema):
    """
    DTO for creating a new Tag entity.
    """
    name: str = Field(..., min_length=1, max_length=50, description="Tag name")
    workspace_id: int = Field(..., description="Parent workspace ID")
    is_active: bool = Field(True, description="Active status flag")


class TagUpdate(BaseSchema):
    """
    DTO for updating an existing Tag entity.
    """
    name: Optional[str] = Field(None, min_length=1, max_length=50, description="Updated tag name")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class TagRead(TimestampSchema):
    """
    DTO for reading Tag entity details.
    """
    name: str = Field(..., description="Tag name")
    workspace_id: int = Field(..., description="Parent workspace ID")


class TagResponse(SuccessResponse[TagRead]):
    """
    Response envelope DTO for single Tag entity payload.
    """
    pass


class TagListResponse(PaginatedResponse[TagRead]):
    """
    Response envelope DTO for paginated Tag entities payload.
    """
    pass
