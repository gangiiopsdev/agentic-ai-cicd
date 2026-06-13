from fastapi import FastAPI
import subprocess
import os
def safe_ping(host: str):
    if not host or len(host) > 100:
        raise ValueError("Invalid host name")
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    return safe_ping(host)