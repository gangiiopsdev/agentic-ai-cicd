from fastapi import FastAPI
import subprocess
import re
from fastapi.exceptions import HTTPException
c
app = FastAPI()

def ping(host: str):
    # Secure implementation
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
    # Secure implementation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}