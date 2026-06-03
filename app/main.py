from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    # Use subprocess.run safely without shell=True and sanitize input
    args = ['ping'] + shlex.split(host)
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return result

def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}