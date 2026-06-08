from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    globally_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts
    if host not in globally_safe_hosts:
        raise ValueError('Unauthorized host')
    return host

app = FastAPI()

@app.get('/ping')
def ping(host: str = Depends(validate_host)):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid characters in host')
    safe_args = shlex.split(host)
    subprocess.run(['ping'] + safe_args, check=True, capture_output=True, shell=False)
    return {'status': 'completed'}