from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    secret_key: str
    frontend_url: str = "http://localhost:5173"
    access_token_expire_minutes: int = 60


settings = Settings()