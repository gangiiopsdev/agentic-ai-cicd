from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str):
    return shlex.quote(host)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get="/ping")
def ping(host: str):