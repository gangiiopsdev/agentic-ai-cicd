from fastapi import FastAPI
import shlex
from fastapi import HTTPException
import asyncio
import re

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Regex pattern to validate host
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

async def ping(host: str):
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host name")
    args = ['ping', '-c', '1', shlex.quote(host)]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}