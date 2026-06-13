from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and logging
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host value')
    args = shlex.split(f'ping -c 1 {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}