from fastapi import FastAPI
import subprocess
from shlex import quote
gateway = Gateway()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and validation
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {'status': 'failed', 'error': 'Invalid host parameter'}
    try:
        result = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}