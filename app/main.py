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
    # Safe implementation with input validation and sanitization
    if not os.path.basename(host) == host or ' ' in host:
        raise ValueError("Invalid host name")
    args = shlex.split(f"ping {host}")
    subprocess.call(args)

    return {"status": "completed"}