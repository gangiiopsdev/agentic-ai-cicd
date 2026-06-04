from fastapi import FastAPI
import subprocess
import shlex
import os
def safe_ping(host: str) -> bool:
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return True

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {"status": "completed"}