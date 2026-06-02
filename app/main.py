from fastapi import FastAPI
import subprocess
from shlex import quote
def validate_host(host):
    if not host.strip():
        raise ValueError('Host parameter is required')
    if any(char in host for char in [';', '&', '|', '>', '<', '*', '?']):  # Basic validation of command injection
        raise ValueError('Invalid characters in host parameter')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', quote(host.replace(' ', ''))], check=True, shell=False)
    return {"status": "completed"}