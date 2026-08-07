from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class ProjectCreate(BaseSchema):
    """
    DTO for creating a new Project entity.
    """
    name: str = Field(..., min_length=2, max_length=100, description="Project name")
    slug: str = Field(..., min_length=2, max_length=100, description="Unique project slug")
    description: Optional[str] = Field(None, max_length=500, description="Project description")
    workspace_id: int = Field(..., description="Parent workspace ID")
    status: str = Field("active", description="Project status")
    is_active: bool = Field(True, description="Active status flag")


class ProjectUpdate(BaseSchema):
    """
    DTO for updating an existing Project entity.
    """
    name: Optional[str] = Field(None, min_length=2, max_length=100, description="Updated project name")
    slug: Optional[str] = Field(None, min_length=2, max_length=100, description="Updated project slug")
    description: Optional[str] = Field(None, max_length=500, description="Updated description")
    status: Optional[str] = Field(None, description="Updated project status")
    is_active: Optional[bool] = Field(None, description="Updated active flag")


class ProjectRead(TimestampSchema):
    """
    DTO for reading Project entity details.
    """
    name: str = Field(..., description="Project name")
    slug: str = Field(..., description="Project slug")
    description: Optional[str] = Field(None, description="Project description")
    workspace_id: int = Field(..., description="Parent workspace ID")
    status: str = Field(..., description="Project status")


class ProjectResponse(SuccessResponse[ProjectRead]):
    """
    Response envelope DTO for single Project entity payload.
    """
    pass


class ProjectListResponse(PaginatedResponse[ProjectRead]):
    """
    Response envelope DTO for paginated Project entities payload.
    """
    pass
