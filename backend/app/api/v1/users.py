from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_user_service
from ...services.user_service import UserService
from ...schemas.user import (
    UserCreate,
    UserUpdate,
    UserRead,
    UserResponse,
    UserListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create User",
    description="Registers a new User entity in the system.",
)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service),
) -> Any:
    existing_user = user_service.get_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with email '{user_in.email}' already exists.",
        )
    created_user = user_service.create(db, user_in.model_dump())
    return UserResponse(
        success=True,
        message="User created successfully",
        data=UserRead.model_validate(created_user),
    )


@router.get(
    "/",
    response_model=UserListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Users",
    description="Retrieves a paginated list of Users with limit/offset and page pagination support.",
)
def list_users(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service),
) -> Any:
    paginated_data = user_service.paginate(db, page=page, page_size=page_size)
    items_read = [UserRead.model_validate(item) for item in paginated_data["items"]]
    return UserListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Get User by ID",
    description="Retrieves single User details by primary key ID.",
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service),
) -> Any:
    user = user_service.get(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found.",
        )
    return UserResponse(
        success=True,
        message="User retrieved successfully",
        data=UserRead.model_validate(user),
    )


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Update User",
    description="Updates existing User entity attributes.",
)
def update_user(
    user_id: int,
    user_in: UserUpdate,
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service),
) -> Any:
    user = user_service.get(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found.",
        )
    updated_user = user_service.update(db, user, user_in.model_dump(exclude_unset=True))
    return UserResponse(
        success=True,
        message="User updated successfully",
        data=UserRead.model_validate(updated_user),
    )


@router.delete(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete User",
    description="Deletes User entity by primary key ID.",
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service),
) -> Any:
    user = user_service.get(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found.",
        )
    user_service.delete(db, user_id)
    return UserResponse(
        success=True,
        message=f"User with ID {user_id} deleted successfully",
        data=None,
    )
