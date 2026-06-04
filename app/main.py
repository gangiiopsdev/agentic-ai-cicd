from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def safe_ping(host):
    if not host.isnumeric() or '.' not in host:
        raise ValueError('Invalid host address')
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}