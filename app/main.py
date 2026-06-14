from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.call(args)

def validate_host(host):
    # Add validation logic to ensure the host is safe to ping
    allowed_hosts = {'example.com', '127.0.0.1'}  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    safe_ping(host)
    return {"status": "completed"}