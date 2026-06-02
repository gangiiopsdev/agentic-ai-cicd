from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host:
        return {'status': 'error', 'output': 'Host is required'}
    if '/' in host or '..' in host or host.startswith('.'):
        return {'status': 'error', 'output': 'Invalid host'}
    result = subprocess.run(['ping', os.path.abspath(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}