from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError("Invalid host")
    # Use a whitelist of allowed hosts or use a more secure method
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
    subprocess.run(["ping", host], check=True)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)