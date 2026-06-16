from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}

    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)