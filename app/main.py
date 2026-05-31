from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.call(shlex.split(f'ping {host}'))

@app.get("/ping")
def ping(host: str):
    safe_ping(host)

    return {"status": "completed"}