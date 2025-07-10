# crazy dev mood
from pydantic import BaseSettings, RedisDsn

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    GOOGLE_AI_KEY: str
    REDIS_URL: RedisDsn = "redis://redis:6379"

    class Config:
        env_file = ".env"

settings = Settings()
