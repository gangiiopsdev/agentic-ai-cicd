from fastapi import FastAPI
import subprocess
from shlex import quote
import os

global_allowed_hosts = {'example.com', 'test.com'}

app = FastAPI()

def ping(host: str):
    if host not in global_allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        result = subprocess.run(['ping', quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)