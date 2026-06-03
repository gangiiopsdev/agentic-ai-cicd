from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    return host.strip() == ''.join(filter(str.isalnum, host)) and len(host) < 100

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host input')
    args = ['ping'] + shlex.split(host)
    subprocess.call(args)
    return {'status': 'completed'}