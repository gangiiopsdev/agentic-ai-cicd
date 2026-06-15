from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize user inputs
    if not host or not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}

    try:
        output = subprocess.check_output(['/usr/bin/ping', quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}