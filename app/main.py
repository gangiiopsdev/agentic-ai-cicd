from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    return True

def sanitize_input(host):
    sanitized_host = shlex.quote(host)
    return sanitized_host

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}

    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    result = subprocess.run(args, capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}