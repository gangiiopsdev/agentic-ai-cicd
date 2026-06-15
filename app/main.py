from fastapi import FastAPI
import subprocess
import shlex
global allowed_hosts
allowed_hosts = ['localhost', '127.0.0.1']

app = FastAPI()

def validate_host(host):
    global allowed_hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', '--count=1'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}