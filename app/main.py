from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    safe_host = shlex.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, text=True)
    return {'status': 'completed'}