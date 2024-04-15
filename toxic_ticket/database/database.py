from typing import List, Union
from beanie import PydanticObjectId
from models.admin import Admin
from models.user import User

admin_collection = Admin
user_collection = User

async def get_tt_admin(admin_username: str) -> bool:
    admin_exists = await Admin.find_one(Admin.username == admin_username)
    if admin_exists:
        return True
    return False

async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin

async def retrieve_users() -> List[User]:
    users = await user_collection.all().to_list()
    return users

async def add_user(new_user: User) -> User:
    user = await new_user.create()
    return user

async def get_user(id: PydanticObjectId) -> User:
    user = await user_collection.get(id)
    return user if user else False 

async def get_user_by_name(username: str) -> User:
    user = await User.find_one(User.username == username)
    return user if user else False

async def delete_user(id: PydanticObjectId) -> bool:
    user = await user_collection.get(id)
    if user:
        await user.delete()
        return True

async def add_toxic_ticket(id) -> Union[bool, User]: 
    user = await user_collection.get(id)
    if user:
        user.toxic_tickets += 1 
        await user.save()
        return user 
    return False

async def add_bulk_toxic_ticket(id, amount: int) -> Union[bool, User]:
    user = await user_collection.get(id)
    if user:
        user.toxic_tickets += amount
        await user.save()
        return user
    return False

async def add_mini_toxic_ticket(id) -> Union[bool, User]:
    user = await user_collection.get(id)
    if user:
        user.mini_toxic_tickets += 1
        await user.save()
        return user
    return False

async def add_bulk_mini_toxic_ticket(id, amount) -> Union[bool, User]:
    user = await user_collection.get(id)
    if user:
        user.mini_toxic_tickets += amount
        await user.save()
        return user
    return False

async def add_pma_sticker(id) -> Union[bool, User]:
    user = await user_collection.get(id)
    if user:
        user.pma_stickers += 1
        await user.save()
        return user
    return False

async def add_bulk_pma_sticker(id, amount) -> Union[bool, User]:
    user = await user_collection.get(id)
    if user:
        user.pma_stickers += amount
        await user.save()
        return user
    return False
