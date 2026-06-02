from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex.split
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}