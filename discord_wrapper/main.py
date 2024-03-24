from fastapi import FastAPI, Depends
import redis

app = FastAPI()

@app.on_event("startup")
async def start_database():
    pass

@app.get("/", tags=["Root"])
async def read_root():
    return { "message": "Hello World" }
