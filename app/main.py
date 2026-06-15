from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and sanitization
    if validate_host(host):
        subprocess.call(["ping", host])
    return {"status": "completed"}

# Function to validate and sanitize the host input
def validate_host(host: str) -> bool:
    allowed_hosts = ["example.com", "test.com"]
    return host in allowed_hosts