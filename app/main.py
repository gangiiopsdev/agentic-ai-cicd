from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True, shell=False)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}