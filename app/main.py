from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid input'}

    args = shlex.split(f'ping -c 1 {host}')
    subprocess.run(args, check=True, capture_output=True)

    return {'status': 'completed'}