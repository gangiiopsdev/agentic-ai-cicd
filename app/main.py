from fastapi import FastAPI
import subprocess
from typing import Optional
import shlex
def sanitize_host(host: str) -> str:
    allowed_hosts = ['localhost', '127.0.0.1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return shlex.quote(host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}
    except ValueError as e:
        return {'status': 'error', 'error': str(e)}