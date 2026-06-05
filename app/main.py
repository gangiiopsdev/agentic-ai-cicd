from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host parameter
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    result = ping(host)
    return {'status': 'completed'}