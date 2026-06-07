from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)