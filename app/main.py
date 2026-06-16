from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() and not '.' in host:
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    # Ensure that the sanitized input does not contain any unexpected characters
    for arg in args:
        if '&&' in arg or ';' in arg or '|' in arg or '`' in arg:
            raise ValueError('Invalid character detected in host name')
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}