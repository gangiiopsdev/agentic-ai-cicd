from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Define allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    command = ['ping', shlex.quote(host)]  # Use shlex.quote to safely quote the host input
    subprocess.call(command)
    return {'status': 'completed'}