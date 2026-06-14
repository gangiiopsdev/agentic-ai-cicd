from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: f'ping {quote(host)}'

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.call(generate_ping_command(host), shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500

# Preventive controls
from fastapi import HTTPException
import re

allowed_hosts = ['example.com', 'localhost']
def validate_host(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        raise HTTPException(status_code=400, detail='Invalid host')