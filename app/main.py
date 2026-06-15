from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', quote(host)])
    return {'status': 'completed'}