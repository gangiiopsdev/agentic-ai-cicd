from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.net']  # Add allowed hosts here
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        safe_ping(host)
    else:
        raise ValueError('Host is not allowed')

    return {"status": "completed"}