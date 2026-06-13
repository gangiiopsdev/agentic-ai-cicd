from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if not host.isalnum() or len(host) > 20:
        return {'error': 'Invalid host'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}