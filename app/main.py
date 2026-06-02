from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    return ping(host)

import re

def validate_host(host: str) -> bool:
    # Basic validation, can be expanded for more robustness
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))