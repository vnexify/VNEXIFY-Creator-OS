from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_tag_service
from ...services.tag_service import TagService
from ...schemas.tag import (
    TagCreate,
    TagUpdate,
    TagRead,
    TagResponse,
    TagListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=TagResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Tag",
    description="Creates a new Tag entity.",
)
def create_tag(
    tag_in: TagCreate,
    db: Session = Depends(get_db),
    tag_service: TagService = Depends(get_tag_service),
) -> Any:
    existing_tag = tag_service.get_by_name(db, tag_in.workspace_id, tag_in.name)
    if existing_tag:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Tag with name '{tag_in.name}' already exists in workspace {tag_in.workspace_id}.",
        )
    created_tag = tag_service.create(db, tag_in.model_dump())
    return TagResponse(
        success=True,
        message="Tag created successfully",
        data=TagRead.model_validate(created_tag),
    )


@router.get(
    "/",
    response_model=TagListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Tags",
    description="Retrieves a paginated list of Tags.",
)
def list_tags(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    tag_service: TagService = Depends(get_tag_service),
) -> Any:
    paginated_data = tag_service.paginate(db, page=page, page_size=page_size)
    items_read = [TagRead.model_validate(item) for item in paginated_data["items"]]
    return TagListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{tag_id}",
    response_model=TagResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Tag by ID",
    description="Retrieves Tag details by primary key ID.",
)
def get_tag(
    tag_id: int,
    db: Session = Depends(get_db),
    tag_service: TagService = Depends(get_tag_service),
) -> Any:
    tag = tag_service.get(db, tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tag with ID {tag_id} not found.",
        )
    return TagResponse(
        success=True,
        message="Tag retrieved successfully",
        data=TagRead.model_validate(tag),
    )


@router.put(
    "/{tag_id}",
    response_model=TagResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Tag",
    description="Updates existing Tag attributes.",
)
def update_tag(
    tag_id: int,
    tag_in: TagUpdate,
    db: Session = Depends(get_db),
    tag_service: TagService = Depends(get_tag_service),
) -> Any:
    tag = tag_service.get(db, tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tag with ID {tag_id} not found.",
        )
    updated_tag = tag_service.update(db, tag, tag_in.model_dump(exclude_unset=True))
    return TagResponse(
        success=True,
        message="Tag updated successfully",
        data=TagRead.model_validate(updated_tag),
    )


@router.delete(
    "/{tag_id}",
    response_model=TagResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Tag",
    description="Deletes Tag entity by ID.",
)
def delete_tag(
    tag_id: int,
    db: Session = Depends(get_db),
    tag_service: TagService = Depends(get_tag_service),
) -> Any:
    tag = tag_service.get(db, tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tag with ID {tag_id} not found.",
        )
    tag_service.delete(db, tag_id)
    return TagResponse(
        success=True,
        message=f"Tag with ID {tag_id} deleted successfully",
        data=None,
    )
