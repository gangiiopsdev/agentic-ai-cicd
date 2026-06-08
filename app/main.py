from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True, capture_output=True)

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping_route(host: str):
    return ping(host)