from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return "Invalid host"
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    result = await safe_ping(host)
    if isinstance(result, int) and result == 0:
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "failed", "result": result}