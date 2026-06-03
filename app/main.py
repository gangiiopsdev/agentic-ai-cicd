from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def ping(host: str):
    # Improved implementation with input validation and whitelisting
    allowed_hosts = ['google.com', 'bing.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
async def ping_route(host: str):
    try:
        return await ping(host)
    except Exception as e:
        return str(e)