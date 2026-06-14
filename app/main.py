from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use a regular expression to validate the input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host) or len(host) > 255:
            raise ValueError('Invalid input')
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    try:
        # Use a regular expression to validate the input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host) or len(host) > 255:
            raise ValueError('Invalid input')
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}