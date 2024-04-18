from fastapi import Depends
from typing import Annotated, Dict, get_type_hints, Type
from config.config import get_redis_connection, Settings
from models.user import User
import json
import errors
import success

async def send_message_to_server(message_args):
    result = await format_message(**message_args)
    return await push_event_to_queue(result.unpack())

async def push_event_to_queue(message: str):
    client = await get_redis_connection()
    await client.publish(Settings().DISCORD_WORKER_CHANNEL, message)
    return success.Success({})

async def format_message(updated_user: User, action: str, amount: int, issuer: str):
    match action:
        case "toxic_ticket":
            message = f"{User.username} has been given {amount} toxic tickets by {issuer}"
        case "mini_tt":
            message = f"{User.username} has been given {amount} mini TT's by {issuer}"
        case "pma_sticker":
            message = f"{User.username} has been awarded {amount} PMA stickers by {issuer}"
        case _:
            message = f"TT System has been updated"
    return success.Success(message)
