from fastapi import FastAPI
import subprocess
import shlex
g from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if not host.isalnum() or len(host) > 100:
        raise HTTPException(status_code=400, detail="Invalid host name")
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}