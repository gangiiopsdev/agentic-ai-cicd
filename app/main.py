from fastapi import FastAPI
import subprocess
import re
from fastapi.exceptions import HTTPException

c
app = FastAPI()

async def ping(host: str):
    # Enhanced validation to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced validation to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}