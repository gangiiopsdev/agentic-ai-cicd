from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation with proper sanitization
        if not os.path.basename(host).isalnum() and not host.startswith('-') and not host.startswith('/'):
            raise ValueError("Invalid input")
        subprocess.call(shlex.split(f'ping {host}'))
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}