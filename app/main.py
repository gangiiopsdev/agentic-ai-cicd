from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host parameter to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError('Invalid host name')
    cmd = ['ping', quote(host)]
    result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}