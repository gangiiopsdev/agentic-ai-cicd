from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    # Use safe subprocess call with shell=False
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}