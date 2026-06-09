from fastapi import FastAPI
import subprocess
cimport = ['ping']

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    subprocess.call(cimport + [host])
    return {'status': 'completed'}