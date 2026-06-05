from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run with list for arguments to avoid shell=True
    subprocess.run(['ping', host], check=True)

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']  # Define a whitelist of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    safe_ping(host)
    return {"status": "completed"}