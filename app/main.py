from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Simple validation for demonstration purposes
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(["ping", host])
    return {"status": "completed"}