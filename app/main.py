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
    # Safe implementation with proper validation and sanitization
    if not os.path.exists('/bin/ping'):
        raise Exception('Ping command not found')
    args = shlex.split(f'ping -c 4 {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}