from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.call(["ping", host])
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Add validation logic for the host
    allowed_hosts = ["example.com", "test.com"]
    return host in allowed_hosts