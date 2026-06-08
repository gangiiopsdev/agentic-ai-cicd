from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run for better control and security
    subprocess.run(['ping', host], check=True, capture_output=True)

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    safe_ping(host)
    return {"status": "completed"}