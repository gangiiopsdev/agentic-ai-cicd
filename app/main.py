from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Basic validation logic (e.g., check for length, characters allowed)
    return len(host) > 0 and all(c.isalnum() or c in ['.', '-'] for c in host)