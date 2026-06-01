from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def run_ping(host: str):
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    sanitized_host = shlex.quote(host)
    return run_ping(sanitized_host)