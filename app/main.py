from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")

    command = ['ping', *shlex.split(host)]
    subprocess.call(command)

    return {"status": "completed"}