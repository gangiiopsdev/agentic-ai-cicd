from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def is_safe_host(hostname):
    allowed_hosts = ['example.com', 'test.com']
    return hostname in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise Exception("Invalid host")

    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)

    return {"status": "completed"}