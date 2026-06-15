from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['8.8.8.8', '8.8.4.4']  # Example allowed hosts
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}