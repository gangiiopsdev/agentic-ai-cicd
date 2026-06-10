from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_safe_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or 'ping' in host:
        return False
    return True

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # List of allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host) or not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}