from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}

# Preventive controls
@app.get('/ping_safe')
def ping_safe(host: str):
    safe_hosts = ['127.0.0.1', '::1']  # List of allowed hosts
    if host not in safe_hosts:
        return {'error': 'Invalid host'}
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}