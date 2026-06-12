from fastapi import FastAPI
import subprocess
import shlex
import re

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    allowed_hosts = ['google.com', 'example.com']  # List of allowed hosts
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        return {'error': 'Invalid host'}, 400
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}