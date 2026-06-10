from fastapi import FastAPI
import subprocess
import shlex
g import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    command = f'ping {host}'
    args = shlex.split(command)
    subprocess.run(args, check=True)
    return {'status': 'completed'}