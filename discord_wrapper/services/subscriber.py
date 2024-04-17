import success
import errors
import json
from config.config import get_redis_connection, Settings
from services.utils.redis_message import RedisMessage

async def process_channel():
    client = await get_redis_connection()
    channel = client.pubsub()
    await channel.subscribe(Settings().DISCORD_WORKER_CHANNEL)
    async for message in channel.listen():
        redis_msg = RedisMessage(message)
        if redis_msg.msgtype != 'subscribe': await process_message(redis_msg.data)

async def process_message(message):
    print(message)
