from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if all(c.isalnum() or c in ('.', '-', '_') for c in host) and len(host) <= 255:
        sanitized_host = re.sub(r'[^a-zA-Z0-9.-_]', '', host)
        subprocess.call(shlex.split(f'ping {sanitized_host}'))
    return {'status': 'completed'}