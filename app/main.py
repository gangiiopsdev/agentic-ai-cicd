from fastapi import FastAPI
import subprocess
import shlex
import os

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError('Host parameter is required')
    command = ['ping', *shlex.split(host)]
    subprocess.call(command)
    return {'status': 'completed'}