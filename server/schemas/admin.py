from pydantic import BaseModel
from fastapi.security import HTTPBasicCredentials
from pydantic import EmailStr

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
                "username": "JorgeEl",
                "email": "test@gmail.com",
            }
        }
