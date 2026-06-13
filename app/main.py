from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced security implementation
    args = shlex.split(f'ping -c 4 {host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}