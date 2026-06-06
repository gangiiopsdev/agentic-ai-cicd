from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def secure_ping(host: str):
    if not host or len(host.strip()) == 0:
        raise ValueError('Invalid command')
    # Further validate and sanitize the input
    safe_host = shlex.split(host)[0]
    if '.' not in safe_host:
        raise ValueError('Invalid hostname format')
    command = ["ping", *shlex.split(safe_host)]
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)