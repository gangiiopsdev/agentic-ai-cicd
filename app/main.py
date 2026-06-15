from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() and not '.' in host:
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}