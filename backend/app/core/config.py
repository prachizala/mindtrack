import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MindTrack"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "mindtrack-jwt-super-secret-key-32-chars")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./mindtrack.db")
    # Standard 32-byte urlsafe base64 Fernet key
    ENCRYPTION_MASTER_KEY: str = os.getenv("ENCRYPTION_MASTER_KEY", "7eL7v9y9m1A5Q_r4Z3x1b2C8d9E0f1G2h3I4j5K6l7M=")

    class Config:
        case_sensitive = True

settings = Settings()
