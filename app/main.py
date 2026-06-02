from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def run_ping(host: str):
    try:
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in '._-')  # Basic sanitization
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

@app.get('/ping')
def ping(host: str):
    return run_ping(host)