from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)