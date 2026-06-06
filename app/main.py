from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional

app = FastAPI()

def safe_ping(host: str) -> bool:
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Ping failed'}
    return {'status': 'completed'}