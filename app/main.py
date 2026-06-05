from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it does not contain shell metacharacters
    if re.search(r'[&|;()<>]', host):
        return {'status': 'error', 'error': 'Invalid input'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

# Additional preventive controls
@app.get('/ping-safe')
def ping_safe(host: str):
    safe_hosts = ['8.8.8.8', '192.168.0.1']  # Define a whitelist of allowed hosts
    if host not in safe_hosts:
        return {'status': 'error', 'error': 'Invalid input'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}