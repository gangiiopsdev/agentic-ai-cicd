from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional

app = FastAPI()

def ping(host: str) -> dict:
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str) -> dict:
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)

def is_safe_hostname(hostname: str) -> bool:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    for char in hostname:
        if char not in allowed_chars:
            return False
    return True