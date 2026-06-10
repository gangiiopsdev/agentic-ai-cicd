from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True, shell=False)
    return {'status': 'completed'}