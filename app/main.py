from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host):
    if not host.isalnum() and '.' in host:
        raise ValueError("Invalid host input")
    return host

@app.get="/ping"
def ping(host: str):
    sanitized_host = safe_ping(host)
    args = shlex.split(f'ping {sanitized_host}')
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}