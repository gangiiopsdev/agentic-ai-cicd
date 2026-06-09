from fastapi import FastAPI
import subprocess
from shlex import quote

global app = FastAPI()

async def safe_ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = quote(host)
    args = ['ping', safe_host]
    await asyncio.create_subprocess_exec(*args, shell=False)

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}