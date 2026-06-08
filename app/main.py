from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run instead
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if validate_host(host):
        return ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

import re

def validate_host(host: str) -> bool:
    # Simple regex to validate hostname
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None