from fastapi import FastAPI
import re
import os

app = FastAPI()

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

def safe_ping(host: str, allowed_hosts: list):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    try:
        output = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['host1.example.com', 'host2.example.com']  # Replace with actual allowed hosts
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = safe_ping(host, allowed_hosts)
        return result
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}