from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    # Sanitize input to prevent command injection
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)