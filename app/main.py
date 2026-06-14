from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe to ping
    return host.isdigit() and len(host) <= 4