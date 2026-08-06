from typing import List, Union
from pydantic import AnyHttpUrl
try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "VNEXIFY Creator OS Backend"
    VERSION: str = "0.1"
    API_V1_STR: str = "/api/v1"
    
    # Local loopback server configuration
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    
    # CORS Origins allowed
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8000",
        "*"
    ]
    
    # SQLite Database connection settings
    DATABASE_URL: str = "sqlite:///./backend/db/vnexify.db"
    
    # AI Engine Defaults
    DEFAULT_AI_PROVIDER: str = "Ollama"
    DEFAULT_AI_MODEL: str = "llama3:8b-instruct"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
