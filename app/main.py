from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
def ping(host: str):
    # Fixed implementation using shlex to safely escape arguments
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}