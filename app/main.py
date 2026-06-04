from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
app = FastAPI()
def ping(host: str):
    validate_host(host)
    subprocess.call(['ping', host], shell=False)
@app.get("/ping")
def ping_endpoint(host: str):    return ping(host)