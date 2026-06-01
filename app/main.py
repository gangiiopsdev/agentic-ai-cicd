from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_safe_hostname(hostname):
    return all(c.isalnum() or c in '-.' for c in hostname)

@app.get('/ping')
def ping(host: str):
    if not host.strip() or not is_safe_hostname(host):
        return {'error': 'Invalid host name'}
    try:
        subprocess.run(shlex.split(f'ping {host}'), check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}