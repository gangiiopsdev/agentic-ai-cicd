from fastapi import FastAPI
import shlex
import os

app = FastAPI()

def validate_host(host: str) -> str:
    if not host.strip():
        raise Exception('Host parameter is required')
    if len(host) > 255:
        raise Exception('Host parameter is too long')
    return host

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    host = validate_host(host)
    args = shlex.split(f'ping -c 4 {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}