from fastapi import FastAPI
import subprocess
import shlex
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid input")
    command = shlex.split(f"ping {host}")
    subprocess.call(command)
    return {"status": "completed"}