from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    # Improved input validation to handle all possible characters and lengths
    if not host.replace('.', '', 1).isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}