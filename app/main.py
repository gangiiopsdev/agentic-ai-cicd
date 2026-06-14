from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    # Define a list of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid host'}, 403
    # Secure implementation
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}