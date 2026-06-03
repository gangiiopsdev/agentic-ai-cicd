from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}