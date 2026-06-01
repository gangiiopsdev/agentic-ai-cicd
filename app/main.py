from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_str):
    return shlex.quote(input_str)

def check_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not check_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}