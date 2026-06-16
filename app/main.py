from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_hostname(hostname):
    if not hostname.isalnum() or '-' not in hostname:
        raise ValueError('Invalid hostname')
    return hostname.replace('.', '_').replace('-', '_')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_hostname(host)
    command = ['ping', sanitized_host]
    subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed"}