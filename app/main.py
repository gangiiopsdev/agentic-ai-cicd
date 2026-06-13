from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host) or re.search(r'^-[^ ]+ ', host):  # Check for potential shell injection
        raise ValueError("Invalid host name")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}