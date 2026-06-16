from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not host.isalnum():
        return {'status': 'invalid host'}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}