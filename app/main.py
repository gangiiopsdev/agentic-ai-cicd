from fastapi import FastAPI
import subprocess
import shlex
import os

global_config = {
    'allowed_hosts': ['example.com', 'localhost']
}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_config['allowed_hosts']:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    else:
        return {'status': 'Host not allowed'}, 403
    return {'status': 'completed'}