from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    command = ['ping', shlex.quote(host)]  # Use shlex.quote to sanitize the input
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, shell=False)
    return {'status': 'completed'}