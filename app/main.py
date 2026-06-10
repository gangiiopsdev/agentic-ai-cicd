from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        if not safe_ping(host):
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    except Exception as e:
        return {'error': str(e)}
    return {'status': 'completed'}