from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', host) and any(c.isdigit() for c in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid input')
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}