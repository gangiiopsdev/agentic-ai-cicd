from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host format'}

    # Use safe subprocess call without shell=True
    args = ['ping', '-c', '1', host]  # Limit ping to one packet for security
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}