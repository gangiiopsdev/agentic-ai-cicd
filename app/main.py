from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

def validate_host(host: str) -> bool:
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    command = ['ping', '-c 1', shlex.quote(host)]
    subprocess.call(command, shell=False)
    return {'status': 'completed'}