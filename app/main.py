from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Add validation logic to ensure the host is safe to ping
    return all(c.isalnum() or c in ['.', '-'] for c in host)