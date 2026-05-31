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
    # Secure implementation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid hostname"}, 400
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}