from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

g@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    # Input validation for host parameter
    if not all(c.isalnum() or c in [".", ":", "/", "-"] for c in host):
        return {"status": "error", "message": "Invalid input"}
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)
    return {"status": "completed"}