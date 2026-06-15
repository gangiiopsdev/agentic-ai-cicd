from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(hostname):
    # Simple regex to validate hostnames
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(hostname))

def ping(host: str):
    if not is_valid_host(host):  # Validate input
        raise ValueError('Invalid input detected')
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)