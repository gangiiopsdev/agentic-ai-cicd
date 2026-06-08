from fastapi import FastAPI
import subprocess
import shlex
import re
def safe_ping(host: str) -> dict:
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    # Escape or sanitize the host input before passing to subprocess
    escaped_host = shlex.quote(host)
    subprocess.run(['ping', *shlex.split(escaped_host)], check=True)
    return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)