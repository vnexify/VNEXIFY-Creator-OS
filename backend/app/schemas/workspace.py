from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class WorkspaceCreate(BaseSchema):
    """
    DTO for creating a new Workspace entity.
    """
    name: str = Field(..., min_length=2, max_length=100, description="Workspace name")
    slug: str = Field(..., min_length=2, max_length=100, description="Unique workspace slug")
    description: Optional[str] = Field(None, max_length=500, description="Workspace description")
    owner_id: int = Field(..., description="Workspace owner user ID")
    is_active: bool = Field(True, description="Active workspace flag")


class WorkspaceUpdate(BaseSchema):
    """
    DTO for updating an existing Workspace entity.
    """
    name: Optional[str] = Field(None, min_length=2, max_length=100, description="Updated workspace name")
    slug: Optional[str] = Field(None, min_length=2, max_length=100, description="Updated workspace slug")
    description: Optional[str] = Field(None, max_length=500, description="Updated description")
    owner_id: Optional[int] = Field(None, description="Updated owner user ID")
    is_active: Optional[bool] = Field(None, description="Updated active flag")


class WorkspaceRead(TimestampSchema):
    """
    DTO for reading Workspace entity details.
    """
    name: str = Field(..., description="Workspace name")
    slug: str = Field(..., description="Unique workspace slug")
    description: Optional[str] = Field(None, description="Workspace description")
    owner_id: int = Field(..., description="Workspace owner user ID")


class WorkspaceResponse(SuccessResponse[WorkspaceRead]):
    """
    Response envelope DTO for single Workspace entity payload.
    """
    pass


class WorkspaceListResponse(PaginatedResponse[WorkspaceRead]):
    """
    Response envelope DTO for paginated Workspace entities payload.
    """
    pass
