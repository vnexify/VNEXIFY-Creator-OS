from typing import Generator
from sqlalchemy.orm import Session
from ..database.session import get_db_session
from ..services import (
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


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency yielding a thread-safe Database Session from DatabaseSessionManager.
    """
    yield from get_db_session()


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
