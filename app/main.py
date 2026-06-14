from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

allowed_hosts = ['8.8.8.8', '127.0.0.1']
def ping(host: str):
    if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host) or host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)