from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.strip().isdigit():
        return {'error': 'Invalid host input'}

    args = shlex.split(f'ping {host}')
    subprocess.call(args)

    return {'status': 'completed'}