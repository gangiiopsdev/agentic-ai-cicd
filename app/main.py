from fastapi import FastAPI
import subprocess
import shlex
import os

current_user = os.getlogin()

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = shlex.split(f'ping {host}')
    subprocess.call(['sudo', '-u', current_user, 'sh', '-c', ' '.join(args)])
    return {'status': 'completed'}