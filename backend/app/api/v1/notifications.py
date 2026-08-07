from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_notification_service
from ...services.notification_service import NotificationService
from ...schemas.notification import (
    NotificationCreate,
    NotificationUpdate,
    NotificationRead,
    NotificationResponse,
    NotificationListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=NotificationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Notification",
    description="Registers a new Notification entity.",
)
def create_notification(
    notification_in: NotificationCreate,
    db: Session = Depends(get_db),
    notification_service: NotificationService = Depends(get_notification_service),
) -> Any:
    created_notif = notification_service.create(db, notification_in.model_dump())
    return NotificationResponse(
        success=True,
        message="Notification created successfully",
        data=NotificationRead.model_validate(created_notif),
    )


@router.get(
    "/",
    response_model=NotificationListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Notifications",
    description="Retrieves a paginated list of Notifications.",
)
def list_notifications(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    notification_service: NotificationService = Depends(get_notification_service),
) -> Any:
    paginated_data = notification_service.paginate(db, page=page, page_size=page_size)
    items_read = [NotificationRead.model_validate(item) for item in paginated_data["items"]]
    return NotificationListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{notification_id}",
    response_model=NotificationResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Notification by ID",
    description="Retrieves Notification details by primary key ID.",
)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    notification_service: NotificationService = Depends(get_notification_service),
) -> Any:
    notification = notification_service.get(db, notification_id)
    if not notification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Notification with ID {notification_id} not found.",
        )
    return NotificationResponse(
        success=True,
        message="Notification retrieved successfully",
        data=NotificationRead.model_validate(notification),
    )


@router.put(
    "/{notification_id}",
    response_model=NotificationResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Notification",
    description="Updates existing Notification attributes.",
)
def update_notification(
    notification_id: int,
    notification_in: NotificationUpdate,
    db: Session = Depends(get_db),
    notification_service: NotificationService = Depends(get_notification_service),
) -> Any:
    notification = notification_service.get(db, notification_id)
    if not notification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Notification with ID {notification_id} not found.",
        )
    updated_notif = notification_service.update(db, notification, notification_in.model_dump(exclude_unset=True))
    return NotificationResponse(
        success=True,
        message="Notification updated successfully",
        data=NotificationRead.model_validate(updated_notif),
    )


@router.delete(
    "/{notification_id}",
    response_model=NotificationResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Notification",
    description="Deletes Notification entity by ID.",
)
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    notification_service: NotificationService = Depends(get_notification_service),
) -> Any:
    notification = notification_service.get(db, notification_id)
    if not notification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Notification with ID {notification_id} not found.",
        )
    notification_service.delete(db, notification_id)
    return NotificationResponse(
        success=True,
        message=f"Notification with ID {notification_id} deleted successfully",
        data=None,
    )
