from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional
import re

app = FastAPI()

def safe_ping(host: str) -> bool:
    try:
        # Validate the host input to ensure it only contains allowed characters
        if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
            raise ValueError("Invalid host")
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return True
    except (subprocess.CalledProcessError, ValueError) as e:
        return False

@app.get('/ping')
async def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Ping failed'}
    return {'status': 'completed'}