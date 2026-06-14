from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def escape_host(host):
    return shlex.quote(host)

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    escaped_host = escape_host(host)
    try:
        result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}