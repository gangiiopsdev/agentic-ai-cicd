from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

def validate_host(host: str) -> bool:
    # Simple validation example: allow only alphanumeric characters and hyphens
    return all(c.isalnum() or c == '-' for c in host)

@app.get('/ping')
def ping(host: str) -> Dict[str, str]:
    if validate_host(host):
        args = ['ping', '--', host]  # Use '--' to prevent command injection
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400