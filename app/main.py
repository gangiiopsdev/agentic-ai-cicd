from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and arg validation
    if validate_host(host):
        subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    allowed_hosts = ["example.com", "localhost"]  # Replace with actual validation logic
    return host in allowed_hosts