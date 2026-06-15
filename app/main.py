from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = {'google.com', 'example.com'}

def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        raise ValueError('Invalid host')
    # Secure implementation with whitelist
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        raise ValueError('Invalid host')
    # Secure implementation with whitelist
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', host], check=True)

def validate_host(host: str) -> bool:
    # Add validation logic here
    return host.strip() != ''