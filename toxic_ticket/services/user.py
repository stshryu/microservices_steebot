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

Example redis pubsub template:
    ...
client = await get_redis_connection()
channel = client.pubsub()
await channel.subscribe({channel_id})
return channel
    ...
"""

async def get_admin() -> bool:
    return False

async def get_toxic_ticket_admin(issuer: str) -> bool:
    return await get_tt_admin(issuer)

async def get_users_service():
    users = await retrieve_users()
    return users

async def get_user_service(id: PydanticObjectId):
    user = await retrieve_user(id)
    return user

async def get_user_by_name_service(username: str):
    user = await get_user_by_name(username)
    return user 

async def add_user_service(user: User):
    new_user = await add_user(user)
    return new_user

async def delete_user_service(id: PydanticObjectId, is_admin: Annotated[bool, Depends(get_admin)]):
    deleted_user = await delete_user(id) if is_admin else False
    return deleted_user

# Keep in mind that Depends() only works when calling from within the FastAPI context. Calling this function directly will not have the intended effect.
# To keep the validation in place, call get_toxic_ticket_admin(issuer) -> and pass that parameter into is_ttadmin to emulate the dependency.
async def add_toxic_ticket_service(id: PydanticObjectId, amount: int, is_ttadmin: Annotated[str, Depends(get_toxic_ticket_admin)]):
    updated_user = await add_bulk_toxic_ticket(id, amount) if is_ttadmin else False
    return updated_user

async def add_mini_toxic_ticket_service(id: PydanticObjectId, amount: int, is_ttadmin: Annotated[bool, Depends(get_toxic_ticket_admin)]):
    updated_user = await add_mini_toxic_ticket(id, amount) if is_ttadmin else False
    return updated_user

async def add_pma_sticker_service(id: PydanticObjectId, amount: int, is_ttadmin: Annotated[bool, Depends(get_toxic_ticket_admin)]):
    updated_user = await add_pma_sticker(id, amount) if is_ttadmin else False
    return updated_user
