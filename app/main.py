from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host format')
    args = shlex.split(f'ping -c 1 {shlex.quote(host)}')  # Limiting to one ping attempt for security reasons
    subprocess.run(args, check=True)
    return {'status': 'completed'}