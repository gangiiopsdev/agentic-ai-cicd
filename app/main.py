from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip():
        raise ValueError("Invalid host")
    command_parts = ['ping', shlex.quote(host)]
    subprocess.call(command_parts)
    return {"status": "completed"}