from fastapi import FastAPI
import subprocess
import shlex
import os
import re

app = FastAPI()

def safe_ping(host: str):
    try:
        if not validate_host(host):
            raise ValueError('Invalid host')
        output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Regex to allow only specific hosts
    allowed_hosts = ['example.com', 'localhost', '127.0.0.1']
    if host in allowed_hosts or re.match(r'^[a-zA-Z0-9.-]{3,}$', host):
        return True
    return False