from fastapi import FastAPI
import subprocess
import os
import shlex
def validate_host(host):
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return False
    return True

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}