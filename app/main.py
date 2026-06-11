from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = f'ping -c 4 {host}'
    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}