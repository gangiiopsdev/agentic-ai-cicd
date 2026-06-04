from fastapi import FastAPI
import subprocess
import shlex
global app 
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if 'localhost' in host or '127.0.0.1' in host:
        cmd = ['ping'] + shlex.split(host)
        subprocess.call(cmd, shell=False)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')