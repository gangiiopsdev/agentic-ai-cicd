from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)

def is_valid_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

@app.get('/ping')
def ping(host: str):
    if not host:
        raise ValueError('Host parameter is required')
    # Sanitize input to prevent command injection
    if not is_valid_host(host):
        raise ValueError('Invalid host format')
    sanitized_host = shlex.quote(sanitize_host(host))
    args = ['ping', sanitized_host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}