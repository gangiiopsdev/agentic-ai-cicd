from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    command = ['ping'] + shlex.split(host)
    output = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
    return {'status': 'completed', 'output': output.stdout}

@app.get('/ping')
def ping_endpoint(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    command = ['ping'] + shlex.split(host)
    output = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
    return {'status': 'completed', 'output': output.stdout}