from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str):
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host name')
    args = ['ping', quote(host)]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}