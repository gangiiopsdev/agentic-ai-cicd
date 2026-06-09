from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['host1', 'host2']  # Define allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    subprocess.call(['ping', host], shell=False)  # Fixed by setting shell=False
    return {'status': 'completed'}