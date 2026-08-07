from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_application_setting_service
from ...services.application_setting_service import ApplicationSettingService
from ...schemas.application_setting import (
    ApplicationSettingCreate,
    ApplicationSettingUpdate,
    ApplicationSettingRead,
    ApplicationSettingResponse,
    ApplicationSettingListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=ApplicationSettingResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Application Setting",
    description="Registers a new ApplicationSetting key-value pair.",
)
def create_application_setting(
    setting_in: ApplicationSettingCreate,
    db: Session = Depends(get_db),
    setting_service: ApplicationSettingService = Depends(get_application_setting_service),
) -> Any:
    existing_setting = setting_service.get_setting_by_key(db, setting_in.key)
    if existing_setting:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Application setting with key '{setting_in.key}' already exists.",
        )
    created_setting = setting_service.create(db, setting_in.model_dump())
    return ApplicationSettingResponse(
        success=True,
        message="Application setting created successfully",
        data=ApplicationSettingRead.model_validate(created_setting),
    )


@router.get(
    "/",
    response_model=ApplicationSettingListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Application Settings",
    description="Retrieves a paginated list of Application Settings.",
)
def list_application_settings(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    setting_service: ApplicationSettingService = Depends(get_application_setting_service),
) -> Any:
    paginated_data = setting_service.paginate(db, page=page, page_size=page_size)
    items_read = [ApplicationSettingRead.model_validate(item) for item in paginated_data["items"]]
    return ApplicationSettingListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{setting_id}",
    response_model=ApplicationSettingResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Application Setting by ID",
    description="Retrieves Application Setting details by primary key ID.",
)
def get_application_setting(
    setting_id: int,
    db: Session = Depends(get_db),
    setting_service: ApplicationSettingService = Depends(get_application_setting_service),
) -> Any:
    setting_entry = setting_service.get(db, setting_id)
    if not setting_entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Application setting with ID {setting_id} not found.",
        )
    return ApplicationSettingResponse(
        success=True,
        message="Application setting retrieved successfully",
        data=ApplicationSettingRead.model_validate(setting_entry),
    )


@router.put(
    "/{setting_id}",
    response_model=ApplicationSettingResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Application Setting",
    description="Updates existing Application Setting attributes.",
)
def update_application_setting(
    setting_id: int,
    setting_in: ApplicationSettingUpdate,
    db: Session = Depends(get_db),
    setting_service: ApplicationSettingService = Depends(get_application_setting_service),
) -> Any:
    setting_entry = setting_service.get(db, setting_id)
    if not setting_entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Application setting with ID {setting_id} not found.",
        )
    updated_setting = setting_service.update(db, setting_entry, setting_in.model_dump(exclude_unset=True))
    return ApplicationSettingResponse(
        success=True,
        message="Application setting updated successfully",
        data=ApplicationSettingRead.model_validate(updated_setting),
    )


@router.delete(
    "/{setting_id}",
    response_model=ApplicationSettingResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Application Setting",
    description="Deletes Application Setting entity by ID.",
)
def delete_application_setting(
    setting_id: int,
    db: Session = Depends(get_db),
    setting_service: ApplicationSettingService = Depends(get_application_setting_service),
) -> Any:
    setting_entry = setting_service.get(db, setting_id)
    if not setting_entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Application setting with ID {setting_id} not found.",
        )
    setting_service.delete(db, setting_id)
    return ApplicationSettingResponse(
        success=True,
        message=f"Application setting with ID {setting_id} deleted successfully",
        data=None,
    )
