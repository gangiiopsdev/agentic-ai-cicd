from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def is_valid_host(host):
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'invalid'}
    subprocess.call(['ping', quote(host)])
    return {'status': 'completed'}