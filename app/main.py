from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

allowed_hosts = {'example.com', 'localhost'}
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Ensure the host is safe to use in subprocess call
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}