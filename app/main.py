from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.strip():
        raise ValueError('Host parameter cannot be empty')
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}