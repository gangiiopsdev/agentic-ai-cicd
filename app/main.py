from fastapi import FastAPI
import subprocess
import re
import shlex
import os

app = FastAPI()

def safe_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not safe_host(host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}