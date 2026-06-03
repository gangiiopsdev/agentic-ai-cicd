from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr)

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    try:
        return ping(host)
    except Exception as e:
        return {'error': str(e)}

import re

def validate_host(host: str) -> bool:
    # Basic validation, can be expanded for more robustness
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))