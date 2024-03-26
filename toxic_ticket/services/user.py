from fastapi import Depends
from typing import Annotated
from database.database import *
from models.user import User
from config.config import get_redis_connection

"""
Example redis usage template:
    ...
client = await get_redis_connection()
await client.set(i, "hello")
print(f"Redis key: {await client.get(1)}")
await client.close()
    ...
"""

async def get_admin() -> bool:
    return False

async def get_toxic_ticket_admin(username: str) -> bool:
    return await get_ttadmin(username)

async def get_users_service():
    users = await retrieve_users()
    return users

async def get_user_service(id: PydanticObjectId):
    user = await retrieve_user(id)
    return user

async def add_user_service(user: User):
    new_user = await add_user(user)
    return new_user

async def delete_user_service(id: PydanticObjectId, is_admin: Annotated[bool, Depends(get_admin)]):
    deleted_user = await delete_user(id) if is_admin else False
    return deleted_user

async def add_toxic_ticket_service(id: PydanticObjectId, is_ttadmin: Annotated[bool, Depends(get_toxic_ticket_admin)]):
    updated_user = await add_toxic_ticket(id) if is_ttadmin else False
    return updated_user

async def add_mini_toxic_ticket_service(id: PydanticObjectId, is_ttadmin: Annotated[bool, Depends(get_toxic_ticket_admin)]):
    updated_user = await add_mini_toxic_ticket(id) if is_ttadmin else False
    return updated_user

async def add_pma_sticker_service(id: PydanticObjectId, is_ttadmin: Annotated[bool, Depends(get_toxic_ticket_admin)]):
    updated_user = await add_pma_sticker(id) if is_ttadmin else False
    return updated_user
