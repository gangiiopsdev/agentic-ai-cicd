from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host in allowed_hosts:
        subprocess.run(['ping', '-c', '1', host], check=True)  # Limit the number of pings for security
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')