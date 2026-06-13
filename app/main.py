from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    # Safe implementation using subprocess.run with check_output and limiting arguments
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return result.stdout

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation to prevent command injection
    try:
        result = safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    else:
        return result