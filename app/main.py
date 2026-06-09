from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
def ping(host: str):
    # Secure implementation
    args = shlex.split(f'ping -c 4 {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}