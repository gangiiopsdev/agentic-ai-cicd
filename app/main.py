from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and sanitization
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')