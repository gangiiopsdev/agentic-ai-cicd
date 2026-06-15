from fastapi import FastAPI
import shlex
import os
import subprocess
def safe_ping(host):
    if not host.isalnum() and '.' in host:
        raise ValueError("Invalid host input")
    return host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = safe_ping(host)
    args = ['ping', shlex.quote(sanitized_host)]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    return {"status": "completed", "output": result.stdout.decode()}