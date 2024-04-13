import redis
from fastapi import FastAPI
from config.config import get_redis_connection, Settings

async def process_channel():
    client = await get_redis_connection()
    channel = client.pubsub()
    await channel.subscribe(Settings().TOXIC_TICKET_CHANNEL)
    async for messages in channel.listen():
        print(messages)
