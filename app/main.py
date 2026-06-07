from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

# Regex pattern to validate host input
def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    subprocess.call(command, shell=False)
    return {'status': 'completed'}