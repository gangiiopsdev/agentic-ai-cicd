from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    if not host.isalnum() or len(host) > 10:
        raise ValueError("Invalid host name")
    return host.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}