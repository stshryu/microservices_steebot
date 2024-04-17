from typing import Optional

import redis.asyncio as redis
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    REDIS_HOST: Optional[str] = None
    REDIS_PORT: Optional[str] = None
    CELERY_BROKER_URL: Optional[str] = None
    CELERY_RESULT_BACKEND: Optional[str] = None
    TOXIC_TICKET_CHANNEL: Optional[str] = None
    DISCORD_WORKER_CHANNEL: Optional[str] = None

    class Config:
        env_file = ".env.dev"
        from_attributes = True

async def get_redis_connection():
    return redis.Redis(
        host=Settings().REDIS_HOST,
        port=Settings().REDIS_PORT,
        decode_responses=True
    )
