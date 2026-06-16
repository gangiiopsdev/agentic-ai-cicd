from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is not None:
        subprocess.run(['ping', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400