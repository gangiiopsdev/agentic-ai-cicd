from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced security implementation
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
    return {'status': 'completed'}