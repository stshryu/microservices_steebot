from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr

class Admin(Document):
    username: str
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "JorgeEl",
                "email": "test@gmail.com",
                "password": "secret"
            }
        }

    class Settings:
        name = "admin"


class AdminSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": { "username": "test@gmail.com", "password": "secret" }
        }


class AdminData(BaseModel):
    username: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "username": "Steve",
                "email": "test@gmail.com"
            }
        }

