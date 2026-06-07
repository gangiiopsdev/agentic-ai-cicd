from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    return host

@app.get("/ping")
async def ping(host: str = validator(validate_host)): # Validate input
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}