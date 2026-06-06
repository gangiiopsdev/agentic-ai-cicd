from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', quote(host)]
    subprocess.call(args)
    return {"status": "completed"}