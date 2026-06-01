from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    # Define a list of allowed hosts
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise Exception('Invalid host')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}