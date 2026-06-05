from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def is_valid_host(host):
    return all(c.isalnum() or c in '-.' for c in host)

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}