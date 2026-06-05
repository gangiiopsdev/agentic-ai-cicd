from fastapi import FastAPI
import subprocess
import shlex
import os

global app
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with command validation and execution
    if not host or len(host) > 255:
        return {"status": "invalid_host"}
    args = shlex.split(f'ping -c 1 {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }