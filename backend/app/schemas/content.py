from typing import Optional, List, Dict, Any
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class ContentCreate(BaseSchema):
    """
    DTO for creating a new Content entity.
    """
    title: str = Field(..., min_length=1, max_length=255, description="Content title")
    slug: str = Field(..., min_length=1, max_length=255, description="Unique content slug")
    body: Optional[str] = Field(None, description="Content body text or markdown")
    content_type: str = Field("article", description="Content type identifier")
    status: str = Field("draft", description="Publication status")
    workspace_id: int = Field(..., description="Parent workspace ID")
    project_id: Optional[int] = Field(None, description="Optional associated project ID")
    folder_id: Optional[int] = Field(None, description="Optional associated folder ID")
    category_id: Optional[int] = Field(None, description="Optional associated category ID")
    author_id: int = Field(..., description="Author user ID")
    metadata_json: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata JSON payload")
    is_active: bool = Field(True, description="Active status flag")


class ContentUpdate(BaseSchema):
    """
    DTO for updating an existing Content entity.
    """
    title: Optional[str] = Field(None, min_length=1, max_length=255, description="Updated title")
    slug: Optional[str] = Field(None, min_length=1, max_length=255, description="Updated slug")
    body: Optional[str] = Field(None, description="Updated body text")
    content_type: Optional[str] = Field(None, description="Updated content type")
    status: Optional[str] = Field(None, description="Updated publication status")
    project_id: Optional[int] = Field(None, description="Updated project ID")
    folder_id: Optional[int] = Field(None, description="Updated folder ID")
    category_id: Optional[int] = Field(None, description="Updated category ID")
    metadata_json: Optional[Dict[str, Any]] = Field(None, description="Updated metadata JSON")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class ContentRead(TimestampSchema):
    """
    DTO for reading Content entity details.
    """
    title: str = Field(..., description="Content title")
    slug: str = Field(..., description="Content slug")
    body: Optional[str] = Field(None, description="Content body text")
    content_type: str = Field(..., description="Content type")
    status: str = Field(..., description="Publication status")
    workspace_id: int = Field(..., description="Parent workspace ID")
    project_id: Optional[int] = Field(None, description="Associated project ID")
    folder_id: Optional[int] = Field(None, description="Associated folder ID")
    category_id: Optional[int] = Field(None, description="Associated category ID")
    author_id: int = Field(..., description="Author user ID")
    metadata_json: Optional[Dict[str, Any]] = Field(None, description="Metadata JSON payload")


class ContentResponse(SuccessResponse[ContentRead]):
    """
    Response envelope DTO for single Content entity payload.
    """
    pass


class ContentListResponse(PaginatedResponse[ContentRead]):
    """
    Response envelope DTO for paginated Content entities payload.
    """
    pass
