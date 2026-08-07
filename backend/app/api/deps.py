from typing import Generator, Optional
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from ..database.session import get_db_session
from ..core.security import decode_token
from ..models.user import User
from ..services import (
    AuthService,
    UserService,
    WorkspaceService,
    ProjectService,
    FolderService,
    CategoryService,
    TagService,
    ContentService,
    MediaService,
    ScheduleService,
    AIProviderService,
    AIJobService,
    ExportJobService,
    AnalyticsService,
    NotificationService,
    ApplicationSettingService,
    SystemLogService,
)

security_scheme = HTTPBearer(auto_error=False)


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency yielding a thread-safe Database Session from DatabaseSessionManager.
    """
    yield from get_db_session()


def get_auth_service() -> AuthService:
    return AuthService()


def get_user_service() -> UserService:
    return UserService()


def get_workspace_service() -> WorkspaceService:
    return WorkspaceService()


def get_project_service() -> ProjectService:
    return ProjectService()


def get_folder_service() -> FolderService:
    return FolderService()


def get_category_service() -> CategoryService:
    return CategoryService()


def get_tag_service() -> TagService:
    return TagService()


def get_content_service() -> ContentService:
    return ContentService()


def get_media_service() -> MediaService:
    return MediaService()


def get_schedule_service() -> ScheduleService:
    return ScheduleService()


def get_ai_provider_service() -> AIProviderService:
    return AIProviderService()


def get_ai_job_service() -> AIJobService:
    return AIJobService()


def get_export_job_service() -> ExportJobService:
    return ExportJobService()


def get_analytics_service() -> AnalyticsService:
    return AnalyticsService()


def get_notification_service() -> NotificationService:
    return NotificationService()


def get_application_setting_service() -> ApplicationSettingService:
    return ApplicationSettingService()


def get_system_log_service() -> SystemLogService:
    return SystemLogService()


def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service),
) -> User:
    """
    Authentication dependency decoding the Bearer JWT access token and returning the current User.
    Raises HTTP 401 Unauthorized if token is missing, invalid, or expired.
    """
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication credentials were not provided.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = credentials.credentials
    try:
        payload = decode_token(token)
        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type. Access token required.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        sub = payload.get("sub")
        if not sub:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token subject.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user_id = int(sub)
        user = user_service.get(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User associated with token not found.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials or token expired.",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Authentication dependency verifying the current user is active.
    Raises HTTP 400 Bad Request if user account is deactivated.
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user account.",
        )
    return current_user
