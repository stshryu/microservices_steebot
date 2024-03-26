from typing import Optional, Any
from beanie import Document
from pydantic import BaseModel, EmailStr


class User(Document):
    username: str
    email: EmailStr
    discord_id: str
    mini_toxic_tickets: int
    toxic_tickets: int
    pma_stickers: int

    class Config:
        json_schema_extra = {
            "example": {
                "username": "JorgeEl",
                "email": "test@gmail.com",
                "discord_id": "abc123test",
                "mini_toxic_tickets": 1,
                "toxic_tickets": 9128,
                "pma_stickers": 2,
            }
        }

    class Settings:
        name = "user"
