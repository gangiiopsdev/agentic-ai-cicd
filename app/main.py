from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)

import re
def validate_host(hostname):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, hostname) is not None