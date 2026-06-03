from fastapi import FastAPI
import re
import shlex
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host to allow only alphanumeric characters and a single dot for subdomains
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input')
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input')
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}