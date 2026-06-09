from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'invalid host'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)
    return {'status': 'completed'}