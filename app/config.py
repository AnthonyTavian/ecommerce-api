from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str 
    
    # JWT
    SECRET_KEY: str 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # App
    APP_NAME: str = "E-commerce API"
    APP_VERSION: str = "1.0.0"

    ALLOWED_ORIGINS: str = "*"
    
    class Config:
        env_file = ".env"

settings = Settings()