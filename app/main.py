from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.strip().isalnum() or '..' in host:
        return {'error': 'Invalid host name'}

    try:
        subprocess.call(shlex.split(f'ping {host}'))
    except Exception as e:
        return {'error': str(e)}

    return {'status': 'completed'}