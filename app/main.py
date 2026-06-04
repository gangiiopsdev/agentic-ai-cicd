from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host: str):
    if not host or '&&' in host or ';' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    args = shlex.split(f'ping {shlex.quote(host)}')
    result = subprocess.run(args, check=True)
    return {'status': 'completed', 'stdout': result.stdout.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)