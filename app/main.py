from fastapi import FastAPI
import subprocess
from shlex import quote
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the hostname input
    if not re.match(r'^[a-zA-Z0-9.-:]+$', host) or len(host) > 255:
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', quote(host)], shell=False)
    return {'status': 'completed'}