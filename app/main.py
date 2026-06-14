from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
@app.get('/ping')
def ping(host: str):
    sanitize_host(host)
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, shell=False)  # Ensure shell=False for security
    return {'status': 'completed'}