from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add allowed hosts here
    return host in allowed_hosts

@app.get="/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')
    return {'status': 'completed'}