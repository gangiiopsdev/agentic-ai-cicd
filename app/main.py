from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input to ensure it's a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    command_parts = ['ping', *shlex.split(host)]
    subprocess.call(command_parts)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}