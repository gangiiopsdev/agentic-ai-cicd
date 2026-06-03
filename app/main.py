from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if 'localhost' in host:
        allowed_hosts = ['localhost', '127.0.0.1']
        if host not in allowed_hosts:
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    return {'status': 'completed'}