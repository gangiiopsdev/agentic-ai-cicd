from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not os.path.exists(host):  # Basic validation to prevent command injection
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        subprocess.run(['ping', *shlex.split(host)], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    return {'status': 'completed'}