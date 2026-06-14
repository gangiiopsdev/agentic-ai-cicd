from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Allow only local hosts for demonstration purposes
    if host in allowed_hosts:
        command = shlex.split(f'ping {host}')
        subprocess.run(command, check=True)
    else:
        raise ValueError('Invalid host')
    return {'status': 'completed'}