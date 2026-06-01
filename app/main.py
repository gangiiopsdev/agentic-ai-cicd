from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)