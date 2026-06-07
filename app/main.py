from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host if host in allowed_hosts else None

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host:
        subprocess.run(['ping', sanitized_host], check=True)
    else:
        raise ValueError('Invalid host')