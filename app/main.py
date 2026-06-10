from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True, capture_output=True, text=True)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}