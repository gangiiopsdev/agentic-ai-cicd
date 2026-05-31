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

def sanitize_host(host: str):
    # Add additional sanitization logic here if needed
    return host

@app.get('/ping')
def ping(host: str):