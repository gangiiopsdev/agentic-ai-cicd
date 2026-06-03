from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char == '.')[:64]

def validate_host(host: str):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400
    sanitized_host = sanitize_input(host)
    subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, capture_output=True)
    return {'status': 'completed'}