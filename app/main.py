from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid command injection
    if not all(c.isalnum() or c in '.:' for c in host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}