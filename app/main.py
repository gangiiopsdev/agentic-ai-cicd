from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}