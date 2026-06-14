from fastapi import FastAPI
import subprocess
from typing import Optional

def safe_ping(host: str) -> dict:
    valid_hosts = ['example.com', 'google.com']  # Replace with a list of allowed hosts
    if host not in valid_hosts:
        raise ValueError('Invalid host')
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None:
        return {"status": "failed", "error": "Host parameter is required"}
    return safe_ping(host)