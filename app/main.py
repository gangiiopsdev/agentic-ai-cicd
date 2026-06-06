from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, shell=False)  # Ensure shell=False to prevent injection
    return {'status': 'completed'}