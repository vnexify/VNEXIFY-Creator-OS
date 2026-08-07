from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_content_service
from ...services.content_service import ContentService
from ...schemas.content import (
    ContentCreate,
    ContentUpdate,
    ContentRead,
    ContentResponse,
    ContentListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=ContentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Content",
    description="Creates a new Content entity.",
)
def create_content(
    content_in: ContentCreate,
    db: Session = Depends(get_db),
    content_service: ContentService = Depends(get_content_service),
) -> Any:
    existing_content = content_service.get_by_slug(db, content_in.workspace_id, content_in.slug)
    if existing_content:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Content with slug '{content_in.slug}' already exists in workspace {content_in.workspace_id}.",
        )
    created_content = content_service.create(db, content_in.model_dump())
    return ContentResponse(
        success=True,
        message="Content created successfully",
        data=ContentRead.model_validate(created_content),
    )


@router.get(
    "/",
    response_model=ContentListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Content",
    description="Retrieves a paginated list of Content items.",
)
def list_content(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    content_service: ContentService = Depends(get_content_service),
) -> Any:
    paginated_data = content_service.paginate(db, page=page, page_size=page_size)
    items_read = [ContentRead.model_validate(item) for item in paginated_data["items"]]
    return ContentListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{content_id}",
    response_model=ContentResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Content by ID",
    description="Retrieves Content details by primary key ID.",
)
def get_content(
    content_id: int,
    db: Session = Depends(get_db),
    content_service: ContentService = Depends(get_content_service),
) -> Any:
    content_item = content_service.get(db, content_id)
    if not content_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content with ID {content_id} not found.",
        )
    return ContentResponse(
        success=True,
        message="Content retrieved successfully",
        data=ContentRead.model_validate(content_item),
    )


@router.put(
    "/{content_id}",
    response_model=ContentResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Content",
    description="Updates existing Content attributes.",
)
def update_content(
    content_id: int,
    content_in: ContentUpdate,
    db: Session = Depends(get_db),
    content_service: ContentService = Depends(get_content_service),
) -> Any:
    content_item = content_service.get(db, content_id)
    if not content_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content with ID {content_id} not found.",
        )
    updated_content = content_service.update(db, content_item, content_in.model_dump(exclude_unset=True))
    return ContentResponse(
        success=True,
        message="Content updated successfully",
        data=ContentRead.model_validate(updated_content),
    )


@router.delete(
    "/{content_id}",
    response_model=ContentResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Content",
    description="Deletes Content entity by ID.",
)
def delete_content(
    content_id: int,
    db: Session = Depends(get_db),
    content_service: ContentService = Depends(get_content_service),
) -> Any:
    content_item = content_service.get(db, content_id)
    if not content_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content with ID {content_id} not found.",
        )
    content_service.delete(db, content_id)
    return ContentResponse(
        success=True,
        message=f"Content with ID {content_id} deleted successfully",
        data=None,
    )
