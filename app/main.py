from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Validate and sanitize input
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    secure_ping(host)
    return {"status": "completed"}