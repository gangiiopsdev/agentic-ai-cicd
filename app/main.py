from fastapi import FastAPI
import subprocess
import shlex
import os
import re
good_hosts = {'example.com', 'test.com'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in good_hosts and re.match(r'^[a-zA-Z0-9.-]+$', host):
        try:
            result = subprocess.run(shlex.split(f'ping {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        raise ValueError('Host not allowed')