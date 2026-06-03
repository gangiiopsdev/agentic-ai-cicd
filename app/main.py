from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = ['127.0.0.1', '::1']

def safe_ping(host: str):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}