from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)