from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def execute_ping(host: str):
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    if os.name == 'nt':
        host = host.replace('/', '\\\\')
    execute_ping(host)
    return {"status": "completed"}