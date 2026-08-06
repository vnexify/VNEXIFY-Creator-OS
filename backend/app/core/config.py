from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "VNEXIFY Creator OS Backend"
    database_url: str = "sqlite:///../db/vnexify.db"


settings = Settings()
