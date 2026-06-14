from fastapi import FastAPI
import subprocess
from shlex import quote

global app = FastAPI()

async def home():
    return {"message": "Agentic Self-Healing Pipeline"}

async def ping(host: str):
    try:
        sanitized_host = quote(host)
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}