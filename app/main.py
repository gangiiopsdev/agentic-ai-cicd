from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    # Define a list of allowed hosts
    allowed_hosts = ['google.com', 'example.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {'status': 'completed'}