from fastapi import FastAPI
import subprocess
import re

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}