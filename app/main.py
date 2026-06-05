from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with command sanitization and input validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    sanitized_host = shlex.quote(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}