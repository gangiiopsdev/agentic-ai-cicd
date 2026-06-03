from fastapi import FastAPI
import os
import subprocess
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_', '@'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1'], input=sanitized_host.encode(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}