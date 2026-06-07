from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    safe_host = validate_host(host)

    command = ['ping', *shlex.split(safe_host)]
    subprocess.call(command)

    return {"status": "completed"}