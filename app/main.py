from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation and sanitization
    if not host.strip() or '.' not in host:
        return {"status": "invalid input"}
    # Use a whitelist of allowed hosts
    allowed_hosts = ['8.8.8.8', '192.168.1.1']  # Example list, replace with actual allowed hosts
    if host in allowed_hosts:
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        return {"status": "invalid input"}