from fastapi import FastAPI
import subprocess
import shlex
cimport = ['ping', host]

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    subprocess.run(shlex.split(' '.join(cimport)), check=True, shell=False)
    return {'status': 'completed'}