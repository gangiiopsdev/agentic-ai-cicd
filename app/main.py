from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    # Basic regex to allow alphanumeric characters, hyphens, and periods
    return re.match(r'^[a-zA-Z0-9-.]+$', host) is not None

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host parameter"}
    try:
        args = shlex.split(f'ping -c 1 {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}