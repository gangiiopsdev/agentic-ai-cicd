from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # More complex validation example
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping_fixed")
def ping_fixed(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host')