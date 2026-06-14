from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping_safe(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get="/ping")
def ping(host: str):
    try:
        ping_safe(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400