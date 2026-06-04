from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)

    # Secure implementation
    subprocess.call(shlex.split(f'ping {host}'))

    return {'status': 'completed'}