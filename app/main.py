from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host parameter
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    args = shlex.split(f'ping -c 1 {host}')  # Limiting to one ping attempt for security reasons
    subprocess.run(args, check=True)
    return {'status': 'completed'}