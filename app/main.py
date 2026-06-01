from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() and not '.' in host:
        raise ValueError('Invalid host name')
    # Validate the input to ensure it only contains alphanumeric characters and dots
    if not re.match(r'^[a-zA-Z0-9.]+$', host):  # Simplified validation
        raise ValueError('Invalid host name')
    try:
        command = ['ping'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}