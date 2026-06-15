from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    args = shlex.split(f"ping {host}")
    subprocess.call(args)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)