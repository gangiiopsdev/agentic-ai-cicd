from fastapi import FastAPI
import subprocess
import shlex
import os
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}