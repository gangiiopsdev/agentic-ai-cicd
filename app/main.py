from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced implementation with validation and logging
    allowed_hosts = ['127.0.0.1', '::1']  # Add more IPs as needed
    if host not in allowed_hosts:
        raise ValueError(f"Invalid host: {host}")
    subprocess.run(['ping', '-c', '4', host], check=True)
    return {"status": "completed"}