from fastapi import FastAPI
import subprocess
import shlex
import os
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        command = shlex.split(f'ping {host}')
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}