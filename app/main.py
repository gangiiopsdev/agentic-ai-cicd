from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_str):
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return input_str if pattern.match(input_str) else ''

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping'] + shlex.split(sanitized_host, posix=True)
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}