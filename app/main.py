from fastapi import FastAPI
import subprocess
from shlex import quote
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate host format
        raise ValueError('Invalid host format')
    sanitized_host = quote(host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}