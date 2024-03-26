from fastapi import APIRouter, Body, Depends
from typing import Annotated
from models.user import User
from schemas.user import Response, UpdateUserModel
from services.user import *
from config.config import get_redis_connection

router = APIRouter()

@router.get("/", response_description="Users retrieved", response_model=Response)
async def get_users():
    users = await get_users_service()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "User data retrieved successfully",
        "data": users,
    }

@router.get("/{id}", response_description="User data retrieved", response_model=Response)
async def get_user_data(id: PydanticObjectId):
    user = await get_user_service(id)
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
    new_user = await add_user_service(user)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "User created successfully",
        "data": new_user,
    }


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: PydanticObjectId):
    deleted_user = await delete_user_service(id) 
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

@router.post("/{id}/add_tt", response_model=Response)
async def add_toxic_ticket(id: PydanticObjectId):
    updated_user = await add_toxic_ticket_service(id)
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

@router.post("/{id}/add_mini_tt", response_model=Response)
async def add_mini_toxic_ticket(id: PydanticObjectId):
    updated_user = await add_mini_toxic_ticket_service(id)
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
            "description": "Only an admin can add a mini toxic ticket",
            "data": False,
        }

@router.post("/{id}/add_pma", response_model=Response)
async def add_pma_sticker(id: PydanticObjectId):
    updated_user = await add_pma_sticker_service(id)
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
            "description": "Only an admin can add a pma sticker",
            "data": False,
        }
