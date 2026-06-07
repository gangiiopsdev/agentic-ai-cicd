from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return bool(re.match(pattern, host))

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {'status': 'completed'}