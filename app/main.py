from fastapi import FastAPI
import subprocess
import shlex
import re

global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        subprocess.call(shlex.split(f'ping {host}'))
    else:
        raise ValueError('Invalid host name')

    return {"status": "completed"}