from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shell=False and ensuring host is safe
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host], shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shell=False and ensuring host is safe
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host], shell=False)

    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Simple example of validation logic
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts