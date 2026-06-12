from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    try:
        # Validate the host input to ensure it is a valid IP address or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host'}
        subprocess.run(['ping', '-c 1', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize and validate the host input further
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    subprocess.run(['ping', '-c 1', host], check=True, shell=False)
    return {'status': 'completed'}