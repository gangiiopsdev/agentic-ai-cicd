from fastapi import FastAPI
import subprocess
import shlex
import os
good_hosts = {'example.com', 'test.com'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in good_hosts:
        try:
            subprocess.run(shlex.split(f'ping {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        raise ValueError('Host not allowed')
    return {'status': 'completed'}