from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid_host"}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}