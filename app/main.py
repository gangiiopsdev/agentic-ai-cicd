from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with proper validation and sanitization
    if not host.isnumeric() or len(host) > 3:
        raise ValueError('Invalid host input')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}