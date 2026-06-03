from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}