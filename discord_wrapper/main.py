from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
import redis
from tasks.toxic_ticket_queue import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello Discord Server" }

@app.get("/test", tags=["Test"])
async def test():
    test = { "username": "testuser", "ticket_type": "toxic_ticket", "amount": 10, "issuer": "test", "ctx": { "thing": "thing" } }
    await add_ticket_to_user(test)
