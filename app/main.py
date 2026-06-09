from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Simple example of host validation
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}