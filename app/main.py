from fastapi import FastAPI
import re
import shlex
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Example validation logic, replace with actual validation
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}