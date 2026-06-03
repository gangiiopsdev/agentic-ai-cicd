from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # More robust regex to validate the host parameter
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        raise ValueError('Invalid input detected in host parameter')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}