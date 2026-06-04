from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Host not allowed')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}