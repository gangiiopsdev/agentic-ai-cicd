from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Host is not allowed')
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}