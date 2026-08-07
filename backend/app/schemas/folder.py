from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class FolderCreate(BaseSchema):
    """
    DTO for creating a new Folder entity.
    """
    name: str = Field(..., min_length=1, max_length=100, description="Folder name")
    workspace_id: int = Field(..., description="Parent workspace ID")
    parent_id: Optional[int] = Field(None, description="Optional parent folder ID for tree structure")
    is_active: bool = Field(True, description="Active status flag")


class FolderUpdate(BaseSchema):
    """
    DTO for updating an existing Folder entity.
    """
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="Updated folder name")
    parent_id: Optional[int] = Field(None, description="Updated parent folder ID")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class FolderRead(TimestampSchema):
    """
    DTO for reading Folder entity details.
    """
    name: str = Field(..., description="Folder name")
    workspace_id: int = Field(..., description="Parent workspace ID")
    parent_id: Optional[int] = Field(None, description="Parent folder ID")


class FolderResponse(SuccessResponse[FolderRead]):
    """
    Response envelope DTO for single Folder entity payload.
    """
    pass


class FolderListResponse(PaginatedResponse[FolderRead]):
    """
    Response envelope DTO for paginated Folder entities payload.
    """
    pass
