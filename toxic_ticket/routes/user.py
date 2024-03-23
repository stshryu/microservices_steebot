from fastapi import APIRouter, Body, Depends
from typing import Annotated
from database.database import *
from models.user import User
from schemas.user import Response, UpdateUserModel
from config.config import get_redis_connection

router = APIRouter()

async def get_admin() -> bool:
    return False 

async def get_ttadmin(username: str) -> bool:
    return await get_ttadmin(username)

""" 
An example redis usage template:
    ...
client = await get_redis_connection()
await client.set(1, "hello")
print(f"Redis key: {await client.get(1)}")
await client.close()
    ...
"""

@router.get("/", response_description="Users retrieved", response_model=Response)
async def get_users():
    users = await retrieve_users()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "User data retrieved successfully",
        "data": users,
    }

@router.get("/{id}", response_description="User data retrieved", response_model=Response)
async def get_user_data(id: PydanticObjectId):
    user = await retrieve_user(id)
    if user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "User data retrieved successfully",
            "data": user,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "User doesn't exist",
    }


@router.post(
    "/",
    response_description="User data added into the database",
    response_model=Response,
)
async def add_user_data(user: User = Body(...)):
    new_user = await add_user(user)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "User created successfully",
        "data": new_user,
    }


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: PydanticObjectId, is_admin: Annotated[bool, Depends(get_admin)]):
    deleted_user = await delete_user(id) if is_admin else False 
    if deleted_user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "User with ID: {} removed".format(id),
            "data": deleted_user,
        }
    else:
        return {
            "status_code": 401,
            "response_type": "error",
            "description": f"Users can only be removed by an admin",
            "data": False,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "User with id {0} doesn't exist".format(id),
        "data": False,
    }


@router.post("/{id}/add_tt", response_model=Response)
async def add_toxic_ticket(id: PydanticObjectId, is_ttadmin: Annotated[bool, Depends(get_ttadmin)]):
    updated_user = await add_toxic_ticket(id) if is_ttadmin else False
    if updated_user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "User with ID: {} updated".format(id),
            "data": updated_user,
        }
    else:
        return {
            "status_code": 401,
            "response_type": "error",
            "description": "Only an admin can add a toxic ticket",
            "data": False,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. User with ID: {} not found".format(id),
        "data": False,
    }

@router.post("/{id}/remove_tt", response_model=Response)
async def remove_toxic_ticket(id: PydanticObjectId, is_ttadmin: Annotated[bool, Depends(get_ttadmin)]):
    updated_user = await remove_toxic_ticket(id) if is_ttadmin else False
    if updated_user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "User with ID: {} updated".format(id),
            "data": updated_user,
        }
    else:
        return {
            "status_code": 401,
            "response_type": "error",
            "description": "Only an admin can remove a toxic ticket",
            "data": False,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. User with ID: {} not found".format(id),
        "data": False,
    }
