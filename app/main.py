from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f'ping -c 1 {shlex.quote(host)}')
    subprocess.run(args, check=True)
    return {"status": "completed"}