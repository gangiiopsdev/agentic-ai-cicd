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
    args = shlex.split(f'ping -c 1 {host}')
    try:
        subprocess.run(['ping', '-c', '1'] + [shlex.quote(arg) for arg in args], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500
    return {'status': 'completed'}