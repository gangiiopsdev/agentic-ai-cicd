from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host: str):
    if not host or host.strip() == '':
        raise ValueError('Host parameter is missing or empty')
    if not host.replace('.', '').replace('-', '').isdigit():
        raise ValueError('Invalid host format')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}