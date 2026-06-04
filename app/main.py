from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    args = shlex.split(f'ping {host}')
    output = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}