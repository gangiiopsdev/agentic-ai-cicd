from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', '127.0.0.1']  # Define allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', quote(host)], check=True, capture_output=True)
    return {'status': 'completed'}