from pydantic import BaseModel, EmailStr
from typing import Optional, Any

class UpdateUserModel(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    discord_id: Optional[str]
    mini_toxic_tickets: Optional[int]
    toxic_tickets: Optional[int]
    pma_stickers: Optional[int]

    class Collection:
        name = "user"

    class Config:
        json_schema_extra = {
            "example": {
                "username": "JorgEl",
                "email": "test@gmail.com",
                "discord_id": "abc123",
                "mini_toxic_tickets": 1,
                "toxic_tickets": 9128,
                "pma_stickers": 2,
            }
        }

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
