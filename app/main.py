from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Use a whitelist of allowed hosts or validate input
    if host not in ['allowed_host1', 'allowed_host2']:
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    return subprocess.run(args, check=True)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}