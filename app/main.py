from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host input')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)