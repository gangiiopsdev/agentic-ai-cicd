from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    # Safe implementation with proper sanitization
    if not host.strip() or not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', *shlex.split(host)]
    subprocess.call(args)

app.get="/ping"(ping)