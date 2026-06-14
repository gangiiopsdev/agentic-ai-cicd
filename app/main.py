from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host to ensure it is a safe IP address or domain name
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Implement validation logic here
    pass