from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'invalid'}
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    subprocess.call(args)
    return {'status': 'completed'}