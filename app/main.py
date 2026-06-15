from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}