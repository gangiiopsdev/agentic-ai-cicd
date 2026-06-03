from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])

def validate_host(host: str) -> bool:
    # Proper implementation of validation logic here
    allowed_hosts = ['example.com', 'test.com']  # Example allowed hosts
    return host in allowed_hosts