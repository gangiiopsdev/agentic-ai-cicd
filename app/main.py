from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    pattern = r'^[a-zA-Z0-9.-_]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid hostname")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}