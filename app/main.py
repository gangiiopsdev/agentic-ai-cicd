from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import List
import re
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    # Ensure the host is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    command = ['ping', '-c', '1', quote(host)]
    result = await asyncio.create_subprocess_exec(*command, check=True)
    return result

@app.get("/ping")
def ping(host: str):
    # Add additional validation or logging for security purposes
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    await safe_ping(host)
    return {"status": "completed"}