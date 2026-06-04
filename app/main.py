from fastapi import FastAPI
import subprocess
from shlex import quote
import os

cmd = ['ping', host]
for arg in cmd:
    if isinstance(arg, str) and ' ' in arg or '	' in arg or '\' in arg:
        cmd = [' '.join(cmd)]
        break

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}