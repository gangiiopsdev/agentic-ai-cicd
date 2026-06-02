from fastapi import FastAPI
import subprocess
import shlex

def is_valid_host(host):
    # Example validation logic: allow only alphanumeric characters and dots
    return host.isalnum() or '.' in host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {'status': 'completed'}