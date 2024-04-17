from fastapi import Depends
from typing import Annotated, Dict, get_type_hints, Type
from config.config import get_redis_connection, Settings
from models.user import User
import json
import errors
import success

async def format_message(updated_user: User, action: str, amount: int, issuer: str):
    # TODO add in the message function to build the response
