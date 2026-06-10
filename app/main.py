from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation with input validation
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', '-c', '1', host], check=True)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., allowed IP ranges or domain names
    return True