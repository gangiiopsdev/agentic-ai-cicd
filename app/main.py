from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to allow only alphanumeric characters and a few special characters
    if not re.match(r'^[a-zA-Z0-9._%-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host input'}

    try:
        args = ['ping'] + shlex.split(host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}