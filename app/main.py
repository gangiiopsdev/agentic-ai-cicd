from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping_secure(host: str):
    # Validate and sanitize input
    if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.\.[0-9]{1,3}\.\.[0-9]{1,3}$', host) or not all(0 <= int(part) <= 255 for part in host.split('.')):
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping -c 1 {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}