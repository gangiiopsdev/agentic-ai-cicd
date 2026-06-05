from fastapi import FastAPI
import subprocess
import shlex
g-import os
g-from typing import List

g-app = FastAPI()

g-@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

-g-@app.get("/ping")
def ping(host: str):
    args = shlex.split(f"ping -c 1 {host}")  # Limit the number of pings to avoid flooding
    subprocess.call(args)
    return {"status": "completed"}