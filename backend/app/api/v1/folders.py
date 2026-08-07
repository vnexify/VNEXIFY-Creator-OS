from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_folder_service
from ...services.folder_service import FolderService
from ...schemas.folder import (
    FolderCreate,
    FolderUpdate,
    FolderRead,
    FolderResponse,
    FolderListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=FolderResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Folder",
    description="Creates a new Folder entity.",
)
def create_folder(
    folder_in: FolderCreate,
    db: Session = Depends(get_db),
    folder_service: FolderService = Depends(get_folder_service),
) -> Any:
    created_folder = folder_service.create(db, folder_in.model_dump())
    return FolderResponse(
        success=True,
        message="Folder created successfully",
        data=FolderRead.model_validate(created_folder),
    )


@router.get(
    "/",
    response_model=FolderListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Folders",
    description="Retrieves a paginated list of Folders.",
)
def list_folders(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    folder_service: FolderService = Depends(get_folder_service),
) -> Any:
    paginated_data = folder_service.paginate(db, page=page, page_size=page_size)
    items_read = [FolderRead.model_validate(item) for item in paginated_data["items"]]
    return FolderListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{folder_id}",
    response_model=FolderResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Folder by ID",
    description="Retrieves Folder details by primary key ID.",
)
def get_folder(
    folder_id: int,
    db: Session = Depends(get_db),
    folder_service: FolderService = Depends(get_folder_service),
) -> Any:
    folder = folder_service.get(db, folder_id)
    if not folder:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Folder with ID {folder_id} not found.",
        )
    return FolderResponse(
        success=True,
        message="Folder retrieved successfully",
        data=FolderRead.model_validate(folder),
    )


@router.put(
    "/{folder_id}",
    response_model=FolderResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Folder",
    description="Updates existing Folder attributes.",
)
def update_folder(
    folder_id: int,
    folder_in: FolderUpdate,
    db: Session = Depends(get_db),
    folder_service: FolderService = Depends(get_folder_service),
) -> Any:
    folder = folder_service.get(db, folder_id)
    if not folder:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Folder with ID {folder_id} not found.",
        )
    updated_folder = folder_service.update(db, folder, folder_in.model_dump(exclude_unset=True))
    return FolderResponse(
        success=True,
        message="Folder updated successfully",
        data=FolderRead.model_validate(updated_folder),
    )


@router.delete(
    "/{folder_id}",
    response_model=FolderResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Folder",
    description="Deletes Folder entity by ID.",
)
def delete_folder(
    folder_id: int,
    db: Session = Depends(get_db),
    folder_service: FolderService = Depends(get_folder_service),
) -> Any:
    folder = folder_service.get(db, folder_id)
    if not folder:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Folder with ID {folder_id} not found.",
        )
    folder_service.delete(db, folder_id)
    return FolderResponse(
        success=True,
        message=f"Folder with ID {folder_id} deleted successfully",
        data=None,
    )
