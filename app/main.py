from fastapi import FastAPI
import os
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize and quote the host input to avoid command injection
    sanitized_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}