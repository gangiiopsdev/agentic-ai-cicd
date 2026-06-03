from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with proper input validation and sanitization
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host name'}
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}