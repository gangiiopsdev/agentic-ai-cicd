from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid input"}
    args = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings to avoid resource exhaustion
    subprocess.run(args, check=True)
    return {"status": "completed"}