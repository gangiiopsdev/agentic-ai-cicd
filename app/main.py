from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        subprocess.call(args, shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 403

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except Exception as e:
        return {'error': str(e)}, 500