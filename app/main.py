from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Define allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}