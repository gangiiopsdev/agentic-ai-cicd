from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def ping(host: str):
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)