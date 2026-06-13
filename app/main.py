from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent injection attacks
    if not host.isalnum() or '..' in host:
        raise ValueError("Invalid host name")
    # Use a whitelist of allowed hosts or IP addresses
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
    subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    return {"status": "completed"}