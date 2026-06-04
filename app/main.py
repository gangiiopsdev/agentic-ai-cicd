from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip():
        raise Exception('Host parameter is required')
    if len(host) > 255:
        raise Exception('Host parameter is too long')
    args = shlex.split(f'ping -c 4 {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}