from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid hostname'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.run(['ping', *args], check=True)
    return {'status': 'completed'}