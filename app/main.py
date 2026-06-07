from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def safe_ping(host: str):
    args = [f'ping', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        return {'status': 'error', 'message': 'Invalid host name'}
    return safe_ping(host)