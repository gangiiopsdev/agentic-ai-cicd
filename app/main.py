from fastapi import FastAPI
import subprocess
from typing import List, Optional
import shlex

app = FastAPI()

def safe_ping(host: str) -> str:
    # Use shlex.quote to safely escape the host parameter
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)