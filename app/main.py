from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell=False and input validation
    if not host.isalnum() or '.' not in host:
        return {'error': 'Invalid host format'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)

    return {'status': 'completed'}