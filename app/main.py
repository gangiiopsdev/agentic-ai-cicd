from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation using a whitelist
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)