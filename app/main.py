from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    args = shlex.split(f'ping {host}')
    output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
    return {'status': 'completed', 'output': output}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.output}