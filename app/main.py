from fastapi import FastAPI
import subprocess
import shlex
import os

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'invalid input'}
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.call(args)

    return {'status': 'completed'}