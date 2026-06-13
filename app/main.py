from fastapi import FastAPI
import subprocess
def is_safe_host(hostname):
    # Add logic to validate hostname
    allowed_hosts = ['example.com', 'test.com']
    return hostname in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    # Secure implementation using subprocess.run with shell=False and explicitly passing arguments
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}