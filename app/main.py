from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}

    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}