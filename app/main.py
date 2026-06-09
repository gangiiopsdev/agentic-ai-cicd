from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    sanitize_host(host)
    # Secure implementation using subprocess.run with shell=False and splitting the command into a list
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}