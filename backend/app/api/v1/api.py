from fastapi import APIRouter
from .health import router as health_router
from .users import router as users_router
from .workspaces import router as workspaces_router
from .projects import router as projects_router
from .folders import router as folders_router
from .categories import router as categories_router
from .tags import router as tags_router
from .contents import router as contents_router
from .media import router as media_router
from .schedules import router as schedules_router
from .ai_providers import router as ai_providers_router
from .ai_jobs import router as ai_jobs_router
from .export_jobs import router as export_jobs_router
from .analytics import router as analytics_router
from .notifications import router as notifications_router
from .application_settings import router as application_settings_router
from .system_logs import router as system_logs_router

api_v1_router = APIRouter()

# Include Health router
api_v1_router.include_router(health_router, tags=["Health"])

# Include Entity routers
api_v1_router.include_router(users_router, prefix="/users", tags=["Users"])
api_v1_router.include_router(workspaces_router, prefix="/workspaces", tags=["Workspaces"])
api_v1_router.include_router(projects_router, prefix="/projects", tags=["Projects"])
api_v1_router.include_router(folders_router, prefix="/folders", tags=["Folders"])
api_v1_router.include_router(categories_router, prefix="/categories", tags=["Categories"])
api_v1_router.include_router(tags_router, prefix="/tags", tags=["Tags"])
api_v1_router.include_router(contents_router, prefix="/contents", tags=["Contents"])
api_v1_router.include_router(media_router, prefix="/media", tags=["Media"])
api_v1_router.include_router(schedules_router, prefix="/schedules", tags=["Schedules"])
api_v1_router.include_router(ai_providers_router, prefix="/ai-providers", tags=["AI Providers"])
api_v1_router.include_router(ai_jobs_router, prefix="/ai-jobs", tags=["AI Jobs"])
api_v1_router.include_router(export_jobs_router, prefix="/export-jobs", tags=["Export Jobs"])
api_v1_router.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
api_v1_router.include_router(notifications_router, prefix="/notifications", tags=["Notifications"])
api_v1_router.include_router(application_settings_router, prefix="/settings", tags=["Application Settings"])
api_v1_router.include_router(system_logs_router, prefix="/system-logs", tags=["System Logs"])
