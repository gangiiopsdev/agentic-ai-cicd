from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        return host
    return None

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is not None:
        subprocess.call(f'ping {sanitized_host}', shell=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}, 400