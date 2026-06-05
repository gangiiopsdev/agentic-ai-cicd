from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional

app = FastAPI()

def safe_ping(host: str) -> bool:
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in '-.' for c in host):
            raise ValueError("Invalid host")
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print(e)
        return False

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Ping failed'}
    return {'status': 'completed'}