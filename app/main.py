from fastapi import FastAPI
import subprocess
import shlex
import re

global_blacklist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')

app = FastAPI()

def validate_host(host):
    return all(char in global_blacklist for char in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host name")
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, check=True)
    return {"status": "completed"}