from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host parameter
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid hostname')

    # Use a whitelisted set of allowed hosts or domains
    allowed_hosts = {'example.com', 'test.example.com'}
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)