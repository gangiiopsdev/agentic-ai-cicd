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
    if not host.startswith('localhost') and not host.startswith('127.0.0.1'):
        return {'status': 'error', 'message': 'Invalid host'}
    command = shlex.split(f'ping {shlex.quote(host)}')
    try:
        result = subprocess.run(command, check=True, capture_output=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.TimeoutExpired:
        return {'status': 'error', 'message': 'Ping request timed out'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed: {e.stderr.decode('utf-8')}'}