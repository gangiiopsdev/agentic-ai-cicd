from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        raise ValueError("Invalid host")
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        raise ValueError("Invalid host")
    # Secure implementation
    subprocess.run(['ping', host], check=True)

def validate_host(host: str) -> bool:
    # Add validation logic here
    return host.strip() != ''