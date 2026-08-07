from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class CategoryCreate(BaseSchema):
    """
    DTO for creating a new Category entity.
    """
    name: str = Field(..., min_length=2, max_length=100, description="Category name")
    slug: str = Field(..., min_length=2, max_length=100, description="Unique category slug")
    description: Optional[str] = Field(None, max_length=500, description="Category description")
    workspace_id: int = Field(..., description="Parent workspace ID")
    is_active: bool = Field(True, description="Active status flag")


class CategoryUpdate(BaseSchema):
    """
    DTO for updating an existing Category entity.
    """
    name: Optional[str] = Field(None, min_length=2, max_length=100, description="Updated category name")
    slug: Optional[str] = Field(None, min_length=2, max_length=100, description="Updated category slug")
    description: Optional[str] = Field(None, max_length=500, description="Updated description")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class CategoryRead(TimestampSchema):
    """
    DTO for reading Category entity details.
    """
    name: str = Field(..., description="Category name")
    slug: str = Field(..., description="Category slug")
    description: Optional[str] = Field(None, description="Category description")
    workspace_id: int = Field(..., description="Parent workspace ID")


class CategoryResponse(SuccessResponse[CategoryRead]):
    """
    Response envelope DTO for single Category entity payload.
    """
    pass


class CategoryListResponse(PaginatedResponse[CategoryRead]):
    """
    Response envelope DTO for paginated Category entities payload.
    """
    pass
