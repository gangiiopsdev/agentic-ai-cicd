from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    safe_hosts = {'example.com', 'test.com'}  # Define a whitelist of allowed hosts
    return host in safe_hosts

@app.get('/ping')
def ping(host: str):
    if is_safe_host(host):
        command = shlex.split(f'ping {shlex.quote(host)}')
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')