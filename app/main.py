from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.startswith('localhost') and not host.startswith('127.0.0.1'):
        return {'status': 'error', 'message': 'Invalid host'}
    command = shlex.split(f'ping {shlex.quote(host)}')
    result = subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}