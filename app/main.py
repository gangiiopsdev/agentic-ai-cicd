from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def escape_host(host):
    host = host.replace(';', '').replace('&', '').replace('|', '')
    return host

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        escaped_host = escape_host(host)
        result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'error': str(e)}