from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not is_safe_host(host):
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", host])
    return {"status": "completed"}

# Function to check if the host is safe
def is_safe_host(host: str) -> bool:
    allowed_hosts = ["example.com", "test.example.com"]  # Replace with actual allowed hosts
    return host in allowed_hosts