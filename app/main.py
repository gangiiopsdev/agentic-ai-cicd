from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Regex to validate the host parameter
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input detected in host parameter')
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}