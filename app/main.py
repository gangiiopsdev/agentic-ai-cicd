from fastapi import FastAPI
import subprocess
import shlex
import os
import re

app = FastAPI()

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        raise ValueError("Invalid host input")
    return host

@app.get="/ping"
def ping(host: str):
    sanitized_host = safe_ping(host)
    args = shlex.split(f'ping {sanitized_host}')
    # Use subprocess.run with shell=False for better security
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}