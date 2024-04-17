from fastapi import Depends
from typing import Annotated, Dict, get_type_hints, Type
from config.config import get_redis_connection, Settings
from models.user import User
import json
import errors
import success

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
    # TODO: Send this message to the appropriate queue for the discord wrapper service
