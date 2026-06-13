from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate the host to ensure it's a safe hostname or IP address
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.call(args)

# Simple example of validation (replace with actual validation logic)
def validate_host(host):
    return '.' in host and len(host.split('.')) == 4

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}