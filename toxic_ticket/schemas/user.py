from pydantic import BaseModel, EmailStr
from typing import Optional, Any

class UpdateUserModel(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    discord_id: Optional[str]
    toxic_tickets: Optional[int]

    class Collection:
        name = "user"

    class Config:
        json_schema_extra = {
            "example": {
                "username": "JorgEl",
                "email": "test@gmail.com",
                "discord_id": "abc123",
                "toxic_tickets": 9128,
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
