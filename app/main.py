from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts or host.startswith('192.168.')

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(shlex.split(f'ping {host}'))
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400