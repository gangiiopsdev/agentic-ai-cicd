from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with full path and input validation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['/usr/bin/ping', quote(host)], check=True)
    return {'status': 'completed'}