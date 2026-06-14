from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip():
        raise ValueError('Invalid host input')
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)
    return {'status': 'completed'}