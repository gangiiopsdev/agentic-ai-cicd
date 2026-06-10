from fastapi import FastAPI
import shlex
import subprocess

gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid host name'}
    args = shlex.split(f'ping -c 1 {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}