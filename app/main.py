from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host or 'ping' in host.split():
        raise ValueError('Invalid host provided')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}