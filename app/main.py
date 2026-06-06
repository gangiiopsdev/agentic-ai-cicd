from fastapi import FastAPI
import subprocess
import shlex
g-import os
g-from typing import List
g-app = FastAPI()

g-@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

-g-@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    args = shlex.split(f"ping -c 1 {host}")  # Limit the number of pings to avoid flooding
    subprocess.call(args)
    return {"status": "completed"}