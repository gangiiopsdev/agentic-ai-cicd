from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}