from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Optional
import re

app = FastAPI()

def run_ping(host: str) -> dict:
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: Optional[str] = None) -> dict:
    if host is None or not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    # Validate and sanitize the host parameter further, e.g., using a whitelist
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    return run_ping(host)