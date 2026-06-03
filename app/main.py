from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Further validation and escaping of host input is recommended
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host input')
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.call(args)
    return {'status': 'completed'}