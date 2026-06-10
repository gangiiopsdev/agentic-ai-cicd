from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    return ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check for IP address format
    return True