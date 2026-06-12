from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_safe(host: str):
    # Sanitize input to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)