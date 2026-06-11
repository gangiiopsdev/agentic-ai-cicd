from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        subprocess.check_output(['ping', host], shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent command injection
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

import re
def validate_host(host: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None