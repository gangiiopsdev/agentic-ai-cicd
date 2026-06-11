from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitize_host(host)
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}