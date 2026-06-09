from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    try:
        host = shlex.quote(host)
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, shlex.Error) as e:
        return {'status': 'failed', 'error': str(e)}

# Prevent directory traversal in the host parameter
@app.get('/ping_secure')
def ping_secure(host: str):
    if not os.path.isabs(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        host = shlex.quote(host)
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, shlex.Error) as e:
        return {'status': 'failed', 'error': str(e)}