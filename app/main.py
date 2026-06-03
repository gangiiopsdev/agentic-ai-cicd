from fastapi import FastAPI
import asyncio

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    await asyncio.create_subprocess_exec('ping', host)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)