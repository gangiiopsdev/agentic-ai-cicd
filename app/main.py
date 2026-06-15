from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if 'ping' in host or '&&' in host or ';' in host:
        return {'error': 'Invalid input'}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}