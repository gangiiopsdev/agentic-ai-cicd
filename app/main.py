from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_safe_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host name")
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {"status": "completed"}