from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement proper host validation and sanitization logic here
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get="/ping")
def ping(host: str):
    sanitize_host(host)
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}