from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    # Fixed implementation with input validation
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}