from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_media_service
from ...services.media_service import MediaService
from ...schemas.media import (
    MediaCreate,
    MediaUpdate,
    MediaRead,
    MediaResponse,
    MediaListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=MediaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Media Asset",
    description="Registers a new Media asset record.",
)
def create_media(
    media_in: MediaCreate,
    db: Session = Depends(get_db),
    media_service: MediaService = Depends(get_media_service),
) -> Any:
    if media_in.file_hash:
        existing_hash = media_service.get_by_hash(db, media_in.file_hash)
        if existing_hash:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Media asset with hash '{media_in.file_hash}' already exists.",
            )
    created_media = media_service.create(db, media_in.model_dump())
    return MediaResponse(
        success=True,
        message="Media asset created successfully",
        data=MediaRead.model_validate(created_media),
    )


@router.get(
    "/",
    response_model=MediaListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Media Assets",
    description="Retrieves a paginated list of Media assets.",
)
def list_media(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    media_service: MediaService = Depends(get_media_service),
) -> Any:
    paginated_data = media_service.paginate(db, page=page, page_size=page_size)
    items_read = [MediaRead.model_validate(item) for item in paginated_data["items"]]
    return MediaListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{media_id}",
    response_model=MediaResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Media Asset by ID",
    description="Retrieves Media asset details by primary key ID.",
)
def get_media(
    media_id: int,
    db: Session = Depends(get_db),
    media_service: MediaService = Depends(get_media_service),
) -> Any:
    media_item = media_service.get(db, media_id)
    if not media_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Media asset with ID {media_id} not found.",
        )
    return MediaResponse(
        success=True,
        message="Media asset retrieved successfully",
        data=MediaRead.model_validate(media_item),
    )


@router.put(
    "/{media_id}",
    response_model=MediaResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Media Asset",
    description="Updates existing Media asset attributes.",
)
def update_media(
    media_id: int,
    media_in: MediaUpdate,
    db: Session = Depends(get_db),
    media_service: MediaService = Depends(get_media_service),
) -> Any:
    media_item = media_service.get(db, media_id)
    if not media_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Media asset with ID {media_id} not found.",
        )
    updated_media = media_service.update(db, media_item, media_in.model_dump(exclude_unset=True))
    return MediaResponse(
        success=True,
        message="Media asset updated successfully",
        data=MediaRead.model_validate(updated_media),
    )


@router.delete(
    "/{media_id}",
    response_model=MediaResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Media Asset",
    description="Deletes Media asset entity by ID.",
)
def delete_media(
    media_id: int,
    db: Session = Depends(get_db),
    media_service: MediaService = Depends(get_media_service),
) -> Any:
    media_item = media_service.get(db, media_id)
    if not media_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Media asset with ID {media_id} not found.",
        )
    media_service.delete(db, media_id)
    return MediaResponse(
        success=True,
        message=f"Media asset with ID {media_id} deleted successfully",
        data=None,
    )
