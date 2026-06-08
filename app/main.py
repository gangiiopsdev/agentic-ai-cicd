from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 100:
        return {'status': 'error', 'message': 'Invalid host name'}
    args = shlex.split(f'ping -c 4 {host}')
    subprocess.call(args)
    return {'status': 'completed'}