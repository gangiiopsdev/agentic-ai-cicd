from fastapi import FastAPI
import subprocess
allowed_hosts = ['example.com', 'another-example.com']  # Replace with a whitelist of allowed hosts

app = FastAPI()

def ping_host(host: str) -> bool:
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return True

@app.get('/ping')
def ping(host: str):
    if not ping_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])
    return {'status': 'completed'}