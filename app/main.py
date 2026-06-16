from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}