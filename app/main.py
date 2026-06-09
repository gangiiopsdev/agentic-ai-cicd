from fastapi import FastAPI
import subprocess
import shlex
import re

def validate_host(host: str):
    return re.match(r'^[a-zA-Z0-9]+$', host) is not None

app = FastAPI()

def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    cmd = shlex.split(f'ping {host}')
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except subprocess.TimeoutExpired:
        return {'status': 'timed out'}

app.get('/')(home)
app.get('/ping')(ping)