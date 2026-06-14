from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    command_parts = ['ping'] + shlex.split(host)
    result = subprocess.run(command_parts, check=True, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}