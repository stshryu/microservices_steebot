from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
import redis
import asyncio
from tasks.toxic_ticket_queue import *
from services.subscriber import *
from services.discordMain import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure listener doesn't run on the same loop as the main thread
    asyncio.create_task(process_channel())
    asyncio.create_task(bot_run())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello Discord Server" }

@app.get("/test", tags=["Test"])
async def test():
    test = { "username": "testuser", "ticket_type": "toxic_ticket", "amount": 10, "issuer": "test", "ctx": { "thing": "thing" } }
    await add_ticket_to_user(test)
