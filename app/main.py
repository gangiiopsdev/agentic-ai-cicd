from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}