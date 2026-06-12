from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input to prevent shell injection
    if not all(char.isalnum() or char in ['-', '.', '_', ':'] for char in host):
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}