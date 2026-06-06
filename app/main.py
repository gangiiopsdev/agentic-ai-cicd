from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    cmd = shlex.split(f'ping {host}')
    subprocess.call(cmd)
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Sanitize input
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid host'}
    cmd = shlex.split(f'ping {host}')
    subprocess.call(cmd)
    return {'status': 'completed'}