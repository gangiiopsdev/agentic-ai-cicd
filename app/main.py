from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    args = shlex.split(f'ping {host}')
    subprocess.call(args)

    return {'status': 'completed'}