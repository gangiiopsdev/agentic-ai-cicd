from fastapi import FastAPI
import subprocess
from shlex import quote

def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    result = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True, check=True)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    result = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True, check=True)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }