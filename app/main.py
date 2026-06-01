from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    pattern = r'^[a-zA-Z0-9.-_]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid hostname")
    args = shlex.split(f'ping {host}')
    # Use check_output to avoid shell=True and ensure subprocess runs in a new process group
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}