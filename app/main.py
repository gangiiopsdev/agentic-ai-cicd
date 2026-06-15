from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_safe_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid hostname")
    try:
        cmd = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)