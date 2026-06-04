from fastapi import FastAPI
import subprocess
from shlex import quote
from pathlib import Path
from typing import Optional
import os

app = FastAPI()

def is_safe_host(host: str) -> bool:
    # Implement more robust validation logic
    return host.isalnum()

def execute_ping_command(host: str) -> dict:
    try:
        result = subprocess.run([os.path.join('/bin', 'ping'), quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return execute_ping_command(host)