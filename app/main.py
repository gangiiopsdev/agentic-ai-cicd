from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    # Enhanced validation to include length check and allowed characters
    if len(host) > 255 or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)