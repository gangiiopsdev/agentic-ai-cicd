from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

app = FastAPI()

def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)