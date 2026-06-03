from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get="/ping")
def ping(host: str):
    validate_host(host)
    command = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings to avoid potential abuse
    subprocess.run(command, check=True)

    return {'status': 'completed'}