from fastapi import FastAPI
import subprocess
import shlex
import re
global_hosts = {'example.com'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_hosts and re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate input with regex
        subprocess.call(shlex.split(f'ping {host}'))
    else:
        return {'status': 'Invalid host'}
    return {'status': 'completed'}