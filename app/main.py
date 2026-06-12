from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}