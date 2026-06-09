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
    if not host.isalnum() and '.' in host:
        raise ValueError("Invalid host input")
    args = shlex.split(f'ping {host}')
    # Use subprocess.run with shell=False for better security
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}