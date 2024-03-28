from fastapi import FastAPI, Depends
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.user import router as UserRouter 

app = FastAPI()

token_listener = lambda: {}

@app.on_event("startup")
async def start_database():
    await initiate_database()

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello World" }

app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(UserRouter, tags=["User"], prefix="/user")
