from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid hostname')
    command = shlex.split(f'ping {host}')
    subprocess.call(command, shell=False)
    return {'status': 'completed'}