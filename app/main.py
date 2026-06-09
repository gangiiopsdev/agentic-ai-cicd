from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Restrict allowed hosts
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    else:
        raise Exception('Invalid host')