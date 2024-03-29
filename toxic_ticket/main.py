from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.user import router as UserRouter 

@asynccontextmanager
async def lifespan(app: FastAPI):
    await initiate_database()
    yield

app = FastAPI(lifespan=lifespan)

token_listener = lambda: {}

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello World" }

app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(UserRouter, tags=["User"], prefix="/user")
