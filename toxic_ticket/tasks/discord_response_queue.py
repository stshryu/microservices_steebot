from fastapi import Depends
from typing import Annotated, Dict, get_type_hints, Type
from config.config import get_redis_connection, Settings
from models.user import User
import json
import errors
import success

async def send_message_to_server(message_args):
    result = await format_ticket_message(**message_args)
    return await push_event_to_queue(result.unpack())

async def send_error_message_to_server(message_args):
    result = await format_error_message(**message_args)
    return await push_event_to_queue(result.unpack())

async def send_user_to_server(user: User, channel: str):
    result = await format_user_message(user, channel)
    return await push_event_to_queue(result.unpack())

async def push_event_to_queue(message: str):
    client = await get_redis_connection()
    await client.publish(Settings().DISCORD_WORKER_CHANNEL, message)
    return success.Success({})

async def format_error_message(username: str, channel: str, action: str):
    response = { "channel": channel }
    match action:
        case "missing_user":
            message = f"<@{username}> doesn't exist as a user in the TT system yet, an admin needs to issue something to the user for the first time before statistics can be retrieved."
        case _:
            message = f"An unexpected error occured"
    response['message'] = message
    return success.Success(json.dumps(response))

async def format_ticket_message(updated_user: User, action: str, amount: int, issuer: str, channel: str):
    response = { "channel": channel }
    match action:
        case "toxic_ticket":
            message = f"<@{updated_user.username}> has been issued {amount} toxic tickets by <@{issuer}>"
        case "mini_tt":
            message = f"<@{updated_user.username}> has been issued {amount} mini TT's by <@{issuer}>"
        case "pma_sticker":
            message = f"<@{updated_user.username}> has been awarded {amount} PMA stickers by <@{issuer}>"
        case _:
            message = f"TT System has been updated"
    response['message'] = message
    return success.Success(json.dumps(response))

async def format_user_message(user: User, channel: str):
    response = { "channel": channel }
    message = f"<@{user.username}> Lifetime Stats:\nToxic Tickets: {user.toxic_tickets}\nMini TT's: {user.mini_toxic_tickets}\nPMA Stickers: {user.pma_stickers}"
    response['message'] = message
    return success.Success(json.dumps(response))


