from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
import redis
import asyncio
from tasks.toxic_ticket_queue import *
from services.subscriber import *
from config.config import Settings
from services.discordMain import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Add to loop
    asyncio.create_task(process_channel())
    asyncio.create_task(main_loop())
    yield
    
app = FastAPI(lifespan=lifespan)

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello Discord Server" }

@app.get("/test", tags=["Test"])
async def test():
    test = { "username": "testuser", "ticket_type": "toxic_ticket", "amount": 10, "issuer": "test", "channel": "" }
    await add_ticket_to_user(test)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
