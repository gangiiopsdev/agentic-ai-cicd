from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a list of allowed hosts or use a more complex validation logic
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}