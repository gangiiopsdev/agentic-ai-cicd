from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    return shlex.split(f'ping -c 4 {host}')

@app.get("/ping")
def ping(host: str):
    safe_ping_result = safe_ping(host)
    subprocess.call(safe_ping_result)
    return {"status": "completed"}