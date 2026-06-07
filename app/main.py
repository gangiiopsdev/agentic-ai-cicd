from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}