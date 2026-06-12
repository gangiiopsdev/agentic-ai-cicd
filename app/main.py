from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_safe_host(host):
    # Add regex pattern to allow only safe hostnames/IP addresses
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}