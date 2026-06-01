from fastapi import FastAPI
import subprocess
from shlex import quote
from os import path as ospath

app = FastAPI()

def secure_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    # Validate host to prevent command injection
    if not ospath.basename(host) == host or '.' in host or '\' in host or '/' in host:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return secure_ping(host)