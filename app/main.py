from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}
    args = shlex.split(f'ping {host}')
    output = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}