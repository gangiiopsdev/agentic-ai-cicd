from fastapi import FastAPI
import subprocess
import shlex
import re
def safe_ping(host: str):
    if not host or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host provided')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}