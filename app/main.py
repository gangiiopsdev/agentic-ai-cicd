from fastapi import FastAPI
import subprocess
from typing import List, Any

app = FastAPI()

def run_command(cmd: List[str]):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    cmd = ["ping", host]
    result = run_command(cmd)
    return {"status": "completed", "output": result}

def is_valid_host(host: str) -> bool:
    # Simple check to validate the host format
    return '.' in host