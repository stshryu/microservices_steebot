from typing import Optional, Any
from beanie import Document
from pydantic import BaseModel, EmailStr


class User(Document):
    username: str
    email: EmailStr
    discord_id: str
    toxic_tickets: int

    class Config:
        json_schema_extra = {
            "example": {
                "username": "JorgeEl",
                "email": "test@gmail.com",
                "discord_id": "abc123test",
                "toxic_tickets": 9128
            }
        }

    class Settings:
        name = "user"
