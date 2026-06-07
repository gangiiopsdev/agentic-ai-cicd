from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping_fixed")
def ping_fixed(host: str):
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Simple validation example
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts