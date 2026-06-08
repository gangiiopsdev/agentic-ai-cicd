from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = shlex.split(f'ping -c 1 {host}')
    result = subprocess.Popen(command, stdout=PIPE, stderr=PIPE, shell=False)
    output, error = result.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}