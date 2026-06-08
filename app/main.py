from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
@app.get('/ping')
def ping(host: str):    validate_host(host)
    # Use subprocess.run instead of subprocess.call
    subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {'status': 'completed'}