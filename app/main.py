from fastapi import FastAPI
import subprocess
import shlex
import os
import re

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use re.match to validate the host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host format'}
        # Use shlex.quote to sanitize the host input
        sanitized_host = shlex.quote(host)
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    # Ensure the host input is validated and sanitized before passing to subprocess
    return safe_ping(host)