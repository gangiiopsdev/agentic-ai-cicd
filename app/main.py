from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Sanitize input by validating and escaping it
    valid_hosts = ['127.0.0.1', '8.8.8.8']  # Example of allowed hosts
    if host not in valid_hosts:
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)