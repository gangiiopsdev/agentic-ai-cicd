from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}