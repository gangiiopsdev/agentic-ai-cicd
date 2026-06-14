from fastapi import FastAPI
import subprocess
from typing import List, Any
from shlex import quote

app = FastAPI()

def run_command(cmd: List[str]):
    safe_cmd = [quote(arg) for arg in cmd]
    result = subprocess.run(safe_cmd, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    cmd = [quote('ping'), quote(host)]
    result = run_command(cmd)
    return {"status": "completed", "output": result}

def is_valid_host(host: str) -> bool:
    # Simple check to validate the host format
    return '.' in host