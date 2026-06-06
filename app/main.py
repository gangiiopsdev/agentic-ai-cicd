from fastapi import FastAPI
import subprocess
import shlex
import re

def validate_host(host: str) -> bool:
    # Basic regex to allow only valid hostnames/IP addresses
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        return {'status': 'invalid host'}, 400