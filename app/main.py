from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}