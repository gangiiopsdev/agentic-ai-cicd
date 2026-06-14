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
    # Validate input to prevent injection
    if not host.strip().isalnum() or '-' not in host:
        return {"status": "error", "output": "Invalid input"}
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}