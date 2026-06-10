from fastapi import FastAPI
import re
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', '127.0.0.1']
    if host in allowed_hosts:
        try:
            subprocess.run(['ping', host], check=True)
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Ping failed: {e}')
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}