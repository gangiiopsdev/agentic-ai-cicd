from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def sanitize_host(host):
    if not host or len(host) > 255:
        return None
    return host

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_host(host)
    if not safe_host:
        return {"status": "failed", "error": "Invalid host name"}
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}