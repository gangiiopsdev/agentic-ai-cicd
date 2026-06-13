from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use a whitelist of allowed hosts or perform additional validation
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}, 403
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}