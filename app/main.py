from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def validate_host(host):
    if not host.isalnum():
        raise ValueError('Invalid hostname')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', '--', quote(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}