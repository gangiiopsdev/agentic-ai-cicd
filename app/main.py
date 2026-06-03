from fastapi import FastAPI
import subprocess
import shlex
import re

global host
host = None

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")

    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)

    return {"status": "completed"}