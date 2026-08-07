from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..deps import get_db, get_auth_service, get_current_active_user
from ...models.user import User
from ...services.auth_service import AuthService
from ...schemas.user import UserRead
from ...schemas.auth import (
    RegisterRequest,
    LoginRequest,
    RefreshRequest,
    AuthResponse,
    UserAuthResponse,
)
from ...schemas.base import SuccessResponse

router = APIRouter()


@router.post(
    "/register",
    response_model=UserAuthResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register New User",
    description="Registers a new user account with hashed credentials.",
)
def register(
    reg_in: RegisterRequest,
    db: Session = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
) -> Any:
    try:
        user = auth_service.register(db, reg_in)
        return UserAuthResponse(
            success=True,
            message="User registered successfully",
            data=UserRead.model_validate(user),
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK,
    summary="User Login",
    description="Authenticates user credentials and returns JWT Access and Refresh Tokens.",
)
def login(
    login_in: LoginRequest,
    db: Session = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
) -> Any:
    user = auth_service.authenticate(db, login_in.email, login_in.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user account.",
        )
    tokens = auth_service.create_user_tokens(user.id)
    return AuthResponse(
        success=True,
        message="Authentication successful",
        data=tokens,
    )


@router.post(
    "/refresh",
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK,
    summary="Refresh Token",
    description="Exchanges a valid Refresh Token for a new token pair.",
)
def refresh(
    refresh_in: RefreshRequest,
    db: Session = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
) -> Any:
    try:
        tokens = auth_service.refresh_tokens(db, refresh_in.refresh_token)
        return AuthResponse(
            success=True,
            message="Tokens refreshed successfully",
            data=tokens,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.post(
    "/logout",
    response_model=SuccessResponse,
    status_code=status.HTTP_200_OK,
    summary="User Logout",
    description="Logs out the currently authenticated user.",
)
def logout(
    current_user: User = Depends(get_current_active_user),
) -> Any:
    return SuccessResponse(
        success=True,
        message=f"User {current_user.email} logged out successfully.",
        data=None,
    )


@router.get(
    "/me",
    response_model=UserAuthResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Current User Profile",
    description="Retrieves profile details of the currently authenticated user.",
)
def get_me(
    current_user: User = Depends(get_current_active_user),
) -> Any:
    return UserAuthResponse(
        success=True,
        message="Current user profile retrieved successfully",
        data=UserRead.model_validate(current_user),
    )
