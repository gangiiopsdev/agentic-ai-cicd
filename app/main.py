from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full executable path and validation of host input
    if not valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['/usr/bin/ping', host], check=True)
    return {"status": "completed"}

def valid_host(host: str) -> bool:
    # Implement host validation logic here, e.g., using regex to allow only alphanumeric characters and periods
    import re
    return re.match(r'^[a-zA-Z0-9.]+$', host) is not None