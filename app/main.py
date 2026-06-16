from fastapi import FastAPI
import subprocess
import shlex

cdef safe_ping(host: str):
    # Sanitize input to prevent shell injection
    if not all(c.isalnum() or c in ' .-' for c in host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    except ValueError as e:
        return {'error': str(e)}

    return {'status': 'completed'}