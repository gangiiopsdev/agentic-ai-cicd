from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_valid_host(host):
    # Simple regex to validate alphanumeric hostnames
    return bool(re.match(r'^[a-zA-Z0-9]+$', host))

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid hostname")
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}