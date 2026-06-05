from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, check=True, capture_output=True)
    return result.stdout.decode('utf-8')

def validate_host(host: str):
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_route(host: str):
    validate_host(host)
    return await ping(host)