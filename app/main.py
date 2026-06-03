from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

global host
host = None

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")

    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}