from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    try:
        result = ping(host)
        return result
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    return host in allowed_hosts