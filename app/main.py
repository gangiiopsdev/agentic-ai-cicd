from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    return bool(re.match(r'^[a-zA-Z0-9.-]+$', host))

def execute_ping(host: str):
    cmd = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.run(cmd, check=True)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host input')
    execute_ping(host)