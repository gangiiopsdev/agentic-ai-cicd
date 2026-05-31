from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)