from typing import Optional
from beanie import init_beanie
import redis.asyncio as redis
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings
import models as models

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

async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(), document_models=models.__all__
    )

async def get_redis_connection():
    return redis.Redis(
        host=Settings().REDIS_HOST, 
        port=Settings().REDIS_PORT, 
        decode_responses=True
    )


