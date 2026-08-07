from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_category_service
from ...services.category_service import CategoryService
from ...schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryRead,
    CategoryResponse,
    CategoryListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Category",
    description="Creates a new Category entity.",
)
def create_category(
    category_in: CategoryCreate,
    db: Session = Depends(get_db),
    category_service: CategoryService = Depends(get_category_service),
) -> Any:
    existing_cat = category_service.get_by_slug(db, category_in.workspace_id, category_in.slug)
    if existing_cat:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Category with slug '{category_in.slug}' already exists in workspace {category_in.workspace_id}.",
        )
    created_cat = category_service.create(db, category_in.model_dump())
    return CategoryResponse(
        success=True,
        message="Category created successfully",
        data=CategoryRead.model_validate(created_cat),
    )


@router.get(
    "/",
    response_model=CategoryListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Categories",
    description="Retrieves a paginated list of Categories.",
)
def list_categories(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    category_service: CategoryService = Depends(get_category_service),
) -> Any:
    paginated_data = category_service.paginate(db, page=page, page_size=page_size)
    items_read = [CategoryRead.model_validate(item) for item in paginated_data["items"]]
    return CategoryListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Category by ID",
    description="Retrieves Category details by primary key ID.",
)
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
    category_service: CategoryService = Depends(get_category_service),
) -> Any:
    category = category_service.get(db, category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with ID {category_id} not found.",
        )
    return CategoryResponse(
        success=True,
        message="Category retrieved successfully",
        data=CategoryRead.model_validate(category),
    )


@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Category",
    description="Updates existing Category attributes.",
)
def update_category(
    category_id: int,
    category_in: CategoryUpdate,
    db: Session = Depends(get_db),
    category_service: CategoryService = Depends(get_category_service),
) -> Any:
    category = category_service.get(db, category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with ID {category_id} not found.",
        )
    updated_cat = category_service.update(db, category, category_in.model_dump(exclude_unset=True))
    return CategoryResponse(
        success=True,
        message="Category updated successfully",
        data=CategoryRead.model_validate(updated_cat),
    )


@router.delete(
    "/{category_id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Category",
    description="Deletes Category entity by ID.",
)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    category_service: CategoryService = Depends(get_category_service),
) -> Any:
    category = category_service.get(db, category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with ID {category_id} not found.",
        )
    category_service.delete(db, category_id)
    return CategoryResponse(
        success=True,
        message=f"Category with ID {category_id} deleted successfully",
        data=None,
    )
