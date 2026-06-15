from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    cmd = ['ping', host]  # Remove re.escape as it is no longer necessary due to validation
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout.strip()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    cmd = ['ping', host]  # Remove re.escape as it is no longer necessary due to validation
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout.strip()}